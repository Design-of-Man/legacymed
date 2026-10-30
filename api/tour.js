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
// HIPAA posture: the form asks for contact details and a preferred time only,
// the page tells visitors not to send medical information, the message is
// capped at 600 characters, and request bodies are never written to logs.
"use strict";

const MAX_MESSAGE = 600;
const ALLOWED_HOSTS = [/^legacymedicalpalmbeach\.com$/, /^www\.legacymedicalpalmbeach\.com$/, /^legacymedical[a-z0-9-]*\.vercel\.app$/, /^localhost(:\d+)?$/, /^127\.0\.0\.1(:\d+)?$/];

const clean = (v, max) => String(v == null ? "" : v).replace(/[\u0000-\u001f\u007f]/g, " ").trim().slice(0, max);
const escapeHtml = (s) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

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
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
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
  const to = String(process.env.TOUR_TO_EMAIL || "").split(",").map((t) => t.trim()).filter(Boolean);
  const from = process.env.TOUR_FROM_EMAIL || "Legacy Medical website <onboarding@resend.dev>";
  if (!to.length) return res.status(503).json({ ok: false, error: "not_configured" });

  const rows = [
    ["Name", data.name], ["Phone", data.phone], ["Email", data.email],
    ["Interested in", data.reason], ["Prefers", data.contact_pref], ["Best time", data.best_time],
    ["Note", data.message], ["Sent from", data.page],
  ].filter(([, v]) => v);
  const subject = "Website request: " + (data.reason || "tour") + " from " + data.name;
  const failed = () => res.status(502).json({ ok: false, error: "We could not send that just now." });

  try {
    if (key) {
      const text = rows.map(([k, v]) => k + ": " + v).join("\n");
      const html = "<table>" + rows.map(([k, v]) => "<tr><th align=left style=\"padding:4px 12px 4px 0\">" + k + "</th><td>" + escapeHtml(v) + "</td></tr>").join("") + "</table>";
      const r = await fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: { Authorization: "Bearer " + key, "Content-Type": "application/json" },
        body: JSON.stringify({ from, to, reply_to: data.email || undefined, subject, text, html }),
      });
      if (!r.ok) {
        console.error("tour: resend delivery failed with status", r.status); // status only, never the body
        return failed();
      }
      await confirmToVisitor(key, from, to[0], data);
      await countLead(data.page);
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
    await countLead(data.page);
    return res.status(200).json({ ok: true });
  } catch (_) {
    console.error("tour: delivery threw");
    return failed();
  }
};
