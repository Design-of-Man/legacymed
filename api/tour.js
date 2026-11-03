// POST /api/tour — tour / contact requests from /meet-and-greet and /contact.
//
// Delivers by email to every address in TOUR_TO_EMAIL (comma-separated):
// through Resend when RESEND_API_KEY is set, otherwise through FormSubmit
// (formsubmit.co), which needs no key. FormSubmit sends the first address
// an "Activate Form" email the first time; until someone clicks it, nothing
// is delivered and the page tells the visitor to call. With no TOUR_TO_EMAIL
// it answers 503 "not_configured". Nothing is stored or logged.
//
// After a delivered email it tells the agency portal that one enquiry arrived
// (POST PORTAL_URL/api/beacon/lead, keyed by LEAD_BEACON_SECRET). The beacon
// carries the site, a random id, the time and which page it came from: no
// name, no contact details, nothing typed. It is skipped when either variable
// is unset and can never fail the request. Added 2026-10-30 so Legacy's leads
// show in the portal like the other client sites.
//
// When the visitor gave an email and Resend is configured, they also get a
// short confirmation (from CONFIRM_FROM, else TOUR_FROM_EMAIL). Fixed text
// plus their first name: nothing they typed is repeated. Best effort; it can
// never fail the request. Added Oct 30, 2026 at Nick's request.
//
// Turnstile (added 2026-11-03): GET returns {"siteKey": "..."} for the
// browser, empty while TURNSTILE_SITE_KEY / TURNSTILE_SECRET_KEY are unset
// (then nothing changes). An "unverified" request is still emailed, but only
// to unverifiedRecipients() with "[Unverified] " on the subject, with no
// visitor confirmation and no portal beacon (it must not count as a lead).
//
// HIPAA posture: the form asks for contact details and a preferred time only,
// the page tells visitors not to send medical information, the message is
// capped at 600 characters, and request bodies are never written to logs.
"use strict";

const { officeEmail, confirmEmail } = require("./_email.js");
const BRAND = { name: "Legacy Medical", color: "#16140F", accent: "#C9A35B", accentInk: "#16140F", kicker: "#C9A35B" };

const MAX_MESSAGE = 600;
const ALLOWED_HOSTS = [/^legacymedicalpalmbeach\.com$/, /^www\.legacymedicalpalmbeach\.com$/, /^legacymedical[a-z0-9-]*\.vercel\.app$/, /^localhost(:\d+)?$/, /^127\.0\.0\.1(:\d+)?$/];

// Cloudflare Turnstile, shared by every Design of Man client site (keep this
// block identical across abacoapodiatry, elite, regenortho, firstrehabnpb and
// legacymed; adapt only the require/export style to the file it lives in).
//
// ON only when BOTH TURNSTILE_SITE_KEY and TURNSTILE_SECRET_KEY are set, so a
// half-configured environment can never mark every real lead unverified.
// The browser sends the token as `_turnstile` (leading underscore: a control
// field, never printed in an email).
//
// Verification outcome is three-way:
//   "off"        keys unset: behave exactly as before Turnstile existed
//   "verified"   Cloudflare said success, OR Cloudflare could not be reached
//                (fail open: their outage must not demote real patients)
//   "unverified" token missing or rejected. The lead is still KEPT wherever this
//                site stores leads, and still emailed, but only to the
//                monitoring inbox (TURNSTILE_UNVERIFIED_TO, else LEAD_CC), with
//                "[Unverified] " on the subject, and the visitor gets NO
//                confirmation email. That confirmation to scraped addresses is
//                what drew spam complaints on the shared Resend account.
//                If neither monitoring variable is set, it goes to the normal
//                recipients with the prefix: a lead is never silently lost.

const TURNSTILE_VERIFY = "https://challenges.cloudflare.com/turnstile/v0/siteverify";

function turnstileOn() {
  return Boolean(process.env.TURNSTILE_SITE_KEY && process.env.TURNSTILE_SECRET_KEY);
}

// What GET on the lead endpoint returns, so the browser can find the site key.
function turnstileConfig() {
  return { siteKey: turnstileOn() ? process.env.TURNSTILE_SITE_KEY : "" };
}

async function turnstileCheck(req, body) {
  if (!turnstileOn()) return "off";
  const token = body && typeof body._turnstile === "string" ? body._turnstile.trim() : "";
  if (!token || token.length > 2048) return "unverified";
  const params = new URLSearchParams({ secret: process.env.TURNSTILE_SECRET_KEY, response: token });
  const ip = String(req.headers["x-forwarded-for"] || "").split(",")[0].trim();
  if (ip) params.set("remoteip", ip);
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), 5000);
  try {
    const r = await fetch(TURNSTILE_VERIFY, { method: "POST", body: params, signal: ctrl.signal });
    const j = await r.json();
    if (j && j.success === true) return "verified";
    console.warn("turnstile: rejected", (j && j["error-codes"] || []).join(","));
    return "unverified";
  } catch (e) {
    console.warn("turnstile: siteverify unreachable, failing open:", e.message);
    return "verified";
  } finally {
    clearTimeout(timer);
  }
}

// Recipients for an unverified lead: the monitoring inbox, or null meaning
// "use the normal recipients" (subject still gets the prefix).
function unverifiedRecipients() {
  const raw = process.env.TURNSTILE_UNVERIFIED_TO || process.env.LEAD_CC || "";
  const list = raw.split(",").map((s) => s.trim()).filter(Boolean);
  return list.length ? list : null;
}

const clean = (v, max) => String(v == null ? "" : v).replace(/[\u0000-\u001f\u007f]/g, " ").trim().slice(0, max);

// Count one delivered enquiry in the portal. Best effort: a slow or failed
// portal must never turn a delivered request into an error for the visitor.
async function countLead(page) {
  const portal = process.env.PORTAL_URL;
  const secret = process.env.LEAD_BEACON_SECRET;
  if (!portal || !secret) return;
  const slug = String(page || "").replace(/^\/+|\/+$/g, "").split("/")[0].toLowerCase();
  const source = /^[a-z][a-z0-9-]{0,39}$/.test(slug) ? slug : "website";
  try {
    const r = await fetch(portal.replace(/\/+$/, "") + "/api/beacon/lead", {
      method: "POST",
      headers: { "Content-Type": "application/json", "x-beacon-key": secret, Origin: "https://legacymedicalpalmbeach.com" },
      body: JSON.stringify({
        site: "legacymedicalpalmbeach.com",
        submissionId: require("crypto").randomUUID(),
        occurredAt: new Date().toISOString(),
        source,
        page: page || null,
      }),
      signal: AbortSignal.timeout(3000),
    });
    if (!r.ok) console.error("tour: lead count failed with status", r.status);
  } catch (_) {
    console.error("tour: lead count threw");
  }
}

// The visitor's "we got it" email. Same promise the page makes, no more.
async function confirmToVisitor(key, from, replyTo, data) {
  if (!data.email) return;
  const first = /https?:|www\.|[<>]/i.test(data.name) ? "there" : data.name.split(/\s+/)[0];
  try {
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: "Bearer " + key, "Content-Type": "application/json" },
      body: JSON.stringify({
        from: process.env.CONFIRM_FROM || from,
        to: [data.email],
        reply_to: replyTo || undefined,
        subject: "We received your request: Legacy Medical",
        html: confirmEmail({
          brand: BRAND, first, ref: "", phone: "(561) 834-9280", site: "legacymedicalpalmbeach.com",
          promise: "Your request is with our office, and we will call or email you back.",
        }),
        text: [
          "Hi " + first + ",",
          "",
          "Thank you for reaching out to Legacy Medical. Your request is with our office, and we will call or email you back.",
          "",
          "If it is urgent, call us at (561) 834-9280.",
          "",
          "Legacy Medical",
          "https://legacymedicalpalmbeach.com",
        ].join("\n"),
      }),
      signal: AbortSignal.timeout(5000),
    });
    if (!r.ok) console.error("tour: confirmation failed with status", r.status);
  } catch (_) {
    console.error("tour: confirmation threw");
  }
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("X-Robots-Tag", "noindex");
  if (req.method === "GET") {
    res.setHeader("Cache-Control", "public, max-age=300");
    return res.status(200).json(turnstileConfig());
  }
  if (req.method !== "POST") {
    res.setHeader("Allow", "GET, POST");
    return res.status(405).json({ ok: false, error: "Use POST." });
  }

  const origin = req.headers.origin || "";
  let originHost = "";
  try { originHost = new URL(origin).host; } catch (_) { originHost = ""; }
  if (!originHost || !ALLOWED_HOSTS.some((re) => re.test(originHost))) {
    return res.status(403).json({ ok: false, error: "Request blocked." });
  }

  let body = req.body;
  if (typeof body === "string") { try { body = JSON.parse(body); } catch (_) { body = null; } }
  if (!body || typeof body !== "object") return res.status(400).json({ ok: false, error: "Empty request." });

  // Spam traps: a hidden field people never see, and a minimum time on the page.
  if (clean(body.company_website, 200) || Number(body.elapsed) < 2500) {
    return res.status(200).json({ ok: true });
  }

  const data = {
    name: clean(body.name, 120),
    email: clean(body.email, 160),
    phone: clean(body.phone, 40),
    reason: clean(body.reason, 80),
    contact_pref: clean(body.contact_pref, 40),
    best_time: clean(body.best_time, 80),
    message: clean(body.message, MAX_MESSAGE + 1),
    page: clean(body.page, 120),
  };
  if (!data.name) return res.status(400).json({ ok: false, error: "Please add your name." });
  if (!data.email && !data.phone) return res.status(400).json({ ok: false, error: "Please add a phone number or email." });
  if (data.email && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(data.email)) return res.status(400).json({ ok: false, error: "Please check the email address." });
  if (data.message.length > MAX_MESSAGE) return res.status(400).json({ ok: false, error: "Please keep the note under 600 characters." });
  if (String(body.no_medical) !== "yes") return res.status(400).json({ ok: false, error: "Please confirm the note has no medical details." });

  const key = process.env.RESEND_API_KEY;
  const officeTo = String(process.env.TOUR_TO_EMAIL || "").split(",").map((t) => t.trim()).filter(Boolean);
  const from = process.env.TOUR_FROM_EMAIL || "Legacy Medical website <onboarding@resend.dev>";
  if (!officeTo.length) return res.status(503).json({ ok: false, error: "not_configured" });

  // Bot check on top of the traps above. Unverified: still emailed, but to the
  // monitoring inbox, prefixed, with no confirmation and no portal count.
  const unverified = (await turnstileCheck(req, body)) === "unverified";
  if (unverified) console.warn("tour: unverified turnstile");
  const to = unverified ? (unverifiedRecipients() || officeTo) : officeTo;

  const rows = [
    ["Name", data.name], ["Phone", data.phone], ["Email", data.email],
    ["Interested in", data.reason], ["Prefers", data.contact_pref], ["Best time", data.best_time],
    ["Note", data.message], ["Sent from", data.page],
  ].filter(([, v]) => v);
  const subject = (unverified ? "[Unverified] " : "") + "Website request: " + (data.reason || "tour") + " from " + data.name;
  const failed = () => res.status(502).json({ ok: false, error: "We could not send that just now." });

  try {
    if (key) {
      const text = rows.map(([k, v]) => k + ": " + v).join("\n");
      const html = officeEmail({
        brand: BRAND,
        title: data.reason ? "New request: " + data.reason : "New tour request",
        fields: [["name", data.name], ["phone", data.phone], ["email", data.email],
          ["Interested in", data.reason], ["Prefers", data.contact_pref],
          ["Best time", data.best_time], ["message", data.message], ["page", data.page]],
        meta: { site: "legacymedicalpalmbeach.com", source: (data.page || "/").replace(/^\//, "") || "home page" },
      });
      const r = await fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: { Authorization: "Bearer " + key, "Content-Type": "application/json" },
        body: JSON.stringify({ from, to, reply_to: data.email || undefined, subject, text, html }),
      });
      if (!r.ok) {
        console.error("tour: resend delivery failed with status", r.status); // status only, never the body
        return failed();
      }
      if (!unverified) {
        await confirmToVisitor(key, from, officeTo[0], data);
        await countLead(data.page);
      }
      return res.status(200).json({ ok: true });
    }

    // FormSubmit: first address is the account; the rest are copied (_cc).
    const site = "https://legacymedicalpalmbeach.com";
    const fields = Object.fromEntries(rows);
    fields._subject = subject;
    fields._template = "table";
    fields._captcha = "false";
    if (to.length > 1) fields._cc = to.slice(1).join(",");
    if (data.email) fields._replyto = data.email;
    const r = await fetch("https://formsubmit.co/ajax/" + encodeURIComponent(to[0]), {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json", Origin: site, Referer: site + (data.page || "/") },
      body: JSON.stringify(fields),
    });
    let out = null;
    try { out = await r.json(); } catch (_) { out = null; }
    if (!r.ok || !out || String(out.success) !== "true") {
      // Before activation FormSubmit answers success "false" and emails the activation link.
      console.error("tour: formsubmit delivery failed with status", r.status, out && String(out.success) === "false" ? "(not activated or rejected)" : "");
      return failed();
    }
    if (!unverified) await countLead(data.page);
    return res.status(200).json({ ok: true });
  } catch (_) {
    console.error("tour: delivery threw");
    return failed();
  }
};
