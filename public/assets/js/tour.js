/* Tour / contact request form.
   Posts JSON to /api/tour (a Vercel function). The form asks for contact
   details only; the page tells visitors not to include medical information,
   and the function rejects messages over a length cap. No analytics script
   runs on any page that carries this form. */
(() => {
  "use strict";
  const form = document.querySelector("form[data-tour]");
  if (!form) return;
  const status = form.querySelector(".form-status");
  const submit = form.querySelector("button[type='submit']");
  const phone = form.dataset.phone;
  const started = Date.now();

  const say = (kind, html) => {
    status.className = "form-status full " + kind;
    status.innerHTML = html;
    status.hidden = false;
    status.focus();
  };

  const fields = Array.from(form.querySelectorAll("input, select, textarea")).filter((f) => !f.closest(".hp"));
  const errFor = (f) => document.getElementById(f.id + "-err");
  const validate = (f) => {
    const err = errFor(f);
    let msg = "";
    if (f.required && !f.value.trim() && f.type !== "checkbox") msg = "Please fill this in.";
    else if (f.type === "checkbox" && f.required && !f.checked) msg = "Please confirm to continue.";
    else if (f.type === "email" && f.value && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(f.value)) msg = "Please check the email address.";
    else if (f.type === "tel" && f.value && f.value.replace(/\D/g, "").length < 10) msg = "Please include the area code.";
    f.setAttribute("aria-invalid", msg ? "true" : "false");
    if (err) { err.textContent = msg; err.hidden = !msg; }
    return !msg;
  };
  fields.forEach((f) => f.addEventListener("blur", () => { if (f.value || f.getAttribute("aria-invalid") === "true") validate(f); }));

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const bad = fields.filter((f) => !validate(f));
    if (bad.length) { bad[0].focus(); return; }
    const data = Object.fromEntries(new FormData(form).entries());
    data.elapsed = Date.now() - started;
    data.page = location.pathname;
    submit.disabled = true;
    submit.setAttribute("aria-busy", "true");
    try {
      const res = await fetch(form.action, {
        method: "POST",
        headers: { "content-type": "application/json", accept: "application/json" },
        body: JSON.stringify(data),
      });
      const out = await res.json().catch(() => ({}));
      if (res.ok && out.ok) {
        form.querySelectorAll(".field, .check, .notice, .btn-row").forEach((n) => (n.hidden = true));
        say("ok", "<strong>Thank you. Your request is with our office.</strong><br>The office will call or email you back. If it is urgent, call <a href=\"tel:" + phone.replace(/\D/g, "").replace(/^/, "+1") + "\">" + phone + "</a>.");
        if (typeof window.gtag === "function") window.gtag("event", "generate_lead", { form: form.dataset.tour });
      } else if (res.status === 503) {
        say("bad", "Online requests are not switched on yet. Please call <a href=\"tel:+1" + phone.replace(/\D/g, "") + "\">" + phone + "</a> and we will set up your visit.");
      } else {
        say("bad", (out.error ? out.error + " " : "Something went wrong. ") + "You can also call <a href=\"tel:+1" + phone.replace(/\D/g, "") + "\">" + phone + "</a>.");
      }
    } catch (_) {
      say("bad", "We could not reach the server. Please call <a href=\"tel:+1" + phone.replace(/\D/g, "") + "\">" + phone + "</a>.");
    } finally {
      submit.disabled = false;
      submit.removeAttribute("aria-busy");
    }
  });
})();
