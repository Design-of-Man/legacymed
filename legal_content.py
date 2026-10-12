"""Legal pages. The website privacy notice and accessibility statement were
written for this site. The Notice of Privacy Practices is the practice's
existing HIPAA notice, carried over from the old site (see npp_text.py)."""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))

PRIVACY = """
<p><strong>Effective October 10, 2026.</strong> This notice covers this website, legacymedicalpalmbeach.com. How Legacy Medical PLLC uses and protects your health information as a patient is described separately in our <a href="/notice-of-privacy-practices">Notice of Privacy Practices</a>.</p>
<h2>What we collect</h2>
<p>If you send a meet and greet or contact request, through the form or the site assistant, we receive what you type: your name, phone number, email address, what you are interested in, the best time to reach you, and any short note. The form asks you not to include medical details. Please follow that request; email and web forms are not the right place for health information.</p>
<p>Our hosting provider, Vercel, keeps standard server logs (such as IP address, browser type and the page requested) to deliver and protect the site.</p>
<h2>Analytics</h2>
<p>We may measure which pages are visited so we can improve the site. Google Analytics only loads if you choose "Allow" on the banner, and it never loads on pages that contain a form. We do not use advertising pixels, retargeting, session recording, or social media tracking, and we do not sell or share personal information for advertising.</p>
<p>The site may also use Vercel Web Analytics, which counts visits without cookies and without identifying individual visitors.</p>
<h2>How we use what you send</h2>
<p>We use form submissions only to reply to you and arrange a meet and greet or call. Submissions are delivered to the practice by email through our email provider. We do not add you to marketing lists.</p>
<h2>Maps and outside links</h2>
<p>Pages with a map load an embedded Google Map, and Google may set its own cookies when it does. The map does not receive anything you type into our forms. Links to other websites, such as hospital or review sites, are governed by those sites' own policies.</p>
<h2>Your choices</h2>
<p>You can clear your analytics choice by clearing this site's data in your browser. To ask what we hold about you from this website, or to have it deleted, contact us at <a href="mailto:info@legacymedicalpalmbeach.com">info@legacymedicalpalmbeach.com</a> or (561) 834-9280.</p>
<h2>Children</h2>
<p>This website is not directed to children under 13, and we do not knowingly collect information from them.</p>
<h2>Changes</h2>
<p>If we change this notice we will update the date at the top of this page.</p>
"""

ACCESSIBILITY = """
<p>Legacy Medical wants everyone to be able to use this website, including people who use screen readers, a keyboard alone, magnification or voice control.</p>
<h2>What we aim for</h2>
<p>This site is built to meet the Web Content Accessibility Guidelines (WCAG) 2.2 at level AA. Every page is checked with automated testing at phone, tablet and desktop sizes before it is published, and the site is designed to be used fully with a keyboard. Motion on the site, including the video and the photo reel, stops if your device is set to reduce motion, and both can be paused.</p>
<h2>No overlay widgets</h2>
<p>We do not use accessibility overlay plugins. We build the pages themselves to work with the assistive technology you already use.</p>
<h2>If something does not work</h2>
<p>If you have trouble with any part of this site, please call us at <a href="tel:+15618349280">(561) 834-9280</a> or email <a href="mailto:info@legacymedicalpalmbeach.com">info@legacymedicalpalmbeach.com</a>. Tell us the page and what happened, and we will help you get the information another way and fix the problem.</p>
<h2>The office</h2>
<p>Our office at 11380 Prosperity Farms Road, Suite 114, is on the first floor and is wheelchair accessible. If you need an accommodation for your visit, let us know when you call.</p>
"""


def _npp():
    path = os.path.join(_HERE, "npp_text.py")
    if os.path.exists(path):
        from npp_text import NPP_HTML
        return NPP_HTML
    return None


_npp_html = _npp()

LEGAL = {
    "privacy": {"title": "Website Privacy Notice | Legacy Medical", "crumb": "Website privacy", "eyebrow": "Privacy",
                "h1": "Website privacy notice", "lede": "What this website collects, and what it does not.",
                "desc": "How the Legacy Medical website handles information: meet and greet requests, consent-based analytics, no advertising pixels, and no tracking on form pages.",
                "body": PRIVACY},
    "accessibility": {"title": "Accessibility Statement | Legacy Medical", "crumb": "Accessibility", "eyebrow": "Accessibility",
                      "h1": "Accessibility statement", "lede": "",
                      "desc": "Legacy Medical's website accessibility statement: WCAG 2.2 AA, no overlay widgets, and how to reach us if any part of the site does not work for you.",
                      "body": ACCESSIBILITY},
}
if _npp_html:
    LEGAL["notice-of-privacy-practices"] = {
        "title": "Notice of Privacy Practices (HIPAA) | Legacy Medical", "crumb": "Notice of Privacy Practices", "eyebrow": "HIPAA",
        "h1": "Notice of Privacy Practices", "lede": "How Legacy Medical PLLC may use and disclose your medical information, and how you can get access to it.",
        "desc": "Legacy Medical PLLC's HIPAA Notice of Privacy Practices: how your medical information may be used and disclosed, and your rights as a patient.",
        "body": _npp_html}
