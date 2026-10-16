/* Legacy Medical — site behaviour. No dependencies.
   Everything here is progressive: with JS off the pages are complete, the
   reveals are visible, the video simply never loads and the poster stays. */
(() => {
  "use strict";
  const doc = document.documentElement;
  const body = document.body;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const desktopNav = window.matchMedia("(min-width: 1101px)"); // keep in sync with site.css

  /* ---------- analytics shim: no-op unless GA4 was loaded with consent ---------- */
  const track = (name, params) => {
    if (typeof window.gtag === "function") window.gtag("event", name, params || {});
  };
  document.addEventListener("click", (e) => {
    const a = e.target.closest("a[href^='tel:'], a[href^='mailto:'], [data-track]");
    if (!a) return;
    if (a.matches("a[href^='tel:']")) track("call_click", { link_location: a.dataset.loc || "page" });
    else if (a.matches("a[href^='mailto:']")) track("email_click", { link_location: a.dataset.loc || "page" });
    else track(a.dataset.track, { link_location: a.dataset.loc || "page" });
  });

  /* ---------- header: a solid banner as soon as the page scrolls, always in view ---------- */
  const header = document.querySelector(".site-header");
  const hero = document.querySelector(".hero");
  const callbar = document.querySelector(".callbar");
  if (hero) body.classList.add("has-hero");
  let lastY = window.scrollY;
  let ticking = false;
  const onScroll = () => {
    const y = window.scrollY;
    const threshold = hero ? hero.offsetHeight - 120 : 24;
    header.classList.toggle("solid", y > 12);
    if (callbar) callbar.classList.toggle("show", y > (hero ? threshold * 0.6 : 400));
    // Nothing floats over the hero: the chat launcher waits until it is passed.
    body.classList.toggle("past-hero", !hero || y > threshold * 0.6);
    lastY = y;
    ticking = false;
  };
  window.addEventListener("scroll", () => {
    if (!ticking) { window.requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });

  onScroll();

  /* ---------- navigation ---------- */
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.getElementById("site-nav");
  const triggers = Array.from(document.querySelectorAll(".nav-trigger"));
  const closeMenus = (except) => {
    triggers.forEach((t) => {
      if (t === except) return;
      t.setAttribute("aria-expanded", "false");
      const m = document.getElementById(t.getAttribute("aria-controls"));
      if (m) m.classList.remove("open");
    });
  };
  const setNav = (open) => {
    body.classList.toggle("nav-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    if (!desktopNav.matches) nav.toggleAttribute("inert", !open);
    if (!open) closeMenus();
  };
  if (toggle && nav) {
    if (!desktopNav.matches) nav.setAttribute("inert", "");
    toggle.addEventListener("click", () => setNav(!body.classList.contains("nav-open")));
    desktopNav.addEventListener("change", (e) => {
      if (e.matches) { nav.removeAttribute("inert"); setNav(false); }
      else nav.toggleAttribute("inert", !body.classList.contains("nav-open"));
    });
  }
  triggers.forEach((t) => {
    t.addEventListener("click", (e) => {
      e.stopPropagation();
      const open = t.getAttribute("aria-expanded") !== "true";
      closeMenus(t);
      t.setAttribute("aria-expanded", String(open));
      const m = document.getElementById(t.getAttribute("aria-controls"));
      if (m) m.classList.toggle("open", open);
    });
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".nav-list > li")) closeMenus();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    const openTrigger = triggers.find((t) => t.getAttribute("aria-expanded") === "true");
    if (openTrigger) { closeMenus(); openTrigger.focus(); return; }
    if (body.classList.contains("nav-open")) { setNav(false); toggle.focus(); }
  });
  document.querySelectorAll(".nav-list li").forEach((li) => {
    li.addEventListener("focusout", (e) => {
      if (desktopNav.matches && !li.contains(e.relatedTarget)) {
        const t = li.querySelector(".nav-trigger");
        if (t) closeMenus();
      }
    });
  });

  /* ---------- videos: swap the poster for the player only on press ---------- */
  document.querySelectorAll(".vid[data-yt]").forEach((box) => {
    const btn = box.querySelector(".vid-play");
    if (!btn) return;
    btn.addEventListener("click", () => {
      const f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(box.dataset.yt) + "?autoplay=1&rel=0&playsinline=1";
      f.title = box.dataset.title || "Video";
      f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
      f.allowFullscreen = true;
      f.referrerPolicy = "strict-origin-when-cross-origin";
      box.replaceChildren(f);
      f.focus();
    });
  });

  /* ---------- reveal on scroll ---------- */
  const revealables = document.querySelectorAll("[data-reveal], .clock");
  if ("IntersectionObserver" in window && !reduceMotion.matches) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealables.forEach((el) => io.observe(el));
  } else {
    revealables.forEach((el) => el.classList.add("in"));
  }

  /* ---------- hero video ----------
     The poster is the LCP element and ships in the HTML. The video gets no
     <source> until after load, and only when the visitor's settings allow it:
     never under reduced motion or Save-Data. Phones get the portrait cut. */
  const video = document.querySelector(".hero-media video");
  const vToggle = document.querySelector(".hero-toggle");
  if (video && vToggle) {
    const conn = navigator.connection || {};
    const saveData = conn.saveData === true || /(^|-)2g$/.test(conn.effectiveType || "");
    let loaded = false;
    let wantPlay = false;
    const setToggle = (playing) => {
      vToggle.setAttribute("aria-pressed", String(playing));
      vToggle.querySelector(".t").textContent = playing ? "Pause" : "Play";
      vToggle.querySelector(".i-play").toggleAttribute("hidden", playing);
      vToggle.querySelector(".i-pause").toggleAttribute("hidden", !playing);
    };
    const attach = () => {
      if (loaded) return;
      loaded = true;
      const portrait = window.matchMedia("(max-aspect-ratio: 4/5)").matches;
      // Pick by the pixels the film actually fills, so it is never upscaled.
      const px = video.clientWidth * Math.min(window.devicePixelRatio || 1, 3);
      const set = portrait ? video.dataset.portrait : (px > 2400 ? video.dataset.uhd : px > 1600 ? video.dataset.qhd : video.dataset.hd);
      const [av1, hevc, avc] = set.split("|");
      const types = ['video/webm; codecs="av01.0.12M.10"', 'video/mp4; codecs="hvc1.1.6.L150.B0"', "video/mp4"];
      [av1, hevc, avc].forEach((src, i) => {
        const s = document.createElement("source"); s.src = src; s.type = types[i]; video.append(s);
      });
      video.load();
    };
    const play = () => {
      wantPlay = true;
      attach();
      const p = video.play();
      if (p && p.catch) p.catch(() => setToggle(false));
    };
    video.addEventListener("playing", () => { video.classList.add("playing"); setToggle(true); });
    video.addEventListener("pause", () => setToggle(false));
    vToggle.addEventListener("click", () => {
      if (video.paused) { play(); track("hero_video_play"); }
      else { wantPlay = false; video.pause(); }
    });
    const autoOK = !reduceMotion.matches && !saveData;
    vToggle.hidden = false;
    setToggle(false);
    if (autoOK) {
      const start = () => ("requestIdleCallback" in window ? requestIdleCallback(play, { timeout: 1500 }) : setTimeout(play, 300));
      if (document.readyState === "complete") start();
      else window.addEventListener("load", start, { once: true });
    }
    // Pause off-screen so a looping video never burns battery below the fold.
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(([en]) => {
        if (!loaded) return;
        if (!en.isIntersecting) { if (!video.paused) { video.pause(); wantPlay = true; } }
        else if (wantPlay && video.paused) video.play().catch(() => {});
      }, { threshold: 0.05 }).observe(video);
    }
  }

  /* ---------- practice photo reel ---------- */
  document.querySelectorAll(".reel").forEach((reel) => {
    const track_ = reel.querySelector(".reel-track");
    const btn = reel.querySelector(".reel-pause");
    if (!track_ || reduceMotion.matches) return;
    const group = track_.querySelector(".reel-group");
    const setSpeed = () => {
      const w = group.getBoundingClientRect().width;
      track_.style.setProperty("--reel-dur", Math.max(30, Math.round(w / 45)) + "s");
    };
    setSpeed();
    window.addEventListener("resize", setSpeed, { passive: true });
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(([en]) => track_.classList.toggle("running", en.isIntersecting), { rootMargin: "100px" }).observe(reel);
    } else track_.classList.add("running");
    if (btn) btn.addEventListener("click", () => {
      const paused = track_.classList.toggle("paused");
      btn.setAttribute("aria-pressed", String(paused));
      btn.setAttribute("aria-label", paused ? "Play photo reel" : "Pause photo reel");
      btn.querySelector(".i-play").toggleAttribute("hidden", !paused);
      btn.querySelector(".i-pause").toggleAttribute("hidden", paused);
    });
  });

  /* ---------- FAQ search ---------- */
  const faqSearch = document.getElementById("faq-q");
  if (faqSearch) {
    const items = Array.from(document.querySelectorAll(".faq details"));
    const status = document.getElementById("faq-status");
    faqSearch.addEventListener("input", () => {
      const q = faqSearch.value.trim().toLowerCase();
      let shown = 0;
      items.forEach((d) => {
        const hit = !q || d.textContent.toLowerCase().includes(q);
        d.hidden = !hit;
        if (hit) shown += 1;
        if (q && hit) d.open = true;
      });
      document.querySelectorAll(".faq-group").forEach((g) => {
        g.hidden = !g.querySelector("details:not([hidden])");
      });
      if (status) status.textContent = q ? shown + (shown === 1 ? " answer" : " answers") + " match" : "";
    });
  }

  /* ---------- journal filter ---------- */
  const chips = document.querySelectorAll(".chips button");
  if (chips.length) {
    const posts = document.querySelectorAll(".post-grid li, .post-list li");
    const more = document.querySelector("[data-more]");
    const LIMIT = 24;
    let cat = "all", expanded = false;
    const apply = () => {
      let n = 0;
      posts.forEach((p) => {
        const match = cat === "all" || p.dataset.cat === cat;
        p.hidden = !match || (cat === "all" && !expanded && n >= LIMIT);
        if (match) n++;
      });
      if (more) more.hidden = !(cat === "all" && !expanded && n > LIMIT);
    };
    chips.forEach((c) => c.addEventListener("click", () => {
      chips.forEach((o) => o.setAttribute("aria-pressed", String(o === c)));
      cat = c.dataset.cat;
      apply();
    }));
    if (more) more.addEventListener("click", () => {
      const first = [...posts].find((p) => p.hidden);
      expanded = true;
      apply();
      if (first) { const a = first.querySelector("a"); if (a) a.focus(); }
    });
    apply();
  }

  /* ---------- live Google reviews (only when the API is configured) ---------- */
  const live = document.querySelector("[data-live-reviews]");
  if (live && "fetch" in window) {
    fetch("/api/reviews", { headers: { accept: "application/json" } })
      .then((r) => (r.ok ? r.json() : null))
      .then((data) => {
        if (!data || !data.rating || !Array.isArray(data.reviews)) return;
        const esc = (s) => String(s).replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
        const badge = live.querySelector("[data-live-badge]");
        if (badge) {
          badge.innerHTML = '<b>' + esc(Number(data.rating).toFixed(1)) + '</b><span>Google rating from ' + esc(data.count) + ' reviews<br><span class="small muted">Live from Google</span></span>';
          badge.hidden = false;
        }
        const list = live.querySelector("[data-live-list]");
        const picks = data.reviews.filter((r) => r.text && r.rating >= 4).slice(0, 4);
        if (list && picks.length) {
          list.innerHTML = picks.map((r) =>
            '<figure class="quote"><blockquote><p>' + esc(r.text.length > 420 ? r.text.slice(0, 417).replace(/\s+\S*$/, "") + "…" : r.text) +
            '</p></blockquote><figcaption><b>' + esc(r.author) + '</b> · Google review' + (r.when ? ' · ' + esc(r.when) : '') + '</figcaption></figure>').join("");
        }
      })
      .catch(() => {});
  }
})();
