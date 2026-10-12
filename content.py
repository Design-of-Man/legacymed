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
PRICE_RANGE = None  # fee not published; do not guess
HEALTH_PLANS = []

ONE_LINER = ("Legacy Medical is a concierge internal medicine practice in Palm Beach Gardens, Florida. "
             "Dr. Yana Shtern, board-certified in internal medicine and nephrology, keeps a small patient panel "
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
    "knows_about": ["Internal medicine", "Nephrology", "Hypertension", "Chronic kidney disease", "Electrolyte disorders",
                    "Kidney stones", "Preventive medicine", "Geriatric care"],
    "same_as": [
        "https://www.healthgrades.com/physician/dr-yana-shtern-gfc4n",
        "https://www.doximity.com/pub/yana-shtern-md",
        "https://www.jupitermed.com/find-a-physician/yana-shtern-md/",
        "https://health.usnews.com/doctors/yana-shtern-650087",
        "https://www.castleconnolly.com/top-doctors/yana-shtern-internal-medicine-62cc071652",
    ],
    "page_title": "Dr. Yana Shtern, MD | Internist and Nephrologist, Palm Beach Gardens",
    "page_desc": ("Dr. Yana Shtern is double board-certified in internal medicine and nephrology, with privileges at Jupiter Medical Center "
                  "and Palm Beach Gardens Medical Center. Her training, background and how she practices."),
    "hero_lede": ("Board-certified in internal medicine and in nephrology, Dr. Shtern has practiced for close to twenty years, first in "
                  "New York City and now in Palm Beach Gardens, where she runs Legacy Medical as a small concierge practice."),
    "home_creds": [
        ("Board certification", "Internal medicine and nephrology, American Board of Internal Medicine"),
        ("Hospital privileges", "Jupiter Medical Center and Palm Beach Gardens Medical Center"),
        ("In practice", "Close to twenty years, in New York City and Palm Beach County"),
        ("Recognition", "Castle Connolly Top Doctor since 2023"),
    ],
    "facts": [
        ("Board certification", "Internal Medicine and Nephrology (ABIM)"),
        ("Medical degree", "St. George's University School of Medicine, 2007"),
        ("Residency and fellowship", "Internal medicine residency and nephrology fellowship, Maimonides Medical Center, Brooklyn"),
        ("Undergraduate", "BS in Pharmacology, Stony Brook University"),
        ("Hospital privileges", "Jupiter Medical Center; Palm Beach Gardens Medical Center"),
        ("Committee work", "Continuing Medical Education Committee, Jupiter Medical Center"),
        ("NPI", "1497940852"),
        ("Florida license", "ME114615"),
    ],
    "bio": [
        "Most of what Dr. Shtern does in a day is internal medicine: physicals, blood pressure, cholesterol, diabetes, infections, the questions that come with getting older, and keeping track of everything a patient's other doctors are doing. Her second board certification, in nephrology, shapes how she does it. Kidney function and blood pressure affect nearly every medication decision, and she reads those numbers the way a kidney specialist does.",
        "She studied pharmacology at Stony Brook University before medical school at St. George's University, then completed her internal medicine residency and a nephrology fellowship at Maimonides Medical Center in Brooklyn. In New York she ran her own practice, served as medical director of an outpatient hemodialysis center, and worked in interventional nephrology.",
        "In Palm Beach County she holds privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center, and sits on the Continuing Medical Education Committee at Jupiter Medical Center. She chose the concierge model so she could keep her panel small enough to know every patient well, be reachable when they need her, and stay involved when they are in the hospital.",
    ],
    "training_h": "From pharmacology to two board certifications",
    "timeline": [
        ("Stony Brook", "BS in Pharmacology", "Stony Brook University, New York."),
        ("2007", "Doctor of Medicine", "St. George's University School of Medicine."),
        ("Brooklyn", "Residency and fellowship", "Internal medicine residency and nephrology fellowship at Maimonides Medical Center, New York City."),
        ("New York", "Private practice and dialysis", "Ran a private practice; medical director of an outpatient hemodialysis center; interventional nephrology."),
        ("Palm Beach", "Legacy Medical", "Concierge internal medicine in Palm Beach Gardens, with privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center."),
    ],
    "verify_intro": "Board certification, licensing and hospital privileges are public record. These are the places to check them:",
    "verify_links": [
        ("ABIM board certification lookup", "https://www.abim.org/verify-physician.aspx?type=id&id=310989", ""),
        ("Castle Connolly Top Doctor profile", "https://www.castleconnolly.com/top-doctors/yana-shtern-internal-medicine-62cc071652", "(Top Doctor since 2023)"),
        ("Jupiter Medical Center physician directory", "https://www.jupitermed.com/find-a-physician/yana-shtern-md/", ""),
        ("Healthgrades profile", "https://www.healthgrades.com/physician/dr-yana-shtern-gfc4n", "(Patient Favorite award)"),
        ("Doximity profile", "https://www.doximity.com/pub/yana-shtern-md", ""),
        ("Florida Department of Health license search", "https://mqa-internet.doh.state.fl.us/MQASearchServices/HealthCareProviders", "(license ME114615)"),
    ],
    "personal": "Dr. Shtern has been married for more than fifteen years and has two teenagers. When she is not at the office she is usually at hot yoga, out fishing, or cooking.",
}

TEAM = [
    {"name": "Dr. Yana Shtern, MD", "role": "Physician and founder", "photo": "dr-yana-shtern", "is_doctor": True,
     "bio": ["Board-certified in internal medicine and nephrology. Dr. Shtern sees every member herself, from the annual physical to a same-day sick visit."],
     "link": "/dr-yana-shtern", "link_label": "Full background"},
    {"name": "Yan Konevsky, RN", "role": "Registered nurse and office manager", "photo": "yan-konevsky-rn",
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
    {"name": "The annual Legacy physical", "icon": "heart", "text": "A thorough yearly exam with lab work and an ECG, then time to go through the results together.", "schema": True, "procedure": True},
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
    "kidney-care": "Nephrology from your own internist: CKD, stones, electrolytes, creatinine that keeps creeping up.",
    "hypertension": "Blood pressure that will not come down, or comes down with side effects you do not like.",
    "geriatric-memory-care": "Care for older adults and the families who help them, including memory concerns.",
    "preventive-care": "The annual Legacy physical, screenings, and an executive-style exam without the day at a hospital.",
    "telehealth": "Video visits for follow-ups, results and questions that do not need an exam.",
    "membership": "Meet Dr. Shtern first, then decide.",
    "insurance-and-fees": "What the membership fee covers and what your insurance still pays for.",
    "faq": "Answers about access, insurance, hospitals and joining.",
    "dr-yana-shtern": "Training, certifications and hospital privileges.",
    "our-team": "Who answers when you call.",
}

# ---------------------------------------------------------------- home
HOME_TITLE = "Concierge Doctor in Palm Beach Gardens | Legacy Medical"
HOME_DESC = ("Concierge internal medicine in Palm Beach Gardens with Dr. Yana Shtern, MD, board-certified in internal medicine and nephrology. "
             "Same or next-day visits and 24/7 phone access.")

HERO_VIDEO = {
    "hd": "/assets/video/inlet-1080.webm|/assets/video/inlet-1080.mp4",
    "sd": "/assets/video/inlet-720.webm|/assets/video/inlet-720.mp4",
    "portrait": "/assets/video/inlet-portrait.webm|/assets/video/inlet-portrait.mp4",
    "posters": {
        "a768": "/assets/video/inlet-poster-768.avif", "a1280": "/assets/video/inlet-poster-1280.avif", "a1920": "/assets/video/inlet-poster-1920.avif",
        "w768": "/assets/video/inlet-poster-768.webp", "w1280": "/assets/video/inlet-poster-1280.webp", "w1920": "/assets/video/inlet-poster-1920.webp",
        "j768": "/assets/video/inlet-poster-768.jpg", "j1280": "/assets/video/inlet-poster-1280.jpg", "j1920": "/assets/video/inlet-poster-1920.jpg",
        "pa": "/assets/video/inlet-poster-portrait-720.avif", "pw": "/assets/video/inlet-poster-portrait-720.webp", "pj": "/assets/video/inlet-poster-portrait-720.jpg",
    },
}

HOME = {
    "kicker": "Concierge internal medicine · Palm Beach Gardens",
    "hero_lines": ["Concierge medicine", "with a doctor who", "<em>knows you</em>."],  # <em> is styled gold, upright: no italic font on the LCP path
    "hero_lede": "Dr. Yana Shtern keeps a small practice on purpose, so every member gets same or next business day visits, unhurried appointments, and a phone answered at any hour.",
    "problem_eyebrow": "The usual way",
    "problem_statement": "Fifteen minutes, a portal message, and a referral to someone you have never met.",
    "problem_lede": "Most primary care runs on volume. It is not that doctors stop caring. A schedule with thirty patients a day leaves no room to listen, to call you back, or to notice what changed since last year.",
    "problems": [
        ("Weeks to get in", "By the time there is an opening, you have either recovered or ended up at urgent care."),
        ("Nobody who knows the whole picture", "Five specialists, five portals, and no one doctor who has read all of it."),
        ("Questions that wait", "A message at 7 p.m. gets an answer in two days, from whoever is covering."),
    ],
    "guide_h": "One physician who knows your history, and has the time to use it.",
    "guide_body": "<p>Dr. Shtern trained in internal medicine and then in nephrology, and is board-certified in both. That combination matters more than it sounds: kidney function and blood pressure shape almost every prescription an internist writes.</p><p>She started Legacy Medical so she could take on fewer patients and do more for each of them. You see her at every visit, and members can reach the practice by phone at any hour.</p>",
    # Centered statement between two practice photos (Private Medical's move).
    "manifesto": "A small practice, on purpose. Fewer members means time to <em>listen</em>, to follow up, and to pick up the phone.",
    "manifesto_photos": [("reception-desk", "The front desk at Legacy Medical"), ("dr-shtern-desk", "Dr. Yana Shtern at her desk")],
    # Hover photos for the areas-of-focus list (topic photos, not the practice).
    "spec_peek": {"kidney-care": "p-kidney-water", "hypertension": "p-bp-walk", "geriatric-memory-care": "p-geri-couple",
                  "preventive-care": "p-prev-run", "telehealth": "p-tele-laptop"},
    "included_h": "What membership includes",
    "included_lede": "An annual membership fee covers access to Dr. Shtern. Office visits and tests are billed to your insurance, as they are now.",
    "clock_h": "The office keeps hours. Your access does not.",
    "clock_lede": "The office is open Monday to Friday. Outside those hours, members can still reach the practice by phone, at night, on weekends and on holidays.",
    "spec_h": "Internal medicine, plus a nephrologist's eye",
    "spec_lede": "Every member gets complete primary care. These are the areas where Dr. Shtern's second specialty and experience add the most.",
    "specialties": [
        ("kidney-care", "Kidney care", "CKD, rising creatinine, kidney stones, electrolyte problems, and care for people on dialysis."),
        ("hypertension", "Hypertension", "Blood pressure that stays high on two or three medicines, or comes with side effects."),
        ("geriatric-memory-care", "Geriatric and memory care", "Healthy aging, memory concerns, and fewer, better prescriptions."),
        ("preventive-care", "Preventive care and physicals", "The annual Legacy physical, with labs and an ECG done here."),
        ("telehealth", "Telehealth", "Video visits for follow-ups, results and medication questions."),
    ],
    "plan_h": "Three steps, no pressure",
    "steps": [
        ("Book a meet and greet", "Call or send a request. We will find a time that suits you."),
        ("Meet Dr. Shtern", "A complimentary meet-and-greet at the office. Ask about anything: the fee, your conditions, how after-hours calls work."),
        ("Join and book your physical", "If it is a fit, enroll and schedule your first Legacy physical. With your permission, the office requests your records from your previous doctor."),
    ],
    "agreement": "<strong>Your insurance still works here.</strong> The membership fee covers access and the extra time. Office visits, labs and tests are billed to your insurance the way they are today.",
    "reviews_h": "What patients say",
    "reviews_note": "Quoted as published on Healthgrades. More patient reviews:",
    "stakes_h": "Small changes are easier to catch early.",
    "stakes_body": "<p>A creatinine that creeps up a little each year, blood pressure that is fine in the office and high at home, a new medicine that does not sit well with an old one. In a rushed system these slip between visits.</p><p>With a doctor who knows your baseline, they come up in conversation instead of in the emergency room.</p>",
    "areas_h": "Close to Jupiter, Juno Beach and the Palm Beaches",
    "areas_lede": "The office sits on Prosperity Farms Road just north of PGA Boulevard, a short drive from most of northern Palm Beach County.",
}

HOME_FAQ = [
    ("How much is the membership fee?", "<p>The fee is not posted online yet. Call the office at <a href=\"tel:+15618349280\">(561) 834-9280</a> and we will go through it, or ask at your meet and greet. Office visits and tests are still billed to your insurance.</p>"),
    ("Do you take insurance?", "<p>Yes, for visits and tests. Medicare, Aetna, Cigna and BlueCross BlueShield are among the plans the practice works with. The membership fee itself is separate and is not billed to insurance. <a href=\"/insurance-and-fees\">How the fee and insurance fit together</a>.</p>"),
    ("Can I meet Dr. Shtern before joining?", "<p>Yes. Your first visit is a complimentary meet and greet, with no obligation. <a href=\"/meet-and-greet\">Book one here</a> or call.</p>"),
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
RATING_LINKS = [
    {"label": "Healthgrades", "url": "https://www.healthgrades.com/physician/dr-yana-shtern-gfc4n"},
    {"label": "US News", "url": "https://health.usnews.com/doctors/yana-shtern-650087"},
    {"label": "Google", "url": "https://www.google.com/maps/search/?api=1&query=Legacy%20Medical%20Concierge%20Dr.%20Yana%20Shtern"},
]

# Practice photos only: Dr. Shtern, the team, the Palm Beach Gardens office.
# The 2020 "Concierge Medicine of Jupiter" shoot is left out: it shows an
# earlier location and unidentified people.
REEL = [
    {"stem": "reception-desk", "alt": "The reception desk and gold Legacy Medical sign"},
    {"stem": "dr-shtern-desk", "alt": "Dr. Yana Shtern at her desk"},
    {"stem": "front-desk-team", "alt": "Dr. Shtern with a member of her team at the front desk"},
    {"stem": "yan-konevsky-rn", "alt": "Yan Konevsky, RN, office manager"},
    {"stem": "dr-yana-shtern", "alt": "Dr. Yana Shtern, MD"},
    {"stem": "reception-wall", "alt": "The Legacy Medical reception wall"},
    {"stem": "team-member", "alt": "A member of the Legacy Medical team"},
    {"stem": "front-desk-scrubs", "alt": "At the Legacy Medical front desk"},
    {"stem": "dr-shtern-full", "alt": "Dr. Shtern at the front desk"},
]

# ---------------------------------------------------------------- concierge medicine
CONCIERGE = {
    "title": "How Concierge Medicine Works | Legacy Medical, Palm Beach Gardens",
    "desc": "How concierge medicine works at Legacy Medical in Palm Beach Gardens: what the membership includes, what insurance still covers, and how it compares with a typical practice.",
    "eyebrow": "Concierge medicine",
    "h1": "Primary care with fewer patients and more time.",
    "lede": "Concierge medicine is a simple trade. You pay an annual membership fee, and in return the practice keeps its patient list small enough that you get your doctor's time and attention when you need them.",
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
        ("Insurance", "Billed for visits and tests", "Still billed for visits and tests; the membership fee is separate"),
    ],
    "sections": [
        ("Why the panel is small", "<p>A typical primary care doctor carries a list of two thousand patients or more. Concierge practices typically keep a few hundred. That is the whole idea: fewer patients means a schedule with room in it, so a same-day visit is normal rather than lucky, and a phone call gets returned by the doctor who knows you.</p><p>Dr. Shtern limits the number of members she takes on.</p>"),
        ("What the fee does not cover", "<p>The membership fee is not insurance. It does not pay for hospital stays, emergency care, specialists, imaging, or prescriptions. Keep your health insurance, including Medicare and any supplemental plan. Office visits and covered tests at Legacy Medical are billed to that insurance as usual.</p><p>If you are weighing the cost, the useful question is what the access is worth to you: how often you have waited weeks to be seen, or gone to urgent care because your doctor could not fit you in. <a href=\"/insurance-and-fees\">More on insurance and fees</a>.</p>"),
        ("Who it suits", "<p>Concierge care tends to suit people who want one doctor to keep track of everything: adults managing high blood pressure, kidney disease or diabetes; retirees and seasonal residents who want continuity between Florida and up north; busy professionals who cannot wait three weeks for an appointment; and adult children arranging care for a parent.</p><p>If your care is simple and your current doctor is easy to reach, you may not need a concierge practice. We will tell you that at your tour if it is true.</p>"),
        ("Concierge care and direct primary care", "<p>The two are often confused. Direct primary care practices usually replace insurance billing with a monthly fee and do not bill insurance at all. Legacy Medical is a concierge practice: the membership covers access, and your insurance is still billed for visits and tests.</p>"),
    ],
    "faqs": [
        ("What is concierge medicine?", "<p>A model of primary care where patients pay an annual membership fee and the doctor keeps a much smaller patient list. The smaller list is what makes same-day visits, longer appointments and direct phone access possible.</p>"),
        ("Is concierge medicine worth it?", "<p>It depends on how you use your doctor. People who manage several conditions, see multiple specialists, travel, or simply want to reach their own doctor quickly tend to find it worthwhile. Come to a meet and greet and ask Dr. Shtern directly; she will be straight with you.</p>"),
        ("Do I still need health insurance?", "<p>Yes. The membership fee does not replace insurance. You will still need coverage for hospital care, specialists, imaging, prescriptions and emergencies, and Legacy Medical bills your insurance for office visits and tests.</p>"),
        ("How many patients does Dr. Shtern see?", "<p>Far fewer than a typical practice, and the panel is capped. Concierge practices typically see six to ten patients a day; ask at your meet and greet how the schedule works here.</p>"),
        ("Will I always see Dr. Shtern?", "<p>Yes. She is the physician for every member.</p>"),
    ],
    "about": [{"@type": "MedicalSpecialty", "name": "Primary care"}, {"@type": "Thing", "name": "Concierge medicine"}],
    "related": ["membership", "insurance-and-fees", "preventive-care"],
}

# ---------------------------------------------------------------- service pages
SERVICE_PAGES = {
    "kidney-care": {
        "title": "Kidney Doctor in Palm Beach Gardens | Nephrology Care, Dr. Yana Shtern",
        "desc": "Board-certified nephrologist Dr. Yana Shtern cares for chronic kidney disease, rising creatinine, kidney stones and electrolyte problems at her Palm Beach Gardens practice.",
        "crumb": "Kidney care",
        "eyebrow": "Nephrology",
        "h1": "Kidney care from a doctor who is also your internist.",
        "lede": "Dr. Shtern is board-certified in nephrology as well as internal medicine. For members, that means kidney problems are looked after by the same doctor who manages everything else, with no handoff in between.",
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
            ("What care looks like here", "<p>For members, kidney care is part of membership rather than a separate referral. Dr. Shtern reviews your labs over time, not just the latest result, checks every prescription against your kidney function, and explains what the numbers mean in plain language.</p><p>Labs are drawn in the office. If you need imaging, a procedure, or dialysis planning, she arranges it and stays involved. She holds privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center.</p>"),
            ("Conditions Dr. Shtern manages", "<ul><li>Chronic kidney disease, all stages</li><li>Acute kidney injury and recovery</li><li>Protein in the urine (proteinuria)</li><li>Kidney stones: medical evaluation and prevention</li><li>Sodium, potassium, calcium and other electrolyte disorders</li><li>Kidney effects of diabetes and high blood pressure</li><li>Medication dosing for reduced kidney function</li><li>Care for patients with end-stage kidney disease, drawing on her dialysis experience</li></ul>"),
        ],
        "faq_h": "Kidney care questions",
        "faqs": [
            ("When should I see a nephrologist?", "<p>Common reasons are an eGFR below 60 that persists, a rapid drop in kidney function, protein or blood in the urine, recurring kidney stones, or blood pressure that will not come under control. If you are a member, you do not need a separate referral: Dr. Shtern is board-certified in nephrology.</p>"),
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
        "desc": "Help for high blood pressure that will not come down, from Dr. Yana Shtern, an internist and nephrologist in Palm Beach Gardens. Home readings, causes, and fewer side effects.",
        "crumb": "Hypertension",
        "eyebrow": "Hypertension",
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
            ("Why it gets complicated", "<p>The kidneys regulate salt and fluid, which is why blood pressure and kidney health are so closely linked, and why hypertension is part of nephrology training. Some high blood pressure has a specific cause, such as narrowed kidney arteries, an adrenal gland that makes too much aldosterone, sleep apnea, or a medicine like an anti-inflammatory or a decongestant. Finding that cause can change the treatment completely.</p>"),
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
        "title": "Geriatric and Memory Care in Palm Beach Gardens | Legacy Medical",
        "desc": "Concierge care for older adults in Palm Beach Gardens and Jupiter: memory concerns, medication reviews, fall prevention, and a doctor who keeps families informed.",
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
            ("Is a Medicare Annual Wellness Visit the same as a physical?", "<p>No. The Medicare Annual Wellness Visit is mostly a planning conversation and screening questionnaire. A physical includes an examination. Members get the annual Legacy physical; ask the office how Medicare billing applies to your visits.</p>"),
        ],
        "about": ["Dementia", "Mild cognitive impairment", "Polypharmacy", "Falls"],
        "related": ["preventive-care", "kidney-care", "concierge-medicine"],
        "cta_h": "Bring your parent, or your questions, to a meet and greet.",
        "photo": "front-desk-team", "photo_alt": "Dr. Shtern and her team at the Legacy Medical front desk",
    },
    "preventive-care": {
        "title": "Executive Physicals in Palm Beach Gardens | Legacy Medical",
        "desc": "The annual Legacy physical: an extended exam with in-office labs and ECG, screenings on schedule, and time to go over results with Dr. Yana Shtern in Palm Beach Gardens.",
        "crumb": "Preventive care and physicals",
        "eyebrow": "Preventive care",
        "h1": "A physical with the time to mean something.",
        "lede": "Every member gets an annual Legacy physical: an extended exam with labs and an ECG done in the office, and a follow-up conversation about what the results mean for you.",
        "specialty": "PrimaryCare",
        "service_node": {"@type": "MedicalProcedure", "name": "Annual Legacy physical", "procedureType": "https://schema.org/NoninvasiveProcedure",
                         "description": "An extended annual physical examination with in-office blood work and electrocardiogram, followed by a results review with the physician."},
        "points": [
            ("time", "An extended visit", "Time for your history, your family's history, and every question on your list."),
            ("lab", "Labs drawn here", "Blood work and stool occult blood testing without a trip to an outside lab."),
            ("ecg", "ECG in the office", "An electrocardiogram as part of the physical."),
            ("calendar", "Screenings on schedule", "Colonoscopy, mammography, bone density and others, arranged and tracked."),
        ],
        "sections": [
            ("What the Legacy physical covers", "<p>The physical starts with a conversation: your history, your family's history, your medicines and supplements, sleep, exercise, and anything that has changed. Then a full examination, an ECG, and blood work drawn in the office.</p><p>When results are back, you and Dr. Shtern go through them together. You leave with a plan for the year: which screenings are due, what to watch, and what to change.</p>"),
            ("An executive-style exam, without the hospital day", "<p>Executive physical programs often run a full day at a hospital campus with a team you will not see again. The Legacy physical covers the core of that work with your own physician, and Dr. Shtern adds imaging or specialist testing when your history or results call for it, rather than by default.</p>"),
            ("Screenings and vaccines", "<p>Dr. Shtern keeps track of what is due and when: colon cancer screening, mammograms, cervical screening, bone density, lung cancer screening for people with a smoking history, and adult vaccines. She arranges the ones done elsewhere and follows up on the results.</p>"),
        ],
        "faq_h": "Physical exam questions",
        "faqs": [
            ("What is included in an executive physical?", "<p>It varies by program. Most include an extended history and exam, thorough blood work, an ECG, and age-appropriate screenings. The Legacy physical includes all of these, with further testing ordered when it is warranted.</p>"),
            ("Is the annual physical covered by insurance?", "<p>Many plans cover a yearly preventive exam and standard screening labs. Coverage varies, so ask the office how your plan applies. The membership fee itself is separate from insurance.</p>"),
            ("Do I need to fast before my physical?", "<p>Often, yes, for certain blood tests. The office will tell you when you book.</p>"),
        ],
        "about": ["Preventive medicine", "Physical examination", "Cancer screening"],
        "related": ["concierge-medicine", "hypertension", "membership"],
        "cta_h": "Start with a meet and greet. Your first physical comes next.",
        "photo": "dr-yana-shtern", "photo_alt": "Dr. Yana Shtern, MD",
    },
    "telehealth": {
        "title": "Telehealth Visits with Dr. Yana Shtern | Legacy Medical",
        "desc": "Video visits with your own concierge doctor in Palm Beach Gardens for follow-ups, results and questions, so you do not always have to come in.",
        "crumb": "Telehealth",
        "eyebrow": "Telehealth",
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
    "Prevention and screening": ("preventive-care", "Preventive care and the Legacy physical"),
    "Heart and blood pressure": ("hypertension", "Help for high blood pressure"),
    "Nutrition": ("preventive-care", "Preventive care and the Legacy physical"),
    "Medications": ("geriatric-memory-care", "Medication reviews"),
    "Infections and vaccines": ("faq", "Same-day sick visits and testing"),
    "Everyday health": ("concierge-medicine", "How concierge medicine works here"),
}

# ---------------------------------------------------------------- membership
MEMBERSHIP = {
    "title": "How to Join Legacy Medical | Concierge Membership, Palm Beach Gardens",
    "desc": "How to become a member of Legacy Medical, Dr. Yana Shtern's concierge practice in Palm Beach Gardens. Start with a complimentary meet and greet with Dr. Shtern.",
    "eyebrow": "Membership",
    "h1": "Meet us first. Then decide.",
    "lede": "Joining starts with a conversation, not a contract. Visit the office, meet Dr. Shtern, and ask everything you want to know about how the practice works and what it costs.",
    "steps": [
        ("Book a meet and greet", "Use the request form or call (561) 834-9280. We will find a time that suits you."),
        ("Meet Dr. Shtern", "A complimentary meet-and-greet at the office. Bring your questions, and a family member if you like."),
        ("Enroll and book your physical", "If it is a good fit, you enroll, we request your records, and you schedule your first Legacy physical."),
    ],
    "agreement": "<strong>No obligation.</strong> The meet and greet is complimentary, and joining is your decision to make afterward.",
    "sections": [
        ("What to bring to the meet and greet", "<ul><li>Your questions about the fee, access and how after-hours calls work</li><li>A list of your current medicines and doctors, if you have one handy</li><li>Your insurance card, so we can tell you how visits are billed</li></ul><p>You do not need medical records for the meet and greet. If you join, we request them from your current doctor with your permission.</p>"),
        ("Who the practice is a good fit for", "<p>Adults who want one physician to know their whole history, people managing blood pressure, kidney disease, diabetes or several specialists, seasonal residents who want continuity, and families arranging care for a parent. Dr. Shtern is an internist: a physician trained in the care of adults.</p>"),
    ],
    "form_h": "Book a meet and greet",
    "form_lede": "Leave your details and the office will call or email you to set up a time. Prefer the phone? Call us during office hours.",
    "faqs": [
        ("Is the meet and greet really free?", "<p>Yes. The meet and greet is complimentary and there is no obligation to join.</p>"),
        ("What does membership cost?", "<p>The fee is not posted online. Call the office or ask at your meet and greet and we will go through it in full. Insurance is still billed for visits and tests.</p>"),
        ("How many members does the practice take?", "<p>The panel is limited, which is what keeps same-day visits possible. Ask the office whether new members are being accepted right now.</p>"),
    ],
}

INSURANCE = {
    "title": "Insurance and Membership Fees | Legacy Medical Concierge Practice",
    "desc": "How the concierge membership fee and your health insurance work together at Legacy Medical in Palm Beach Gardens, including Medicare, HSAs and what the fee covers.",
    "eyebrow": "Insurance and fees",
    "h1": "Two parts: a membership fee, and your insurance.",
    "lede": "Legacy Medical is a concierge practice that still works with insurance. The membership fee pays for access and time. Your insurance pays for visits and tests, as it does now.",
    "sections": [
        ("The membership fee", "<p>Members pay an annual fee directly to the practice. It covers what insurance does not pay for: a limited patient panel, same or next-business-day appointments, extended visits, 24/7 phone access and Dr. Shtern's time coordinating your care.</p><p>The fee is not published online yet. Call <a href=\"tel:+15618349280\">(561) 834-9280</a> or ask at your tour and the office will go through it with you.</p>"),
        ("What insurance still pays for", "<p>Office visits, lab work, ECGs and other covered services are billed to your health insurance. Plans the practice works with include Medicare, Aetna, Cigna and BlueCross BlueShield. Coverage, copays and deductibles depend on your plan, so check with the office before your first visit.</p><p>Keep your insurance. The membership does not cover hospital care, specialists, imaging, emergency care or prescriptions.</p>"),
        ("Medicare", "<p>Medicare does not pay concierge membership fees. If you have Medicare, the fee is separate, and covered services at your visits are billed to Medicare under its usual rules. Ask the office how this works for your plan, including any Medicare Advantage or supplemental coverage.</p>"),
    ],
    "faqs": [
        ("Does insurance cover the concierge fee?", "<p>No. Health insurance, including Medicare, does not pay the membership fee. It does pay for covered services at your visits.</p>"),
        ("Can I use an HSA or FSA for the fee?", "<p>Rules on using health savings or flexible spending accounts for concierge fees are not settled and depend on your plan. Ask your plan administrator or tax adviser before you count on it.</p>"),
        ("Is the concierge fee tax deductible?", "<p>That depends on your situation. A tax adviser can tell you whether it counts as a deductible medical expense for you.</p>"),
        ("Which insurance plans do you accept?", "<p>The practice works with Medicare, Aetna, Cigna and BlueCross BlueShield, among others. Plans change, so call the office to confirm yours.</p>"),
    ],
    "cta_lede": "We would rather explain the fee in person than post a number without context. Call the office, or come in for a meet and greet and ask.",
}

FAQ_PAGE = {
    "title": "Questions About Concierge Medicine at Legacy Medical | FAQ",
    "desc": "Answers about Legacy Medical's concierge practice in Palm Beach Gardens: appointments, after-hours calls, insurance, Medicare, hospitals, labs and joining.",
    "h1": "Straight answers.",
    "lede": "If your question is not here, call the office at (561) 834-9280.",
}

FAQ_GROUPS = [
    {"name": "Access and appointments", "pairs": [
        ("How quickly can I be seen?", "<p>Members are seen the same or next business day when something comes up. Routine visits are scheduled at a time that suits you.</p>"),
        ("Can I reach Dr. Shtern after hours?", "<p>Yes. Members have phone access to the practice 24 hours a day, 7 days a week. In an emergency, always call 911 first.</p>"),
        ("How long are visits?", "<p>Long enough to cover what you came in for. Visits are not booked in 15-minute slots.</p>"),
        ("Do you offer video visits?", "<p>Yes, for many follow-ups and results reviews. <a href=\"/telehealth\">About telehealth</a>.</p>"),
        ("What are the office hours?", "<p>Monday to Thursday 9:00 AM to 5:00 PM, Friday 9:00 AM to 2:00 PM. Closed on weekends, with member phone access around the clock.</p>"),
    ]},
    {"name": "Insurance and fees", "pairs": [
        ("How much does membership cost?", "<p>The fee is not published online. Call the office or ask at your meet and greet.</p>"),
        ("Do you bill insurance?", "<p>Yes, for office visits, labs and covered tests. Plans include Medicare, Aetna, Cigna and BlueCross BlueShield. <a href=\"/insurance-and-fees\">More on insurance and fees</a>.</p>"),
        ("Does Medicare pay the membership fee?", "<p>No. Medicare does not cover concierge fees. Covered services at your visits are billed to Medicare as usual.</p>"),
    ]},
    {"name": "Care and coordination", "pairs": [
        ("Are labs done in the office?", "<p>Yes. Blood is drawn in the office, and ECGs, stool occult blood tests and rapid flu, COVID-19 and strep tests are done here too.</p>"),
        ("What happens if I need a specialist?", "<p>Dr. Shtern chooses the specialist, contacts them, and follows up on what they find, so your care stays in one place.</p>"),
        ("Which hospitals does Dr. Shtern use?", "<p>She has privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center.</p>"),
        ("Do you treat kidney disease and high blood pressure?", "<p>Yes. Dr. Shtern is board-certified in nephrology as well as internal medicine. See <a href=\"/kidney-care\">kidney care</a> and <a href=\"/hypertension\">hypertension</a>.</p>"),
        ("Is there a patient portal?", "<p>Yes. Ask the office for access when you join.</p>"),
    ]},
    {"name": "Joining", "pairs": [
        ("How do I join?", "<p>Start with a complimentary meet and greet with Dr. Shtern. <a href=\"/meet-and-greet\">Book a meet and greet</a> or call (561) 834-9280.</p>"),
        ("What happens to my medical records?", "<p>With your permission, the office requests them from your previous doctor when you join.</p>"),
        ("Where are you located?", "<p>11380 Prosperity Farms Road, Suite 114, Palm Beach Gardens, FL 33410, on the first floor. See <a href=\"/contact\">directions</a>.</p>"),
    ]},
]

# ---------------------------------------------------------------- areas
AREAS_PAGE = {
    "title": "Areas We Serve: Jupiter, Juno Beach and the Palm Beaches",
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
        "title": "Concierge Doctor for Jupiter, FL | Legacy Medical, 15 Minutes Away",
        "desc": "A concierge internist about 15 minutes from Jupiter. Dr. Yana Shtern has privileges at Jupiter Medical Center and sees members the same or next business day.",
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
        "title": "Concierge Doctor in North Palm Beach | Legacy Medical, 6 Minutes Away",
        "desc": "Concierge internal medicine about six minutes from North Palm Beach. Same or next-day visits, labs in the office, and 24/7 phone access with Dr. Yana Shtern.",
        "h1": "A concierge internist six minutes from North Palm Beach.",
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
        "title": "Concierge Doctor Near Juno Beach | Legacy Medical, Palm Beach Gardens",
        "desc": "A concierge internist about seven minutes from Juno Beach, between Jupiter Medical Center and Palm Beach Gardens Medical Center, both hospitals where Dr. Shtern has privileges.",
        "h1": "Seven minutes from Juno Beach, with two hospitals close by.",
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
        "title": "Private Physician for Tequesta | Legacy Medical Concierge Practice",
        "desc": "Concierge internal medicine for Tequesta residents, about 17 minutes south. Dr. Yana Shtern has privileges at nearby Jupiter Medical Center.",
        "h1": "A private physician for Tequesta, a short drive down US-1.",
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
        "title": "Concierge Medicine for Palm Beach Residents | Legacy Medical",
        "desc": "Concierge internal medicine for Palm Beach island residents with Dr. Yana Shtern, board-certified in internal medicine and nephrology, about 25 minutes north in Palm Beach Gardens.",
        "h1": "Concierge medicine for Palm Beach, without the island waitlist.",
        "lede": "Palm Beach has plenty of concierge practices, and many are full. Legacy Medical is about 25 minutes north, and its physician is double board-certified in internal medicine and nephrology.",
        "from_label": "the town of Palm Beach",
        "sections": [
            ("A different kind of credential", "<p>Most concierge internists are trained in internal medicine alone. Dr. Shtern is also board-certified in nephrology and was medical director of a dialysis center, which makes a difference for anyone managing high blood pressure, kidney disease, or a long list of medications.</p>"),
            ("Making the drive easy", "<p>Many visits happen by <a href=\"/telehealth\">video</a>. For the rest, the office is a first-floor suite with accessible entry and minimal time in the waiting room.</p>"),
        ],
        "directions": "From Palm Beach, cross to Okeechobee Boulevard, take I-95 north to PGA Boulevard, head east, then north on Prosperity Farms Road.",
        "faqs": [("Do you see patients who live on Palm Beach island?", "<p>Yes. The office is roughly 25 minutes from the island without traffic.</p>")],
    },
    "west-palm-beach": {
        "name": "West Palm Beach",
        "title": "Concierge Doctor for West Palm Beach | Legacy Medical, Dr. Yana Shtern",
        "desc": "Concierge internal medicine and nephrology for West Palm Beach residents, about 20 minutes up I-95 in Palm Beach Gardens. Same or next-day visits.",
        "h1": "Twenty minutes up I-95 from West Palm Beach.",
        "lede": "For West Palm Beach residents, the office is a straight run up I-95 to PGA Boulevard. Members are seen the same or next business day.",
        "from_label": "downtown West Palm Beach",
        "sections": [
            ("Internist and nephrologist", "<p>Dr. Shtern is board-certified in internal medicine and nephrology. If you are managing kidney disease, hard-to-control blood pressure or electrolyte problems, you get both kinds of care from one doctor. See <a href=\"/kidney-care\">kidney care</a> and <a href=\"/hypertension\">hypertension</a>.</p>"),
            ("When you cannot come in", "<p>Many follow-ups, lab reviews and medication checks happen by <a href=\"/telehealth\">video visit</a>, and members can reach the practice by phone at any hour.</p>"),
        ],
        "directions": "Take I-95 north to the PGA Boulevard exit, head east, then turn north on Prosperity Farms Road to Suite 114.",
        "faqs": [("How far is Legacy Medical from West Palm Beach?", "<p>About 14 miles from downtown, roughly 21 minutes without traffic.</p>")],
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
JOURNAL_DESC = "Health articles from Legacy Medical, a concierge internal medicine practice in Palm Beach Gardens: blood pressure, kidney health, nutrition, prevention and more."

LEGAL = {}  # privacy, notice-of-privacy-practices, accessibility: see legal_content.py
from legal_content import LEGAL  # noqa: E402,F811


def llms_txt(P, D, pages, url):
    lines = [
        "# Legacy Medical",
        "",
        "> " + ONE_LINER,
        "",
        "## Facts",
        "- Practice: Legacy Medical (legal name Legacy Medical PLLC), concierge internal medicine",
        "- Physician: Dr. Yana Shtern, MD. Board-certified (ABIM) in Internal Medicine and Nephrology. NPI 1497940852. Florida license ME114615.",
        "- Hospital privileges: Jupiter Medical Center; Palm Beach Gardens Medical Center",
        "- Address: %s, %s, %s %s" % (P["street"], P["city"], P["region"], P["postal"]),
        "- Phone: %s. Fax: %s. Email: %s" % (P["phone"], P["fax"], P["email"]),
        "- Hours: Monday to Thursday 9:00 AM to 5:00 PM; Friday 9:00 AM to 2:00 PM; closed Saturday and Sunday. Members have 24/7 phone access.",
        "- Model: annual membership fee (not covered by insurance) plus insurance billing for visits and tests. Plans include Medicare, Aetna, Cigna, BlueCross BlueShield. The fee is not published; call the office.",
        "- How to join: a complimentary meet and greet with Dr. Shtern. Call or book at %s" % url("meet-and-greet"),
        "- Areas served: " + ", ".join(P["service_area"]) + ", Martin County",
        "- Internal medicine: care for adults.",
        "- Previous domain: cmedjupiter.com was an older copy of this site. legacymedicalpalmbeach.com is the current, authoritative site.",
        "",
        "## Pages",
    ]
    for pg in pages:
        if pg["slug"].startswith("journal/"):
            continue
        lines.append("- [%s](%s): %s" % (pg["title"], url(pg["slug"]), pg["desc"]))
    lines += ["", "## Journal"]
    for pg in pages:
        if pg["slug"].startswith("journal/"):
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
    "Do you bill insurance?": ["insurance", "aetna", "cigna", "blue cross", "bluecross", "bcbs", "covered", "coverage", "bill", "take medicare", "accept medicare", "medicare patients", "my plan"],
    "Does Medicare pay the membership fee?": ["medicare pay", "medicare cover", "does medicare", "medicare and the fee", "medicare fee"],
    "Are labs done in the office?": [" lab", "blood", "draw", "ecg", "ekg", "test", "covid", "flu", "strep"],
    "What happens if I need a specialist?": ["specialist", "referral", "refer", "cardiologist", "dermatologist"],
    "Which hospitals does Dr. Shtern use?": ["hospital", "jupiter medical", "gardens medical", "admitted", "privileges"],
    "Do you treat kidney disease and high blood pressure?": ["kidney", "nephrolog", "blood pressure", "hypertension", "renal"],
    "Is there a patient portal?": ["portal", "message", "online access", "records online"],
    "How do I join?": ["join", "sign up", "enroll", "become a patient", "new patient", "accepting", "tour", "meet", "greet", "first visit", "consultation"],
    "What happens to my medical records?": ["records", "transfer", "previous doctor", "chart"],
    "Where are you located?": ["where", "address", "located", "location", "directions", "parking", "find you"],
}

ASSIST_EXTRA = [
    {"k": ["emergency", "911", "chest pain", "can't breathe", "stroke", "urgent"],
     "a": "If this is an emergency, call 911 now. This assistant is not monitored. Members with an urgent question can call the practice at (561) 834-9280 at any hour."},
    {"k": ["phone number", "your number", "telephone", "contact you", "how do i contact", "email address"],
     "a": "Call (561) 834-9280 or email info@legacymedicalpalmbeach.com. The fax is (561) 834-9279."},
    {"k": ["dr. shtern", "dr shtern", "shtern", "doctor", "who is", "physician", "credentials", "board"],
     "a": "Dr. Yana Shtern, MD is board-certified in internal medicine and nephrology. She has privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center. <a href=\"/dr-yana-shtern\">About Dr. Shtern</a>."},
    {"k": ["concierge", "what is", "how does it work", "difference", "membership include", "included", "what do i get"],
     "a": "Concierge medicine means a smaller practice: same or next business day visits, unhurried appointments, and phone access to the practice around the clock. <a href=\"/concierge-medicine\">How it works here</a>."},
    {"k": ["area", "serve", "jupiter", "tequesta", "juno", "north palm", "palm beach", "stuart", "hobe sound"],
     "a": "Members come from across North County: Jupiter, Juno Beach, Tequesta, North Palm Beach, Palm Beach and West Palm Beach, plus Hobe Sound and Stuart. <a href=\"/areas-we-serve\">Areas and drive times</a>."},
    {"k": ["physical", "annual exam", "checkup", "check-up", "preventive", "screening"],
     "a": "Members get the annual Legacy physical: a thorough yearly exam with lab work and an ECG, then time to go through the results together. <a href=\"/preventive-care\">Preventive care and physicals</a>."},
    {"k": ["memory", "dementia", "elderly", "parent", "geriatric", "aging"],
     "a": "Dr. Shtern cares for older adults and the families who help them, including memory concerns and medication reviews. With the patient's written permission she can keep family members updated. <a href=\"/geriatric-memory-care\">Geriatric and memory care</a>."},
    {"k": ["prescription", "refill", "medication", "pharmacy"],
     "a": "Questions about your own medications are best handled by phone, so please call the office at (561) 834-9280 rather than writing them here."},
]

# ---------------------------------------------------------------- meet and greet
# The first visit. Only facts the practice has confirmed: it is complimentary,
# in person at the office, with Dr. Shtern, and carries no obligation.
MEET = {
    "title": "Meet and Greet with Dr. Shtern | Legacy Medical, Palm Beach Gardens",
    "desc": "Your first visit to Legacy Medical is a complimentary meet and greet with Dr. Yana Shtern in Palm Beach Gardens. What happens, what to ask, and how to book.",
    "eyebrow": "Your first visit",
    "h1": "It starts with a conversation.",
    "lede": "Before anyone joins, they sit down with Dr. Shtern. The meet and greet is complimentary, it happens at the office, and there is no obligation to join.",
    "steps": [
        ("You get in touch", "Call (561) 834-9280 or send the short form on this page. The office finds a time that suits you."),
        ("You meet Dr. Shtern", "A relaxed conversation in her office on Prosperity Farms Road. Bring a spouse or an adult child if you like."),
        ("You decide later", "There is no pressure to decide in the room. If you join, the office requests your records and books your first Legacy physical."),
    ],
    "sections": [
        ("What the meet and greet is", "<p>A chance for you and Dr. Shtern to see whether the practice is right for you. You talk about what you want from a doctor, how your care is going now, and how membership works day to day. Dr. Shtern explains how she practices, how members reach her, and what the membership fee includes.</p>"),
        ("Questions worth asking", "<ul><li>How quickly can members be seen when something comes up?</li><li>How do after-hours calls work, and who answers?</li><li>What does the membership fee include, and what is still billed to insurance?</li><li>How do you work with my specialists and with the hospital if I am admitted?</li><li>How large is the practice, and are new members being accepted right now?</li><li>What happens to my care when I am away for the summer?</li></ul><p>There are no wrong questions. Many people bring a written list.</p>"),
        ("What to bring", "<ul><li>Your questions, written down if that helps</li><li>A list of your current medicines and the doctors you see, if you have one handy</li><li>Your insurance card, so the office can tell you how visits are billed</li></ul><p>You do not need medical records. If you join, the office requests them from your current doctor with your permission.</p>"),
        ("Coming with a parent or partner", "<p>Families are welcome. Adult children often come along when they are arranging care for a parent, and couples often meet Dr. Shtern together. With the patient's written permission, she can keep family members updated later on.</p>"),
    ],
    "form_h": "Book a meet and greet",
    "form_lede": "Leave your details and the office will call or email you to set a time. Prefer the phone? Call during office hours.",
    "faqs": [
        ("Is the meet and greet really free?", "<p>Yes. It is complimentary and there is no obligation to join.</p>"),
        ("Where does it take place?", "<p>At the office: 11380 Prosperity Farms Road, Suite 114, Palm Beach Gardens. It is a first-floor suite with accessible entry.</p>"),
        ("Can I ask about the membership fee?", "<p>Please do. The fee is not posted online, and Dr. Shtern and the office would rather explain it in person, with what it covers.</p>"),
        ("Can my family member come?", "<p>Yes. Spouses and adult children are welcome.</p>"),
    ],
}

# ---------------------------------------------------------------- guide pages
# Audience and comparison pages. Same rule as everywhere: only confirmed facts
# about the practice; outside facts carry a link to the source.
GUIDES = {
    "seasonal-residents": {
        "title": "Concierge Doctor for Seasonal Residents | Legacy Medical, Palm Beach",
        "desc": "Primary care for seasonal residents of Palm Beach County: one internist who keeps your records current, coordinates with your doctors up north, and stays reachable.",
        "crumb": "Seasonal residents", "eyebrow": "Seasonal residents",
        "h1": "One doctor here who keeps up with you between seasons.",
        "lede": "Many people split the year between Palm Beach County and somewhere else. Concierge care suits that well: one physician who knows your history in Florida, stays in touch with your doctors elsewhere, and is easy to reach when you are back.",
        "photo": "dr-shtern-desk", "photo_alt": "Dr. Yana Shtern at her desk at Legacy Medical in Palm Beach Gardens",
        "sections": [
            ("When you arrive for the season", "<p>A doctor who has your records before you land makes the first weeks easier. With your permission, the office requests records from your physicians up north, so recent labs, imaging and medication changes are already in your chart.</p><p>Members are seen the same or next business day, so a cough that started on the drive down, or a prescription that needs adjusting, does not have to wait.</p>"),
            ("While you are here", "<p>Labs are drawn in the office, and ECGs and rapid flu, COVID-19 and strep tests are done there too. If you need a specialist, Dr. Shtern chooses one, makes the call and follows up on what they find. If you are admitted, she has privileges at Jupiter Medical Center and Palm Beach Gardens Medical Center.</p>"),
            ("When you head north", "<p>Before you leave, it helps to go over your medicines, refills and anything that should be followed up while you are away. With your permission, the office can send notes and results to your doctors at home so nobody starts from scratch.</p><p>Members can reach the practice by phone at any hour. Video visits work well for many follow-ups and results reviews, though licensing rules differ from state to state, so ask the office what applies where you will be.</p>"),
            ("Medicare in two places", "<p>Original Medicare works with participating doctors anywhere in the country, while Medicare Advantage plans usually use regional networks. <a href=\"https://www.medicare.gov/health-drug-plans/health-plans/your-coverage-options\" rel=\"noopener\">Medicare explains the difference</a>, and it matters if you see doctors in two states. The membership fee itself is not covered by Medicare; visits and tests are billed as usual. <a href=\"/insurance-and-fees\">How the fee and insurance fit together</a>.</p>"),
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
        "photo": "front-desk-team", "photo_alt": "Dr. Yana Shtern with a member of her team at the Legacy Medical front desk",
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
            ("What the membership fee pays for", "<p>The annual fee covers what insurance does not pay for: a limited patient panel, same or next-business-day appointments, unhurried visits, and phone access around the clock. <a href=\"https://www.medicare.gov/coverage/concierge-care\" rel=\"noopener\">Medicare does not cover membership fees</a>. Legacy Medical explains its fee in person at the meet and greet rather than posting a number without context.</p>"),
            ("Who tends to find it worthwhile", "<p>People who see several specialists, manage blood pressure, kidney disease or diabetes, travel or split the year between two homes, or are arranging care for a parent. People who rarely see a doctor may find a traditional practice suits them fine. <a href=\"/journal/is-a-concierge-doctor-right-for-me\">Is a concierge doctor right for you?</a></p>"),
        ],
        "faqs": [
            ("Is concierge medicine the same as direct primary care?", "<p>No. Direct primary care practices usually do not bill insurance and charge a monthly fee for most primary care. Concierge practices like Legacy Medical bill insurance for visits and tests and charge a separate membership fee. <a href=\"/journal/concierge-vs-direct-primary-care\">More on the difference</a>.</p>"),
            ("Do I lose my insurance if I join?", "<p>No. Insurance, including Medicare, is still billed for office visits, labs and tests. The membership fee is separate.</p>"),
            ("How do I find out what membership costs?", "<p>Call the office or ask at your complimentary meet and greet.</p>"),
        ],
        "related_posts": ["concierge-medicine-cost", "concierge-medicine-vs-mdvip", "does-medicare-cover-concierge-medicine", "questions-to-ask-a-concierge-doctor"],
        "related": ["concierge-medicine", "insurance-and-fees", "meet-and-greet"],
    },
}
CARD_BLURBS.update({
    "meet-and-greet": "Your first visit: a complimentary conversation with Dr. Shtern.",
    "seasonal-residents": "Continuity for people who split the year between Florida and somewhere else.",
    "for-families": "For adult children arranging care for a parent.",
    "concierge-vs-traditional-primary-care": "Access, time, insurance and fees, compared side by side.",
})
CATEGORY_OWNERS.update({
    "Seasonal residents": ("seasonal-residents", "Care for seasonal residents"),
    "Kidney health": ("kidney-care", "Kidney care and nephrology"),
    "Aging and family": ("for-families", "Care for an aging parent"),
})

# More set answers for the assistant. Facts only from this file; anything the
# practice has not confirmed gets "please ask the office".
ASSIST_EXTRA += [
    {"k": ["meet and greet", "meet & greet", "first visit", "first appointment", "consultation", "free visit", "complimentary"],
     "a": "Your first visit is a complimentary meet and greet with Dr. Shtern at the office. You talk about what you want from a doctor and how membership works, ask anything you like, and there is no obligation to join. <a href=\"/meet-and-greet\">About the meet and greet</a>."},
    {"k": ["what to bring", "bring with me", "should i bring"],
     "a": "For the meet and greet: your questions, a list of your current medicines and doctors if you have one, and your insurance card. You do not need medical records. <a href=\"/meet-and-greet\">More about the first visit</a>."},
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
     "a": "Dr. Shtern earned her medical degree at St. George's University School of Medicine and completed her internal medicine residency and nephrology fellowship at Maimonides Medical Center in Brooklyn. <a href=\"/dr-yana-shtern\">Her full background</a>."},
    {"k": ["castle connolly", "award", "recognition", "top doctor"],
     "a": "Dr. Shtern has been recognized as a Castle Connolly Top Doctor since 2023. <a href=\"/dr-yana-shtern\">About Dr. Shtern</a>."},
    {"k": ["license", "npi", "verify", "board certified", "board-certified", "certified"],
     "a": "Dr. Shtern is board-certified by the American Board of Internal Medicine in internal medicine and nephrology. Her Florida license is ME114615 and her NPI is 1497940852. <a href=\"/dr-yana-shtern\">Links to verify her credentials</a>."},
    {"k": ["kidney", "ckd", "creatinine", "egfr", "dialysis", "kidney stone", "nephrologist", "nephrology"],
     "a": "Dr. Shtern is board-certified in nephrology as well as internal medicine, so kidney care is part of her everyday practice: chronic kidney disease, rising creatinine, stones, electrolyte problems and care for people on dialysis. <a href=\"/kidney-care\">Kidney care</a>."},
    {"k": ["blood pressure", "hypertension", "bp "],
     "a": "High blood pressure, including blood pressure that stays high on two or three medicines, is one of Dr. Shtern's focus areas. <a href=\"/hypertension\">Hypertension care</a>."},
    {"k": ["diabetes", "cholesterol", "thyroid", "chronic"],
     "a": "Chronic disease management, including diabetes and cholesterol, is part of membership. For a question about your own condition, please call the office at (561) 834-9280. <a href=\"/concierge-medicine\">What membership includes</a>."},
    {"k": ["ecg", "ekg", "electrocardiogram", "heart test"],
     "a": "ECGs are done in the office, and an ECG is part of the annual Legacy physical."},
    {"k": ["flu test", "covid test", "strep", "rapid test", "sick visit", "sick", "cold", "fever"],
     "a": "Rapid flu, COVID-19 and strep tests are done in the office, and members are seen the same or next business day when they are sick. If you feel seriously unwell, call 911."},
    {"k": ["executive physical", "annual physical", "legacy physical", "check up", "checkup"],
     "a": "Members get the annual Legacy physical: a thorough yearly exam with lab work and an ECG, then time to go through the results together. <a href=\"/preventive-care\">Preventive care and physicals</a>."},
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
     "a": "Legacy Medical is an independent practice, not part of a national network. <a href=\"/journal/concierge-medicine-vs-mdvip\">How the models differ</a>."},
    {"k": ["direct primary care", "dpc"],
     "a": "Direct primary care practices usually do not bill insurance. Legacy Medical bills insurance for visits and tests and charges a separate membership fee. <a href=\"/journal/concierge-vs-direct-primary-care\">More on the difference</a>."},
    {"k": ["hsa", "fsa", "health savings", "flexible spending", "tax deductible", "deductible"],
     "a": "Whether a membership fee can come from an HSA or FSA depends on your plan and the tax rules, so please check with a tax advisor. <a href=\"/journal/hsa-fsa-concierge-medicine-fees\">What the 2026 rules say</a>."},
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
    "preventive-care": {"What the Legacy physical covers": "p-prev-stetho", "Screenings and vaccines": "p-prev-run"},
    "telehealth": {"What works well by video": "p-tele-laptop"},
    "seasonal-residents": {"When you arrive for the season": "p-seasonal-coast", "When you head north": "p-seasonal-travel"},
    "for-families": {"Come to the meet and greet together": "p-family-talk", "If your parent is in the hospital": "p-family-hands"},
    "concierge-vs-traditional-primary-care": {"Why the numbers matter": "p-compare-calendar"},
    "concierge-medicine": {"Why the panel is small": "p-concierge-phone", "Who it suits": "reception-desk"},
    "meet-and-greet": {"What the meet and greet is": "p-meet-coffee", "Coming with a parent or partner": "front-desk-scrubs"},
    "membership": {"What to bring to the meet and greet": "reception-wall"},
    "insurance-and-fees": {"The membership fee": "p-insurance-papers"},
    "areas-we-serve": {"Seasonal residents": "p-areas-palms"},
}
