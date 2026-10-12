/* Legacy Medical site assistant.
   Set answers only: no AI and no outside service. Every reply comes from
   /assets/assist.json, which build.py writes from the FAQ in content.py, so
   the assistant and the FAQ page can never disagree. Anything it cannot match
   goes to the office phone.
   Tour requests go to /api/tour, the same function and checks as the tour
   form (honeypot, time on page, no-medical-details confirmation). Nothing the
   visitor types is stored on the device or sent to analytics; if delivery
   fails, the visitor is told to call. */
(() => {
  "use strict";
  const me = document.currentScript;
  const FAQ_URL = (me && me.dataset.faq) || "/assets/assist.json";
  const started = Date.now();
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  let D = null;        // assist.json once loaded
  let mode = "menu";   // menu | ask | tour
  let step = 0;
  let draft = {};
  let launcher, panel, log, form, input, lastFocus;

  const h = (tag, cls, html) => {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  };
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const telLink = () => '<a href="tel:' + D.tel + '">' + D.phone + "</a>";
  const ICON = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M12 3C6.9 3 3 6.5 3 10.8c0 2.4 1.2 4.5 3.2 5.9L5.6 20c-.1.5.4.9.8.7l3.6-1.8c.6.1 1.3.2 2 .2 5.1 0 9-3.5 9-7.8S17.1 3 12 3z"/></svg>';

  function build() {
    launcher = h("button", "as-launch", ICON + "<span>Questions? Ask us</span>");
    launcher.type = "button";
    launcher.setAttribute("aria-expanded", "false");
    launcher.setAttribute("aria-controls", "as-panel");
    document.body.appendChild(launcher);

    panel = h("div", "as-panel");
    panel.id = "as-panel";
    panel.hidden = true;
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-labelledby", "as-title");
    panel.innerHTML =
      '<div class="as-head"><img src="/assets/img/legacy-mark-80.png" width="35" height="20" alt="">' +
      '<div><p class="as-title" id="as-title">Legacy Medical</p><p class="as-sub">Quick answers and tour requests</p></div>' +
      '<button type="button" class="as-close" aria-label="Close the assistant"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M4 4l12 12M16 4 4 16"/></svg></button></div>' +
      '<div class="as-log" role="log" aria-live="polite"></div>' +
      '<form class="as-input" hidden><label class="sr-only" for="as-text">Your message</label>' +
      '<input id="as-text" type="text" autocomplete="off" maxlength="600" placeholder="Type here">' +
      '<button type="submit" class="as-send" aria-label="Send"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M2 10 18 2l-4 8 4 8z"/></svg></button></form>' +
      '<p class="as-fine">Not for emergencies: call 911. General information only, not medical advice.</p>';
    document.body.appendChild(panel);

    log = panel.querySelector(".as-log");
    form = panel.querySelector(".as-input");
    input = form.querySelector("input");

    launcher.addEventListener("click", open);
    panel.querySelector(".as-close").addEventListener("click", close);
    form.addEventListener("submit", (e) => { e.preventDefault(); submit(); });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !panel.hidden) close(); });
  }

  /* Phones get a full-height sheet sized to the visual viewport, so the input
     stays above the on-screen keyboard (iOS does not shrink the layout
     viewport for it). */
  const phone = matchMedia("(max-width: 600px)");
  const vv = window.visualViewport;
  const fit = () => {
    if (!vv || !phone.matches || panel.hidden) return;
    panel.style.setProperty("--as-h", vv.height + "px");
    panel.style.setProperty("--as-top", vv.offsetTop + "px");
  };
  if (vv) { vv.addEventListener("resize", () => fit()); vv.addEventListener("scroll", () => fit()); }

  async function load() {
    if (D) return true;
    try {
      const r = await fetch(FAQ_URL, { headers: { accept: "application/json" } });
      D = await r.json();
      return true;
    } catch (_) { return false; }
  }

  async function open() {
    lastFocus = document.activeElement;
    panel.hidden = false;
    launcher.setAttribute("aria-expanded", "true");
    launcher.hidden = true;
    document.documentElement.classList.add("as-open");
    fit();
    if (!log.childElementCount) {
      if (!(await load())) {
        say('Sorry, the assistant could not load. Please call <a href="tel:+15618349280">(561) 834-9280</a>.');
        return;
      }
      greet();
    }
    panel.querySelector(".as-close").focus({ preventScroll: true });
  }
  function close() {
    panel.hidden = true;
    launcher.hidden = false;
    launcher.setAttribute("aria-expanded", "false");
    document.documentElement.classList.remove("as-open");
    (lastFocus && lastFocus !== document.body ? lastFocus : launcher).focus({ preventScroll: true });
  }

  function say(html, who) {
    const m = h("div", "as-msg " + (who === "me" ? "as-me" : "as-bot"), html);
    log.appendChild(m);
    log.scrollTop = log.scrollHeight;
    return m;
  }
  function later(fn) {
    if (reduce) return fn();
    const t = h("div", "as-msg as-bot as-typing", "<i></i><i></i><i></i>");
    t.setAttribute("aria-hidden", "true");
    log.appendChild(t);
    log.scrollTop = log.scrollHeight;
    setTimeout(() => { t.remove(); fn(); }, 450);
  }
  function chips(list) {
    const wrap = h("div", "as-chips");
    list.forEach((c) => {
      const b = h("button", "as-chip" + (c.main ? " as-chip-main" : ""), esc(c.label));
      b.type = "button";
      b.addEventListener("click", () => { wrap.remove(); c.go(); });
      wrap.appendChild(b);
    });
    log.appendChild(wrap);
    log.scrollTop = log.scrollHeight;
    return wrap;
  }
  const focusFirst = (wrap) => { const b = wrap && wrap.querySelector("button"); if (b) b.focus({ preventScroll: true }); };

  function menu() {
    mode = "menu";
    form.hidden = true;
    focusFirst(chips([
      { label: "Request a tour", main: true, go: startTour },
      { label: "Ask a question", go: startAsk },
      { label: "Call " + D.phone, go: () => { location.href = "tel:" + D.tel; } },
    ]));
  }
  function greet() {
    say("Hello. I can answer common questions about Legacy Medical, or take a tour request for the office. What would you like to do?");
    menu();
  }

  /* ---------------------------------------------------------------- ask */
  function startAsk() {
    mode = "ask";
    form.hidden = false;
    later(() => {
      say("Ask about membership, insurance, hours, Dr. Shtern, or the office. I answer from the practice's own information.");
      focusFirst(chips(["How much is membership?", "Do you take Medicare?", "Where are you?", "After-hours access"].map((q) => ({
        label: q, go: () => { say(esc(q), "me"); later(() => answer(q)); },
      }))));
      input.focus({ preventScroll: true });
    });
  }
  function answer(q) {
    const ql = " " + q.toLowerCase() + " ";
    let best = null, score = 0;
    D.faq.forEach((f) => {
      let s = 0;
      f.k.forEach((k) => { if (ql.indexOf(k) !== -1) s += k.length; });
      if (s > score) { score = s; best = f; }
    });
    say(best ? best.a : "I don't want to guess on that one. The office can answer it: call " + telLink() + " (" + D.hours + ") or email <a href=\"mailto:" + D.email + "\">" + D.email + "</a>.");
    chips([
      { label: "Request a tour", main: true, go: startTour },
      { label: "Back to the menu", go: menu },
    ]);
    input.focus({ preventScroll: true });
  }

  /* --------------------------------------------------------------- tour */
  const STEPS = [
    { key: "name", q: "Happy to set that up. What is your name?",
      ok: (v) => v.length >= 2, err: "Could you share your full name?" },
    { key: "phone", q: "Thank you, {name}. What is the best phone number for the office to call?",
      ok: (v) => v.replace(/\D/g, "").length >= 10, err: "Please include the area code, for example (561) 555-0100." },
    { key: "email", q: "And your email address? This one is optional.", skip: "Skip",
      ok: (v) => v === "" || /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v), err: "That email doesn't look right. Mind checking it?" },
    { key: "reason", q: "What are you interested in?",
      pick: ["A tour and meet-and-greet", "Membership questions", "Kidney or blood pressure care", "Care for a parent", "Something else"] },
    { key: "best_time", q: "When is the best time to reach you?",
      pick: ["Weekday mornings", "Weekday afternoons", "Any time"] },
    { key: "message", q: "Anything else the office should know? Please leave out medical details; those are best discussed with Dr. Shtern directly.", skip: "Nothing else",
      ok: (v) => v.length <= 600, err: "Please keep it under 600 characters." },
  ];
  function startTour() {
    mode = "tour";
    step = 0;
    draft = {};
    ask();
  }
  function ask() {
    const s = STEPS[step];
    form.hidden = !!s.pick;
    later(() => {
      say(esc(s.q.replace("{name}", (draft.name || "").split(" ")[0])));
      let wrap = null;
      if (s.pick) wrap = chips(s.pick.map((p) => ({ label: p, go: () => { say(esc(p), "me"); accept(p); } })));
      if (s.skip) wrap = chips([{ label: s.skip, go: () => { say(esc(s.skip), "me"); accept(""); } }]);
      if (s.pick) focusFirst(wrap); else input.focus({ preventScroll: true });
    });
  }
  function accept(v) {
    draft[STEPS[step].key] = v;
    step++;
    if (step < STEPS.length) ask(); else review();
  }
  function review() {
    form.hidden = true;
    later(() => {
      const rows = [["Name", draft.name], ["Phone", draft.phone], ["Email", draft.email], ["Interested in", draft.reason], ["Best time", draft.best_time], ["Note", draft.message]]
        .filter((r) => r[1]).map((r) => "<br><strong>" + r[0] + ":</strong> " + esc(r[1])).join("");
      say("Here is what I'll send to the office:" + rows);
      focusFirst(chips([
        { label: "Send request", main: true, go: send },
        { label: "Start over", go: startTour },
      ]));
    });
  }
  async function send() {
    const wait = say("Sending...");
    let res = null, out = {};
    try {
      res = await fetch("/api/tour", {
        method: "POST",
        headers: { "content-type": "application/json", accept: "application/json" },
        body: JSON.stringify(Object.assign({}, draft, {
          contact_pref: draft.email ? "Either" : "Phone call",
          page: location.pathname + " (assistant)",
          elapsed: Date.now() - started,
          no_medical: "yes",
          company_website: "",
        })),
      });
      out = await res.json().catch(() => ({}));
    } catch (_) { res = null; }
    wait.remove();
    if (res && res.ok && out.ok) {
      say("Thank you. Your request is with the office, and they will call you back. If it's urgent, call " + telLink() + ".");
      if (typeof window.gtag === "function") window.gtag("event", "generate_lead", { form: "assistant" });
      draft = {};
    } else if (res && res.status === 503) {
      say("Online requests are not switched on yet. Please call " + telLink() + " and the office will set up your visit.");
    } else {
      say(((out && out.error) ? esc(out.error) + " " : "Sorry, that didn't go through. ") + "Please call " + telLink() + ".");
    }
    menu();
  }

  function submit() {
    const v = input.value.trim();
    if (!v) return;
    input.value = "";
    say(esc(v), "me");
    if (mode === "tour") {
      const s = STEPS[step];
      if (s.ok && !s.ok(v)) { later(() => { say(esc(s.err)); input.focus({ preventScroll: true }); }); return; }
      accept(v);
    } else {
      later(() => answer(v));
    }
  }

  build();
  window.LegacyAssist = { open };
})();
