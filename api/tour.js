// POST /api/tour — tour / contact requests from /membership and /contact.
//
// Delivers by email through Resend when RESEND_API_KEY and TOUR_TO_EMAIL are
// set in the Vercel project. Until they are, it answers 503 "not_configured"
// and the page tells the visitor to call; nothing is stored or logged.
//
// HIPAA posture: the form asks for contact details and a preferred time only,
// the page tells visitors not to send medical information, the message is
// capped at 600 characters, and request bodies are never written to logs.
"use strict";

const MAX_MESSAGE = 600;
const ALLOWED_HOSTS = [/^legacymedicalpalmbeach\.com$/, /^www\.legacymedicalpalmbeach\.com$/, /^legacymedical[a-z0-9-]*\.vercel\.app$/, /^localhost(:\d+)?$/, /^127\.0\.0\.1(:\d+)?$/];

const clean = (v, max) => String(v == null ? "" : v).replace(/[\u0000-\u001f\u007f]/g, " ").trim().slice(0, max);
const escapeHtml = (s) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

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
  const to = process.env.TOUR_TO_EMAIL;
  const from = process.env.TOUR_FROM_EMAIL || "Legacy Medical website <onboarding@resend.dev>";
  if (!key || !to) return res.status(503).json({ ok: false, error: "not_configured" });

  const rows = [
    ["Name", data.name], ["Phone", data.phone], ["Email", data.email],
    ["Interested in", data.reason], ["Prefers", data.contact_pref], ["Best time", data.best_time],
    ["Note", data.message], ["Sent from", data.page],
  ].filter(([, v]) => v);
  const text = rows.map(([k, v]) => k + ": " + v).join("\n");
  const html = "<table>" + rows.map(([k, v]) => "<tr><th align=left style=\"padding:4px 12px 4px 0\">" + k + "</th><td>" + escapeHtml(v) + "</td></tr>").join("") + "</table>";

  try {
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: "Bearer " + key, "Content-Type": "application/json" },
      body: JSON.stringify({
        from, to: to.split(",").map((s) => s.trim()).filter(Boolean),
        reply_to: data.email || undefined,
        subject: "Website request: " + (data.reason || "tour") + " from " + data.name,
        text, html,
      }),
    });
    if (!r.ok) {
      console.error("tour: delivery failed with status", r.status); // status only, never the body
      return res.status(502).json({ ok: false, error: "We could not send that just now." });
    }
    return res.status(200).json({ ok: true });
  } catch (_) {
    console.error("tour: delivery threw");
    return res.status(502).json({ ok: false, error: "We could not send that just now." });
  }
};
