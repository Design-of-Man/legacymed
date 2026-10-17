"""Journal batch C (October 2026): prevention and screening, healthy aging, and
aging and family. Every medical or legal fact is linked inline to the official
or primary source it came from. Nothing about the practice beyond the facts in
content.py. Not yet medically reviewed (reviewed_by stays None until
Dr. Shtern signs off). The Florida advance directive article is general
information, not legal advice."""

USPSTF = "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/"
NEI = "https://www.nei.nih.gov/eye-health-information/eye-conditions-and-diseases/"
FS765 = "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0700-0799/0765/"

POSTS = [
    # 1 ---------------------------------------------------------------------
    {
        "slug": "colon-cancer-screening-colonoscopy-stool-tests",
        "title": "Colon cancer screening: colonoscopy, stool tests and when to start",
        "seo_title": "Colon Cancer Screening: Which Test and When | Legacy Medical",
        "date": "2026-10-16T09:00:00",
        "modified": "2026-10-16T09:00:00",
        "category": "Prevention and screening",
        "excerpt": "Screening for colorectal cancer now starts at 45. The test options, how often each one is "
                   "repeated, and what happens after an abnormal result.",
        "blocks": [
            {"type": "p", "text": "Colorectal screening can do two useful things. It can find cancer early, when it is "
             "easier to treat, and it can find polyps, small growths in the colon or rectum, so they can be removed "
             "before they have a chance to turn into cancer. That second job is why this screening matters so much, "
             "and why the starting age moved a few years ago."},
            {"type": "p", "text": "This article covers who should be screened, the tests you can choose from, and what "
             "to do if you have symptoms."},
            {"type": "h2", "text": "When to start, and when to stop"},
            {"type": "p", "text": "The U.S. Preventive Services Task Force updated its [colorectal cancer screening "
             "recommendation](" + USPSTF + "colorectal-cancer-screening) in May 2021. It recommends screening "
             "for all adults aged 45 to 75. For ages 50 to 75 the evidence is strongest (an A grade); the earlier start "
             "at 45 carries a B grade. For adults 76 to 85, the Task Force recommends deciding case by case, based on "
             "overall health, past screening results and personal preference. As of October 2026, the 2021 statement "
             "is still the current version."},
            {"type": "p", "text": "Those ages are for people at average risk. The CDC notes that you may need to "
             "[start before 45 or be screened more often](https://www.cdc.gov/colorectal-cancer/screening/index.html) "
             "if you have inflammatory bowel disease such as Crohn's disease or ulcerative colitis, a personal or "
             "family history of colorectal cancer or polyps, or a genetic syndrome such as Lynch syndrome or familial "
             "adenomatous polyposis. If any of these apply, the schedule should be set with your doctor."},
            {"type": "h2", "text": "The test options"},
            {"type": "p", "text": "The Task Force lists several acceptable approaches rather than a single test. "
             "Each has its own repeat interval:"},
            {"type": "ul", "items": [
                "**Colonoscopy, every 10 years.** A doctor examines the whole colon with a camera and can remove "
                "most polyps during the same procedure.",
                "**FIT (fecal immunochemical test) or high-sensitivity guaiac stool test, every year.** A kit you "
                "use at home to check stool for hidden blood.",
                "**Stool DNA test combined with FIT, every 1 to 3 years.** Checks stool for blood and for altered "
                "DNA. The CDC describes it as an [every-three-year test](https://www.cdc.gov/colorectal-cancer/screening/index.html).",
                "**CT colonography, every 5 years.** An imaging study, sometimes called virtual colonoscopy.",
                "**Flexible sigmoidoscopy, every 5 years,** or every 10 years when paired with a yearly FIT. "
                "It looks at the rectum and the lower part of the colon only.",
            ]},
            {"type": "p", "text": "One point is easy to miss. With a stool test, CT colonography or sigmoidoscopy, an "
             "abnormal result means the next step is a colonoscopy. The CDC is clear that these tests [need a "
             "follow-up colonoscopy](https://www.cdc.gov/colorectal-cancer/screening/index.html) when the result is "
             "positive, so a home test is the start of the process rather than the whole of it."},
            {"type": "h2", "text": "Choosing between them"},
            {"type": "p", "text": "Colonoscopy examines the entire colon and is the only option that can remove most "
             "polyps at the same sitting. It also involves bowel preparation the day before, sedation, and a ride home. "
             "Stool tests ask nothing of you beyond collecting a sample, but they have to be repeated on schedule to "
             "work, and a positive result leads to a colonoscopy anyway."},
            {"type": "p", "text": "Some practical questions help narrow the choice:"},
            {"type": "ul", "items": [
                "Have you had polyps before? If so, follow-up is usually by colonoscopy on a schedule based on what "
                "was found.",
                "Would you complete a yearly home kit reliably, every year?",
                "Do you take blood thinners, or have heart or lung conditions that affect sedation? Your doctor "
                "will want to plan around them.",
                "Do you split the year between Florida and another state? It helps to know where your last report "
                "lives and who will follow up a result.",
            ]},
            {"type": "p", "text": "On cost, the CDC notes that most health plans [cover screening tests with no "
             "deductible or co-pay](https://www.cdc.gov/colorectal-cancer/screening/index.html). Details vary by "
             "plan, so it is worth checking before you book, particularly for the follow-up colonoscopy after an "
             "abnormal stool test."},
            {"type": "h2", "text": "Symptoms are a different conversation"},
            {"type": "p", "text": "Screening is meant for people who feel well. Polyps and early cancers often cause "
             "no symptoms, which is the reason to screen. If you do have symptoms, you need a medical evaluation "
             "rather than a routine screening test. The CDC lists these [possible "
             "symptoms](https://www.cdc.gov/colorectal-cancer/symptoms/index.html):"},
            {"type": "ul", "items": [
                "A change in bowel habits",
                "Blood in or on your stool",
                "Diarrhea, constipation, or a feeling that the bowel does not empty all the way",
                "Abdominal pain, aches or cramps that do not go away",
                "Weight loss you cannot explain",
                "Low iron levels in the blood (anemia)",
            ]},
            {"type": "p", "text": "Many other conditions cause these symptoms, and most are not cancer. Still, call "
             "your doctor rather than waiting for your next screening date. Heavy rectal bleeding, or bleeding with "
             "dizziness or fainting, needs emergency care."},
            {"type": "p", "text": "For a broader look at lowering cancer risk, see our article on [cancer prevention "
             "and risk factors](/blog/cancer-prevention-risk-factors)."},
            {"type": "p", "text": "At Legacy Medical, Dr. Shtern goes over your family history and past reports, "
             "helps you pick the test that fits, and offers stool occult blood testing in the office. If a "
             "colonoscopy is the right choice, she [coordinates the referral](/specialists-and-hospital-care) and "
             "reviews the findings with you. Screening is part of [preventive care](/preventive-care) here. To meet "
             "her first, the first visit is a complimentary [meet and greet](/meet-and-greet)."},
        ],
        "sources": [],
        "stale_note": None,
        "reviewed_by": None,
    },
    # 2 ---------------------------------------------------------------------
    {
        "slug": "prostate-cancer-screening-psa-test",
        "title": "Prostate cancer screening and the PSA test: making a shared decision",
        "seo_title": "Prostate Cancer Screening and the PSA Test | Legacy Medical",
        "date": "2026-10-16T09:10:00",
        "modified": "2026-10-16T09:10:00",
        "category": "Prevention and screening",
        "excerpt": "The PSA test is a choice, not a routine. What the official guidance says, the real numbers on "
                   "benefit and harm, and questions to bring to your doctor.",
        "blocks": [
            {"type": "p", "text": "Most screening tests come with a simple instruction: get it on schedule. The PSA "
             "test for prostate cancer is different. Federal guidance asks men in a certain age range to decide for "
             "themselves, after a real conversation with their doctor. That can feel like being handed homework, but "
             "the reasons behind it are worth understanding."},
            {"type": "h2", "text": "What the PSA test measures"},
            {"type": "p", "text": "PSA, or prostate-specific antigen, is a protein made by the prostate. The blood test "
             "measures how much is circulating. Higher levels can occur with prostate cancer, but the CDC notes that "
             "PSA is also affected by [age, an enlarged prostate, infection, certain procedures and certain "
             "medicines](https://www.cdc.gov/prostate-cancer/screening/index.html). The National Cancer Institute "
             "adds that [inflammation and benign prostatic "
             "hyperplasia](https://www.cancer.gov/types/prostate/patient/prostate-screening-pdq), a common "
             "noncancerous enlargement, can both raise the number."},
            {"type": "p", "text": "So a high PSA is a reason to look further, not a diagnosis. The usual next steps "
             "are repeating the test, sometimes imaging, and in some cases a biopsy."},
            {"type": "h2", "text": "What the guidelines say"},
            {"type": "p", "text": "The U.S. Preventive Services Task Force's [current "
             "recommendation](" + USPSTF + "prostate-cancer-screening), from 2018, says:"},
            {"type": "ul", "items": [
                "**Men aged 55 to 69:** the decision to have PSA screening should be an individual one, made after "
                "talking through the benefits and harms with a clinician.",
                "**Men 70 and older:** the Task Force recommends against routine PSA screening.",
            ]},
            {"type": "p", "text": "The Task Force has an [update in "
             "progress](https://www.uspreventiveservicestaskforce.org/uspstf/draft-update-summary/prostate-cancer-screening-adults), "
             "but as of October 2026 no new draft has replaced the 2018 statement. Other medical groups publish their "
             "own advice, and the CDC notes that recommendations [differ between "
             "organizations](https://www.cdc.gov/prostate-cancer/screening/index.html). The Task Force also does not "
             "recommend the rectal exam as a screening test, because evidence of benefit is lacking."},
            {"type": "h2", "text": "The numbers behind the decision"},
            {"type": "p", "text": "The Task Force estimated what happens when 1,000 men aged 55 to 69 are offered PSA "
             "screening over about 13 years. Seeing the figures side by side explains why it is a judgment call:"},
            {"type": "ul", "items": [
                "About 240 get at least one positive PSA result, many of them false alarms.",
                "About 220 have at least one biopsy.",
                "About 100 are diagnosed with prostate cancer, and about 65 receive surgery or radiation at first.",
                "About 3 avoid cancer that spreads, and about 1.3 avoid dying of prostate cancer.",
            ]},
            {"type": "p", "text": "The harms are real too. Some cancers found by screening would never have caused "
             "symptoms in a man's lifetime, which is called overdiagnosis. Biopsies can cause bleeding, pain and "
             "infection. The Task Force reports that among men treated, about 1 in 5 who have surgery develop "
             "long-term urinary incontinence and about 2 in 3 develop long-term erectile dysfunction."},
            {"type": "p", "text": "One thing has changed the balance in recent years. More men with low-risk cancer now "
             "choose [active surveillance](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/616060): "
             "close monitoring with regular tests, and treatment only if the cancer shows signs of changing. The Task "
             "Force noted that its use rose from about 10 percent of low-risk cases in 2005 to 2009 to about 40 "
             "percent in 2010 to 2013. Finding a slow cancer no longer has to mean immediate surgery."},
            {"type": "h2", "text": "Who has higher risk"},
            {"type": "p", "text": "The CDC lists the main [risk "
             "factors](https://www.cdc.gov/prostate-cancer/risk-factors/index.html) as:"},
            {"type": "ul", "items": [
                "**Age.** Risk rises as men get older.",
                "**Being Black or African American.** Black men are more likely to get prostate cancer, to get it "
                "younger, and to die from it. The Task Force notes they are more than twice as likely as white men "
                "to die of it.",
                "**Family history.** A father, brother or son with prostate cancer raises risk. Relatives with "
                "breast, ovarian or pancreatic cancer can point to an inherited gene change.",
            ]},
            {"type": "p", "text": "Men at higher risk may weigh the decision differently, and some may want to talk "
             "about it before 55."},
            {"type": "h2", "text": "Questions worth asking"},
            {"type": "ul", "items": [
                "Given my age, health and family history, how much would screening likely help me?",
                "If my PSA comes back high, what would happen next, step by step?",
                "Do any of my medicines or conditions affect the result?",
                "If a low-risk cancer were found, would active surveillance be an option?",
                "If I decide against screening now, when should we revisit it?",
            ]},
            {"type": "p", "text": "Urinary symptoms are a separate matter from screening. Trouble starting, a weak "
             "stream, getting up often at night, or blood in the urine or semen deserve a visit whatever your "
             "screening choice. Our article on [how often you should "
             "urinate](/blog/how-often-should-you-urinate) covers what is typical."},
            {"type": "p", "text": "At Legacy Medical, appointments leave room for this kind of decision, and labs "
             "including PSA are drawn in the office if you choose to test. Dr. Shtern can walk through your own risk "
             "and results at the annual [executive physical](/preventive-care). If you would like to meet her first, "
             "the first visit is a complimentary [meet and greet](/meet-and-greet)."},
        ],
        "sources": [],
        "stale_note": None,
        "reviewed_by": None,
    },
    # 3 ---------------------------------------------------------------------
    {
        "slug": "abdominal-aortic-aneurysm-screening",
        "title": "Abdominal aortic aneurysm screening: who should get the one-time ultrasound",
        "seo_title": "AAA Screening: Who Needs the One-Time Ultrasound | Legacy Medical",
        "date": "2026-10-16T09:20:00",
        "modified": "2026-10-16T09:20:00",
        "category": "Prevention and screening",
        "excerpt": "A quick, painless ultrasound can find a weak spot in the body's largest artery before it causes "
                   "trouble. Who the guidelines say should have it, and when.",
        "blocks": [
            {"type": "p", "text": "Among the screening tests offered after 65, this one is easy to overlook. It is a "
             "single abdominal ultrasound, it takes a few minutes, it involves no needles or radiation, and for "
             "the right person it is done once in a lifetime. It looks for an abdominal aortic aneurysm, often "
             "shortened to AAA."},
            {"type": "h2", "text": "What an aortic aneurysm is"},
            {"type": "p", "text": "The aorta is the body's main artery. It runs from the heart down through the chest "
             "and abdomen. An aneurysm is a bulge in a weakened section of its wall. The National Heart, Lung, and "
             "Blood Institute notes that the abdomen is [the most common "
             "place](https://www.nhlbi.nih.gov/health/aortic-aneurysm) for one to form, and that it can grow without "
             "causing any symptoms."},
            {"type": "p", "text": "The Task Force defines an AAA as an aorta [3.0 centimeters across or "
             "larger](" + USPSTF + "abdominal-aortic-aneurysm-screening). Most small aneurysms are simply "
             "watched. The concern is a large one, which can tear or rupture, a life-threatening emergency. Finding "
             "an aneurysm early means it can be measured over time and repaired before it reaches that point. In "
             "men, repair is generally considered at 5.5 centimeters or larger."},
            {"type": "h2", "text": "Who should be screened"},
            {"type": "p", "text": "The U.S. Preventive Services Task Force [2019 "
             "recommendation](" + USPSTF + "abdominal-aortic-aneurysm-screening), still current as of October "
             "2026, breaks it down by sex and smoking history:"},
            {"type": "ul", "items": [
                "**Men aged 65 to 75 who have ever smoked:** one-time ultrasound screening is recommended.",
                "**Men aged 65 to 75 who have never smoked:** screening is offered selectively, based on medical "
                "history, family history, other risk factors and personal preference.",
                "**Women aged 65 to 75 who have ever smoked or have a family history of AAA:** the evidence is not "
                "yet strong enough to recommend for or against.",
                "**Women who have never smoked and have no family history:** routine screening is not recommended.",
            ]},
            {"type": "p", "text": "Smoking is the single biggest driver. In the trials the Task Force reviewed, "
             "screening men lowered deaths from AAA and the number of ruptures. It also led to more operations, "
             "which is part of why the advice is targeted rather than universal."},
            {"type": "h2", "text": "Other risk factors"},
            {"type": "p", "text": "The NHLBI lists several [risk factors for "
             "AAA](https://www.nhlbi.nih.gov/health/aortic-aneurysm/causes) beyond age and smoking:"},
            {"type": "ul", "items": [
                "**Family history.** About 1 in 5 people with a parent, sibling or child who had an AAA will develop "
                "one.",
                "**Being male.** Men develop AAA more often, though women who have one may rupture at a smaller "
                "size.",
                "**High blood pressure, high cholesterol and atherosclerosis,** including coronary or peripheral "
                "artery disease.",
                "**COPD, obesity, and kidney disease,** including chronic kidney disease and polycystic kidney "
                "disease.",
                "**Aneurysms elsewhere in the body.**",
            ]},
            {"type": "p", "text": "Current smokers may also have aneurysms that grow faster. Quitting helps at any age."},
            {"type": "h2", "text": "Medicare coverage and what to expect"},
            {"type": "p", "text": "Medicare Part B covers a [one-time AAA screening "
             "ultrasound](https://www.medicare.gov/coverage/abdominal-aortic-aneurysm-screening) for people at risk: "
             "anyone with a family history of AAA, or a man aged 65 to 75 who has smoked at least 100 cigarettes in "
             "his lifetime. You need a referral from your doctor. If the provider accepts Medicare assignment, there "
             "is usually no cost for the scan."},
            {"type": "p", "text": "The test itself is simple. You lie on your back while a technician moves a probe "
             "over your abdomen. You may be asked to fast for a few hours beforehand so gas in the bowel does not "
             "blur the picture. If the aorta is normal size, most people never need the test again. If a small "
             "aneurysm is found, the usual plan is repeat imaging at set intervals and close attention to blood "
             "pressure, cholesterol and smoking."},
            {"type": "h2", "text": "Warning signs that need 911"},
            {"type": "p", "text": "A rupture is an emergency. The NHLBI describes the signs as [sudden, severe pain "
             "in the stomach, chest or back](https://www.nhlbi.nih.gov/health/aortic-aneurysm/symptoms), along with "
             "light-headedness and a rapid heart rate. If you or someone with you has these symptoms, call 911. "
             "Do not drive yourself to the hospital."},
            {"type": "p", "text": "Because blood pressure and cholesterol both affect the aorta, our articles on "
             "[home blood pressure monitoring](/blog/home-blood-pressure-monitoring) and [ApoB and lipoprotein(a)]"
             "(/blog/apob-and-lipoprotein-a) are useful companions to this one."},
            {"type": "p", "text": "At Legacy Medical, Dr. Shtern reviews which screenings fit your age, smoking "
             "history and family history, writes the referral when the scan makes sense, and keeps track of any "
             "follow-up. Her Nephrology training means [blood pressure](/hypertension) and kidney health get close "
             "attention too. If you would like to meet her, the first visit is a complimentary [meet and "
             "greet](/meet-and-greet)."},
        ],
        "sources": [],
        "stale_note": None,
        "reviewed_by": None,
    },
    # 4 ---------------------------------------------------------------------
    {
        "slug": "hepatitis-c-and-hepatitis-b-screening",
        "title": "Hepatitis C and hepatitis B screening for adults",
        "seo_title": "Hepatitis C and B Screening for Adults | Legacy Medical",
        "date": "2026-10-16T09:30:00",
        "modified": "2026-10-16T09:30:00",
        "category": "Prevention and screening",
        "excerpt": "The CDC now advises every adult to be tested for hepatitis C and hepatitis B at least once. Why, "
                   "which blood tests are used, and what a positive result means today.",
        "blocks": [
            {"type": "p", "text": "Hepatitis B and hepatitis C are viral infections of the liver. Both can sit quietly "
             "for years, slowly causing scarring, and both are found with a simple blood test. Over the past few "
             "years the CDC has moved from testing only people with known risk factors to recommending that every "
             "adult be tested at least once."},
            {"type": "p", "text": "If you have never been tested, or are not sure, this is an easy item to add to "
             "your next blood draw."},
            {"type": "h2", "text": "Why test people who feel fine"},
            {"type": "p", "text": "The CDC notes that many people with hepatitis C [look and feel "
             "healthy](https://www.cdc.gov/hepatitis-c/about/index.html), and that most people who are infected "
             "develop a lifelong infection. Left untreated, it can lead to cirrhosis, liver failure and liver cancer, "
             "and it is a leading cause of liver transplants in the United States."},
            {"type": "p", "text": "Hepatitis B is similar. According to the CDC, about [1 in 2 people with hepatitis "
             "B do not know they are infected](https://www.cdc.gov/hepatitis-b/about/index.html), and many have no "
             "symptoms for decades. Chronic infection can also cause cirrhosis and liver cancer."},
            {"type": "p", "text": "Both viruses spread through blood, and hepatitis B also through other body fluids. "
             "Many people who test positive cannot point to a clear exposure, which is part of why testing everyone "
             "once makes sense."},
            {"type": "h2", "text": "Hepatitis C: test once, and the cure"},
            {"type": "p", "text": "The CDC's [hepatitis C testing "
             "recommendations](https://www.cdc.gov/hepatitis-c/hcp/diagnosis-testing/index.html), first issued in "
             "2020, say:"},
            {"type": "ul", "items": [
                "All adults 18 and older should be tested at least once in their lifetime.",
                "Pregnant women should be tested during each pregnancy.",
                "People with ongoing risk, including people on maintenance hemodialysis and people who inject drugs, "
                "should be tested regularly.",
                "Anyone who asks for a test should get one.",
            ]},
            {"type": "p", "text": "For most adults, that means a single test. Dialysis is one of the exceptions on "
             "both lists: people on maintenance dialysis are tested for hepatitis B and C on a regular schedule, which "
             "is one of the places where kidney care and liver screening meet."},
            {"type": "p", "text": "Testing starts with an antibody test. If it is reactive, a second test looks for "
             "the virus itself (HCV RNA). A positive antibody with a negative RNA result usually means a past "
             "infection that has cleared or been treated."},
            {"type": "p", "text": "The news after a positive result is better than it used to be. Current oral "
             "medicines [cure more than 95 percent of people in 8 to 12 "
             "weeks](https://www.cdc.gov/hepatitis-c/treatment/index.html). Hepatitis C has gone from a lifelong "
             "condition to one that, for most people, is treated once and finished."},
            {"type": "h2", "text": "Hepatitis B: test once, with three markers"},
            {"type": "p", "text": "In 2023 the CDC updated its [hepatitis B testing "
             "advice](https://www.cdc.gov/hepatitis-b/hcp/diagnosis-testing/index.html):"},
            {"type": "ul", "items": [
                "All adults 18 and older should be screened at least once.",
                "The recommended screen is a triple panel: hepatitis B surface antigen (HBsAg), surface antibody "
                "(anti-HBs) and total core antibody (anti-HBc).",
                "People with ongoing risk, including people on dialysis, people with HIV and people who inject drugs, "
                "should be tested periodically.",
                "Anyone who asks for a test should get one.",
            ]},
            {"type": "p", "text": "The three markers together answer three questions: are you infected now, have you "
             "been infected in the past, and are you protected by vaccination or past infection. That last answer "
             "is useful on its own."},
            {"type": "p", "text": "Treatment for chronic hepatitis B is different from hepatitis C. The CDC notes "
             "that medicines exist for chronic hepatitis B but [are not a "
             "cure](https://www.cdc.gov/hepatitis-b/about/index.html), and that regular liver monitoring by a "
             "specialist matters."
             ""},
            {"type": "h2", "text": "What about the hepatitis B vaccine?"},
            {"type": "p", "text": "If your triple panel shows you are not immune, vaccination may be the next step. "
             "The CDC currently [recommends the hepatitis B "
             "vaccine](https://www.cdc.gov/hepatitis-b/vaccination/index.html) for adults aged 19 to 59, and for "
             "adults 60 and older who have risk factors for hepatitis B. Vaccine "
             "advice has been under review in recent years, so it is worth confirming the current guidance with "
             "your doctor."},
            {"type": "h2", "text": "When to call sooner"},
            {"type": "p", "text": "Screening is for people without symptoms. The CDC lists signs of liver infection "
             "such as [yellow skin or eyes, dark urine, clay-colored stools, nausea and "
             "fatigue](https://www.cdc.gov/hepatitis-c/about/index.html). If you notice yellowing of the skin or "
             "eyes, call your doctor promptly. Confusion, vomiting blood or black stools need emergency care."},
            {"type": "p", "text": "For a fuller picture of routine blood work, see [what you need from an annual "
             "physical](/blog/annual-physical-what-you-need)."},
            {"type": "p", "text": "At Legacy Medical, blood is drawn in the office, so hepatitis B and C screening can "
             "be added to the [labs](/labs-and-tests) you are already having. If a result is positive, Dr. Shtern "
             "explains it and coordinates the right specialist. To meet her first, the first visit is a "
             "complimentary [meet and greet](/meet-and-greet)."},
        ],
        "sources": [],
        "stale_note": None,
        "reviewed_by": None,
    },
    # 5 ---------------------------------------------------------------------
    {
        "slug": "eye-health-after-50",
        "title": "Eye health after 50: glaucoma, macular degeneration and cataracts",
        "seo_title": "Eye Health After 50: Glaucoma, AMD, Cataracts | Legacy Medical",
        "date": "2026-10-16T09:40:00",
        "modified": "2026-10-16T09:40:00",
        "category": "Healthy aging",
        "excerpt": "Three common eye conditions of later life, how each one shows up, who is at higher risk, and "
                   "the eye symptoms that need same-day care.",
        "blocks": [
            {"type": "p", "text": "Needing reading glasses is the eye change everyone expects. Less obvious are the "
             "conditions that can take vision slowly, often before you notice anything wrong. Glaucoma, age-related "
             "macular degeneration and cataracts all become more common after 50, and for each one, finding it early "
             "changes what can be done."},
            {"type": "p", "text": "The main tool is a dilated eye exam, in which drops widen the pupils so an eye "
             "doctor can see the retina and optic nerve. The National Eye Institute explains [what the exam "
             "involves](https://www.nei.nih.gov/eye-health-information/healthy-vision/finding-eye-doctor/get-dilated-eye-exam)."},
            {"type": "h2", "text": "Glaucoma: the quiet one"},
            {"type": "p", "text": "Glaucoma is a group of diseases that damage the optic nerve. According to the NEI, "
             "it [usually has no early "
             "symptoms](" + NEI + "glaucoma), and side vision tends to go first, so slowly that "
             "many people do not notice. There is no cure, but treatment with eye drops, laser or surgery can often "
             "stop further damage. Vision already lost does not come back, which is the argument for finding it early."},
            {"type": "p", "text": "The NEI lists higher risk for:"},
            {"type": "ul", "items": [
                "People over 60, especially Hispanic or Latino adults",
                "African American adults over 40",
                "Anyone with a family history of glaucoma",
            ]},
            {"type": "p", "text": "For people at higher risk, the NEI recommends a dilated eye exam every 1 to 2 "
             "years."},
            {"type": "h2", "text": "Macular degeneration: central vision"},
            {"type": "p", "text": "Age-related macular degeneration, or AMD, affects the macula, the part of the "
             "retina responsible for sharp, straight-ahead vision. The NEI notes it is a [leading cause of vision "
             "loss in older adults](" + NEI + "age-related-macular-degeneration), "
             "though it does not cause complete blindness. Risk is higher after 55, with a family history, in white "
             "adults, and in people who smoke."},
            {"type": "p", "text": "Early AMD usually causes no symptoms. Later, straight lines may look wavy, a "
             "blurry or blank spot may appear in the center of vision, and colors may look duller. The NEI calls "
             "wavy lines a warning sign of late AMD and advises seeing an eye doctor right away if it happens."},
            {"type": "p", "text": "There are two forms. The dry form is more common and progresses slowly. For people "
             "with intermediate dry AMD, a specific combination of vitamins and minerals studied by the NEI may help "
             "slow progression to late AMD. The supplements are meant for people who already have AMD. The wet form is less common but can cause "
             "faster vision loss, and it is treated with injections into the eye."},
            {"type": "p", "text": "The NEI's advice for lowering risk will sound familiar: do not smoke, stay active, "
             "keep blood pressure and cholesterol in a healthy range, and eat leafy greens and fish."},
            {"type": "h2", "text": "Cataracts: clouding of the lens"},
            {"type": "p", "text": "A cataract is a cloudy area in the eye's lens. By age 80, the NEI reports, [more "
             "than half of Americans either have cataracts or have had surgery for "
             "them](" + NEI + "cataracts). Common signs are blurry or faded vision, glare, halos around "
             "lights, and trouble seeing at night, which matters a great deal for night driving."},
            {"type": "p", "text": "Risk factors include age, diabetes, smoking, heavy drinking, steroid medicines and "
             "a lot of sun exposure. In Florida, that last one deserves attention: the NEI recommends sunglasses and "
             "a brimmed hat outdoors. Surgery replaces the cloudy lens with an artificial one, and the NEI describes "
             "it as very safe, with about 9 in 10 people seeing better afterward. It is usually timed for when "
             "cataracts start to interfere with daily life."},
            {"type": "h2", "text": "How often to be checked, and when not to wait"},
            {"type": "p", "text": "The NEI advises a dilated exam every 1 to 2 years from age 60, and for people at "
             "higher risk of glaucoma. People with diabetes need one [at least once a "
             "year](" + NEI + "diabetic-retinopathy) to check for diabetic retinopathy."},
            {"type": "p", "text": "Some eye symptoms are emergencies. Go to an emergency room or call your eye doctor "
             "right away for:"},
            {"type": "ul", "items": [
                "A sudden shower of new floaters, flashes of light, or a dark shadow or curtain across part of your "
                "vision. These can signal a [retinal detachment](" + NEI + "retinal-detachment).",
                "Sudden severe eye pain with redness, blurred vision and nausea, which can be a form of glaucoma "
                "called angle-closure.",
                "Sudden loss of vision in one eye, or sudden double vision. Call 911 if it comes with weakness, "
                "numbness or trouble speaking, since these can be signs of stroke.",
            ]},
            {"type": "p", "text": "Eye health ties into the rest of your care. Blood sugar, blood pressure and "
             "smoking all affect the eyes, and our articles on [prediabetes and the A1c "
             "test](/blog/prediabetes-and-a1c) and [protecting your skin in the Florida "
             "sun](/blog/skin-cancer-checks-florida) cover related ground."},
            {"type": "p", "text": "At Legacy Medical, Dr. Shtern keeps track of when your last eye exam was, makes sure "
             "your eye doctor knows about conditions such as diabetes, and reviews medicines like steroids that can "
             "affect the eyes. She [coordinates with specialists](/specialists-and-hospital-care) so results come "
             "back to one place. To meet her, the first visit is a complimentary [meet and greet](/meet-and-greet)."},
        ],
        "sources": [],
        "stale_note": None,
        "reviewed_by": None,
    },
    # 6 ---------------------------------------------------------------------
    {
        "slug": "depression-in-older-adults",
        "title": "Depression in older adults: signs that are easy to miss",
        "seo_title": "Depression in Older Adults: Signs Easy to Miss | Legacy Medical",
        "date": "2026-10-16T09:50:00",
        "modified": "2026-10-16T09:50:00",
        "category": "Healthy aging",
        "excerpt": "Depression in later life often looks like tiredness, aches or lost interest rather than sadness. "
                   "The signs, what can mimic it, and how it is treated.",
        "blocks": [
            {"type": "p", "text": "Depression is common in later life, but it is not a normal part of getting older. "
             "The National Institute on Aging puts it plainly: most older adults [feel satisfied with their "
             "lives](https://www.nia.nih.gov/health/mental-and-emotional-health/depression-and-older-adults), even "
             "with more illnesses than younger people. When low mood, flatness or loss of interest settle in for "
             "weeks, it deserves the same attention as any other medical problem."},
            {"type": "p", "text": "The difficulty is that depression in older adults often does not look the way "
             "people expect."},
            {"type": "h2", "text": "Why it is easy to miss"},
            {"type": "p", "text": "The NIA notes that for some older adults, [sadness is not the main "
             "symptom](https://www.nia.nih.gov/health/mental-and-emotional-health/depression-and-older-adults). "
             "Instead they may feel numb, lose interest in things they used to enjoy, or simply not talk about "
             "feelings the way younger adults might. In some people depression shows up mainly as physical "
             "complaints: aches, headaches, digestive problems."},
            {"type": "p", "text": "It also overlaps with other things that happen with age. Poor sleep gets blamed on "
             "getting older. Fatigue gets blamed on a heart condition or a new medicine. Forgetfulness raises worry "
             "about dementia, when trouble concentrating can be a symptom of depression."},
            {"type": "h2", "text": "Signs to watch for"},
            {"type": "p", "text": "The NIA lists these common symptoms in older adults. If several last more than two "
             "weeks, talk with your doctor:"},
            {"type": "ul", "items": [
                "A persistent sad, anxious or empty mood",
                "Feeling hopeless, guilty, worthless or helpless",
                "Irritability or restlessness",
                "Loss of interest in activities you used to enjoy",
                "Low energy or fatigue, or moving and talking more slowly",
                "Trouble concentrating, remembering or making decisions",
                "Sleeping poorly, waking very early, or sleeping too much",
                "Eating more or less than usual, with weight gain or loss you did not intend",
                "Drinking more, or taking more risks",
                "Thoughts of death or suicide",
            ]},
            {"type": "p", "text": "Family members often notice first: a parent who stops calling friends, skips the "
             "weekly card game, lets the mail pile up or seems short-tempered. Those changes are worth a gentle "
             "question."},
            {"type": "h2", "text": "Who is at higher risk"},
            {"type": "p", "text": "The NIA links a higher risk of depression to serious illness such as stroke or "
             "cancer, a personal or family history of depression, caregiver stress, sleep problems, loneliness and "
             "isolation, low physical activity, limits on daily activities, and alcohol misuse. Major losses, "
             "including the death of a spouse, retirement or a move away from friends, can set it off."},
            {"type": "p", "text": "Depression and dementia also overlap. The NIA notes that depression is common in "
             "people with dementia, and that it can sometimes be an early warning sign. That is one more reason to "
             "have changes in mood or memory looked at rather than waiting."},
            {"type": "h2", "text": "Getting checked and getting treated"},
            {"type": "p", "text": "The U.S. Preventive Services Task Force [recommends screening all adults for "
             "depression](" + USPSTF + "screening-depression-suicide-risk-adults), "
             "and its 2023 statement explicitly includes adults 65 and older. Screening is usually a short set of "
             "questions at a regular visit."},
            {"type": "p", "text": "A good evaluation also looks for other causes. Certain medicines and medical "
             "conditions can produce the same symptoms, and the NIA notes that a doctor can rule these out with an "
             "exam, a careful history and lab tests. Side effects of common medicines are one example worth "
             "checking."},
            {"type": "p", "text": "Treatment works for most people. The main options are:"},
            {"type": "ul", "items": [
                "**Talk therapy,** such as cognitive behavioral therapy or interpersonal therapy, with a "
                "psychologist, licensed clinical social worker or psychiatrist.",
                "**Medicines,** most often SSRIs in older adults. Because aging changes how the body handles drugs, "
                "the starting dose and possible interactions need care.",
                "**Both together,** which is common.",
                "**Other treatments,** such as brain stimulation therapies, for depression that has not improved "
                "with the usual approaches.",
            ]},
            {"type": "p", "text": "The NIA notes it is common to try more than one treatment before finding the right "
             "fit, and that outpatient mental health care is generally covered by Medicare and private insurance. "
             "Regular activity, sleep and staying in touch with people help alongside treatment, though they do not "
             "replace it."},
            {"type": "h2", "text": "If someone is in crisis"},
            {"type": "p", "text": "If you or someone you love is thinking about suicide, call or text "
             "[988](https://988lifeline.org/), the Suicide and Crisis Lifeline, available 24 hours a day. If there "
             "is immediate danger, call 911. The NIA notes that asking someone directly whether they are thinking "
             "about suicide does not make them more likely to act on it, and can help them open up."},
            {"type": "p", "text": "Related reading: [memory changes and when to see a "
             "doctor](/blog/memory-changes-when-to-see-a-doctor), [hearing loss and "
             "memory](/blog/hearing-loss-and-memory), and [reviewing medicines in older "
             "adults](/blog/medication-review-older-adults)."},
            {"type": "p", "text": "At Legacy Medical, visits are unhurried, which makes it easier to bring up mood, "
             "sleep or grief. Dr. Shtern checks for medical causes, reviews every medicine, and refers to a mental "
             "health professional when that is the right step. Families of older patients can read more on "
             "[care for families](/for-families). To meet her first, the first visit is a complimentary [meet and "
             "greet](/meet-and-greet)."},
        ],
        "sources": [],
        "stale_note": None,
        "reviewed_by": None,
    },
    # 7 ---------------------------------------------------------------------
    {
        "slug": "loneliness-and-social-connection",
        "title": "Loneliness and social connection as a health issue",
        "seo_title": "Loneliness and Health: Why Connection Matters | Legacy Medical",
        "date": "2026-10-16T10:00:00",
        "modified": "2026-10-16T10:00:00",
        "category": "Healthy aging",
        "excerpt": "Loneliness and isolation are linked to heart disease, stroke, depression and dementia. What the "
                   "research shows and practical ways to rebuild connection.",
        "blocks": [
            {"type": "p", "text": "Doctors ask about smoking, alcohol and exercise at almost every visit. Fewer ask "
             "who you talked to this week. The research of the past decade suggests they should, because social "
             "connection turns out to be closely tied to physical health, especially as people get older."},
            {"type": "h2", "text": "Loneliness and isolation are not the same thing"},
            {"type": "p", "text": "The National Institute on Aging draws a useful distinction. [Loneliness is the "
             "distressing feeling of being alone or "
             "separated](https://www.nia.nih.gov/health/loneliness-and-social-isolation/loneliness-and-social-isolation-tips-staying-connected). "
             "Social isolation is having few people to interact with regularly. You can live alone and feel "
             "connected, and you can feel lonely in a full house or a busy community."},
            {"type": "p", "text": "Both become more likely with age. The NIA points to hearing and vision loss, "
             "memory problems, trouble getting around, and the loss of family and friends. Retirement, the death of "
             "a spouse, caring for someone who is ill, and moving away from familiar people all play a part. "
             "Moving to Florida in retirement, or splitting the year between two homes, can mean starting over "
             "socially in one place or both."},
            {"type": "h2", "text": "What the research shows"},
            {"type": "p", "text": "In 2023 the U.S. Surgeon General issued an [advisory on loneliness and "
             "isolation](https://www.hhs.gov/sites/default/files/surgeon-general-social-connection-advisory.pdf). "
             "Among its findings:"},
            {"type": "ul", "items": [
                "About one in two U.S. adults reported experiencing loneliness in recent years, even before the "
                "pandemic.",
                "Loneliness and social isolation were linked to a 26 percent and 29 percent higher risk of "
                "premature death.",
                "Poor social connection was associated with a 29 percent higher risk of heart disease and a 32 "
                "percent higher risk of stroke.",
                "The advisory compared the mortality effect of social disconnection to smoking up to 15 cigarettes "
                "a day.",
            ]},
            {"type": "p", "text": "The NIA adds high blood pressure, weakened immune function, anxiety, depression, "
             "cognitive decline and dementia to the list of associated risks. People who are lonely or isolated "
             "also tend to have longer hospital stays and more readmissions."},
            {"type": "p", "text": "These studies show associations, and the arrows run both ways: poor health can "
             "make people more isolated, and isolation can make health worse. Part of the link is behavior. The "
             "NIA notes that lonely people are more likely to exercise less, drink more, smoke and sleep poorly. Part "
             "may be biological, with long-term stress responses that promote inflammation."},
            {"type": "h2", "text": "Practical ways to rebuild connection"},
            {"type": "p", "text": "Connection is something you can work on, much like fitness. The NIA suggests "
             "starting small and choosing what suits you:"},
            {"type": "ul", "items": [
                "**Schedule contact.** A standing phone call, a weekly lunch, a regular video chat with "
                "grandchildren.",
                "**Join something with a rhythm.** A walking group, a class, a faith community, a book club or a "
                "volunteer shift brings the same faces back each week.",
                "**Volunteer.** The NIA links helping others with a sense of purpose and better health.",
                "**Combine movement and company.** Exercising with a friend counts twice.",
                "**Learn the technology.** Libraries and community centers often teach video calling and email.",
                "**Consider a pet,** if you are able to care for one.",
                "**Introduce yourself to neighbors.** Small, regular contact adds up.",
            ]},
            {"type": "p", "text": "For local programs, the federal [Eldercare Locator](https://eldercare.acl.gov/home), "
             "at 800-677-1116, connects older adults and families with Area Agencies on Aging and community services."},
            {"type": "h2", "text": "Fix what gets in the way"},
            {"type": "p", "text": "Sometimes the barrier is medical. Hearing loss is a common one: the NIA notes that "
             "people who cannot follow conversations may withdraw, and can even be mistaken for confused. Treating "
             "it can reopen a social life. Our article on [hearing loss and "
             "memory](/blog/hearing-loss-and-memory) explains why it matters. Poor vision, fear of falling, "
             "incontinence, chronic pain and depression can all keep people at home, and all can be addressed."},
            {"type": "p", "text": "Other barriers are practical. The NIA lists lack of transportation, being unable to "
             "leave home without help, financial strain and language barriers among the risk factors for isolation. "
             "If giving up driving is on the horizon, it helps to plan rides, deliveries and regular visits before "
             "the keys are handed over."},
            {"type": "p", "text": "If you feel lonely much of the time, tell your doctor. That is part of your health, "
             "and it often connects to sleep, mood, blood pressure and memory. If loneliness comes with persistent "
             "sadness or thoughts of self-harm, see our article on [depression in older "
             "adults](/blog/depression-in-older-adults), and call or text 988 in a crisis."},
            {"type": "p", "text": "At Legacy Medical, Dr. Shtern asks about the parts of life that affect health "
             "beyond lab numbers, and has the time to listen. For adult children watching a parent become more "
             "isolated, our page on [care for families](/for-families) explains how she can help. The first visit is "
             "a complimentary [meet and greet](/meet-and-greet)."},
        ],
        "sources": [],
        "stale_note": None,
        "reviewed_by": None,
    },
    # 8 ---------------------------------------------------------------------
    {
        "slug": "brain-health-what-the-evidence-supports",
        "title": "Keeping your brain healthy: what the evidence supports",
        "seo_title": "Brain Health: What the Evidence Supports | Legacy Medical",
        "date": "2026-10-16T10:10:00",
        "modified": "2026-10-16T10:10:00",
        "category": "Healthy aging",
        "excerpt": "Blood pressure, hearing, exercise and social contact have real evidence behind them. Supplements "
                   "and brain-training apps mostly do not. A plain look at the research.",
        "blocks": [
            {"type": "p", "text": "There is no shortage of products promising a sharper memory. The real evidence on "
             "protecting the brain is less exciting to market and more useful: much of it comes down to the same "
             "things that protect the heart and blood vessels, plus hearing, sleep and other people."},
            {"type": "p", "text": "This article sorts what has solid support from what does not, as of late 2026."},
            {"type": "h2", "text": "How much of dementia might be preventable"},
            {"type": "p", "text": "In 2024 the Lancet Commission on dementia, an international expert group, "
             "published an [updated report](https://pubmed.ncbi.nlm.nih.gov/39096926/) naming 14 modifiable risk "
             "factors across life. They are less education early in life, hearing loss, high LDL cholesterol, "
             "depression, head injury, physical inactivity, diabetes, smoking, high blood pressure, obesity, "
             "excessive alcohol, social isolation, air pollution and untreated vision loss. High LDL and vision loss "
             "were new additions."},
            {"type": "p", "text": "The Commission estimated that nearly half of dementia cases, about 45 percent, "
             "could in theory be prevented or delayed if all 14 were removed. That is a population estimate, not a "
             "promise to any one person, and age and genes still matter. But it means a good share of risk sits in "
             "things that can be treated."},
            {"type": "h2", "text": "What has the strongest support"},
            {"type": "p", "text": "**Blood pressure control.** In the SPRINT MIND trial, published in JAMA in 2019, "
             "adults 50 and older with high blood pressure were assigned to a systolic target below 120 or below 140. "
             "The [lower target reduced mild cognitive impairment](https://pubmed.ncbi.nlm.nih.gov/30688979/), often a "
             "step before dementia. The reduction in dementia itself did not reach statistical significance, and the "
             "authors noted the trial ended early and may have been too small to show it. Our article on [blood "
             "pressure and brain health](/blog/blood-pressure-and-brain-health) covers this in more detail."},
            {"type": "p", "text": "**A combination of healthy habits.** The US POINTER trial, published in JAMA in "
             "2025, followed more than 2,000 adults aged 60 to 79 at higher risk of decline. Both groups were "
             "encouraged to exercise, eat well, stay mentally and socially active and monitor heart health. The "
             "group with a [structured, coached program improved slightly "
             "more](https://pubmed.ncbi.nlm.nih.gov/40720610/) on thinking tests over two years than the group that "
             "worked on it alone. The difference was modest, but it suggests that structure and accountability help."},
            {"type": "p", "text": "**Physical activity.** The National Institute on Aging describes [several studies "
             "linking activity with brain health](https://www.nia.nih.gov/health/brain-health/cognitive-health-and-older-adults), "
             "while noting that more research is needed on exactly how much exercise prevents decline. Since activity "
             "also lowers blood pressure, blood sugar and depression, it supports several risk factors at once."},
            {"type": "p", "text": "**Hearing.** Hearing loss is one of the larger risk factors in the Lancet list. "
             "Our article on [hearing loss and memory](/blog/hearing-loss-and-memory) explains the link and the "
             "case for testing."},
            {"type": "p", "text": "**Social contact.** The NIA cites research in which high social engagement, such as "
             "visiting neighbors and volunteering, was associated with better thinking in later life. See [loneliness "
             "and social connection](/blog/loneliness-and-social-connection)."},
            {"type": "h2", "text": "What has weaker support"},
            {"type": "ul", "items": [
                "**Supplements.** The NIA states that no vitamin or supplement is currently recommended for "
                "preventing Alzheimer's or cognitive decline. Recent trials found a daily multivitamin may modestly "
                "help memory in older adults, which is different from preventing dementia.",
                "**Brain-training apps.** The NIA warns there is not enough evidence that commercial brain games have "
                "the effect seen in research-based cognitive training. Hobbies that keep you learning and around "
                "other people are still worth doing for their own sake.",
                "**Single foods or diets as a cure.** Healthy eating patterns support the heart and weight, which "
                "helps the brain indirectly, but no single food prevents dementia.",
            ]},
            {"type": "h2", "text": "A practical checklist"},
            {"type": "ul", "items": [
                "Know your blood pressure, ideally from [home readings](/blog/home-blood-pressure-monitoring), "
                "and treat it if it is high.",
                "Check LDL cholesterol and blood sugar, and treat them when needed.",
                "Have your hearing and vision tested, and use hearing aids or glasses if they help.",
                "Move most days, including some strength and balance work.",
                "Do not smoke, and keep alcohol low.",
                "Protect your head: wear a seatbelt and a bike helmet, and reduce fall risks at home.",
                "Treat depression and poor sleep rather than putting up with them.",
                "Keep people in your week.",
            ]},
            {"type": "p", "text": "One more item belongs on the list. The NIA notes that some medicines and "
             "combinations of medicines can cause confusion and memory problems in older adults. A [medication "
             "review](/blog/medication-review-older-adults) is a simple place to start. And if memory is already "
             "changing, see [memory changes: when to see a doctor](/blog/memory-changes-when-to-see-a-doctor)."},
            {"type": "p", "text": "At Legacy Medical, Dr. Shtern works through these risk factors with you over time, "
             "with labs drawn in the office and close attention to blood pressure. For patients and families "
             "concerned about memory, our page on [geriatric and memory care](/geriatric-memory-care) explains how "
             "she approaches it. To meet her, the first visit is a complimentary [meet and greet](/meet-and-greet)."},
        ],
        "sources": [],
        "stale_note": None,
        "reviewed_by": None,
    },
    # 9 ---------------------------------------------------------------------
    {
        "slug": "caregiver-burnout-caring-for-a-parent",
        "title": "Caregiver burnout: looking after yourself while caring for a parent",
        "seo_title": "Caregiver Burnout: Caring for a Parent and You | Legacy Medical",
        "date": "2026-10-16T10:20:00",
        "modified": "2026-10-16T10:20:00",
        "category": "Aging and family",
        "excerpt": "Caring for a parent is meaningful and exhausting. The warning signs of caregiver stress, how to "
                   "ask for help, and where to find respite.",
        "blocks": [
            {"type": "p", "text": "Caring for an aging parent often starts small: a ride to an appointment, help with "
             "the pill box, a daily phone call. Over months it can grow into a second job, layered on top of work, a "
             "marriage and your own health. Many caregivers find real meaning in it. Many also reach a point where "
             "they are running on empty without quite noticing."},
            {"type": "p", "text": "You are far from alone. A CDC analysis of national survey data found that [about "
             "one in five adults](https://pubmed.ncbi.nlm.nih.gov/32078592/) had provided care to a family member or "
             "friend in the previous 30 days."},
            {"type": "h2", "text": "Why caregivers' own health slips"},
            {"type": "p", "text": "The National Institute on Aging notes that caregivers are [less likely to get "
             "preventive care](https://www.nia.nih.gov/health/caregiving/taking-care-yourself-tips-caregivers) such as "
             "annual checkups, and tend to have higher rates of physical and mental health problems, sleep problems "
             "and conditions like high blood pressure. The time goes to someone else's appointments, and your own get "
             "postponed."},
            {"type": "h2", "text": "Warning signs of caregiver stress"},
            {"type": "p", "text": "The NIA lists these signs. Learning your own early warnings makes it easier to act "
             "before you are completely overwhelmed:"},
            {"type": "ul", "items": [
                "Feeling exhausted, overwhelmed or anxious",
                "Becoming easily angered or impatient",
                "Feeling lonely or cut off from others",
                "Trouble sleeping, or not getting enough sleep",
                "Feeling sad or hopeless, or losing interest in things you used to enjoy",
                "Frequent headaches, pain or other physical problems",
                "No time to exercise or cook proper meals for yourself",
                "Skipping your own basic care",
                "Relying more on alcohol or medicines, including prescription drugs",
            ]},
            {"type": "p", "text": "If sadness or hopelessness lasts more than a couple of weeks, that may be "
             "depression, which is treatable. Our article on [depression in older "
             "adults](/blog/depression-in-older-adults) lists the signs, and they apply at any age. If you ever "
             "feel you might harm yourself or the person you care for, call or text 988, or call 911 in an emergency."},
            {"type": "h2", "text": "Asking for help, and making it specific"},
            {"type": "p", "text": "Many caregivers say they did too much on their own. The NIA suggests a few ways to "
             "make asking easier:"},
            {"type": "ul", "items": [
                "Keep a running list of tasks, so when someone offers, they can pick one.",
                "Start with small, concrete requests: one grocery run, one afternoon visit, one ride.",
                "Match the task to the person. A sibling who lives far away may handle insurance calls or bills.",
                "Use text or email if asking face to face is hard.",
                "Expect some people to say no, and do not take it personally.",
            ]},
            {"type": "p", "text": "Family is not the only source of help. The NIA suggests telling your own doctor "
             "that you are a caregiver, talking with a counselor, contacting your local senior center or Area Agency "
             "on Aging, and asking your faith community about support groups."},
            {"type": "h2", "text": "Respite: a real break"},
            {"type": "p", "text": "Respite care is short-term care that gives the main caregiver time off. The NIA "
             "describes [several forms](https://www.nia.nih.gov/health/caregiving/what-respite-care): family, friends "
             "or volunteers stepping in, in-home aides, adult day programs, and state or veterans' programs. For "
             "someone receiving hospice care, Medicare covers most of the cost of up to five consecutive days of "
             "respite in a hospital or skilled nursing facility. Some long-term care insurance policies cover respite "
             "too."},
            {"type": "p", "text": "To find local services, the federal [Eldercare Locator](https://eldercare.acl.gov/home) "
             "at 800-677-1116 connects families with Area Agencies on Aging and community programs, including "
             "caregiver support."},
            {"type": "h2", "text": "Looking after yourself in practice"},
            {"type": "ul", "items": [
                "**Keep your own appointments.** Put your checkup on the calendar as firmly as your parent's.",
                "**Protect sleep.** Aim for seven to nine hours, with regular bed and wake times when you can.",
                "**Move a little every day.** A short walk counts.",
                "**Eat real meals.** Batch cooking or a meal service can help on heavy weeks.",
                "**Keep one thing that is yours.** A standing tennis game, a weekly lunch, an hour with a book.",
                "**Find people who understand.** Caregiver support groups, in person or online, can be a relief.",
            ]},
            {"type": "p", "text": "Paperwork helps too. Having your parent's medication list, doctors and advance "
             "directives in one place saves hours in a crisis. See our articles on [concierge care for aging "
             "parents](/blog/concierge-care-for-aging-parents) and [Florida advance "
             "directives](/blog/florida-advance-directives-health-care-surrogate)."},
            {"type": "p", "text": "At Legacy Medical, members reach the practice by phone at any hour, and Dr. "
             "Shtern coordinates specialists and hospital care, which takes some of the load off family. With your "
             "parent's permission, she can keep you informed. Our page on [care for families](/for-families) "
             "explains how that works, and the first visit is a complimentary [meet and greet](/meet-and-greet)."},
        ],
        "sources": [],
        "stale_note": None,
        "reviewed_by": None,
    },
    # 10 --------------------------------------------------------------------
    {
        "slug": "florida-advance-directives-health-care-surrogate",
        "title": "Advance directives in Florida: health care surrogate and living will basics",
        "seo_title": "Florida Health Care Surrogate and Living Will | Legacy Medical",
        "date": "2026-10-16T10:30:00",
        "modified": "2026-10-16T10:30:00",
        "category": "Aging and family",
        "excerpt": "How Florida law handles a health care surrogate, a living will and decisions when there is no "
                   "directive, with links to the statute. General information, not legal advice.",
        "blocks": [
            {"type": "p", "text": "Most people put off advance directives because the subject is uncomfortable. Yet "
             "they are among the most practical documents an adult can have. If an illness or injury leaves you "
             "unable to speak for yourself, a directive tells your doctors who should decide for you and what you "
             "would want."},
            {"type": "p", "text": "**This article is general information, not legal advice.** Florida's rules are set "
             "out in [Chapter 765 of the Florida Statutes](" + FS765 + "0765.html). For advice on your own situation, "
             "especially with a complicated family, property in more than one state, or a guardianship question, "
             "speak with a Florida attorney who handles estate planning or elder law."},
            {"type": "h2", "text": "The main documents"},
            {"type": "p", "text": "Florida law defines an [advance directive](" + FS765 + "Sections/0765.101.html) "
             "broadly. It includes:"},
            {"type": "ul", "items": [
                "**A designation of health care surrogate,** naming the person who makes health care decisions "
                "for you.",
                "**A living will,** stating your wishes about life-prolonging treatment in specific situations.",
                "**An anatomical gift,** your decision about organ and tissue donation.",
            ]},
            {"type": "p", "text": "You can complete one, two or all three. Florida's Agency for Health Care "
             "Administration publishes a [consumer guide with sample "
             "forms](https://quality.healthfinder.fl.gov/report-guides/advance-directives). The statute provides "
             "suggested wording, but its own text says a living will [may, but need not, follow that "
             "form](" + FS765 + "Sections/0765.303.html)."},
            {"type": "h2", "text": "Health care surrogate"},
            {"type": "p", "text": "Under [section 765.202](" + FS765 + "Sections/0765.202.html):"},
            {"type": "ul", "items": [
                "The designation must be signed in front of **two adult witnesses.**",
                "The person you name as surrogate cannot be one of the witnesses.",
                "At least one witness must be **neither your spouse nor a blood relative.**",
                "You may name an **alternate surrogate** in case the first is unwilling or unavailable.",
                "Your surrogate should be given an exact copy.",
            ]},
            {"type": "p", "text": "Florida also lets you choose whether your surrogate's authority starts "
             "[immediately or only if you lose capacity](" + FS765 + "Sections/0765.101.html). Immediate authority "
             "can help a spouse or adult child who already helps with appointments and records."},
            {"type": "p", "text": "Under [section 765.204](" + FS765 + "Sections/0765.204.html), you are presumed able to "
             "make your own decisions, and while you can, your wishes control. If capacity is in question, your "
             "physician evaluates it and records the result, and a second physician is involved when the first is "
             "unsure."},
            {"type": "h2", "text": "Living will"},
            {"type": "p", "text": "Under [section 765.302](" + FS765 + "Sections/0765.302.html), any competent adult may "
             "make a living will directing whether life-prolonging procedures are provided, withheld or withdrawn if "
             "they have a terminal condition, an end-stage condition, or a persistent vegetative state. It needs the "
             "same witnessing as a surrogate designation: two witnesses, at least one neither a spouse nor a blood "
             "relative."},
            {"type": "p", "text": "The statute puts the responsibility on you to let your primary physician know the "
             "living will exists, so that it becomes part of your medical record. In practice, give copies to your "
             "doctor, your surrogate and close family, and tell them where the original is kept. The AHCA guide also "
             "suggests a wallet card saying you have a directive."},
            {"type": "h2", "text": "If there is no directive"},
            {"type": "p", "text": "When an incapacitated adult has no directive, [section "
             "765.401](" + FS765 + "Sections/0765.401.html) sets an order of people who may act as a proxy: a "
             "court-appointed guardian, then a spouse, then a majority of adult children who are reasonably "
             "available, then a parent, then a majority of adult siblings, then a close relative or friend who meets "
             "the statute's conditions, and finally a licensed clinical social worker chosen through a bioethics "
             "committee."},
            {"type": "p", "text": "That order may not match whom you would choose. A partner you are not married to, "
             "or one child who knows your wishes best, is not automatically first in line. Naming a surrogate avoids "
             "this."},
            {"type": "h2", "text": "Changes, other states and DNR orders"},
            {"type": "ul", "items": [
                "**Changing or revoking.** Under [section 765.104](" + FS765 + "Sections/0765.104.html), you can amend "
                "or revoke a directive at any time with a signed and dated writing, by destroying it, by an oral "
                "statement, or by signing a new one. Divorce revokes a former spouse's designation as surrogate "
                "unless the document or court order says otherwise.",
                "**Directives from another state.** [Section 765.112](" + FS765 + "Sections/0765.112.html) says a "
                "directive validly made under another state's law, or Florida's, is valid in Florida. Seasonal "
                "residents may still want an attorney to review older documents.",
                "**Do not resuscitate orders.** A Florida DNRO is a separate form, [DH Form "
                "1896](https://www.floridahealth.gov/about-us/resources/do-not-resuscitate-order/). The Department "
                "of Health says it must be printed on yellow paper and signed by your physician or another authorized "
                "clinician to be honored by emergency crews outside a hospital.",
            ]},
            {"type": "p", "text": "Financial decisions are handled differently, usually through a durable power of "
             "attorney under a separate chapter of Florida law. An attorney can explain how the documents fit together."},
            {"type": "p", "text": "Our articles on [concierge care for aging "
             "parents](/blog/concierge-care-for-aging-parents) and [what happens with a concierge doctor during a "
             "hospital stay](/blog/concierge-doctor-hospital-stay) cover the medical side of planning ahead."},
            {"type": "p", "text": "At Legacy Medical, Dr. Shtern is glad to talk through the medical questions behind "
             "a living will, such as what a ventilator or feeding tube involves, and to keep copies of your "
             "directives in your chart. She holds privileges at local hospitals and stays involved if you are "
             "admitted. Families can read more on [care for families](/for-families), and the first visit is a "
             "complimentary [meet and greet](/meet-and-greet)."},
        ],
        "sources": [],
        "stale_note": None,
        "reviewed_by": None,
    },
]
