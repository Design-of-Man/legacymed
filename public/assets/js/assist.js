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
      '<div><p class="as-title" id="as-title">Legacy Medical</p><p class="as-sub">Quick answers and meet and greet requests</p></div>' +
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
      index();
      return true;
    } catch (_) { return false; }
  }

  /* ---- matching ------------------------------------------------------
     Every answer is scored against the question three ways: hand-picked
     keyword phrases (strongest), words shared with the answer's own
     question, and words shared with the answer text. Shared words count
     for more when they are rare across all answers (inverse document
     frequency), so "kidney" outweighs "doctor". Pages and articles are
     scored the same way so a question without a set answer still gets
     pointed at the right page. */
  const STOP = new Set("a an and are as at be but by can could do does for from had has have how i if in is it its me my of on or our please should so tell that the their them there they this to us was we what when where which who why will with would you your about any get got know much many want need just also into than then too very more most some does dont doesnt im ive id legacy medical practice office dr shtern yana doctor".split(" "));
  const SYN = { price: "fee", cost: "fee", costs: "fee", fees: "fee", charge: "fee", expensive: "fee", afford: "fee", pay: "fee",
    hours: "hour", open: "hour", closed: "hour", appointment: "visit", appointments: "visit", appt: "visit", see: "visit", seen: "visit",
    insurer: "insurance", insured: "insurance", coverage: "insurance", covered: "insurance", cover: "insurance",
    located: "location", address: "location", directions: "location", where: "location",
    mom: "parent", dad: "parent", mother: "parent", father: "parent", parents: "parent",
    kidneys: "kidney", renal: "kidney", pressure: "blood", bp: "blood", join: "member", joining: "member", membership: "member", members: "member" };
  const toks = (s) => String(s).toLowerCase().replace(/<[^>]+>/g, " ").replace(/[^a-z0-9 ]+/g, " ").split(/\s+/)
    .filter((w) => w && !STOP.has(w)).map((w) => {
      if (SYN[w]) return SYN[w];
      if (w.length > 5 && /ing$/.test(w)) w = w.slice(0, -3);
      else if (w.length > 4 && /ed$/.test(w)) w = w.slice(0, -2);
      if (w.length > 3 && /ies$/.test(w)) w = w.slice(0, -3) + "y";
      else if (w.length > 3 && /s$/.test(w) && !/ss$/.test(w)) w = w.slice(0, -1);
      return SYN[w] || w;
    });
  let IDF = {};
  function index() {
    const docs = D.faq.map((f) => new Set(toks((f.q || "") + " " + f.a)));
    const df = {};
    docs.forEach((d) => d.forEach((t) => { df[t] = (df[t] || 0) + 1; }));
    const n = docs.length;
    Object.keys(df).forEach((t) => { IDF[t] = Math.log(1 + n / df[t]); });
    D.faq.forEach((f) => { f._q = new Set(toks(f.q || "")); f._a = new Set(toks(f.a)); });
    D.pages.forEach((p) => { p._t = new Set(toks(p.t)); p._d = new Set(toks(p.d)); });
  }
  const w = (t) => IDF[t] || Math.log(1 + D.faq.length);
  function scoreFaq(f, ql, qt) {
    let s = 0;
    f.k.forEach((k) => { if (ql.indexOf(k) !== -1) s += 2 + k.length / 2; });
    qt.forEach((t) => { if (f._q.has(t)) s += 1.6 * w(t); else if (f._a.has(t)) s += 0.6 * w(t); });
    // A question that names something the visitor did not ask about ("North" Palm Beach) ranks a little lower.
    f._q.forEach((t) => { if (qt.indexOf(t) === -1) s -= 0.12 * w(t); });
    return s;
  }
  function scorePage(p, qt) {
    let s = 0;
    qt.forEach((t) => { if (p._t.has(t)) s += 1.4 * w(t); else if (p._d.has(t)) s += 0.5 * w(t); });
    return s;
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
      { label: "Book a meet and greet", main: true, go: startTour },
      { label: "Ask a question", go: startAsk },
      { label: "Call " + D.phone, go: () => { location.href = "tel:" + D.tel; } },
    ]));
  }
  function greet() {
    say("Hello. I can answer common questions about Legacy Medical, or set up a complimentary meet and greet with Dr. Shtern. What would you like to do?");
    menu();
  }

  /* ---------------------------------------------------------------- ask */
  function startAsk() {
    mode = "ask";
    form.hidden = false;
    later(() => {
      say("Ask anything about membership, fees and insurance, Dr. Shtern, kidney or blood pressure care, the meet and greet, or the office. I answer from the practice's own information.");
      focusFirst(chips(["What happens at the meet and greet?", "How much is membership?", "Do you take Medicare?", "Can I reach Dr. Shtern after hours?", "Where are you?", "Do you treat kidney disease?"].map((q) => ({
        label: q, go: () => { say(esc(q), "me"); later(() => answer(q)); },
      }))));
      input.focus({ preventScroll: true });
    });
  }
  function answer(q) {
    const ql = " " + q.toLowerCase().replace(/[^a-z0-9&' -]+/g, " ") + " ";
    const qt = [...new Set(toks(q))];
    let best = null, score = 0;
    D.faq.forEach((f) => {
      const s = scoreFaq(f, ql, qt);
      if (s > score) { score = s; best = f; }
    });
    const pages = D.pages.map((p) => [scorePage(p, qt), p]).filter((x) => x[0] >= 2.6).sort((a, b) => b[0] - a[0]);
    if (best && score >= 3) {
      let html = best.a;
      if (best.u && html.indexOf('href="' + best.u + '"') === -1 && best.u !== "/") html += ' <a href="' + best.u + '">Read more</a>.';
      const extra = pages.filter((x) => x[0] >= 4).map((x) => x[1]).filter((p) => html.indexOf('href="' + p.u + '"') === -1).slice(0, 2);
      if (extra.length) html += "<br><br>Related: " + extra.map((p) => '<a href="' + p.u + '">' + esc(p.t) + "</a>").join(" · ");
      say(html);
    } else if (pages.length) {
      say("I don't have a set answer for that, but these pages cover it:<br>" + pages.slice(0, 3).map((x) => '<a href="' + x[1].u + '">' + esc(x[1].t) + "</a>").join("<br>") +
          "<br><br>Or ask the office directly: " + telLink() + ".");
    } else {
      say("I don't want to guess on that one. The office can answer it: call " + telLink() + " (" + D.hours + ") or email <a href=\"mailto:" + D.email + "\">" + D.email + "</a>.");
    }
    chips([
      { label: "Book a meet and greet", main: true, go: startTour },
      { label: "Ask something else", go: () => input.focus({ preventScroll: true }) },
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
      pick: ["A meet and greet with Dr. Shtern", "Membership questions", "Kidney or blood pressure care", "Care for a parent", "Something else"] },
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
