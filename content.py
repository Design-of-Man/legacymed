"""Page copy for Legacy Medical. Facts come from the practice's own sites, the
10 Oct 2026 audit, and source pages linked where each claim is used. Nothing
here is invented: where a fact is unconfirmed it is left out and listed in
_dev/OPEN-ITEMS.md instead.

House style (enforced by `python3 build.py --check`): no em dashes, no stock
phrases from the banned list in build.py, sentence-case headings."""

# ---------------------------------------------------------------- facts
GEO = {"lat": 26.844234, "lng": -80.0720754}  # OSM house-level match, 2026-10-10

SOCIALS = [  # only profiles the practice itself links. The old site's "Instagram" icon pointed at LinkedIn.
    {"label": "Legacy Medical on Facebook", "url": "https://www.facebook.com/legacymedicalpalmbeach", "icon": "facebook"},
]
CLINIC_SAME_AS = ["https://www.youtube.com/@LegacyMedicalConciergeofPa-i6d"]
# Instagram: the home page gets a "Follow along" section and the footer an icon
# as soon as the practice confirms its account. Left empty until then (never guess a handle).
INSTAGRAM = {"handle": "legacymedicalconcierge", "url": "https://www.instagram.com/legacymedicalconcierge/"}  # confirmed by the owner, Oct 16 2026
if INSTAGRAM["url"]:
    SOCIALS.append({"label": "Legacy Medical on Instagram", "url": INSTAGRAM["url"], "icon": "instagram"})
PRICE_RANGE = None  # fee not published; do not guess
HEALTH_PLANS = []

ONE_LINER = ("Legacy Medical is a Concierge Internal Medicine practice in Palm Beach Gardens, Florida. "
             "Dr. Yana Shtern, board-certified in Internal Medicine and Nephrology, keeps a small patient panel "
             "so members get same or next-business-day visits, appointments with time to talk, and phone access "
             "around the clock.")

DOCTOR = {
    "name": "Yana Shtern, MD",
    "title": "Concierge internist and nephrologist",
    "photo": "dr-yana-shtern",
    "npi": "1497940852",
    "license": "ME114615",
    "board_certs": ["Internal Medicine", "Nephrology"],
    "hospitals": [
        {"name": "Jupiter Medical Center", "url": "https://www.jupitermed.com/",
         "address": {"@type": "PostalAddress", "streetAddress": "1210 S Old Dixie Hwy", "addressLocality": "Jupiter", "addressRegion": "FL", "postalCode": "33458", "addressCountry": "US"}},
        {"name": "Palm Beach Gardens Medical Center", "url": "https://www.pbgmc.com/",
         "address": {"@type": "PostalAddress", "streetAddress": "3360 Burns Rd", "addressLocality": "Palm Beach Gardens", "addressRegion": "FL", "postalCode": "33410", "addressCountry": "US"}},
    ],
    "member_of": ["Continuing Medical Education Committee, Jupiter Medical Center"],
    "education": [
        {"name": "Stony Brook University", "college": True},
        {"name": "St. George's University School of Medicine", "college": True},
        {"name": "Maimonides Medical Center"},
    ],
    "knows_about": ["Internal Medicine", "Nephrology", "Hypertension", "Chronic kidney disease", "Electrolyte disorders",
                    "Kidney stones", "Preventive medicine", "Geriatric care"],
    "same_as": [
        "https://www.healthgrades.com/physician/dr-yana-shtern-gfc4n",
        "https://www.doximity.com/pub/yana-shtern-md",
        "https://www.jupitermed.com/find-a-physician/yana-shtern-md/",
        "https://health.usnews.com/doctors/yana-shtern-650087",
        "https://www.castleconnolly.com/top-doctors/yana-shtern-internal-medicine-62cc071652",
    ],
    "page_title": "Internist in Palm Beach Gardens | Dr. Yana Shtern, MD",
    "page_desc": ("Dr. Yana Shtern is a concierge internist in Palm Beach Gardens, double board-certified in Internal Medicine and "
                  "Nephrology. Her training, hospital affiliations and how she practices."),
    "hero_lede": ("Board-certified in Internal Medicine and in Nephrology, Dr. Shtern has practiced for close to twenty years, first in "
                  "New York City and now in Palm Beach Gardens, where she runs Legacy Medical as a small concierge practice."),
    "home_creds": [
        ("Board certification", "Internal Medicine and Nephrology, American Board of Internal Medicine"),
        ("Hospital affiliations", "Jupiter Medical Center and Palm Beach Gardens Medical Center"),
        ("In practice", "Close to twenty years, in New York City and Palm Beach County"),
        ("Recognition", "Castle Connolly Top Doctor since 2023"),
    ],
    "facts": [
        ("Board certification", "Internal Medicine and Nephrology (ABIM)"),
        ("Medical degree", "St. George's University School of Medicine, 2007"),
        ("Residency and fellowship", "Internal Medicine residency and Nephrology fellowship, Maimonides Medical Center, New York City"),
        ("Undergraduate", "BS in Pharmacology, Stony Brook University"),
        ("Hospital affiliations", "Jupiter Medical Center; Palm Beach Gardens Medical Center"),
        ("Committee work", "Continuing Medical Education Committee, Jupiter Medical Center"),
    ],
    "bio": [
        "What Dr. Shtern does in a day is Internal Medicine: physicals, blood pressure, cholesterol, diabetes, infections, the questions that come with getting older, and keeping track of everything a patient’s other doctors are doing. Her second board certification, in Nephrology, shapes how she does it. Kidney function and blood pressure affect nearly every medication decision, and she reads those numbers the way a kidney specialist does.",
        "Dr. Yana Shtern is a double board-certified Internist, Nephrologist and Hypertension specialist and she has been practicing medicine for nearly 20 years. She received a Bachelor of Science degree in Pharmacology from Stony Brook University. She then earned her medical degree from St. George’s University School of Medicine. Dr. Shtern completed both her Internal Medicine residency and Nephrology fellowship training at Maimonides Medical Center in New York City.",
        "Dr. Shtern holds American Board of Internal Medicine certifications in both Internal Medicine and Nephrology. Prior to her work as a concierge physician in Florida, Dr. Shtern ran a successful medical practice in New York City, as well as having served as a Medical Director of an outpatient hemodialysis center. Dr. Shtern also has extensive training and experience as an Interventional Nephrologist having performed a variety of percutaneous endovascular surgical procedures for hemodialysis and cancer patients in numerous outpatient office-based surgical centers across New York City for many years.",
        "Dr. Shtern has privileges at Jupiter Medical Center as well as Palm Beach Gardens Medical Center. She is also a member of the Continuing Medical Education Committee at Jupiter Medical Center.",
        "Dr. Shtern places an emphasis on providing compassionate &amp; complete preventative medical care for her patients using a detail-oriented and personally planned approach for every individual. The concierge model of medicine allows her to provide highly individualized and personalized medical care. Dr. Shtern believes that reaching optimal health requires an ongoing, strong patient-physician relationship built on trust and integrity. Her goal is to provide complete &amp; thorough healthcare of the highest standard while forming a life-long bond for health with each and every one of her patients.",
    ],
    "training_h": "From pharmacology to two board certifications",
    "timeline": [
        ("Stony Brook", "BS in Pharmacology", "Stony Brook University, New York."),
        ("2007", "Doctor of Medicine", "St. George's University School of Medicine."),
        ("NYC", "Residency and fellowship", "Internal Medicine residency and Nephrology fellowship at Maimonides Medical Center, New York City."),
        ("New York", "Private practice and dialysis", "Ran a private practice; medical director of an outpatient hemodialysis center; Interventional Nephrology."),
        ("Palm Beach", "Legacy Medical", "Concierge Internal Medicine in Palm Beach Gardens, with privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center."),
    ],
    "verify_intro": "Board certification, licensing and hospital privileges are public record. These are the places to check them:",
    "verify_links": [
        ("ABIM board certification lookup", "https://www.abim.org/verify-physician.aspx?type=id&id=310989", ""),
        ("Castle Connolly Top Doctor profile", "https://www.castleconnolly.com/top-doctors/yana-shtern-internal-medicine-62cc071652", "(Top Doctor since 2023)"),
        ("Jupiter Medical Center physician directory", "https://www.jupitermed.com/find-a-physician/yana-shtern-md/", ""),
        ("Healthgrades profile", "https://www.healthgrades.com/physician/dr-yana-shtern-gfc4n", "(Patient Favorite award)"),
        ("Doximity profile", "https://www.doximity.com/pub/yana-shtern-md", ""),
    ],
    "personal": "Dr. Shtern has been married for more than fifteen years and has two teenagers. When she is not at the office she is usually at hot yoga, out fishing, or cooking.",
}

TEAM = [
    {"name": "Dr. Yana Shtern, MD", "role": "Physician and founder", "photo": "dr-yana-shtern", "is_doctor": True,
     "bio": ["Board-certified in Internal Medicine and Nephrology. Dr. Shtern sees every member herself, from the annual physical to a same-day sick visit."],
     "link": "/dr-yana-shtern", "link_label": "Full background"},
    {"name": "Yan Konevsky, RN", "role": "Registered nurse and office manager", "photo": "yan-konevsky-rn-oct-2026",
     "creds": ["Registered Nurse", "BSN, Wagner College", "BBA in Finance, Hofstra University"],
     "bio": ["Yan runs the office and is a registered nurse. He holds a BSN from Wagner College and a BBA in finance from Hofstra University, and before Legacy Medical he managed an outpatient hemodialysis center in New York City.",
             ]},
]

TEAM_PAGE = {
    "title": "Our Team | Legacy Medical, Palm Beach Gardens",
    "desc": "Meet the small team at Legacy Medical in Palm Beach Gardens: Dr. Yana Shtern, MD, and Yan Konevsky, RN, who runs the office.",
    "h1": "A small office, on purpose.",
    "lede": "Legacy Medical is a small office, and that is deliberate. Fewer patients means the people here know yours by name.",
}

# ---------------------------------------------------------------- services (from the practice's own list)
SERVICES_INCLUDED = [
    {"name": "Same or next-business-day visits", "icon": "calendar", "text": "When something comes up, you are seen that day or the next business day, not in three weeks."},
    {"name": "Phone access around the clock", "icon": "phone", "text": "Members can reach the practice by phone 24 hours a day, 7 days a week, including weekends and holidays."},
    {"name": "Extended visits", "icon": "time", "text": "Appointments are long enough to cover everything on your list, with minimal time in the waiting room."},
    {"name": "The annual executive physical", "icon": "heart", "text": "A thorough yearly exam with lab work and an ECG, then time to go through the results together.", "schema": True, "procedure": True},
    {"name": "Lab draws in the office", "icon": "lab", "text": "Blood is drawn here, so there is no separate trip to a lab. Stool occult blood testing too.", "schema": True, "procedure": True},
    {"name": "ECGs in the office", "icon": "ecg", "text": "Electrocardiograms done during your visit, without a separate appointment elsewhere.", "schema": True, "procedure": True},
    {"name": "Rapid respiratory tests", "icon": "shield", "text": "In-office testing for flu A and B, COVID-19 and strep, so a sick visit ends with an answer.", "schema": True, "procedure": True},
    {"name": "Telehealth", "icon": "screen", "text": "Video visits when coming in is not practical, including for many follow-ups.", "schema": True},
    {"name": "Specialist coordination", "icon": "people", "text": "Dr. Shtern picks the specialist, makes the call, and keeps track of what they find.", "schema": True},
    {"name": "Medication management", "icon": "pill", "text": "One doctor keeping an eye on every prescription, dose and interaction.", "schema": True},
    {"name": "Chronic disease management", "icon": "gauge", "text": "Blood pressure, diabetes, cholesterol, kidney and thyroid care, followed closely between visits.", "schema": True},
    {"name": "Preventive care and advocacy", "icon": "home", "text": "Screenings on schedule, vaccines up to date, and someone on your side when the system gets complicated.", "schema": True},
]

CARD_BLURBS = {
    "concierge-medicine": "How membership works, what it includes, and what it does not.",
    "kidney-care": "A board-certified nephrologist who is also your internist: CKD, stones, electrolytes, creatinine that keeps creeping up.",
    "hypertension": "Blood pressure that will not come down, or comes down with side effects you do not like.",
    "geriatric-memory-care": "Care for older adults and the families who help them, including memory concerns.",
    "preventive-care": "Executive annual physicals, screenings, and no day at a hospital.",
    "telehealth": "Video visits for follow-ups, results and questions that do not need an exam.",
    "membership": "Meet Dr. Shtern first, then decide.",
    "insurance-and-fees": "What concierge medicine costs here: the concierge fee, and what your insurance still pays for.",
    "faq": "Answers about access, insurance, hospitals and joining.",
    "dr-yana-shtern": "Training, certifications and hospital affiliations.",
    "our-team": "Who answers when you call.",
}

# ---------------------------------------------------------------- home
HOME_TITLE = "Concierge Doctor in Palm Beach Gardens, FL | Legacy Medical"
HOME_DESC = ("Concierge doctor in Palm Beach Gardens: Dr. Yana Shtern, MD, board-certified in Internal Medicine and Nephrology. "
             "One patient at a time, 24/7 phone access.")

HERO_VIDEO = {
    # Juno Beach Pier drone clip (Juno.MP4 in Dropbox /kashuba, 2688x1512), the same shot as the RegenOrtho hero.
    # Same edit as RegenOrtho (slowed approach, dissolve over the exposure snap) but no grade; see _dev/video/PROVENANCE.md.
    # 1512 is the camera's native height, so uhd and qhd both get the 1512 set and are never upscaled.
    # Each set: AV1 webm | HEVC mp4 (Safari) | H.264 mp4 (last resort).
    "uhd": "/assets/video/juno-1512.webm|/assets/video/juno-1512-hevc.mp4|/assets/video/juno-1080.mp4",
    "qhd": "/assets/video/juno-1512.webm|/assets/video/juno-1512-hevc.mp4|/assets/video/juno-1080.mp4",
    "hd": "/assets/video/juno-1080.webm|/assets/video/juno-1080-hevc.mp4|/assets/video/juno-1080.mp4",
    "portrait": "/assets/video/juno-portrait.webm|/assets/video/juno-portrait-hevc.mp4|/assets/video/juno-portrait.mp4",
    "posters": {
        "a768": "/assets/video/juno-poster-768.avif", "a1280": "/assets/video/juno-poster-1280.avif",
        "w768": "/assets/video/juno-poster-768.webp", "w1280": "/assets/video/juno-poster-1280.webp",
        "j768": "/assets/video/juno-poster-768.jpg", "j1280": "/assets/video/juno-poster-1280.jpg",
        "pa": "/assets/video/juno-poster-portrait.avif", "pw": "/assets/video/juno-poster-portrait.webp", "pj": "/assets/video/juno-poster-portrait.jpg",
    },
}

HOME = {
    "kicker": "One-on-one concierge medicine · Palm Beach Gardens",
    "hero_lines": ["A medical practice", "where patients", "<em>come first</em>."],  # <em> is styled gold, upright: no italic font on the LCP path
    "hero_lede": "Dr. Yana Shtern keeps a very small practice on purpose and sees one patient at a time. Every member gets same or next business day visits, unhurried appointments, and a phone answered at any hour.",
    "problem_eyebrow": "The usual way",
    "problem_statement": "Fifteen minutes, a portal message, and a referral to someone you have never met.",
    "problem_lede": "Most primary care runs on volume. It is not that doctors stop caring. A schedule with thirty patients a day leaves no room to listen, to call you back, or to notice what changed since last year.",
    "problems": [
        ("Weeks to get in", "By the time there is an opening, you have either recovered or ended up at urgent care."),
        ("Nobody who knows the whole picture", "Five specialists, five portals, and no one doctor who has read all of it."),
        ("Questions that wait", "A message at 7 p.m. gets an answer in two days, from whoever is covering."),
    ],
    "guide_h": "One physician who knows your history, and has the time to use it.",
    "guide_body": "<p>Dr. Shtern trained in Internal Medicine and then in Nephrology, and is board-certified in both. That combination matters more than it sounds: kidney function and blood pressure shape almost every prescription an internist writes.</p><p>She started Legacy Medical so she could take on fewer patients and do more for each of them. You see her at every visit, and members can reach the practice by phone at any hour.</p>",
    # Centered statement between two practice photos (Private Medical's move).
    "manifesto": "One patient at a time. A <em>very</em> small practice on purpose, so there is time to listen, to follow up, and to pick up the phone.",
    # Why concierge matters. "Before" figures are published averages (GAO 2005; Medical Care 2021);
    # the "after" figures are Legacy Medical's own limits (client, Oct 2026): no more than 300 members,
    # no more than 8 patients a day, appointments of about an hour.
    "why_h": "Why concierge care <em>matters</em>",
    "why_lede": ("Most primary care physicians run on short appointments and a list of thousands of patients. Legacy Medical changes the arithmetic: "
                 "a small practice by design, so each member gets real time, quick access, and a physician who follows through."),
    "why_stats": [
        ("One", "patient at a time", "Dr. Shtern does not double-book. Your appointment time is yours alone."),
        ("2,700 → 300", "patients per doctor", "The average primary care practice carries about 2,700 patients. Legacy Medical takes no more than 300.", "Before: GAO, 2005"),
        ("26 → 8", "patients a day", "A typical primary care physician sees about 26 patients a day. Dr. Shtern sees no more than 8.", "Before: GAO, 2005"),
        ("18 min → 1 hr", "per appointment", "The average primary care visit lasts 18 minutes. A Legacy appointment runs about an hour, and longer when you need it.", "Before: Medical Care, 2021"),
        ("24/7", "phone access", "Members reach the practice at any hour, including weekends and holidays."),
    ],
    "manifesto_photos": [("reception-desk", "The front desk at Legacy Medical"), ("front-desk-scrubs", "At the Legacy Medical front desk")],
    # One-on-one care: every line traces to a confirmed fact in DOCTOR, HOME or SERVICES_INCLUDED.
    "personal_h": "Your doctor, <em>personally</em>",
    "personal_lede": "Concierge care here is one on one. The same physician, every time, with the time and the access to treat you as a person rather than an appointment slot.",
    "personal_photo": ("dr-shtern-desk", "Dr. Yana Shtern at her desk at Legacy Medical"),
    "personal": [
        ("The same doctor at every visit", "You see Dr. Shtern each time you come in, so the doctor in the room already knows your history."),
        ("One patient at a time", "She does not double-book. The time on your appointment is yours, long enough to cover everything on your list."),
        ("Seen when you need it", "Same or next business day visits when something comes up, and the practice answers the phone at any hour."),
        ("Results you go through together", "Labs and ECGs are done in the office, and she walks you through what the numbers mean."),
        ("With you in the hospital", "She holds privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center, and stays involved if you are admitted."),
    ],
    "included_h": "What membership <em>includes</em>",
    "included_lede": "An annual concierge fee covers access to Dr. Shtern. Office visits and tests are billed to your insurance, as they are now.",
    "clock_h": "The office keeps hours. Your access does not.",
    "clock_lede": "The office is open Monday to Friday. Outside those hours, members can still reach the practice by phone, at night, on weekends and on holidays.",
    "spec_h": "Internal Medicine, plus a <em>nephrologist's eye</em>",
    "spec_lede": "Every member gets complete primary care. These are the areas where Dr. Shtern's second specialty and experience add the most.",
    "specialties": [
        ("kidney-care", "Kidney care", "CKD, rising creatinine, kidney stones, electrolyte problems, and care for people on dialysis."),
        ("hypertension", "Hypertension", "Blood pressure that stays high on two or three medicines, or comes with side effects."),
        ("geriatric-memory-care", "Geriatric and memory care", "Healthy aging, memory concerns, and fewer, better prescriptions."),
        ("preventive-care", "Executive annual physicals", "Annual executive physical, with labs and ECG done here."),
        ("telehealth", "Telehealth", "Video visits for follow-ups, results and medication questions."),
    ],
    "plan_h": "Three steps, <em>no pressure</em>",
    "steps": [
        ("Book a meet and greet", "Call or send a request. We will find a time that suits you."),
        ("Meet Dr. Shtern", "A complimentary meet-and-greet at the office. Ask about anything: the fee, your conditions, how after-hours calls work."),
        ("Join and book your first visit", "If it is a fit, enroll and schedule your first patient visit. With your permission, the office requests your records from your previous doctor."),
    ],
    "agreement": "<strong>Your insurance still works here.</strong> The concierge fee covers access and the extra time. Office visits, labs and tests are billed to your insurance the way they are today.",
    "reviews_h": "What patients say on <em>Google</em>",
    "reviews_note": "Quoted as published on Google. More patient reviews:",
    "stakes_h": "Small changes are easier to catch early.",
    "stakes_body": "<p>A creatinine that creeps up a little each year, blood pressure that is fine in the office and high at home, a new medicine that does not sit well with an old one. In a rushed system these slip between visits.</p><p>With a doctor who knows your baseline, they come up in conversation instead of in the emergency room.</p>",
    "areas_h": "Close to Jupiter, Juno Beach and the Palm Beaches",
    "areas_lede": "The office sits on Prosperity Farms Road just north of PGA Boulevard, a short drive from most of northern Palm Beach County.",
}

HOME_FAQ = [
    ("How much is the concierge fee?", "<p>The fee is not posted online yet. Call the office at <a href=\"tel:+15618349280\">(561) 834-9280</a> and we will go through it, or ask at your meet and greet. Office visits and tests are still billed to your insurance.</p>"),
    ("Do you take insurance?", "<p>Yes, for visits and tests. Medicare, Aetna, Cigna and BlueCross BlueShield are among the plans the practice works with. The concierge fee itself is separate and is not billed to insurance. <a href=\"/insurance-and-fees\">How the fee and insurance fit together</a>.</p>"),
    ("Can I meet Dr. Shtern before joining?", "<p>Yes. Your first visit is a complimentary meet and greet. <a href=\"/meet-and-greet\">Book one here</a> or call.</p>"),
    ("Where is the office?", "<p>11380 Prosperity Farms Road, Suite 114, Palm Beach Gardens, FL 33410. It is a first-floor suite with accessible entry.</p>"),
]

# Verbatim, as published on Healthgrades and shown on the practice's old site.
# Reviewer names are not shown there, so none are shown here.
_HG = '<a class="inline-link" href="https://www.healthgrades.com/physician/dr-yana-shtern-gfc4n" rel="noopener" target="_blank">Healthgrades<span class="sr-only"> (opens in a new tab)</span></a>'
TESTIMONIALS = [
    {"quote": "I saw Dr. Shtern for a complicated health issue. She was amazing in every way. She identified the cause of my problem rather than only trying to treat my symptoms as the other doctors I saw did. Her bedside manner was great, she's really nice and caring, very smart, and went above and beyond for me. I wish more doctors here were like her. Thank you Dr. Shtern!!!", "who": "Patient review", "source_html": _HG + ", November 2019"},
    {"quote": "Dr. Shtern was highly recommended by a friend, and having just gone to see her myself, I can see why everyone raves about her. She is definitely the real deal. I'm always a nervous wreck when seeing a doctor but she made me feel very comfortable right from the start and patiently addressed my concerns.", "who": "Patient review", "source_html": _HG + ", October 2021"},
    {"quote": "Wonderful doctor! Dr. Shtern is extremely caring and professional. Takes the time to talk and explain everything. Highly recommended doctor.", "who": "Patient review", "source_html": _HG + ", November 2021"},
    {"quote": "I've been a patient for 3 months and I can attest that Dr. Shtern is a brilliant physician. She quickly saw a problem I had/have after exam and lab work that 2 other doctors dismissed and she made sure it was taken care off. Thank you doctor!", "who": "Patient review", "source_html": _HG + ", January 2023"},
]
# Google Business Profile: "Legacy Medical Concierge - Dr. Yana Shtern". Rating and count are a
# snapshot read from the public listing on Oct 16, 2026 and shown with that date; main.js replaces
# them with live figures whenever /api/reviews is configured. Never typed in by hand.
GOOGLE = {
    "place_id": "ChIJ9-heFHwr34gRt2Rs2caAsOY",
    "url": "https://www.google.com/maps/place/?q=place_id:ChIJ9-heFHwr34gRt2Rs2caAsOY",
    "rating": "5.0", "count": 45, "as_of": "October 2026",
}
# Verbatim Google reviews, names as the reviewers published them on Google. Each one was read from
# the listing on Oct 16, 2026 (date = month the review was posted).
GOOGLE_REVIEWS = [
    {"quote": "Dr. Shtern and her team are fantastic! Extremely knowledgeable, detailed, thoughtful, caring, and attentive. She is always communicating with other doctors and whenever there's an issue she is on top of it. Her office is beautiful, clean, and very efficiently run.", "who": "Rich Anderson", "when": "April 2026"},
    {"quote": "My mother and I are patients of Dr. Shtern and we are very pleased with the great level of care that we have received from her over the years. She knows all the best specialists in the community and is always in communication with our other doctors. She is a great communicator and her attention to details is second to none. We highly recommend Dr. Shtern.", "who": "Noah Forgione", "when": "February 2025"},
    {"quote": "Dr. Shtern is an outstanding doctor, very personable, thoughtful, and detailed. She takes time to learn about her patients and asks questions that help her understand her patients medical issues, concerns, and needs. I've seen many doctors in my life, and Dr. Yana Shtern is unquestionably one of the very best. I couldn't be happier that she's my primary care doctor, and I look forward to years of being in her care.", "who": "John Pearson", "when": "February 2025"},
    {"quote": "Dr. Yana Shtern is an exceptional physician. She is incredibly thorough and takes the time to deeply investigate each patient's condition before making a diagnosis. With her background in Nephrology, she is especially knowledgeable in managing hypertension and heart disease.", "who": "Ekaterina Simakova", "when": "April 2026"},
    {"quote": "Dr Shtern is a wonderful physician and a pleasure to work with. She is an excellent clinician and a compassionate person, with a deep commitment to her patients' needs. Her staff is efficient, attentive, and most competent. She's a superstar - Highest recommendation!!", "who": "Marc F. Matarazzo", "when": "January 2026"},
    {"quote": "Dr. Shtern is everything I can possibly ask for in a doctor. She's very attentive and caring. She's extremely knowledgeable in her work and takes her time to listen to my needs and always delivers great care.", "who": "Evelyn G", "when": "September 2024"},
]
RATING_LINKS = [
    {"label": "Google", "url": GOOGLE["url"]},
    {"label": "Healthgrades", "url": "https://www.healthgrades.com/physician/dr-yana-shtern-gfc4n"},
    {"label": "US News", "url": "https://health.usnews.com/doctors/yana-shtern-650087"},
]

# Practice photos only: Dr. Shtern, the team, the Palm Beach Gardens office.
# The 2020 "Concierge Medicine of Jupiter" shoot is left out: it shows an
# earlier location and unidentified people.
REEL = [
    {"stem": "reception-desk", "alt": "The reception desk and gold Legacy Medical sign"},
    {"stem": "dr-shtern-desk", "alt": "Dr. Yana Shtern at her desk"},
    {"stem": "yan-konevsky-rn-oct-2026", "alt": "Yan Konevsky, RN, office manager"},
    {"stem": "dr-yana-shtern", "alt": "Dr. Yana Shtern, MD"},
    {"stem": "reception-wall", "alt": "The Legacy Medical reception wall"},
    {"stem": "front-desk-scrubs", "alt": "At the Legacy Medical front desk"},
    {"stem": "dr-shtern-full", "alt": "Dr. Shtern at the front desk"},
]

# ---------------------------------------------------------------- concierge medicine
CONCIERGE = {
    "title": "What Is Concierge Medicine? How It Works | Legacy Medical",
    "desc": "What is concierge medicine, and how does it work? At Legacy Medical in Palm Beach Gardens: what membership includes, what insurance covers, and how it compares.",
    "eyebrow": "Concierge medicine",
    "h1": "Concierge medicine: primary care with fewer patients and more time.",
    "lede": "Concierge medicine is a simple trade. You pay an annual concierge fee, and in return the practice keeps its patient list small enough that you get your doctor's time and attention when you need them.",
    "included_lede": "Membership covers access to Dr. Shtern and the extra time. These are part of every membership.",
    "compare_lede": "Concierge practices vary. This is how Legacy Medical works, next to the high-volume model most people are used to.",
    "compare": [
        ("Getting an appointment", "Often weeks for a routine visit", "Same or next business day"),
        ("Who you see", "Whoever is available", "Dr. Shtern, every visit"),
        ("Length of a visit", "Often 15 minutes or less", "As long as the visit needs"),
        ("After hours", "Answering service or urgent care", "Phone access 24/7 for members"),
        ("Labs and ECG", "Separate trip to a lab", "Drawn and done in the office"),
        ("Specialists", "A referral slip and a phone number", "Dr. Shtern chooses, calls and follows up"),
        ("Hospital stays", "A hospitalist you have never met", "Your doctor has privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center"),
        ("Insurance", "Billed for visits and tests", "Still billed for visits and tests; the concierge fee is separate"),
    ],
    "sections": [
        ("Why the panel is small", "<p>A typical primary care doctor carries a list of two thousand patients or more. Concierge practices typically keep a few hundred. That is the whole idea: fewer patients means a schedule with room in it, so a same-day visit is normal rather than lucky, and a phone call gets returned by the doctor who knows you.</p><p>Dr. Shtern limits the number of members she takes on, and she sees one patient at a time.</p>"),
        ("What the fee does not cover", "<p>The concierge fee is not insurance. It does not pay for hospital stays, emergency care, specialists, imaging, or prescriptions. Keep your health insurance, including Medicare and any supplemental plan. Office visits and covered tests at Legacy Medical are billed to that insurance as usual.</p><p>If you are weighing the cost, the useful question is what the access is worth to you: how often you have waited weeks to be seen, or gone to urgent care because your doctor could not fit you in. <a href=\"/insurance-and-fees\">What concierge medicine costs here</a>.</p>"),
        ("Who it suits", "<p>Concierge care tends to suit people who want one doctor to keep track of everything: adults managing high blood pressure, kidney disease or diabetes; retirees and seasonal residents who want continuity between Florida and up north; busy professionals who cannot wait three weeks for an appointment; and adult children arranging care for a parent.</p><p>If your care is simple and your current doctor is easy to reach, you may not need a concierge practice. We will tell you that at your tour if it is true.</p>"),
        ("Concierge care and direct primary care", "<p>The two are often confused. Direct primary care practices usually replace insurance billing with a monthly fee and do not bill insurance at all. Legacy Medical is a concierge practice: the membership covers access, and your insurance is still billed for visits and tests.</p>"),
    ],
    "faqs": [
        ("What is concierge medicine?", "<p>A model of primary care where patients pay an annual concierge fee and the doctor keeps a much smaller patient list. The smaller list is what makes same-day visits, longer appointments and direct phone access possible.</p>"),
        ("Is concierge medicine worth it?", "<p>It depends on how you use your doctor. People who manage several conditions, see multiple specialists, travel, or simply want to reach their own doctor quickly tend to find it worthwhile. Come to a meet and greet and ask Dr. Shtern directly; she will be straight with you.</p>"),
        ("Do I still need health insurance?", "<p>Yes. The concierge fee does not replace insurance. You will still need coverage for hospital care, specialists, imaging, prescriptions and emergencies, and Legacy Medical bills your insurance for office visits and tests.</p>"),
        ("How many patients does Dr. Shtern see?", "<p>Far fewer than a typical practice. Legacy Medical takes no more than 300 members, and Dr. Shtern sees no more than eight patients a day, one at a time, never two booked into the same slot. Appointments run about an hour, and longer when your needs call for it.</p>"),
        ("Will I always see Dr. Shtern?", "<p>Yes. She is the physician for every member.</p>"),
    ],
    "about": [{"@type": "MedicalSpecialty", "name": "Primary care"}, {"@type": "Thing", "name": "Concierge medicine"}],
    "related": ["membership", "insurance-and-fees", "preventive-care"],
}

# ---------------------------------------------------------------- service pages
SERVICE_PAGES = {
    "kidney-care": {
        "title": "Nephrologist and Kidney Doctor in Palm Beach Gardens, FL",
        "desc": "Dr. Yana Shtern is a board-certified nephrologist and internist in Palm Beach Gardens: chronic kidney disease treatment, rising creatinine, stones and electrolytes.",
        "crumb": "Kidney care",
        "eyebrow": "Nephrology in Palm Beach Gardens",
        "h1": "A kidney doctor who is also your internist.",
        "lede": "Dr. Shtern is board-certified in Nephrology as well as Internal Medicine. For members, that means kidney problems are looked after by the same doctor who manages everything else, with no handoff in between.",
        "specialty": "Renal",
        "points": [
            ("kidney", "Chronic kidney disease", "Staging, slowing progression, and adjusting every medication for kidney function."),
            ("lab", "Abnormal lab results", "A rising creatinine, a falling eGFR, or protein in the urine, explained and followed."),
            ("gauge", "Electrolyte problems", "Low sodium, high potassium, and other imbalances that often come from medications."),
            ("shield", "Kidney stones", "Medical evaluation and prevention, so one stone does not turn into several."),
            ("heart", "Acute kidney injury", "Follow-up after a hospital stay or a sudden drop in kidney function."),
            ("people", "Dialysis experience", "Dr. Shtern was medical director of a hemodialysis center in New York."),
        ],
        "sections": [
            ("When to think about your kidneys", "<p>Kidney disease rarely causes symptoms until it is advanced. Most people find out from a routine blood test: a creatinine that is a little high, an eGFR that has dropped since last year, or protein in a urine sample. High blood pressure and diabetes are the two most common causes, and both are things an internist is already treating.</p><p>That is why it helps to have one doctor reading all of it. A blood pressure medicine, an anti-inflammatory for a sore knee, a contrast scan and a dehydrating summer can each nudge kidney function. Together they add up.</p>"),
            ("Chronic kidney disease treatment and follow-up", "<p>For members, kidney care is part of membership rather than a separate referral. Dr. Shtern reviews your labs over time, not just the latest result, checks every prescription against your kidney function, and explains what the numbers mean in plain language.</p><p>Labs are drawn in the office. If you need imaging, a procedure, or dialysis planning, she arranges it and stays involved. She holds privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center.</p>"),
            ("Conditions Dr. Shtern manages", "<ul><li>Chronic kidney disease, all stages</li><li>Acute kidney injury and recovery</li><li>Protein in the urine (proteinuria)</li><li>Kidney stones: medical evaluation and prevention</li><li>Sodium, potassium, calcium and other electrolyte disorders</li><li>Kidney effects of diabetes and high blood pressure</li><li>Medication dosing for reduced kidney function</li><li>Care for patients with end-stage kidney disease, drawing on her dialysis experience</li></ul>"),
        ],
        "faq_h": "Kidney care questions",
        "faqs": [
            ("When should I see a nephrologist?", "<p>Common reasons are an eGFR below 60 that persists, a rapid drop in kidney function, protein or blood in the urine, recurring kidney stones, or blood pressure that will not come under control. If you are a member, you do not need a separate referral: Dr. Shtern is board-certified in Nephrology.</p>"),
            ("What does eGFR mean?", "<p>Estimated glomerular filtration rate. It is calculated from your creatinine level, age and sex, and estimates how well your kidneys filter blood. Lower numbers mean less filtering, and a single low result is less important than the trend over time.</p>"),
            ("Can kidney disease be slowed?", "<p>Often, yes. Controlling blood pressure and blood sugar, choosing medications carefully, and avoiding things that strain the kidneys all help. Some newer medicines also slow progression for the right patients.</p>"),
            ("Do I need to be a member to see Dr. Shtern for kidney care?", "<p>Legacy Medical is a membership practice. Call the office to talk through your situation.</p>"),
        ],
        "about": ["Chronic kidney disease", "Acute kidney injury", "Proteinuria", "Kidney stones", "Electrolyte imbalance", "End-stage renal disease"],
        "related": ["hypertension", "preventive-care", "concierge-medicine"],
        "cta_h": "Questions about your kidney numbers?",
        "photo": "dr-shtern-full", "photo_alt": "Dr. Yana Shtern, board-certified nephrologist, at Legacy Medical",
    },
    "hypertension": {
        "title": "Hypertension Specialist in Palm Beach Gardens | Legacy Medical",
        "desc": "A high blood pressure doctor in Palm Beach Gardens: Dr. Yana Shtern, internist and nephrologist, for pressure that will not come down. Home readings, causes, fewer side effects.",
        "crumb": "Hypertension",
        "eyebrow": "Hypertension specialist care",
        "h1": "When blood pressure will not come down.",
        "lede": "High blood pressure is common and usually straightforward. When it is not, because the numbers stay high on several medicines, swing between home and office, or come with side effects, it helps to see a doctor who has spent a career on it.",
        "specialty": "Renal",
        "points": [
            ("gauge", "Resistant hypertension", "Pressure that stays high on three or more medicines."),
            ("heart", "Home and office mismatch", "White-coat readings, or the reverse: normal in the office, high at home."),
            ("lab", "Looking for a cause", "Kidney, hormone and medication causes that are easy to miss."),
            ("pill", "Simpler regimens", "Fewer pills, better timing, and fewer side effects."),
        ],
        "sections": [
            ("Why it gets complicated", "<p>The kidneys regulate salt and fluid, which is why blood pressure and kidney health are so closely linked, and why hypertension is part of Nephrology training. Some high blood pressure has a specific cause, such as narrowed kidney arteries, an adrenal gland that makes too much aldosterone, sleep apnea, or a medicine like an anti-inflammatory or a decongestant. Finding that cause can change the treatment completely.</p>"),
            ("How Dr. Shtern approaches it", "<p>It starts with good numbers. Office readings alone can mislead, so Dr. Shtern relies on accurate home readings and looks at the pattern rather than one visit. She reviews every medication and supplement, checks kidney function and electrolytes with labs drawn in the office, and looks for secondary causes when the history suggests one.</p><p>The goal is blood pressure that is controlled on a regimen you can live with. Because members can reach her directly, adjusting a dose does not have to wait for the next appointment.</p>"),
            ("Taking a good home reading", "<ol><li>Sit quietly for five minutes first, back supported, feet flat, arm resting at heart level.</li><li>Use a validated upper-arm cuff in the right size. Wrist cuffs are less reliable.</li><li>No caffeine, exercise or smoking in the 30 minutes before.</li><li>Take two readings a minute apart, morning and evening, and write both down.</li><li>Bring the log, or the cuff itself, to your visit.</li></ol>"),
        ],
        "faq_h": "Blood pressure questions",
        "faqs": [
            ("What blood pressure is too high?", "<p>Current American guidelines define high blood pressure as 130/80 or higher on repeated readings. A reading of 180/120 or higher, especially with chest pain, shortness of breath, weakness or vision changes, needs emergency care: call 911.</p>"),
            ("What is resistant hypertension?", "<p>Blood pressure that stays above goal despite three medicines from different classes at good doses, usually including a diuretic. It often has a fixable cause, which is why it deserves a closer look.</p>"),
            ("Why is my pressure higher at the doctor's office?", "<p>That is called white-coat hypertension, and it is common. Home readings or 24-hour monitoring show whether your pressure is high in everyday life, which is what matters for treatment.</p>"),
        ],
        "about": ["Hypertension", "Resistant hypertension", "White coat hypertension", "Secondary hypertension"],
        "related": ["kidney-care", "preventive-care", "telehealth"],
        "cta_h": "Bring your blood pressure log. We will read it with you.",
        "photo": "dr-shtern-desk", "photo_alt": "Dr. Yana Shtern at her desk in Palm Beach Gardens",
    },
    "geriatric-memory-care": {
        "title": "Geriatric Care Doctor in Palm Beach Gardens | Legacy Medical",
        "desc": "Geriatric care in Palm Beach Gardens and Jupiter from a concierge doctor: memory concerns, medication reviews, fall prevention, and families kept informed.",
        "crumb": "Geriatric and memory care",
        "eyebrow": "Geriatric medicine",
        "h1": "Care for older adults, and the people who help them.",
        "lede": "Getting older brings more prescriptions, more specialists, and more questions from family. A concierge practice suits this stage of life well: longer visits, one doctor coordinating everything, and someone who picks up the phone.",
        "specialty": "Geriatric",
        "points": [
            ("brain", "Memory concerns", "Cognitive screening, a careful look for reversible causes, and a plan."),
            ("pill", "Medication review", "Fewer pills where possible, and none that work against each other."),
            ("home", "Staying independent", "Falls, balance, hearing, vision and home safety, addressed early."),
            ("people", "Family in the loop", "With your permission, Dr. Shtern talks with the family members who help you."),
        ],
        "sections": [
            ("Memory and thinking", "<p>Forgetfulness worries people, and it deserves a proper evaluation rather than reassurance or alarm. Dr. Shtern starts with a cognitive screen and a careful history, often with a family member present, and checks for causes that can be treated: thyroid problems, low vitamin B12, medication side effects, poor sleep, depression, hearing loss, or an infection.</p><p>When a memory disorder is likely, she arranges the right specialist and imaging, and stays your doctor throughout. Care for memory concerns changes over time, and continuity matters.</p>"),
            ("Fewer, better prescriptions", "<p>Older adults are more sensitive to many medicines, and kidney function, which Dr. Shtern watches closely as a nephrologist, changes how many drugs should be dosed. A full review often finds a medication that can be stopped, a dose that can be lowered, or two prescriptions from two specialists that should not be taken together.</p>"),
            ("Help for families", "<p>Often the person arranging care is an adult child, sometimes living in another state. With the patient's written permission, Dr. Shtern can update family members, coordinate with home health and other doctors, and help everyone plan ahead. If your parent is hospitalized, she has privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center.</p>"),
        ],
        "faq_h": "Questions from families",
        "faqs": [
            ("My parent is forgetting things. Where do we start?", "<p>Start with a visit where there is time to take a full history and do a cognitive screen, ideally with you present. Several common causes of memory trouble are treatable, so it is worth checking properly.</p>"),
            ("Can you talk to me about my parent's care?", "<p>Yes, with your parent's written authorization. Once that is on file, Dr. Shtern can discuss their care with you directly.</p>"),
            ("Is a Medicare Annual Wellness Visit the same as a physical?", "<p>No. The Medicare Annual Wellness Visit is mostly a planning conversation and screening questionnaire. A physical includes an examination. Members get the annual executive physical; ask the office how Medicare billing applies to your visits.</p>"),
        ],
        "about": ["Dementia", "Mild cognitive impairment", "Polypharmacy", "Falls"],
        "related": ["preventive-care", "kidney-care", "concierge-medicine"],
        "cta_h": "Bring your parent, or your questions, to a meet and greet.",
        "photo": "dr-shtern-full", "photo_alt": "Dr. Yana Shtern at the Legacy Medical front desk",
    },
    "preventive-care": {
        "title": "Executive Physicals in Palm Beach Gardens | Annual Physical",
        "desc": "Executive physicals in Palm Beach Gardens: the annual executive physical, an extended exam with in-office labs and ECG, then time with Dr. Yana Shtern to go over results.",
        "crumb": "Preventive care and physicals",
        "eyebrow": "Executive annual physicals",
        "h1": "A physical with the time to mean something.",
        "lede": "Every member gets an annual executive physical: an extended exam with labs and an ECG done in the office, and a follow-up conversation about what the results mean for you.",
        "specialty": "PrimaryCare",
        "service_node": {"@type": "MedicalProcedure", "name": "Annual executive physical", "procedureType": "https://schema.org/NoninvasiveProcedure",
                         "description": "An extended annual physical examination with in-office blood work and electrocardiogram, followed by a results review with the physician."},
        "points": [
            ("time", "An extended visit", "Time for your history, your family's history, and every question on your list."),
            ("lab", "Labs drawn here", "Blood work and stool occult blood testing without a trip to an outside lab."),
            ("ecg", "ECG in the office", "An electrocardiogram as part of the physical."),
            ("calendar", "Screenings on schedule", "Colonoscopy, mammography, bone density and others, arranged and tracked."),
        ],
        "sections": [
            ("What the annual executive physical covers", "<p>The physical starts with a conversation: your history, your family's history, your medicines and supplements, sleep, exercise, and anything that has changed. Then a full examination, an ECG, and blood work drawn in the office.</p><p>When results are back, you and Dr. Shtern go through them together. You leave with a plan for the year: which screenings are due, what to watch, and what to change.</p>"),
            ("An executive-style exam, without the hospital day", "<p>Executive physical programs often run a full day at a hospital campus with a team you will not see again. The annual executive physical here covers the core of that work with your own physician, and Dr. Shtern adds imaging or specialist testing when your history or results call for it, rather than by default.</p>"),
            ("Screenings and vaccines", "<p>Dr. Shtern keeps track of what is due and when: colon cancer screening, mammograms, cervical screening, bone density, lung cancer screening for people with a smoking history, and adult vaccines. She arranges the ones done elsewhere and follows up on the results.</p>"),
        ],
        "faq_h": "Physical exam questions",
        "faqs": [
            ("What is included in an executive physical?", "<p>It varies by program. Most include an extended history and exam, thorough blood work, an ECG, and age-appropriate screenings. The annual executive physical here includes all of these, with further testing ordered when it is warranted.</p>"),
            ("Is the annual physical covered by insurance?", "<p>Many plans cover a yearly preventive exam and standard screening labs. Coverage varies, so ask the office how your plan applies. The concierge fee itself is separate from insurance.</p>"),
            ("Do I need to fast before my physical?", "<p>Often, yes, for certain blood tests. The office will tell you when you book.</p>"),
        ],
        "about": ["Preventive medicine", "Physical examination", "Cancer screening"],
        "related": ["concierge-medicine", "hypertension", "membership"],
        "cta_h": "Start with a meet and greet. Your first physical comes next.",
        "photo": "dr-yana-shtern", "photo_alt": "Dr. Yana Shtern, MD",
    },
    "telehealth": {
        "title": "Concierge Telehealth with Dr. Yana Shtern | Legacy Medical",
        "desc": "Concierge telehealth: video visits with Dr. Yana Shtern, your own doctor in Palm Beach Gardens, for follow-ups, lab results and medication questions.",
        "crumb": "Telehealth",
        "eyebrow": "Concierge telehealth",
        "h1": "See your doctor without the drive.",
        "lede": "Plenty of medical care does not need an exam table. For members, many follow-ups, lab reviews and medication questions can happen by video with Dr. Shtern.",
        "specialty": "PrimaryCare",
        "points": [
            ("screen", "Video visits", "Face to face with your own doctor, from home or the office."),
            ("lab", "Results reviews", "Go through lab results without driving in."),
            ("pill", "Medication check-ins", "Dose changes and side effects, discussed the same week."),
        ],
        "sections": [
            ("What works well by video", "<p>Reviewing lab results, adjusting blood pressure medicine based on your home readings, checking how a new prescription is going, and many simple sick visits are all well suited to a video call. Dr. Shtern will tell you when an in-person exam is the better choice, and with same or next-business-day appointments, that is rarely a long wait.</p>"),
            ("Traveling or out of state", "<p>Telemedicine rules depend on where you are when the visit happens, and physicians generally need a license in that state. If you spend part of the year outside Florida, ask the office how Dr. Shtern can help while you are away, and how she coordinates with doctors where you are.</p>"),
        ],
        "faq_h": "Telehealth questions",
        "faqs": [
            ("What do I need for a video visit?", "<p>A phone, tablet or computer with a camera and a reasonable internet connection. The office will send you what you need to join.</p>"),
        ],
        "about": [{"@type": "Thing", "name": "Telemedicine"}],
        "related": ["concierge-medicine", "hypertension", "preventive-care"],
        "photo": "dr-shtern-desk", "photo_alt": "Dr. Yana Shtern at her desk",
    },
}

CATEGORY_OWNERS = {  # journal category -> the page that owns the topic
    "Concierge medicine": ("concierge-medicine", "How concierge medicine works here"),
    "Prevention and screening": ("preventive-care", "Preventive care and the annual executive physical"),
    "Heart and blood pressure": ("hypertension", "Help for high blood pressure"),
    "Nutrition": ("preventive-care", "Preventive care and the annual executive physical"),
    "Medications": ("geriatric-memory-care", "Medication reviews"),
    "Infections and vaccines": ("faq", "Same-day sick visits and testing"),
    "Everyday health": ("concierge-medicine", "How concierge medicine works here"),
}

# ---------------------------------------------------------------- membership
MEMBERSHIP = {
    "title": "Concierge Medicine Membership in Palm Beach Gardens",
    "desc": "How to join Legacy Medical, a concierge medicine membership with Dr. Yana Shtern in Palm Beach Gardens. Start with a complimentary meet and greet, then decide.",
    "eyebrow": "Concierge membership",
    "h1": "Meet us first. Then decide.",
    "lede": "Joining starts with a conversation, not a contract. Visit the office, meet Dr. Shtern, and ask everything you want to know about how the practice works and what it costs.",
    "steps": [
        ("Book a meet and greet", "Use the request form or call (561) 834-9280. We will find a time that suits you."),
        ("Meet Dr. Shtern", "A complimentary meet-and-greet at the office. Bring your questions, and a family member if you like."),
        ("Enroll and book your first visit", "If it is a good fit, you enroll, we request your records, and you schedule your first patient visit."),
    ],
    "agreement": "<strong>Meet first, decide later.</strong> The meet and greet is complimentary, and joining is your decision to make afterward.",
    "sections": [
        ("What to bring to the meet and greet", "<p>Nothing. The meet and greet is simply a chance to see the office, meet Dr. Shtern, and decide whether the practice feels like the right fit. There is no paperwork and nothing to prepare. If you have questions, bring them along, and bring a family member if you like.</p>"),
        ("Who the practice is a good fit for", "<p>Adults who want one physician to know their whole history, people managing blood pressure, kidney disease, diabetes or several specialists, seasonal residents who want continuity, and families arranging care for a parent. Dr. Shtern is an internist: a physician trained in the care of adults.</p>"),
    ],
    "form_h": "Book a meet and greet",
    "form_lede": "Leave your details and the office will call or email you to set up a time. Prefer the phone? Call us during office hours.",
    "faqs": [
        ("Is the meet and greet really free?", "<p>Yes. The meet and greet is complimentary.</p>"),
        ("What does membership cost?", "<p>The fee is not posted online. Call the office or ask at your meet and greet and we will go through it in full. Insurance is still billed for visits and tests.</p>"),
        ("How many members does the practice take?", "<p>The panel is limited, which is what keeps same-day visits possible. Ask the office whether new members are being accepted right now.</p>"),
    ],
}

INSURANCE = {
    "title": "Concierge Medicine Cost and How It Works With Insurance",
    "desc": "How much does concierge medicine cost? How the concierge fee and your insurance, including Medicare and HSAs, work together at Legacy Medical in Palm Beach Gardens.",
    "eyebrow": "Insurance and fees",
    "h1": "What concierge medicine costs: a concierge fee, plus your insurance.",
    "lede": "Legacy Medical is a concierge practice that still works with insurance. The concierge fee pays for access and time. Your insurance pays for visits and tests, as it does now.",
    "sections": [
        ("The concierge fee", "<p>Members pay an annual fee directly to the practice. It covers what insurance does not pay for: a limited patient panel, same or next-business-day appointments, extended visits, 24/7 phone access and Dr. Shtern's time coordinating your care.</p><p>The fee is not published online yet. Call <a href=\"tel:+15618349280\">(561) 834-9280</a> or ask at your tour and the office will go through it with you.</p>"),
        ("What insurance still pays for", "<p>Office visits, lab work, ECGs and other covered services are billed to your health insurance. Plans the practice works with include Medicare, Aetna, Cigna and BlueCross BlueShield. Coverage, copays and deductibles depend on your plan, so check with the office before your first visit.</p><p>Keep your insurance. The membership does not cover hospital care, specialists, imaging, emergency care or prescriptions.</p>"),
        ("Medicare", "<p>Medicare does not pay concierge fees. If you have Medicare, the fee is separate, and covered services at your visits are billed to Medicare under its usual rules. Ask the office how this works for your plan, including any Medicare Advantage or supplemental coverage.</p>"),
    ],
    "faqs": [
        ("How much does concierge medicine cost here?", "<p>The annual concierge fee is not published online yet. Call the office at <a href=\"tel:+15618349280\">(561) 834-9280</a> or ask at your meet and greet and we will go through it. Office visits, labs and covered tests are billed to your insurance separately, as they are today.</p>"),
        ("How does concierge medicine work with insurance?", "<p>The concierge fee is paid directly to the practice and covers access and time. Office visits, lab work, ECGs and other covered services are billed to your health insurance, including Medicare, under your plan's usual rules.</p>"),
        ("Does insurance cover the concierge fee?", "<p>No. Health insurance, including Medicare, does not pay the concierge fee. It does pay for covered services at your visits.</p>"),
        ("Can I use an HSA or FSA for the fee?", "<p>Rules on using health savings or flexible spending accounts for concierge fees are not settled and depend on your plan. Ask your plan administrator or tax adviser before you count on it.</p>"),
        ("Is the concierge fee tax deductible?", "<p>That depends on your situation. A tax adviser can tell you whether it counts as a deductible medical expense for you.</p>"),
        ("Which insurance plans do you accept?", "<p>The practice works with Medicare, Aetna, Cigna and BlueCross BlueShield, among others. Plans change, so call the office to confirm yours.</p>"),
    ],
    "cta_lede": "We would rather explain the fee in person than post a number without context. Call the office, or come in for a meet and greet and ask.",
}

FAQ_PAGE = {
    "title": "Concierge Medicine FAQ: Is It Worth It? | Legacy Medical",
    "desc": "Is concierge medicine worth it? Answers about Legacy Medical in Palm Beach Gardens: appointments, after-hours calls, insurance, Medicare, hospitals and joining.",
    "h1": "Frequently asked questions.",
    "lede": "Straight answers about how the practice works. If your question is not here, call the office at (561) 834-9280.",
}

FAQ_GROUPS = [
    {"name": "Concierge medicine", "pairs": [
        ("Why choose concierge medicine?", "<p>Concierge medicine is a membership model: you pay an annual fee, the practice keeps its patient list small, and in return you get around-the-clock phone access, same or next-business-day appointments, and visits long enough to cover everything on your mind. It restores the relationship between physician and patient that a high-volume practice has no room for. <a href=\"/concierge-medicine\">How it works here</a>.</p>"),
        ("Is there a limit to how many people can join?", "<p>Yes. The practice limits membership to a small number of patients so that every patient gets as much time as they need. Appointments are never hurried: Dr. Shtern takes her time with each visit. Ask the office whether new members are being accepted right now.</p>"),
    ]},
    {"name": "Access and appointments", "pairs": [
        ("How quickly can I be seen?", "<p>Members are seen the same or next business day when something comes up. Routine visits are scheduled at a time that suits you.</p>"),
        ("Can I reach Dr. Shtern after hours?", "<p>Yes. Members have phone access to the practice 24 hours a day, 7 days a week. In an emergency, always call 911 first.</p>"),
        ("What is Dr. Shtern's availability?", "<p>The practice is available to members by phone 24/7. In-person visits are booked the same or next business day with little to no wait, and telehealth visits are available when coming in is not practical.</p>"),
        ("How long are visits?", "<p>As long as you need. Visits are not booked in 15-minute slots, so there is time to cover everything you came in for without feeling rushed.</p>"),
        ("Do you offer video visits?", "<p>Yes, for many follow-ups and results reviews. <a href=\"/telehealth\">About telehealth</a>.</p>"),
        ("What are the office hours?", "<p>Monday to Thursday 9:00 AM to 5:00 PM, Friday 9:00 AM to 2:00 PM. Closed on weekends, with member phone access around the clock.</p>"),
    ]},
    {"name": "Insurance and fees", "pairs": [
        ("How much does membership cost?", "<p>There is an annual concierge fee. It covers what insurance will not or may not pay for: the extended annual executive physical, health promotion, and much greater access to your physician. Office visits, services and tests are billed through your insurance, as in a traditional Internal Medicine practice. The fee itself is not published online. Call the office or ask at your meet and greet.</p>"),
        ("Is concierge medicine worth it?", "<p>It depends on how you use your doctor. People who manage several conditions, see multiple specialists, travel, or simply want to reach their own doctor quickly tend to find it worthwhile. Come to a meet and greet and ask Dr. Shtern directly; she will be straight with you. <a href=\"/concierge-medicine\">How concierge medicine works here</a>.</p>"),
        ("Do you bill insurance?", "<p>Yes, for office visits, labs and covered tests. Plans include Medicare, Aetna, Cigna and BlueCross BlueShield. <a href=\"/insurance-and-fees\">More on insurance and fees</a>.</p>"),
        ("Does Medicare pay the concierge fee?", "<p>No. Medicare does not cover concierge fees. Covered services at your visits are billed to Medicare as usual.</p>"),
    ]},
    {"name": "Care and coordination", "pairs": [
        ("Are labs done in the office?", "<p>Yes. Blood is drawn in the office, and ECGs, stool occult blood tests and rapid flu, COVID-19 and strep tests are done here too.</p>"),
        ("What happens if I need a specialist?", "<p>Dr. Shtern coordinates your care the way a quarterback runs a team. She chooses the specialist, contacts them, works with the specialists you already see, and follows up on what they find, so your care stays in one place.</p>"),
        ("How do I get prescription refills?", "<p>Refills for established patients are issued during regular office hours. Request them through the patient portal or by calling (561) 834-9280, and ask a few days before you run out so there is no gap in your medication.</p>"),
        ("Which hospitals does Dr. Shtern use?", "<p>She has privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center.</p>"),
        ("Do you treat kidney disease and high blood pressure?", "<p>Yes. Dr. Shtern is board-certified in Nephrology as well as Internal Medicine. See <a href=\"/kidney-care\">kidney care</a> and <a href=\"/hypertension\">hypertension</a>.</p>"),
        ("Is there a patient portal?", "<p>Yes. Ask the office for access when you join.</p>"),
    ]},
    {"name": "Joining", "pairs": [
        ("How do I join?", "<p>Start with a complimentary meet and greet with Dr. Shtern. <a href=\"/meet-and-greet\">Book a meet and greet</a> or call (561) 834-9280.</p>"),
        ("What happens to my medical records?", "<p>With your permission, the office requests them from your previous doctor when you join.</p>"),
        ("Where are you located?", "<p>11380 Prosperity Farms Road, Suite 114, Palm Beach Gardens, FL 33410, on the first floor. See <a href=\"/contact\">directions</a>.</p>"),
        ("Is the office easy to get to from where I live?", "<p>The office is in the heart of Palm Beach Gardens, and members come from Jupiter, Juno Beach, Tequesta, Hobe Sound, Stuart, North Palm Beach, Palm Beach and West Palm Beach. <a href=\"/areas-we-serve\">Drive times from each town</a>.</p>"),
    ]},
]

# ---------------------------------------------------------------- areas
AREAS_PAGE = {
    "title": "Concierge Medicine for Jupiter, Stuart and the Palm Beaches",
    "desc": "Legacy Medical's Palm Beach Gardens office serves Jupiter, North Palm Beach, Juno Beach, Tequesta, Palm Beach, West Palm Beach, Hobe Sound and Stuart. Drive times and routes.",
    "h1": "Most of North County is less than twenty minutes away.",
    "lede": "The office is on Prosperity Farms Road, just north of PGA Boulevard in Palm Beach Gardens. These are the towns members most often come from, with honest drive times.",
    "method_note": "Distances and drive times are estimates from the office to each town center, calculated with OpenStreetMap routing without traffic. In season, allow 20 to 50 percent longer.",
    "sections": [
        ("Seasonal residents", "<p>Many members split the year between Florida and somewhere else. Concierge care suits that well: one doctor keeps your records current, coordinates with your physicians up north, and is reachable by phone wherever you are.</p>"),
        ("Hospitals", "<p>Dr. Shtern holds privileges at two hospitals: Jupiter Medical Center, on Old Dixie Highway in Jupiter, and Palm Beach Gardens Medical Center, on Burns Road about two miles from the office. Which one is nearer depends on where you live.</p>"),
    ],
    "map_lede": "First-floor suite with accessible entry, a short drive east of I-95 and west of US-1.",
}

LOCATIONS = []      # built below from GEO_DATA
ALL_AREAS = []      # every town on the hub table, including Hobe Sound and Stuart

GEO_DATA = {
    "Jupiter": {"distance_mi": 7.7, "drive_min": 14, "route": "PGA Boulevard west, then Alternate A1A north into Jupiter; US-1 is the coastal alternative",
                "route_short": "Alt A1A or US-1", "hospital": "Jupiter Medical Center, 1210 S Old Dixie Hwy", "hospital_short": "Jupiter Medical Center"},
    "North Palm Beach": {"distance_mi": 2.6, "drive_min": 6, "route": "Prosperity Farms Road south, or PGA Boulevard east to US-1",
                         "route_short": "Prosperity Farms Rd or US-1", "hospital": "Palm Beach Gardens Medical Center, 3360 Burns Rd", "hospital_short": "Palm Beach Gardens Medical Center"},
    "Juno Beach": {"distance_mi": 3.5, "drive_min": 7, "route": "US-1 south to PGA Boulevard, then west to Prosperity Farms Road",
                   "route_short": "US-1", "hospital": "Jupiter Medical Center or Palm Beach Gardens Medical Center, about equally close", "hospital_short": "Either, about equal"},
    "Tequesta": {"distance_mi": 9.3, "drive_min": 17, "route": "US-1 south through Jupiter and Juno Beach to PGA Boulevard",
                 "route_short": "US-1", "hospital": "Jupiter Medical Center, 1210 S Old Dixie Hwy", "hospital_short": "Jupiter Medical Center"},
    "Palm Beach": {"distance_mi": 14.6, "drive_min": 23, "route": "Over the bridge to Okeechobee Boulevard, I-95 north to PGA Boulevard, then east",
                   "route_short": "Okeechobee Blvd and I-95", "hospital": "Palm Beach Gardens Medical Center, 3360 Burns Rd", "hospital_short": "Palm Beach Gardens Medical Center"},
    "West Palm Beach": {"distance_mi": 14.0, "drive_min": 21, "route": "I-95 north to PGA Boulevard, then east to Prosperity Farms Road",
                        "route_short": "I-95", "hospital": "Palm Beach Gardens Medical Center, 3360 Burns Rd", "hospital_short": "Palm Beach Gardens Medical Center"},
    "Hobe Sound": {"distance_mi": 18.4, "drive_min": 31, "route": "US-1 south past Jonathan Dickinson State Park, through Tequesta and Jupiter",
                   "route_short": "US-1", "hospital": "Jupiter Medical Center", "hospital_short": "Jupiter Medical Center"},
    "Stuart": {"distance_mi": 29.6, "drive_min": 39, "route": "Kanner Highway to I-95 south, exit PGA Boulevard east",
               "route_short": "I-95", "hospital": "Jupiter Medical Center", "hospital_short": "Jupiter Medical Center"},
    "Palm Beach Gardens": {"distance_mi": 1.2, "drive_min": 4, "route": "PGA Boulevard", "route_short": "PGA Blvd",
                           "hospital": "Palm Beach Gardens Medical Center", "hospital_short": "Palm Beach Gardens Medical Center"},
}

_LOC_COPY = {
    "jupiter": {
        "name": "Jupiter",
        "title": "Concierge Doctor for Jupiter, FL | Legacy Medical",
        "desc": "A concierge doctor about 15 minutes from Jupiter. Dr. Yana Shtern, internist, has privileges at Jupiter Medical Center and sees members the same or next business day.",
        "h1": "A concierge doctor for Jupiter, with Jupiter Medical Center privileges.",
        "lede": "From Jupiter the office is about 15 minutes south, down Alternate A1A or US-1. And if you ever need the hospital, Dr. Shtern has privileges at Jupiter Medical Center, which is likely the closest one to home.",
        "from_label": "central Jupiter",
        "sections": [
            ("Why Jupiter members drive south", "<p>Jupiter has good hospitals and plenty of physicians, but a same-week appointment with your own primary care doctor can still be hard to get. From Jupiter, Abacoa or Jupiter Farms, the drive down Alt A1A is about a quarter of an hour.</p><p>Many visits do not need the drive at all. Results reviews and many follow-ups happen by <a href=\"/telehealth\">video</a>.</p>"),
            ("If you are admitted to Jupiter Medical Center", "<p>Dr. Shtern holds privileges at Jupiter Medical Center on Old Dixie Highway and sits on its Continuing Medical Education Committee. If you are admitted, she can follow your care and talk with the hospital team, rather than leaving it to a doctor who has never met you.</p>"),
        ],
        "directions": "From central Jupiter, take Alternate A1A south to PGA Boulevard, head east, then turn north on Prosperity Farms Road. The office is on the left, Suite 114, first floor.",
        "faqs": [
            ("How far is Legacy Medical from Jupiter?", "<p>About 7.7 miles from central Jupiter, roughly 15 minutes without traffic.</p>"),
            ("Does Dr. Shtern have privileges at Jupiter Medical Center?", "<p>Yes. She also has privileges at Palm Beach Gardens Medical Center.</p>"),
        ],
    },
    "north-palm-beach": {
        "name": "North Palm Beach",
        "title": "Concierge Doctor for North Palm Beach | Legacy Medical",
        "desc": "A concierge doctor about six minutes from North Palm Beach. Same or next-day visits, labs in the office, and 24/7 phone access with Dr. Yana Shtern, internist.",
        "h1": "A concierge doctor six minutes from North Palm Beach.",
        "lede": "The office is just up Prosperity Farms Road from the village, close enough that a same-day sick visit is a short trip rather than an afternoon.",
        "from_label": "North Palm Beach",
        "sections": [
            ("Close enough for same-day care", "<p>When something comes up, members are seen the same or next business day. From North Palm Beach that means a short drive up Prosperity Farms Road or US-1, a visit with Dr. Shtern, and often a lab draw or rapid test before you leave.</p>"),
            ("Hospital care nearby", "<p>Palm Beach Gardens Medical Center on Burns Road is about two miles from the village, and Dr. Shtern holds privileges there. She also has privileges at Jupiter Medical Center.</p>"),
        ],
        "directions": "From North Palm Beach, head north on Prosperity Farms Road past PGA Boulevard. The office is at 11380 Prosperity Farms Road, Suite 114.",
        "faqs": [("How far is the office from North Palm Beach?", "<p>About 2.6 miles, roughly 6 minutes by car.</p>")],
    },
    "juno-beach": {
        "name": "Juno Beach",
        "title": "Concierge Doctor for Juno Beach, FL | Legacy Medical",
        "desc": "A concierge doctor about seven minutes from Juno Beach, between Jupiter Medical Center and Palm Beach Gardens Medical Center, where Dr. Shtern has privileges.",
        "h1": "A concierge doctor seven minutes from Juno Beach, with two hospitals close by.",
        "lede": "Juno Beach sits almost exactly between the two hospitals where Dr. Shtern has privileges, and the office is a short drive down US-1 and across PGA Boulevard.",
        "from_label": "Juno Beach",
        "sections": [
            ("Care for year-round and seasonal residents", "<p>If you live in Juno Beach part of the year, concierge care keeps your records current with one doctor, and phone access continues when you are away. Dr. Shtern coordinates with your physicians in other states when you need it.</p>"),
            ("Two hospitals, one doctor", "<p>Jupiter Medical Center and Palm Beach Gardens Medical Center are each about four miles from Juno Beach. Dr. Shtern has privileges at both, so she can stay involved whichever one you are taken to.</p>"),
        ],
        "directions": "From Juno Beach, take US-1 south to PGA Boulevard, turn west, then north on Prosperity Farms Road to Suite 114.",
        "faqs": [("How far is Legacy Medical from Juno Beach?", "<p>About 3.5 miles, around 7 minutes without traffic.</p>")],
    },
    "tequesta": {
        "name": "Tequesta",
        "title": "Concierge Doctor and Private Physician for Tequesta, FL",
        "desc": "A concierge doctor and private physician for Tequesta, about 17 minutes south in Palm Beach Gardens. Dr. Yana Shtern has privileges at nearby Jupiter Medical Center.",
        "h1": "A concierge doctor and private physician for Tequesta, a short drive down US-1.",
        "lede": "From Tequesta the office is about 17 minutes south on US-1. Jupiter Medical Center, where Dr. Shtern has privileges, is closer still.",
        "from_label": "Tequesta",
        "sections": [
            ("Worth the drive, and often no drive", "<p>Members come from Tequesta and Jupiter Inlet Colony for unhurried visits, labs done in the office and a doctor who returns calls. Plenty of follow-ups happen by <a href=\"/telehealth\">video</a>, which saves the trip altogether.</p>"),
            ("If you need the hospital", "<p>Jupiter Medical Center is the nearest hospital to most of Tequesta, about three miles away. Dr. Shtern holds privileges there and at Palm Beach Gardens Medical Center.</p>"),
        ],
        "directions": "From Tequesta, follow US-1 south through Jupiter and Juno Beach to PGA Boulevard, turn west, then north on Prosperity Farms Road.",
        "faqs": [("How long is the drive from Tequesta?", "<p>About 9 miles, roughly 17 minutes without traffic, longer in season.</p>")],
    },
    "palm-beach": {
        "name": "Palm Beach",
        "title": "Concierge Doctor for Palm Beach, FL | Legacy Medical",
        "desc": "A concierge doctor for Palm Beach island residents: Dr. Yana Shtern, board-certified in Internal Medicine and Nephrology, about 25 minutes north in Palm Beach Gardens.",
        "h1": "Concierge medicine for Palm Beach, without the island waitlist.",
        "lede": "Palm Beach has plenty of concierge practices, and many are full. Legacy Medical is about 25 minutes north, and its physician is double board-certified in Internal Medicine and Nephrology.",
        "from_label": "the town of Palm Beach",
        "sections": [
            ("A different kind of credential", "<p>Most concierge internists are trained in Internal Medicine alone. Dr. Shtern is also board-certified in Nephrology and was medical director of a dialysis center, which makes a difference for anyone managing high blood pressure, kidney disease, or a long list of medications.</p>"),
            ("Making the drive easy", "<p>Many visits happen by <a href=\"/telehealth\">video</a>. For the rest, the office is a first-floor suite with accessible entry and minimal time in the waiting room.</p>"),
        ],
        "directions": "From Palm Beach, cross to Okeechobee Boulevard, take I-95 north to PGA Boulevard, head east, then north on Prosperity Farms Road.",
        "faqs": [("Do you see patients who live on Palm Beach island?", "<p>Yes. The office is roughly 25 minutes from the island without traffic.</p>")],
    },
    "west-palm-beach": {
        "name": "West Palm Beach",
        "title": "Concierge Medicine for West Palm Beach | Legacy Medical",
        "desc": "Concierge medicine for West Palm Beach residents from a doctor who is also a nephrologist, about 20 minutes up I-95 in Palm Beach Gardens. Same or next-day visits.",
        "h1": "A concierge doctor twenty minutes up I-95 from West Palm Beach.",
        "lede": "For West Palm Beach residents, the office is a straight run up I-95 to PGA Boulevard. Members are seen the same or next business day.",
        "from_label": "downtown West Palm Beach",
        "sections": [
            ("Internist and nephrologist", "<p>Dr. Shtern is board-certified in Internal Medicine and Nephrology. If you are managing kidney disease, hard-to-control blood pressure or electrolyte problems, you get both kinds of care from one doctor. See <a href=\"/kidney-care\">kidney care</a> and <a href=\"/hypertension\">hypertension</a>.</p>"),
            ("When you cannot come in", "<p>Many follow-ups, lab reviews and medication checks happen by <a href=\"/telehealth\">video visit</a>, and members can reach the practice by phone at any hour.</p>"),
        ],
        "directions": "Take I-95 north to the PGA Boulevard exit, head east, then turn north on Prosperity Farms Road to Suite 114.",
        "faqs": [("How far is Legacy Medical from West Palm Beach?", "<p>About 14 miles from downtown, roughly 21 minutes without traffic.</p>")],
    },
    # Added Oct 17, 2026: the practice has patients from both towns (client). Distances and routes are GEO_DATA's.
    "hobe-sound": {
        "name": "Hobe Sound",
        "title": "Concierge Doctor for Hobe Sound, FL | Legacy Medical",
        "desc": "A concierge doctor for Hobe Sound, about 30 minutes south on US-1 in Palm Beach Gardens. Dr. Yana Shtern, internist, sees members the same or next business day.",
        "h1": "A concierge doctor for Hobe Sound, about half an hour down US-1.",
        "lede": "Legacy Medical already cares for patients from Hobe Sound. The office is about 30 minutes south on US-1, and many follow-ups happen by video, so not every visit means the drive.",
        "from_label": "Hobe Sound",
        "sections": [
            ("Fewer trips, more time when you come", "<p>When you do come in, visits are unhurried, and labs and ECGs are done in the office, so one trip covers what might otherwise take several. Results reviews, medication checks and many follow-ups happen by <a href=\"/telehealth\">video</a>, and members can reach the practice by phone at any hour.</p>"),
            ("If you need the hospital", "<p>Of the hospitals Dr. Shtern is affiliated with, Jupiter Medical Center is the nearer one to Hobe Sound, on the way down US-1. She is also affiliated with Palm Beach Gardens Medical Center.</p>"),
        ],
        "directions": "From Hobe Sound, take US-1 south past Jonathan Dickinson State Park and through Tequesta and Jupiter to PGA Boulevard, turn west, then north on Prosperity Farms Road to Suite 114.",
        "faqs": [("How far is Legacy Medical from Hobe Sound?", "<p>About 18 miles, roughly 31 minutes without traffic, longer in season.</p>")],
    },
    "stuart": {
        "name": "Stuart",
        "title": "Concierge Doctor for Stuart, FL | Legacy Medical",
        "desc": "Concierge medicine for Stuart residents, about 40 minutes down I-95 in Palm Beach Gardens, from a doctor board-certified in Internal Medicine and Nephrology.",
        "h1": "Concierge medicine for Stuart, a straight run down I-95.",
        "lede": "Legacy Medical already cares for patients from Stuart. The office is about 40 minutes south by I-95, and video visits and around-the-clock phone access mean much of your care does not need the drive.",
        "from_label": "Stuart",
        "sections": [
            ("Internist and nephrologist", "<p>Dr. Shtern is board-certified in Internal Medicine and Nephrology, so if you are managing kidney disease, hard-to-control blood pressure or a long medication list, you get both kinds of care from one doctor. See <a href=\"/kidney-care\">kidney care</a> and <a href=\"/hypertension\">hypertension</a>.</p>"),
            ("Making the distance work", "<p>Many follow-ups, lab reviews and medication checks happen by <a href=\"/telehealth\">video visit</a>. When you come in, labs are drawn in the office, so there is no separate trip to a lab.</p>"),
        ],
        "directions": "From Stuart, take Kanner Highway to I-95 south, exit at PGA Boulevard and head east, then turn north on Prosperity Farms Road to Suite 114.",
        "faqs": [("How far is Legacy Medical from Stuart?", "<p>About 30 miles, roughly 39 minutes without traffic.</p>")],
    },
}

for slug, copy in _LOC_COPY.items():
    g = GEO_DATA[copy["name"]]
    d = dict(copy)
    d.update({"slug": slug, "distance_mi": g["distance_mi"], "drive_min": g["drive_min"], "route": g["route"], "hospital": g["hospital"]})
    LOCATIONS.append(d)
LOCATIONS.sort(key=lambda l: l["drive_min"])
for name, g in sorted(GEO_DATA.items(), key=lambda kv: kv[1]["drive_min"]):
    slug = next((s for s, c in _LOC_COPY.items() if c["name"] == name), None)
    ALL_AREAS.append({"name": name, "slug": slug, **g})

# ---------------------------------------------------------------- contact + journal
CONTACT_TITLE = "Contact Legacy Medical | (561) 834-9280, Palm Beach Gardens"
CONTACT_DESC = "Call (561) 834-9280 or visit Legacy Medical at 11380 Prosperity Farms Road, Suite 114, Palm Beach Gardens, FL 33410. Office hours, directions and a contact form."
CONTACT_LEDE = "The quickest way to reach us is by phone during office hours. Members have phone access around the clock."
DIRECTIONS = "From I-95, take the PGA Boulevard exit east, then turn north on Prosperity Farms Road. From US-1, head west on PGA Boulevard and turn north. Suite 114 is on the first floor and is wheelchair accessible."

JOURNAL_LEDE = "Articles from the practice on blood pressure, kidney health, prevention and getting the most out of your care. General information, not advice for your situation."
JOURNAL_DESC = "Health articles from Legacy Medical, a Concierge Internal Medicine practice in Palm Beach Gardens: blood pressure, kidney health, nutrition, prevention and more."

LEGAL = {}  # privacy, notice-of-privacy-practices, accessibility: see legal_content.py
from legal_content import LEGAL  # noqa: E402,F811


def llms_txt(P, D, pages, url):
    lines = [
        "# Legacy Medical",
        "",
        "> " + ONE_LINER,
        "",
        "## Facts",
        "- Practice: Legacy Medical (legal name Legacy Medical PLLC), Concierge Internal Medicine",
        "- Physician: Dr. Yana Shtern, MD. Board-certified (ABIM) in Internal Medicine and Nephrology.",
        "- Hospital affiliations: Jupiter Medical Center; Palm Beach Gardens Medical Center",
        "- Address: %s, %s, %s %s" % (P["street"], P["city"], P["region"], P["postal"]),
        "- Phone: %s. Fax: %s. Email: %s" % (P["phone"], P["fax"], P["email"]),
        "- Hours: Monday to Thursday 9:00 AM to 5:00 PM; Friday 9:00 AM to 2:00 PM; closed Saturday and Sunday. Members have 24/7 phone access.",
        "- Model: annual concierge fee (not covered by insurance) plus insurance billing for visits and tests. Plans include Medicare, Aetna, Cigna, BlueCross BlueShield. The fee is not published; call the office.",
        "- How to join: a complimentary meet and greet with Dr. Shtern. Call or book at %s" % url("meet-and-greet"),
        "- Areas served: " + ", ".join(P["service_area"]) + ", Martin County",
        "- Internal Medicine: care for adults.",
        "- Previous domain: cmedjupiter.com was an older copy of this site. legacymedicalpalmbeach.com is the current, authoritative site.",
        "",
        "## Pages",
    ]
    for pg in pages:
        if pg["slug"].startswith("blog/"):
            continue
        lines.append("- [%s](%s): %s" % (pg["title"], url(pg["slug"]), pg["desc"]))
    lines += ["", "## Blog"]
    for pg in pages:
        if pg["slug"].startswith("blog/"):
            lines.append("- [%s](%s)" % (pg["title"].replace(" | Legacy Medical", ""), url(pg["slug"])))
    return "\n".join(lines) + "\n"

# ---------------------------------------------------------------- assistant
# The site assistant (assets/js/assist.js) answers from set text only: no AI,
# no outside service. build.py turns FAQ_GROUPS plus the extras below into
# public/assets/assist.json. Each FAQ question needs keywords here; build
# fails if one is missing, so a new FAQ can never be silently unanswerable.
ASSIST_KEYWORDS = {
    "How quickly can I be seen?": ["seen", "same day", "same-day", "next day", "how soon", "how quickly", "how fast", "get an appointment", "get in", "wait"],
    "Can I reach Dr. Shtern after hours?": ["after hours", "after-hours", "night", "weekend", "24/7", "24 hours", "reach dr", "cell phone"],
    "How long are visits?": ["how long", "visit length", "minutes", "rushed"],
    "Do you offer video visits?": ["video", "telehealth", "virtual", "zoom", "remote"],
    "What are the office hours?": ["hour", "open", "close", "friday", "monday", "when are you"],
    "How much does membership cost?": ["cost", "price", "fee", "how much", "expensive", "annual", "afford"],
    "Is concierge medicine worth it?": ["worth it", "is it worth", "worthwhile", "worth the"],
    "Do you bill insurance?": ["insurance", "aetna", "cigna", "blue cross", "bluecross", "bcbs", "covered", "coverage", "bill", "take medicare", "accept medicare", "medicare patients", "my plan"],
    "Does Medicare pay the concierge fee?": ["medicare pay", "medicare cover", "does medicare", "medicare and the fee", "medicare fee"],
    "Are labs done in the office?": [" lab", "blood", "draw", "ecg", "ekg", "test", "covid", "flu", "strep"],
    "What happens if I need a specialist?": ["specialist", "referral", "refer", "cardiologist", "dermatologist"],
    "Which hospitals does Dr. Shtern use?": ["hospital", "jupiter medical", "gardens medical", "admitted", "privileges"],
    "Do you treat kidney disease and high blood pressure?": ["kidney", "nephrolog", "blood pressure", "hypertension", "renal"],
    "Is there a patient portal?": ["portal", "message", "online access", "records online"],
    "How do I join?": ["join", "sign up", "enroll", "become a patient", "new patient", "accepting", "tour", "meet", "greet", "first visit", "consultation"],
    "What happens to my medical records?": ["records", "transfer", "previous doctor", "chart"],
    "Where are you located?": ["where", "address", "located", "location", "directions", "parking", "find you"],
    "Why choose concierge medicine?": ["why concierge", "why choose", "worth it", "benefit", "advantage", "subscription", "relationship"],
    "Is there a limit to how many people can join?": ["limit", "how many patients", "how many members", "panel", "full", "waiting list", "waitlist"],
    "What is Dr. Shtern's availability?": ["availability", "available", "reach the doctor", "get hold"],
    "How do I get prescription refills?": ["refill", "prescription", "pharmacy", "medication", "renew"],
    "Is the office easy to get to from where I live?": ["easy to get", "how far", "far from", "accessible from", "near me", "close to me"],
}

ASSIST_EXTRA = [
    {"k": ["emergency", "911", "chest pain", "can't breathe", "stroke", "urgent"],
     "a": "If this is an emergency, call 911 now. This assistant is not monitored. Members with an urgent question can call the practice at (561) 834-9280 at any hour."},
    {"k": ["phone number", "your number", "telephone", "contact you", "how do i contact", "email address"],
     "a": "Call (561) 834-9280 or email info@legacymedicalpalmbeach.com. The fax is (561) 834-9279."},
    {"k": ["dr. shtern", "dr shtern", "shtern", "doctor", "who is", "physician", "credentials", "board"],
     "a": "Dr. Yana Shtern, MD is board-certified in Internal Medicine and Nephrology. She has privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center. <a href=\"/dr-yana-shtern\">About Dr. Shtern</a>."},
    {"k": ["concierge", "what is", "how does it work", "difference", "membership include", "included", "what do i get"],
     "a": "Concierge medicine means a smaller practice: same or next business day visits, unhurried appointments, and phone access to the practice around the clock. <a href=\"/concierge-medicine\">How it works here</a>."},
    {"k": ["area", "serve", "jupiter", "tequesta", "juno", "north palm", "palm beach", "stuart", "hobe sound"],
     "a": "Members come from across North County: Jupiter, Juno Beach, Tequesta, North Palm Beach, Palm Beach and West Palm Beach, plus Hobe Sound and Stuart. <a href=\"/areas-we-serve\">Areas and drive times</a>."},
    {"k": ["physical", "annual exam", "checkup", "check-up", "preventive", "screening"],
     "a": "Members get the annual executive physical: a thorough yearly exam with lab work and an ECG, then time to go through the results together. <a href=\"/preventive-care\">Preventive care and physicals</a>."},
    {"k": ["memory", "dementia", "elderly", "parent", "geriatric", "aging"],
     "a": "Dr. Shtern cares for older adults and the families who help them, including memory concerns and medication reviews. With the patient's written permission she can keep family members updated. <a href=\"/geriatric-memory-care\">Geriatric and memory care</a>."},
    {"k": ["prescription", "refill", "medication", "pharmacy"],
     "a": "Questions about your own medications are best handled by phone, so please call the office at (561) 834-9280 rather than writing them here."},
]

# ---------------------------------------------------------------- meet and greet
# The first visit. Only facts the practice has confirmed: it is complimentary,
# in person at the office, with Dr. Shtern.
# ---------------------------------------------------------------- for patients
# Practical pages modelled on the "For patients" section of leading concierge
# sites. Every statement comes from SERVICES_INCLUDED, FAQ_GROUPS or DOCTOR.
GUIDES_PATIENTS = {
    "same-or-next-day-visits": {
        "title": "Same or Next Business Day Visits | Legacy Medical",
        "desc": "Legacy Medical members are seen the same or next business day when something comes up, with phone access to the practice around the clock.",
        "crumb": "Same or next day visits", "eyebrow": "For patients",
        "h1": "Seen today or tomorrow, by the doctor who knows you.",
        "lede": "When something comes up, members are seen the same or next business day. The visit is with Dr. Shtern, one patient at a time, and long enough to sort it out.",
        "photo": "reception-desk", "photo_alt": "The front desk at Legacy Medical in Palm Beach Gardens",
        "sections": [
            ("How it works", "<p>Call the office and say what is going on. Members are seen that day or the next business day, rather than waiting weeks for an opening. Routine visits are booked at a time that suits you.</p><p>Office hours are Monday to Thursday 9 AM to 5 PM and Friday 9 AM to 2 PM. Outside those hours, members can still reach the practice by phone, 24 hours a day, including weekends and holidays.</p>"),
            ("Why the schedule has room", "<p>Dr. Shtern keeps a small practice on purpose and sees one patient at a time. Visits are not booked in 15-minute slots, so there is space in the day for the person who calls in the morning with a fever, a new pain, or a blood pressure reading that will not come down.</p><p><a href=\"/concierge-medicine\">How concierge medicine works here</a>.</p>"),
            ("An answer before you leave", "<p>Many sick visits end with a result, not a referral to somewhere else. Blood is drawn in the office, ECGs are done during the visit, and rapid tests for flu A and B, COVID-19 and strep are run here. <a href=\"/labs-and-tests\">Labs and tests in the office</a>.</p><p>If coming in is not practical, many follow-ups and results reviews can happen by <a href=\"/telehealth\">video visit</a>.</p>"),
        ],
        "faqs": [
            ("How quickly can I be seen?", "<p>Members are seen the same or next business day when something comes up.</p>"),
            ("What if it is the weekend?", "<p>The office is closed on weekends, but members can reach the practice by phone at any hour. In an emergency, call 911 first.</p>"),
            ("Can a follow-up be done by video?", "<p>Often, yes. Many follow-ups and results reviews work well as a video visit. <a href=\"/telehealth\">About telehealth</a>.</p>"),
        ],
        "related_posts": ["concierge-doctor-telehealth", "how-to-choose-a-concierge-doctor", "what-is-concierge-medicine"],
        "related": ["telehealth", "labs-and-tests", "concierge-medicine"],
    },
    "chronic-care": {
        "title": "Chronic Care: Blood Pressure, Diabetes, Kidney | Legacy Medical",
        "desc": "Ongoing care for blood pressure, diabetes, cholesterol, kidney and thyroid conditions from Dr. Yana Shtern, a concierge internist and nephrologist in Palm Beach Gardens.",
        "crumb": "Chronic care support", "eyebrow": "For patients",
        "h1": "Long-term conditions, followed closely between visits.",
        "lede": "Blood pressure, diabetes, cholesterol, kidney and thyroid conditions do best with one doctor watching the whole picture. At Legacy Medical, that doctor is Dr. Shtern, every time.",
        "photo": "p-geri-meds", "photo_alt": "A weekly pill organizer on a linen tablecloth",
        "sections": [
            ("One doctor for the whole picture", "<p>Chronic conditions rarely come one at a time. High blood pressure, diabetes, cholesterol and kidney function affect each other, and so do the medicines used to treat them. Dr. Shtern is board-certified in Internal Medicine and in Nephrology, so the kidney side of that picture is part of the same visit rather than a separate referral.</p><p>See <a href=\"/hypertension\">hypertension</a> and <a href=\"/kidney-care\">kidney care</a>.</p>"),
            ("Medication management", "<p>One doctor keeps an eye on every prescription, dose and interaction. That matters most when several specialists are involved, when a kidney or liver condition changes how a medicine is cleared, or when a new prescription quietly duplicates an old one. <a href=\"/blog/medication-review-older-adults\">Why a full medication review matters</a>.</p>"),
            ("Between visits", "<p>Labs are drawn in the office and reviewed with you, home blood pressure readings can be sent in and discussed, and many check-ins can happen by video. When something changes, members are seen the same or next business day.</p>"),
        ],
        "faqs": [
            ("Which conditions does Dr. Shtern manage?", "<p>Blood pressure, diabetes, cholesterol, kidney and thyroid conditions, among the other problems an internist looks after. She is also board-certified in Nephrology.</p>"),
            ("Will you work with my specialists?", "<p>Yes. Dr. Shtern chooses specialists when you need one, contacts them, and follows up on what they find. <a href=\"/specialists-and-hospital-care\">Specialists and hospital care</a>.</p>"),
            ("Can I send home blood pressure readings?", "<p>Yes. Bring or send your log so the numbers can be reviewed together. <a href=\"/blog/home-blood-pressure-monitoring\">How to take an accurate home reading</a>.</p>"),
        ],
        "related_posts": ["home-blood-pressure-monitoring", "egfr-kidney-lab-results-explained", "medication-review-older-adults"],
        "related": ["hypertension", "kidney-care", "preventive-care"],
    },
    "specialists-and-hospital-care": {
        "title": "Specialists and Hospital Care | Legacy Medical",
        "desc": "Dr. Yana Shtern chooses and contacts specialists, follows up on what they find, and holds privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center.",
        "crumb": "Specialists and hospital care", "eyebrow": "For patients",
        "h1": "Your care stays in one place, even when it moves around.",
        "lede": "When you need a specialist or a hospital stay, Dr. Shtern stays involved. She chooses the specialist, makes the call, and keeps track of what they find.",
        "photo": "p-family-hands", "photo_alt": "Two people holding hands in a quiet room",
        "sections": [
            ("When you need a specialist", "<p>Dr. Shtern picks the specialist for your situation, contacts them, and follows up on what they find, so the plan comes back to one doctor who knows your whole history. You are not left carrying results between offices.</p>"),
            ("If you are admitted", "<p>Dr. Shtern holds privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center, and stays involved when members are in the hospital. <a href=\"/blog/concierge-doctor-hospital-stay\">What a concierge doctor does during a hospital stay</a>.</p>"),
            ("Someone on your side", "<p>Part of membership is advocacy: screenings on schedule, vaccines up to date, and a doctor who helps when the system gets complicated. For families arranging care for a parent, see <a href=\"/for-families\">for families</a>.</p>"),
        ],
        "faqs": [
            ("Which hospitals does Dr. Shtern use?", "<p>She has privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center.</p>"),
            ("What happens if I need a specialist?", "<p>Dr. Shtern chooses the specialist, contacts them, and follows up on what they find.</p>"),
            ("I split the year between two states. Can you work with my doctors up north?", "<p>Yes. Many members are seasonal residents. <a href=\"/seasonal-residents\">Care between seasons</a>.</p>"),
        ],
        "related_posts": ["concierge-doctor-hospital-stay", "concierge-care-for-aging-parents", "transfer-medical-records-to-florida-doctor"],
        "related": ["for-families", "seasonal-residents", "concierge-medicine"],
    },
    "labs-and-tests": {
        "title": "Labs and Tests in the Office | Legacy Medical, Palm Beach Gardens",
        "desc": "Blood draws, ECGs, stool occult blood tests and rapid flu, COVID-19 and strep tests are done in the Legacy Medical office in Palm Beach Gardens.",
        "crumb": "Labs and tests in the office", "eyebrow": "For patients",
        "h1": "Blood drawn here, results explained here.",
        "lede": "Most routine testing happens during your visit, so there is no separate trip to a lab, and Dr. Shtern goes through the results with you.",
        "photo": "p-kidney-labs", "photo_alt": "Sample tubes in a rack in soft light",
        "sections": [
            ("What is done in the office", "<ul><li>Blood draws for routine and follow-up lab work</li><li>ECGs (electrocardiograms) during your visit</li><li>Stool occult blood testing</li><li>Rapid tests for flu A and B, COVID-19 and strep</li></ul><p>Imaging and specialized tests are arranged with trusted local providers when you need them.</p>"),
            ("Results you go through together", "<p>The annual executive physical includes lab work and an ECG, then time to go through the results together. Numbers like eGFR, A1c and cholesterol are easier to act on when the doctor who ordered them explains what changed and why. <a href=\"/blog/egfr-kidney-lab-results-explained\">Reading your kidney labs</a>.</p>"),
            ("Insurance", "<p>Labs and covered tests are billed to your insurance as they are today. <a href=\"/insurance-and-fees\">More on insurance and fees</a>.</p>"),
        ],
        "faqs": [
            ("Are labs done in the office?", "<p>Yes. Blood is drawn in the office, and ECGs, stool occult blood tests and rapid flu, COVID-19 and strep tests are done here too.</p>"),
            ("Do I have to fast?", "<p>Some tests need fasting and many do not. The office will tell you when you book.</p>"),
            ("Are tests billed to insurance?", "<p>Yes, labs and covered tests are billed to your insurance.</p>"),
        ],
        "related_posts": ["egfr-kidney-lab-results-explained", "annual-physical-what-you-need", "executive-physical-exam-what-to-expect"],
        "related": ["preventive-care", "kidney-care", "insurance-and-fees"],
    },
}

PATIENTS_PAGE = {
    "title": "For Patients | Legacy Medical, Palm Beach Gardens",
    "desc": "Practical information for Legacy Medical members and new patients: visits, after-hours calls, labs, specialists, records, insurance, privacy, and health articles and videos.",
    "eyebrow": "For patients",
    "h1": "Everything you need, in one place.",
    "lede": "How visits, calls, labs and records work at Legacy Medical, with articles and videos for when you want to read further.",
    "guide": [
        ("Your first visit", "Every membership starts with a complimentary meet and greet with Dr. Shtern. Bring your questions, a list of your medicines and doctors, and your insurance card.", "meet-and-greet", "About the meet and greet"),
        ("Booking a visit", "Members are seen the same or next business day when something comes up. Office hours are Monday to Thursday 9 to 5 and Friday 9 to 2.", "same-or-next-day-visits", "Same or next day visits"),
        ("After hours", "Members can reach the practice by phone 24 hours a day, including weekends and holidays. In an emergency, call 911 first.", "contact", "Contact the office"),
        ("Labs and tests", "Blood draws, ECGs, stool occult blood tests and rapid flu, COVID-19 and strep tests are done in the office.", "labs-and-tests", "Labs and tests"),
        ("Ongoing conditions", "Blood pressure, diabetes, cholesterol, kidney and thyroid care, with one doctor managing every prescription.", "chronic-care", "Chronic care support"),
        ("Specialists and hospitals", "Dr. Shtern chooses and contacts specialists and holds privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center.", "specialists-and-hospital-care", "Specialists and hospital care"),
        ("Records and the portal", "With your permission the office requests your records from your previous doctor. Ask the office for patient portal access when you join.", "blog/transfer-medical-records-to-florida-doctor", "Moving your records"),
        ("Insurance", "Office visits, labs and covered tests are billed to your insurance, including Medicare. The concierge fee is separate.", "insurance-and-fees", "Insurance and fees"),
        ("Video visits", "Many follow-ups and results reviews can be done by video when coming in is not practical.", "telehealth", "Telehealth"),
        ("Part of the year away", "Seasonal residents get one doctor here who stays in touch with their physicians elsewhere.", "seasonal-residents", "Seasonal residents"),
    ],
}

CARD_BLURBS.update({
    "same-or-next-day-visits": "Seen the same or next business day, with phone access at any hour.",
    "chronic-care": "Blood pressure, diabetes, cholesterol, kidney and thyroid care, followed closely.",
    "specialists-and-hospital-care": "Dr. Shtern picks the specialist and stays involved in the hospital.",
    "labs-and-tests": "Blood draws, ECGs and rapid tests done during your visit.",
    "patients": "Visits, calls, labs, records and insurance, in one place.",
    "blog": "Articles on concierge care, prevention and healthy aging.",
    "videos": "A film from the practice and trusted health explainers.",
})

# ---------------------------------------------------------------- videos
# Practice films are Legacy Medical's own (YouTube channel "Legacy Medical
# Concierge of Palm Beach"). The library holds short explainers from public
# health organizations, each checked with YouTube oEmbed (title + channel).
# Nothing loads from YouTube until the visitor presses play. To add a film
# Dr. Shtern records, add one dict to PRACTICE_FILMS and run
# tools/fetch_video_thumbs.py.
VIDEOS_PAGE = {
    "title": "Videos | Legacy Medical, Palm Beach Gardens",
    "desc": "Watch a short film from Legacy Medical and trusted explainers on blood pressure, kidney health, heart and stroke warning signs, screening and healthy aging.",
    "eyebrow": "Videos",
    "h1": "Watch, then ask us anything.",
    "lede": "A short film from the practice, and a small library of trusted explainers from public health organizations on the topics members ask about most.",
    "library_h": "Trusted explainers",
    "library_lede": "Chosen for clear, reliable information from organizations like the CDC, the National Institutes of Health and the American Heart Association. They are general education, made by those organizations rather than by Legacy Medical, and not advice for your own situation.",
}
PRACTICE_FILMS = [
    {"id": "raReWdCy3tA", "title": "Legacy Medical: Dr. Yana Shtern",
     "summary": "A short look at Legacy Medical and Dr. Yana Shtern's concierge practice in Palm Beach Gardens.",
     "channel": "Legacy Medical Concierge of Palm Beach"},
]
VIDEO_LIBRARY = [
    {"id": 'TLiD3vh_X8o', "title": 'Blood pressure done right: The correct way to measure yours at home.', "channel": 'American Heart Association', "topic": 'Blood pressure',
     "summary": 'Step by step, how to sit, position your arm and cuff, and take an accurate blood pressure reading at home.', "related": 'blog/home-blood-pressure-monitoring'},
    {"id": 'r5XTTeP039Q', "title": 'Mayo Clinic Explains Hypertension', "channel": 'Mayo Clinic', "topic": 'Blood pressure',
     "summary": 'A Mayo Clinic nephrologist explains what the two blood pressure numbers mean, who gets hypertension, how it is diagnosed and treated.', "related": 'hypertension'},
    {"id": 'g4SV7SJLP_g', "title": 'Get to Know Your Kidneys', "channel": "NIH (NIDDK)", "topic": 'Kidney health',
     "summary": 'What your kidneys do every day, why kidney disease is often silent at first, and everyday habits that help protect them.', "related": 'kidney-care'},
    {"id": 'fFn0ygOOBuI', "title": 'What is eGFR, and how is it used to measure kidney function?', "channel": 'National Kidney Foundation', "topic": 'Kidney health',
     "summary": 'A kidney specialist explains how eGFR is calculated from a blood test and what a higher or lower number says about kidney function.', "related": 'blog/egfr-kidney-lab-results-explained'},
    {"id": '1PKBTpVhvVk', "title": 'Mayo Clinic Minute: Avoiding kidney stones', "channel": 'Mayo Clinic', "topic": 'Kidney health',
     "summary": 'A Mayo Clinic nephrologist explains why kidney stones form and why drinking enough water each day is the simplest way to prevent them.', "related": 'blog/heat-hydration-kidney-health'},
    {"id": 'Ih_4BHoZv0U', "title": 'Mayo Clinic Minute: The role of cholesterol in heart health', "channel": 'Mayo Clinic', "topic": "Heart health",
     "summary": 'What cholesterol is, how the bad kind builds plaque in arteries, and which food choices can help bring your levels down.', "related": 'blog/heart-healthy-foods'},
    {"id": 'gfFMSaSoU6U', "title": 'Turning back the clock on prediabetes', "channel": "CDC", "topic": 'Diabetes and metabolism',
     "summary": 'How the CDC National Diabetes Prevention Program helps people with prediabetes make small, lasting changes that lower their risk of type 2 diabetes.', "related": 'preventive-care'},
    {"id": 'G1lwVhnnkoU', "title": '10-minute Workout for Older Adults', "channel": 'National Institute on Aging', "topic": 'Healthy aging',
     "summary": 'A follow-along routine for older adults with a warm-up, leg and arm strength moves, balance work and stretching, using only a chair.', "related": 'blog/health-benefits-of-exercise'},
    {"id": 'UAlxu7NiKNk', "title": 'STEADI for Older Adults', "channel": "CDC", "topic": 'Healthy aging',
     "summary": 'Simple steps that lower fall risk after 65, including strength and balance exercise, medication and vision checks, footwear and home safety.', "related": 'blog/concierge-care-for-aging-parents'},
    {"id": '0xubzGiAjEU', "title": 'Mayo Clinic Minute: Heat exhaustion and heatstroke', "channel": 'Mayo Clinic', "topic": 'Everyday health',
     "summary": 'How to recognize heat exhaustion before it becomes heatstroke, the warning sign of confusion, and how hydration and breaks keep you safe.', "related": 'blog/heat-hydration-kidney-health'},
    {"id": 'qTkqm6weTX4', "title": 'Mayo Clinic Minute - Who should be screened for colorectal cancer?', "channel": 'Mayo Clinic', "topic": 'Screening and vaccines',
     "summary": 'Who is at higher risk for colorectal cancer, why screening starting at age 45 matters, and why early detection makes it highly treatable.', "related": 'blog/cancer-prevention-risk-factors'},
    {"id": 'zhGxsKdLNkE', "title": 'Mayo Clinic Minute: Why vaccines are especially important for older people', "channel": 'Mayo Clinic', "topic": 'Screening and vaccines',
     "summary": 'Why the immune system weakens with age and how flu, shingles and other vaccines help older adults avoid serious complications and hospital stays.', "related": 'blog/yearly-flu-vaccine-benefits'},
]

MEET = {
    "title": "Meet and Greet with Dr. Shtern | Legacy Medical",
    "desc": "Your first visit to Legacy Medical is a complimentary meet and greet with Dr. Yana Shtern in Palm Beach Gardens. What happens, what to ask, and how to book.",
    "eyebrow": "Your first visit",
    "h1": "It starts with a conversation.",
    "lede": "Before anyone joins, they sit down with Dr. Shtern. The meet and greet is complimentary, and it happens at the office.",
    "steps": [
        ("You get in touch", "Call (561) 834-9280 or send the short form on this page. The office finds a time that suits you."),
        ("You meet Dr. Shtern", "A relaxed conversation in her office on Prosperity Farms Road. Bring a spouse or an adult child if you like."),
        ("You decide later", "There is no pressure to decide in the room. If you join, the office requests your records and books your first patient visit."),
    ],
    "sections": [
        ("What the meet and greet is", "<p>A chance for you and Dr. Shtern to see whether the practice is right for you. You talk about what you want from a doctor, how your care is going now, and how membership works day to day. Dr. Shtern explains how she practices, how members reach her, and what the concierge fee includes.</p>"),
        ("Questions worth asking", "<ul><li>How quickly can members be seen when something comes up?</li><li>How do after-hours calls work, and who answers?</li><li>What does the concierge fee include, and what is still billed to insurance?</li><li>How do you work with my specialists and with the hospital if I am admitted?</li><li>How large is the practice, and are new members being accepted right now?</li><li>What happens to my care when I am away for the summer?</li></ul>"),
        ("What to bring", "<p>Nothing. The meet and greet is simply a chance to see the office, meet Dr. Shtern, and decide whether the practice feels like the right fit. There is no paperwork and nothing to prepare. If you have questions, bring them along, and bring a family member if you like.</p>"),
        ("Coming with a parent or partner", "<p>Families are welcome. Adult children often come along when they are arranging care for a parent, and couples often meet Dr. Shtern together. With the patient's written permission, she can keep family members updated later on.</p>"),
    ],
    "form_h": "Book a meet and greet",
    "form_lede": "Leave your details and the office will call or email you to set a time. Prefer the phone? Call during office hours.",
    "faqs": [
        ("Is the meet and greet really free?", "<p>Yes. It is complimentary.</p>"),
        ("Where does it take place?", "<p>At the office: 11380 Prosperity Farms Road, Suite 114, Palm Beach Gardens. It is a first-floor suite with accessible entry.</p>"),
        ("Can I ask about the concierge fee?", "<p>Please do. The fee is not posted online, and Dr. Shtern and the office would rather explain it in person, with what it covers.</p>"),
        ("Can my family member come?", "<p>Yes. Spouses and adult children are welcome.</p>"),
    ],
}

# ---------------------------------------------------------------- guide pages
# Audience and comparison pages. Same rule as everywhere: only confirmed facts
# about the practice; outside facts carry a link to the source.
GUIDES_BASE = {
    "seasonal-residents": {
        "title": "Concierge Doctor for Seasonal Residents | Legacy Medical",
        "desc": "Primary care for seasonal residents of Palm Beach County: one internist who keeps your records current, coordinates with your doctors up north, and stays reachable.",
        "crumb": "Seasonal residents", "eyebrow": "Seasonal residents",
        "h1": "One doctor here who keeps up with you between seasons.",
        "lede": "Many people split the year between Palm Beach County and somewhere else. Concierge care suits that well: one physician who knows your history in Florida, stays in touch with your doctors elsewhere, and is easy to reach when you are back.",
        "photo": "dr-shtern-desk", "photo_alt": "Dr. Yana Shtern at her desk at Legacy Medical in Palm Beach Gardens",
        "sections": [
            ("When you arrive for the season", "<p>A doctor who has your records before you land makes the first weeks easier. With your permission, the office requests records from your physicians up north, so recent labs, imaging and medication changes are already in your chart.</p><p>Members are seen the same or next business day, so a cough that started on the drive down, or a prescription that needs adjusting, does not have to wait.</p>"),
            ("While you are here", "<p>Labs are drawn in the office, and ECGs and rapid flu, COVID-19 and strep tests are done there too. If you need a specialist, Dr. Shtern chooses one, makes the call and follows up on what they find. If you are admitted, she has privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center.</p>"),
            ("When you head north", "<p>Before you leave, it helps to go over your medicines, refills and anything that should be followed up while you are away. With your permission, the office can send notes and results to your doctors at home so nobody starts from scratch.</p><p>Members can reach the practice by phone at any hour. Video visits work well for many follow-ups and results reviews, though licensing rules differ from state to state, so ask the office what applies where you will be.</p>"),
            ("Medicare in two places", "<p>Original Medicare works with participating doctors anywhere in the country, while Medicare Advantage plans usually use regional networks. <a href=\"https://www.medicare.gov/health-drug-plans/health-plans/your-coverage-options\" rel=\"noopener\">Medicare explains the difference</a>, and it matters if you see doctors in two states. The concierge fee itself is not covered by Medicare; visits and tests are billed as usual. <a href=\"/insurance-and-fees\">How the fee and insurance fit together</a>.</p>"),
        ],
        "faqs": [
            ("Can I join if I live in Florida only part of the year?", "<p>Ask at your meet and greet. Dr. Shtern can explain how membership works around your time away.</p>"),
            ("Can you send my records to my doctor up north?", "<p>Yes, with your written permission.</p>"),
            ("How do I reach the practice when I am away?", "<p>Members can call the practice at any hour. Many follow-ups can be done by video, depending on where you are.</p>"),
        ],
        "related_posts": ["snowbird-primary-care-palm-beach", "transfer-medical-records-to-florida-doctor", "medicare-living-in-two-states", "hurricane-season-health-checklist"],
        "related": ["telehealth", "insurance-and-fees", "meet-and-greet"],
    },
    "for-families": {
        "title": "Concierge Care for an Aging Parent | Legacy Medical, Palm Beach",
        "desc": "For families arranging care for a parent in Palm Beach County: one internist who coordinates specialists, reviews medicines, and keeps you informed with permission.",
        "crumb": "For families", "eyebrow": "For families",
        "h1": "Care for a parent, with room for the family in it.",
        "lede": "Often the person arranging care is an adult child, sometimes living in another state. Dr. Shtern works with families: one physician who knows your parent well, keeps the specialists in step, and keeps you informed when your parent wants you to be.",
        "photo": "front-desk-scrubs", "photo_alt": "Dr. Yana Shtern at the Legacy Medical front desk",
        "sections": [
            ("Come to the meet and greet together", "<p>Families are welcome at the first visit. It is a good time to ask how the practice handles calls from family, how hospital stays are followed, and what happens when something changes on a weekend. <a href=\"/meet-and-greet\">About the meet and greet</a>.</p>"),
            ("Keeping you informed", "<p>With your parent's written permission, Dr. Shtern can update family members, talk with home health agencies and other doctors, and help everyone plan ahead. Members, and the family helping them, can reach the practice by phone at any hour.</p>"),
            ("Fewer, better prescriptions", "<p>Older adults are more sensitive to many medicines, and kidney function, which Dr. Shtern watches closely as a nephrologist, changes how many drugs should be dosed. A full review often finds a medicine that can be stopped, a dose that can be lowered, or two prescriptions from two specialists that should not be taken together. <a href=\"/geriatric-memory-care\">Geriatric and memory care</a>.</p>"),
            ("If your parent is in the hospital", "<p>Dr. Shtern has privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center. When a member is admitted, she can follow their care and talk with the hospital team, so the family has one doctor to ask.</p>"),
            ("Paperwork worth having in place", "<p>Two documents save a great deal of trouble later: a HIPAA authorization naming who the practice may speak with, and, in Florida, a designation of a health care surrogate who can make medical decisions if your parent cannot. <a href=\"https://www.flsenate.gov/Laws/Statutes/2025/765.202\" rel=\"noopener\">Florida law sets out how a surrogate is designated</a>; an elder law attorney can help with the details.</p>"),
        ],
        "faqs": [
            ("Can you talk to me about my mother's care?", "<p>Yes, once she has given written permission naming you. The office can help with the form.</p>"),
            ("I live out of state. How do I stay involved?", "<p>With your parent's permission, Dr. Shtern can update you by phone. Members can reach the practice at any hour.</p>"),
            ("Does Dr. Shtern see patients with memory problems?", "<p>Yes. Memory concerns are part of her geriatric care. <a href=\"/geriatric-memory-care\">More on geriatric and memory care</a>.</p>"),
        ],
        "related_posts": ["concierge-care-for-aging-parents", "memory-changes-when-to-see-a-doctor", "medication-review-older-adults", "concierge-doctor-hospital-stay"],
        "related": ["geriatric-memory-care", "meet-and-greet", "kidney-care"],
    },
    "concierge-vs-traditional-primary-care": {
        "title": "Concierge vs. Traditional Primary Care: A Side-by-Side Look",
        "desc": "How concierge medicine differs from traditional primary care: access, visit length, practice size, insurance and fees, compared side by side by a Palm Beach Gardens practice.",
        "crumb": "Concierge vs. traditional care", "eyebrow": "Side by side",
        "h1": "Concierge and traditional primary care, side by side.",
        "lede": "Both are primary care. The difference is mostly arithmetic: how many patients one doctor looks after, and what that leaves time for. Here is how the two compare, using Legacy Medical as the concierge example.",
        "compare": True,
        "sections": [
            ("Why the numbers matter", "<p>A 2005 report by the U.S. Government Accountability Office looked at physicians who had switched to concierge care. Before switching, their practices averaged about 2,700 patients; afterward, about 490. The number of patients they saw in a day fell from roughly 26 to about 10. <a href=\"https://www.gao.gov/products/gao-05-929\" rel=\"noopener\">Read the GAO report</a>. The figures are two decades old, but the trade-off they describe is the same today: fewer patients per doctor is what makes time and access possible.</p>"),
            ("What stays the same", "<p>Concierge care is still primary care. At Legacy Medical your insurance, including Medicare, is billed for office visits, labs and tests, as it is now. You keep your specialists, and prescriptions work the same way.</p>"),
            ("What the concierge fee pays for", "<p>The annual fee covers what insurance does not pay for: a limited patient panel, same or next-business-day appointments, unhurried visits, and phone access around the clock. <a href=\"https://www.medicare.gov/coverage/concierge-care\" rel=\"noopener\">Medicare does not cover concierge fees</a>. Legacy Medical explains its fee in person at the meet and greet rather than posting a number without context.</p>"),
            ("Who tends to find it worthwhile", "<p>People who see several specialists, manage blood pressure, kidney disease or diabetes, travel or split the year between two homes, or are arranging care for a parent. People who rarely see a doctor may find a traditional practice suits them fine. <a href=\"/blog/is-a-concierge-doctor-right-for-me\">Is a concierge doctor right for you?</a></p>"),
        ],
        "faqs": [
            ("Is concierge medicine the same as direct primary care?", "<p>No. Direct primary care practices usually do not bill insurance and charge a monthly fee for most primary care. Concierge practices like Legacy Medical bill insurance for visits and tests and charge a separate concierge fee. <a href=\"/blog/concierge-vs-direct-primary-care\">More on the difference</a>.</p>"),
            ("Do I lose my insurance if I join?", "<p>No. Insurance, including Medicare, is still billed for office visits, labs and tests. The concierge fee is separate.</p>"),
            ("How do I find out what membership costs?", "<p>Call the office or ask at your complimentary meet and greet.</p>"),
        ],
        "related_posts": ["concierge-medicine-cost", "concierge-medicine-vs-mdvip", "does-medicare-cover-concierge-medicine", "questions-to-ask-a-concierge-doctor"],
        "related": ["concierge-medicine", "insurance-and-fees", "meet-and-greet"],
    },
}
GUIDES = dict(GUIDES_BASE, **GUIDES_PATIENTS)
CARD_BLURBS.update({
    "meet-and-greet": "Your first visit: a complimentary conversation with Dr. Shtern.",
    "seasonal-residents": "Continuity for people who split the year between Florida and somewhere else.",
    "for-families": "For adult children arranging care for a parent.",
    "concierge-vs-traditional-primary-care": "Access, time, insurance and fees, compared side by side.",
})
CATEGORY_OWNERS.update({
    "Seasonal residents": ("seasonal-residents", "Care for seasonal residents"),
    "Kidney health": ("kidney-care", "Kidney care and Nephrology"),
    "Aging and family": ("for-families", "Care for an aging parent"),
    "Healthy aging": ("preventive-care", "Preventive care and the annual executive physical"),
})

# More set answers for the assistant. Facts only from this file; anything the
# practice has not confirmed gets "please ask the office".
ASSIST_EXTRA += [
    {"k": ["meet and greet", "meet & greet", "first visit", "first appointment", "consultation", "free visit", "complimentary"],
     "a": "Your first visit is a complimentary meet and greet with Dr. Shtern at the office. You talk about what you want from a doctor and how membership works, and ask anything you like. <a href=\"/meet-and-greet\">About the meet and greet</a>."},
    {"k": ["what to bring", "bring with me", "should i bring"],
     "a": "Nothing is needed for the meet and greet. Come see the office, meet Dr. Shtern, and find out whether the practice is a fit. Bring your questions if you have them. <a href=\"/meet-and-greet\">More about the first visit</a>."},
    {"k": ["friday", "weekend", "saturday", "sunday", "holiday"],
     "a": "The office is open Monday to Thursday 9 AM to 5 PM and Friday 9 AM to 2 PM, and closed on weekends. Members can still reach the practice by phone at any hour, including weekends and holidays."},
    {"k": ["wheelchair", "accessible", "accessibility", "walker", "stairs", "elevator", "first floor"],
     "a": "Suite 114 is on the first floor, with accessible entry. If you need an accommodation for your visit, mention it when you call (561) 834-9280."},
    {"k": ["wifi", "wi-fi", "waiting room", "internet"],
     "a": "The office is a first-floor suite with free Wi-Fi."},
    {"k": ["fax"], "a": "The office fax number is (561) 834-9279."},
    {"k": ["email", "e-mail", "write to"], "a": "You can email info@legacymedicalpalmbeach.com. Please keep medical details out of email; call the office for anything about your health."},
    {"k": ["language", "spanish", "russian", "speak"],
     "a": "Please ask the office which languages are spoken: call (561) 834-9280."},
    {"k": ["accepting", "new patients", "taking patients", "openings", "waitlist", "wait list"],
     "a": "The practice keeps a limited panel. Call (561) 834-9280 to ask whether new members are being accepted right now, or <a href=\"/meet-and-greet\">book a meet and greet</a>."},
    {"k": ["nurse", "yan", "konevsky", "office manager", "staff", "team"],
     "a": "Yan Konevsky, RN is the practice's registered nurse and office manager. Before Legacy Medical he managed an outpatient hemodialysis center in New York City. <a href=\"/our-team\">Meet the team</a>."},
    {"k": ["education", "medical school", "trained", "training", "residency", "fellowship", "where did she"],
     "a": "Dr. Shtern earned her medical degree at St. George's University School of Medicine and completed her Internal Medicine residency and Nephrology fellowship at Maimonides Medical Center in New York City. <a href=\"/dr-yana-shtern\">Her full background</a>."},
    {"k": ["castle connolly", "award", "recognition", "top doctor"],
     "a": "Dr. Shtern has been recognized as a Castle Connolly Top Doctor since 2023. <a href=\"/dr-yana-shtern\">About Dr. Shtern</a>."},
    {"k": ["license", "npi", "verify", "board certified", "board-certified", "certified"],
     "a": "Dr. Shtern is board-certified by the American Board of Internal Medicine in Internal Medicine and Nephrology. <a href=\"/dr-yana-shtern\">Links to verify her credentials</a>."},
    {"k": ["kidney", "ckd", "creatinine", "egfr", "dialysis", "kidney stone", "nephrologist", "Nephrology"],
     "a": "Dr. Shtern is board-certified in Nephrology as well as Internal Medicine, so kidney care is part of her everyday practice: chronic kidney disease, rising creatinine, stones, electrolyte problems and care for people on dialysis. <a href=\"/kidney-care\">Kidney care</a>."},
    {"k": ["blood pressure", "hypertension", "bp "],
     "a": "High blood pressure, including blood pressure that stays high on two or three medicines, is one of Dr. Shtern's focus areas. <a href=\"/hypertension\">Hypertension care</a>."},
    {"k": ["diabetes", "cholesterol", "thyroid", "chronic"],
     "a": "Chronic disease management, including diabetes and cholesterol, is part of membership. For a question about your own condition, please call the office at (561) 834-9280. <a href=\"/concierge-medicine\">What membership includes</a>."},
    {"k": ["ecg", "ekg", "electrocardiogram", "heart test"],
     "a": "ECGs are done in the office, and an ECG is part of the annual executive physical."},
    {"k": ["flu test", "covid test", "strep", "rapid test", "sick visit", "sick", "cold", "fever"],
     "a": "Rapid flu, COVID-19 and strep tests are done in the office, and members are seen the same or next business day when they are sick. If you feel seriously unwell, call 911."},
    {"k": ["executive physical", "annual physical", "legacy physical", "check up", "checkup"],
     "a": "Members get the annual executive physical: a thorough yearly exam with lab work and an ECG, then time to go through the results together. <a href=\"/preventive-care\">Preventive care and physicals</a>."},
    {"k": ["video", "telehealth", "virtual visit", "zoom", "remote"],
     "a": "Video visits work well for many follow-ups, results reviews and medication questions. <a href=\"/telehealth\">About telehealth</a>."},
    {"k": ["snowbird", "seasonal", "part of the year", "up north", "summer", "two homes"],
     "a": "Many members split the year between Florida and somewhere else. With your permission the office can request records from, and send notes to, your doctors up north, and members can reach the practice by phone at any hour. <a href=\"/seasonal-residents\">Care for seasonal residents</a>."},
    {"k": ["mother", "father", "mom", "dad", "parent", "family member", "caregiver", "adult child", "bring my", "daughter", "son ", "wife", "husband", "spouse", "partner"],
     "a": "Families are welcome, including at the meet and greet. With your parent's written permission, Dr. Shtern can keep you informed and coordinate with other doctors and home health. <a href=\"/for-families\">For families</a>."},
    {"k": ["memory", "dementia", "alzheimer", "forgetful", "confusion"],
     "a": "Memory concerns are part of Dr. Shtern's geriatric care, alongside medication reviews and fall prevention. <a href=\"/geriatric-memory-care\">Geriatric and memory care</a>."},
    {"k": ["records", "medical records", "transfer", "previous doctor", "old doctor"],
     "a": "If you join, the office requests your records from your previous doctor with your permission. You do not need them for the meet and greet."},
    {"k": ["mdvip", "signaturemd", "concierge choice"],
     "a": "Legacy Medical is an independent practice, not part of a national network. <a href=\"/blog/concierge-medicine-vs-mdvip\">How the models differ</a>."},
    {"k": ["direct primary care", "dpc"],
     "a": "Direct primary care practices usually do not bill insurance. Legacy Medical bills insurance for visits and tests and charges a separate concierge fee. <a href=\"/blog/concierge-vs-direct-primary-care\">More on the difference</a>."},
    {"k": ["hsa", "fsa", "health savings", "flexible spending", "tax deductible", "deductible"],
     "a": "Whether a concierge fee can come from an HSA or FSA depends on your plan and the tax rules, so please check with a tax advisor. <a href=\"/blog/hsa-fsa-concierge-medicine-fees\">What the 2026 rules say</a>."},
    {"k": ["worth it", "why concierge", "benefit", "advantages", "versus", " vs ", "traditional", "regular doctor"],
     "a": "Concierge care means a smaller practice: same or next business day visits, unhurried appointments and phone access at any hour, with insurance still billed for visits and tests. <a href=\"/concierge-vs-traditional-primary-care\">Concierge and traditional care side by side</a>."},
    {"k": ["cancel", "reschedule", "change my appointment", "running late", "late"],
     "a": "Please call the office at (561) 834-9280 to change or cancel an appointment."},
    {"k": ["bill", "billing", "invoice", "statement", "payment"],
     "a": "For a billing question, please call the office at (561) 834-9280."},
    {"k": ["portal", "log in", "login", "online account"],
     "a": "Members can ask the office for patient portal access when they join."},
    {"k": ["vaccine", "vaccination", "shot", "flu shot"],
     "a": "Please call the office at (561) 834-9280 to ask which vaccines are available."},
    {"k": ["house call", "home visit", "come to my home"],
     "a": "Please ask the office about visits outside the office: call (561) 834-9280."},
]

ASSIST_EXTRA += [
    {"k": ["one patient", "one at a time", "double book", "double-book", "overbook", "how many patients a day", "waiting room", "wait long", "rushed"],
     "a": "Dr. Shtern sees one patient at a time. Appointments are not double-booked, so your time with her is yours alone and unhurried. <a href=\"/concierge-medicine\">How concierge care works here</a>."},
    {"k": ["why concierge", "is concierge worth it", "worth it", "benefits of concierge", "why join", "why choose"],
     "a": "Concierge care means a much smaller practice. The average primary care practice carries about 2,700 patients and sees about 26 a day (GAO, 2005); Legacy Medical takes no more than 300 members and Dr. Shtern sees no more than 8 a day. That means appointments of about an hour, one patient at a time, same or next business day visits, and phone access at any hour. <a href=\"/concierge-vs-traditional-primary-care\">Concierge and traditional care compared</a>."},
    {"k": ["child", "children", "kids", "pediatric", "baby", "teen", "teenager"],
     "a": "Dr. Shtern is an internist: a physician trained in the care of adults. For a question about a younger family member, please call the office at (561) 834-9280."},
    {"k": ["parking", "park"],
     "a": "The office is at 11380 Prosperity Farms Road, Suite 114, a first-floor suite. Call (561) 834-9280 if you have questions about parking or getting in. <a href=\"/contact\">Directions</a>."},
]

# Photos beside page sections: {page slug: {section heading: image stem}}.
# Stems are built by tools/build_images.py from tools/images.json. Topic
# photos (p-*) are licensed stock (Pexels) and only illustrate a subject;
# they are never captioned or described as the practice.
SECTION_IMAGES = {
    "kidney-care": {"When to think about your kidneys": "p-kidney-water", "Conditions Dr. Shtern manages": "p-kidney-labs"},
    "hypertension": {"Why it gets complicated": "p-bp-walk", "Taking a good home reading": "p-bp-cuff"},
    "geriatric-memory-care": {"Memory and thinking": "p-geri-couple", "Fewer, better prescriptions": "p-geri-meds"},
    "preventive-care": {"What the annual executive physical covers": "p-prev-stetho", "Screenings and vaccines": "p-prev-run"},
    "telehealth": {"What works well by video": "p-tele-laptop"},
    "seasonal-residents": {"When you arrive for the season": "p-seasonal-coast", "When you head north": "p-seasonal-travel"},
    "for-families": {"Come to the meet and greet together": "p-family-talk", "If your parent is in the hospital": "p-family-hands"},
    "concierge-vs-traditional-primary-care": {"Why the numbers matter": "p-compare-calendar"},
    "concierge-medicine": {"Why the panel is small": "p-concierge-phone", "Who it suits": "reception-desk"},
    "meet-and-greet": {"What the meet and greet is": "p-meet-coffee", "Coming with a parent or partner": "front-desk-scrubs"},
    "membership": {"What to bring to the meet and greet": "reception-wall"},
    "insurance-and-fees": {"The concierge fee": "p-insurance-papers"},
}
