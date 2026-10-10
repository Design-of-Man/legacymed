/* Consent-gated Google Analytics 4. Only included by build.py when GA4_ID is
   set, and never on a page that carries a form. Nothing loads from Google
   until the visitor accepts; declining is remembered and nothing loads. */
(() => {
  "use strict";
  const me = document.currentScript;
  const id = me && me.dataset.ga;
  if (!id) return;
  const KEY = "lm-consent";
  let choice = null;
  try { choice = localStorage.getItem(KEY); } catch (_) {}

  const load = () => {
    window.gtag("consent", "update", { analytics_storage: "granted" });
    const s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(id);
    document.head.appendChild(s);
    window.gtag("js", new Date());
    // No ad features, no Google Signals, and the page path only (no query strings).
    window.gtag("config", id, { allow_google_signals: false, allow_ad_personalization_signals: false, page_location: location.origin + location.pathname });
  };

  if (choice === "granted") { load(); return; }
  if (choice === "denied") return;

  const box = document.createElement("div");
  box.className = "consent";
  box.setAttribute("role", "region");
  box.setAttribute("aria-label", "Cookie choice");
  box.innerHTML = '<p>We would like to count visits with Google Analytics to see which pages help people. No advertising, and nothing about your health. <a class="inline-link" href="/privacy">Privacy</a></p>' +
    '<div class="btn-row"><button type="button" class="btn small" data-c="granted">Allow</button><button type="button" class="btn ghost small" data-c="denied">No thanks</button></div>';
  box.addEventListener("click", (e) => {
    const b = e.target.closest("[data-c]");
    if (!b) return;
    try { localStorage.setItem(KEY, b.dataset.c); } catch (_) {}
    if (b.dataset.c === "granted") load();
    box.remove();
  });
  const show = () => document.body.appendChild(box);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", show, { once: true });
  else show();
})();
