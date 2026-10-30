"""Journal batch E: blood in the urine (hematuria). Chosen from Search Console, Oct 2026:
"blood in urine treatment in palm beach gardens" was landing on /kidney-care at position 30
with no article behind it, and it is a question a Nephrologist answers better than most.
Sourced from official pages linked inline; nothing about the practice beyond the facts in
content.py. Not yet medically reviewed (reviewed_by stays None until Dr. Shtern signs off)."""

POSTS = [
 {'slug': 'blood-in-urine-hematuria',
  'title': 'Blood in your urine: what it can mean and what testing looks like',
  'seo_title': 'Blood in Urine (Hematuria): Causes and Testing | Legacy Medical',
  'date': '2026-10-30T09:00:00',
  'modified': '2026-10-30T09:00:00',
  'category': 'Kidney health',
  'excerpt': "Visible or found on a urine test, blood in the urine always deserves a look. What can cause it, "
             "what the workup involves, and when to call right away.",
  'blocks': [
   {'type': 'p',
    'text': "Seeing pink, red or brown urine is alarming. Hearing that a routine urine test found blood you "
            "could not see is confusing in a different way. Both have a name, hematuria, and both deserve "
            "follow-up, though most of the time the cause turns out to be something treatable."},
   {'type': 'p',
    'text': "This guide explains the two kinds of hematuria, the common and the serious causes, and what the "
            "testing usually involves, based on the NIH's kidney and urology institute (NIDDK) and MedlinePlus."},
   {'type': 'h2', 'text': 'Two kinds: the blood you see and the blood you do not'},
   {'type': 'p',
    'text': "The NIDDK describes [two types of hematuria]"
            "(https://www.niddk.nih.gov/health-information/urologic-diseases/hematuria-blood-urine):"},
   {'type': 'ul',
    'items': ['**Gross hematuria** is blood you can see. It only takes a small amount of blood to change the '
              'color, and in most cases it causes no pain.',
              '**Microscopic hematuria** is blood found only on a urine test or under a microscope. It does not '
              'change the color of urine and usually has no symptoms, which is why it so often turns up at a '
              'routine physical.']},
   {'type': 'p',
    'text': "For microscopic blood, the American Urological Association's guideline panel defines it as "
            "[3 or more red blood cells per high power field on microscopic evaluation of a single "
            "specimen](https://pubmed.ncbi.nlm.nih.gov/32698717/). The NIDDK notes that your clinician may repeat "
            "the urine test to confirm it before going further."},
   {'type': 'h2', 'text': 'Red urine that is not blood'},
   {'type': 'p',
    'text': "Not every red tinge is blood. MedlinePlus points out that [urine can turn red from certain "
            "medicines, beets or other foods](https://medlineplus.gov/ency/article/003138.htm), and lists berries "
            "and rhubarb among the foods your provider may ask about. Blood can also come from somewhere other "
            "than the urinary tract and end up in the sample. The NIDDK notes that a menstrual period can make a "
            "urine test read positive, and a repeat test after the period ends is the usual answer."},
   {'type': 'p',
    'text': "None of that is a reason to wait and see. If you notice red or brown urine and are not sure why, "
            "tell your doctor."},
   {'type': 'h2', 'text': 'What can cause blood in the urine'},
   {'type': 'p',
    'text': "The NIDDK lists the more common causes as:"},
   {'type': 'ul',
    'items': ['Infection or inflammation of the bladder, kidney, urethra or prostate',
              'Urinary tract stones, or a recent procedure on the urinary tract',
              'An enlarged prostate (BPH)',
              'Vigorous exercise, such as long-distance running',
              'Sexual activity, trauma or endometriosis',
              'Some medicines, including blood thinners, certain antibiotics, and aspirin or other pain relievers']},
   {'type': 'p',
    'text': "The more serious causes on the same list include cancer of the bladder, kidney or prostate, "
            "blood-clotting disorders, sickle cell disease, and kidney disease involving the glomeruli, the tiny "
            "filters inside each kidney. Inflammation of those filters is called glomerulonephritis, and it is one "
            "of the reasons blood in the urine can be a kidney question as much as a bladder one."},
   {'type': 'p',
    'text': "Age and habits change the odds. The National Cancer Institute calls [smoking a major risk factor "
            "for bladder cancer](https://www.cancer.gov/types/bladder/causes-risk-factors) and notes that the risk "
            "rises with age. Workplace exposure to paints, dyes, metals or petroleum products is on that list too. "
            "The urology guideline above uses factors like these, along with how much blood was found and whether "
            "it persists, to sort people into low, intermediate and high risk groups."},
   {'type': 'p',
    'text': "If you take a blood thinner, do not assume the medicine explains it. Keep taking it as prescribed "
            "and call your doctor, who can decide whether more testing is needed."},
   {'type': 'h2', 'text': 'What the workup usually involves'},
   {'type': 'p',
    'text': "According to the NIDDK, the starting point is your medical history, a physical exam and a urinalysis. "
            "Expect questions like the ones MedlinePlus lists: when you first noticed it, the color, whether "
            "urinating hurts or happens more often, what medicines you take, and whether you have had kidney "
            "problems, surgery or an injury."},
   {'type': 'p',
    'text': "Depending on those answers, further tests may include:"},
   {'type': 'ul',
    'items': ['**A urine culture** to look for infection.',
              '**Blood tests**, such as creatinine to check kidney function and a complete blood count. Our guide '
              'to [reading your kidney lab results](/blog/egfr-kidney-lab-results-explained) explains eGFR.',
              '**A check for protein in the urine.** Blood and protein together point toward the kidney filters; '
              'see [the UACR urine test](/blog/uacr-protein-in-urine-test).',
              '**Imaging** of the kidneys and bladder, such as an ultrasound or a CT scan.',
              '**Cystoscopy**, in which a urologist uses a thin camera to look inside the bladder and urethra.',
              '**A kidney biopsy**, in a smaller number of people, when the pattern suggests disease of the '
              'kidney itself.']},
   {'type': 'p',
    'text': "How far the testing goes depends on your risk. The guideline panel recommends that cystoscopy and "
            "imaging be matched to each person's risk and decided together with the patient."},
   {'type': 'h2', 'text': 'Treatment, and when to call right away'},
   {'type': 'p',
    'text': "There is no treatment for hematuria itself. The NIDDK explains that clinicians treat the underlying "
            "cause, such as an infection or a stone, and that you may not need treatment at all if no serious "
            "condition is found. It also notes that diet has not been shown to cause or prevent hematuria."},
   {'type': 'p',
    'text': "MedlinePlus says never to ignore blood you can see in your urine, and to contact your provider "
            "right away if you also have:"},
   {'type': 'ul',
    'items': ['Fever, nausea, vomiting or shaking chills',
              'Pain in your abdomen, side or back',
              'Blood clots in your urine',
              'Trouble passing urine at all']},
   {'type': 'p',
    'text': "If you have severe pain or cannot urinate, our guide to [the ER, urgent care or calling your "
            "doctor](/blog/er-urgent-care-or-call-your-doctor) can help you decide where to go."},
   {'type': 'p',
    'text': "Blood in the urine sits where Internal Medicine, Urology and Nephrology meet. Some causes need a "
            "urologist's camera; others show up in the kidney numbers on your blood work. Dr. Yana Shtern is "
            "board-certified in both Internal Medicine and Nephrology, so she can read the urine test, the "
            "kidney labs and your medicine list together and decide which specialist, if any, you need next. "
            "The [kidney care](/kidney-care) page explains how she looks after kidney health at Legacy Medical, "
            "and members can usually be seen the [same or next business day](/same-or-next-day-visits)."},
   {'type': 'p',
    'text': "If a recent urine test came back with blood and you would like a second set of eyes on it, start "
            "with a complimentary [meet and greet](/meet-and-greet) at our Palm Beach Gardens office."},
  ],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},
]
