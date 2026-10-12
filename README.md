# Legacy Medical website

legacymedicalpalmbeach.com: concierge internal medicine with Dr. Yana Shtern, MD, Palm Beach Gardens, FL.

```bash
python3 build.py --check      # regenerate public/ and vercel.json
python3 _dev/preflight.py     # pre-deploy gate (exits non-zero on any blocker)
python3 _dev/verify.py        # every page in Chromium: axe, console, 404s, overflow
```

See CLAUDE.md for how the generator is organised and `_dev/OPEN-ITEMS.md` for what still needs the practice.
