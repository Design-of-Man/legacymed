/* UserWay accessibility widget, carried over from the practice's old site
   (account QQECAXmKWE, client request Oct 20, 2026). Loads after the page so
   it never delays the hero; position, colour and features come from the
   practice's UserWay dashboard. The CSP allows https://*.userway.org. */
(() => {
  "use strict";
  const me = document.currentScript;
  const account = me && me.dataset.account;
  if (!account) return;
  const load = () => {
    const s = document.createElement("script");
    s.src = "https://cdn.userway.org/widget.js";
    s.setAttribute("data-account", account);
    s.async = true;
    document.body.appendChild(s);
  };
  if (document.readyState === "complete") load();
  else window.addEventListener("load", load, { once: true });
})();
