"""Journal batch D: practical patient guides (visit prep, lab panels, where to get
care, travel with medicines, allergies, mosquito-borne illness, checkups after 50,
hydration and fiber). Sourced from official pages linked inline; nothing about the
practice beyond the facts in content.py. Not yet medically reviewed (reviewed_by
stays None until Dr. Shtern signs off)."""

POSTS = [
 {'slug': 'how-to-prepare-for-a-doctors-visit',
  'title': "How to prepare for a doctor's visit: a simple checklist",
  'seo_title': "How to Prepare for a Doctor's Visit: Checklist | Legacy Medical",
  'date': '2026-10-17T09:00:00',
  'modified': '2026-10-17T09:00:00',
  'category': 'Concierge medicine',
  'excerpt': "A short checklist for getting the most out of any appointment: what to write down, what to bring, "
             "and what to ask before you leave.",
  'blocks': [
   {'type': 'p',
    'text': "Most of what a doctor learns at a visit comes from you: what changed, when it started, what you are "
            "taking and what worries you. A little preparation turns a rushed appointment into a useful one, "
            "and it matters most when you have several conditions, see more than one specialist, or are "
            "helping a parent with their care."},
   {'type': 'p',
    'text': "The checklist below draws on guidance from the National Institute on Aging and the Agency for "
            "Healthcare Research and Quality (AHRQ). Print it, copy it into your phone, or keep it in the "
            "folder you bring to appointments."},
   {'type': 'h2', 'text': 'A few days before'},
   {'type': 'p',
    'text': "The National Institute on Aging suggests [starting a list ahead of "
            "time](https://www.nia.nih.gov/health/medical-care-and-appointments/how-prepare-doctors-appointment) "
            "and putting your main concerns at the top, so they come up early instead of in the last two "
            "minutes. Three or four priorities is a realistic number for one visit."},
   {'type': 'ul',
    'items': ['**Your top concerns.** Write each one as a short sentence. "Tired by 3 p.m. most days since '
              'August" is more useful than "fatigue."',
              '**New symptoms in detail.** When it started, how often it happens, how long it lasts, what makes '
              'it better or worse, and how it affects your day.',
              '**Changes since your last visit.** A fall, a hospital or urgent care stop, a new specialist, a '
              'change in sleep, appetite, mood or memory.',
              '**Questions about tests or treatment.** If you had labs or imaging elsewhere, note where and when '
              'so the results can be requested.']},
   {'type': 'h2', 'text': 'Your medication list'},
   {'type': 'p',
    'text': "This is the single most useful thing you can bring. AHRQ recommends [bringing every medicine you "
            "take](https://www.ahrq.gov/patients-consumers/patient-involvement/ask-your-doctor/questions-before-appointment.html), "
            "including over-the-counter drugs, vitamins and supplements, and knowing your current conditions, "
            "past surgeries and illnesses. Some doctors prefer the bottles themselves; others are happy with a "
            "complete list. Either way, include:"},
   {'type': 'ul',
    'items': ['The name and dose of each prescription, and how you actually take it (which may differ from the '
              'label).',
              'Over-the-counter medicines you use regularly, such as pain relievers, sleep aids, antacids and '
              'allergy pills.',
              'Vitamins, supplements, herbal products and eye drops.',
              'Anything you stopped recently, and why.',
              'Allergies and past bad reactions to medicines.']},
   {'type': 'p',
    'text': "If you take five or more medicines, ask for a dedicated review. Our article on [medication reviews "
            "for older adults](/blog/medication-review-older-adults) explains what that involves."},
   {'type': 'h2', 'text': 'What to bring on the day'},
   {'type': 'ul',
    'items': ['Your list of concerns and your medication list.',
              'Insurance and Medicare cards and a photo ID.',
              'Recent results or records from other doctors, if the office does not already have them.',
              'Home readings, such as a blood pressure or blood sugar log. See [home blood pressure '
              'monitoring](/blog/home-blood-pressure-monitoring) for how to take readings the right way.',
              'Your glasses and working hearing aids, which the National Institute on Aging specifically '
              'reminds people to bring.',
              'A notepad, or a family member or friend who can take notes.']},
   {'type': 'p',
    'text': "Bringing someone helps, especially for a new diagnosis or a complicated plan. The NIA's guidance is "
            "to choose a person who can listen and write things down without taking over the conversation. "
            "If you want to record the visit, ask the doctor first."},
   {'type': 'p',
    'text': "For a video visit, the same list applies. Find a quiet, well-lit spot, have your medicine bottles "
            "within reach, and test your camera and sound a few minutes early."},
   {'type': 'h2', 'text': 'During the visit and before you leave'},
   {'type': 'p',
    'text': "Start with your top concern, even if it feels awkward. Be specific and honest about how you are "
            "taking your medicines and about alcohol, sleep and mood. Doctors can only work with what they "
            "hear."},
   {'type': 'p',
    'text': "AHRQ's [10 questions you should "
            "know](https://www.ahrq.gov/patients-consumers/patient-involvement/ask-your-doctor/10questions.html) "
            "are a good template. Before you leave, make sure you can answer these:"},
   {'type': 'ol',
    'items': ['What do you think is going on, and how sure are we?',
              'What is this test or medicine for, and what are the side effects?',
              'Are there other options, including waiting and watching?',
              'When and how will I get my results?',
              'What should I do if things get worse, and who do I call?',
              'When should I come back?']},
   {'type': 'p',
    'text': "Repeat the plan back in your own words. It is a simple way to catch a misunderstanding before it "
            "becomes a missed dose or a skipped test."},
   {'type': 'h2', 'text': 'After the visit'},
   {'type': 'p',
    'text': "Update your medication list the same day if anything changed, and throw out the old version. Put "
            "follow-up tests and appointments on the calendar. If you were referred to a specialist, ask how "
            "the two offices will share notes. Our piece on [the annual "
            "physical](/blog/annual-physical-what-you-need) covers what a yearly visit should include."},
   {'type': 'p',
    'text': "At Legacy Medical, visits are unhurried by design, and Dr. Shtern reviews your records and "
            "medicines with you rather than around you. Members can reach the practice by phone at any hour, "
            "and video visits are available through [telehealth](/telehealth). If you are considering a "
            "change, the first step is a complimentary [meet and greet](/meet-and-greet)."}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'cbc-and-metabolic-panel-explained',
  'title': 'Reading your blood work: the CBC and metabolic panel in plain English',
  'seo_title': 'CBC and Metabolic Panel in Plain English | Legacy Medical',
  'date': '2026-10-17T09:10:00',
  'modified': '2026-10-17T09:10:00',
  'category': 'Everyday health',
  'excerpt': 'What each line on a complete blood count and a metabolic panel measures, and why a '
             'single flagged number is rarely the whole story.',
  'blocks': [
   {'type': 'p',
    'text': "Two blood tests show up at nearly every physical: the complete blood count (CBC) and the "
            "metabolic panel, which appears on lab reports as the CMP. Together they cover your blood cells, blood sugar, "
            "electrolytes, kidneys and liver. When the results land in your patient portal, they can look like "
            "a wall of abbreviations with a few numbers flagged in red."},
   {'type': 'p',
    'text': "This guide explains what each part measures, based on the NIH's MedlinePlus pages, and how to think "
            "about a result that falls outside the range."},
   {'type': 'h2', 'text': 'First, what the reference range means'},
   {'type': 'p',
    'text': "Every result sits beside a reference range. MedlinePlus explains that these ranges come from testing "
            "large groups of healthy people, and that [it is common for healthy people to sometimes have results "
            "outside the reference range](https://medlineplus.gov/lab-tests/how-to-understand-your-lab-results/). "
            "Labs use different methods, so ranges differ between labs, and you cannot directly compare a "
            "result from one lab with another. Using the same lab over time makes trends easier to read."},
   {'type': 'p',
    'text': "That is why doctors look at patterns: a value compared with your own past results, alongside your "
            "symptoms and medicines. A single flag is a prompt for a question, not a diagnosis."},
   {'type': 'h2', 'text': 'The complete blood count (CBC)'},
   {'type': 'p',
    'text': "A [CBC](https://medlineplus.gov/lab-tests/complete-blood-count-cbc/) counts and measures the cells "
            "in your blood:"},
   {'type': 'ul',
    'items': ['**Red blood cells (RBC)** carry oxygen from your lungs to the rest of your body.',
              '**Hemoglobin** is the iron-rich protein inside red cells that does the carrying. Low hemoglobin is '
              'what most people mean by anemia.',
              '**Hematocrit** is the share of your blood made up of red cells.',
              '**MCV (mean corpuscular volume)** is the average size of your red cells. Small or large cells can '
              'point toward different causes of anemia, such as low iron or low vitamin B12.',
              '**White blood cells (WBC)** fight infection. A "CBC with differential" also breaks the total '
              'into the five main types.',
              '**Platelets** help your blood clot.']},
   {'type': 'p',
    'text': "MedlinePlus notes that diet, activity, medicines, menstrual periods and hydration can all affect a "
            "CBC, and that an abnormal result does not automatically mean you have a condition that needs "
            "treatment."},
   {'type': 'h2', 'text': 'The metabolic panel (CMP)'},
   {'type': 'p',
    'text': "A [CMP](https://medlineplus.gov/lab-tests/comprehensive-metabolic-panel-cmp/) is 14 tests from one "
            "tube of blood. A basic metabolic panel (BMP) includes 8 of them and leaves out the liver tests and "
            "proteins. Grouped by what they tell you:"},
   {'type': 'ul',
    'items': ['**Glucose** is your blood sugar. The CDC lists a [fasting result of 99 mg/dL or less as normal, '
              '100 to 125 as prediabetes and 126 or higher as diabetes '
              'range](https://www.cdc.gov/diabetes/diabetes-testing/index.html). A non-fasting sample reads '
              'higher, so it matters whether you ate. See [prediabetes and A1c](/blog/prediabetes-and-a1c).',
              '**Electrolytes: sodium, potassium, chloride and bicarbonate** help control fluid balance, nerve '
              'and muscle function and the acid-base balance of your blood. Diuretics and some blood pressure '
              'medicines commonly shift these.',
              '**Calcium** matters for nerves, muscles and the heart, as well as bone.',
              '**Kidney tests: BUN (blood urea nitrogen) and creatinine** are waste products the kidneys clear.',
              '**Proteins: albumin and total protein.** Albumin is the main protein in blood and is made by the '
              'liver.',
              '**Liver tests: ALP, ALT, AST and bilirubin.** ALP, ALT and AST are enzymes; bilirubin is a '
              'breakdown product of old red cells that the liver clears.']},
   {'type': 'p',
    'text': "MedlinePlus notes you may be asked to fast for several hours before a CMP. Follow the instructions "
            "your doctor's office gives you, and ask whether you should take your morning medicines."},
   {'type': 'h2', 'text': 'Where kidney numbers fit in'},
   {'type': 'p',
    'text': "Most labs also report an estimated glomerular filtration rate, or eGFR, calculated from your "
            "creatinine along with age and sex. The NIDDK explains that [a GFR of 60 or more is in the normal "
            "range, and a GFR below 60 may mean kidney "
            "disease](https://www.niddk.nih.gov/health-information/kidney-disease/chronic-kidney-disease-ckd/tests-diagnosis). "
            "Creatinine comes from muscle, so very low or very high muscle mass, dehydration and some medicines "
            "can move it. Our article on [reading your kidney lab "
            "results](/blog/egfr-kidney-lab-results-explained) walks through eGFR and the urine test that "
            "goes with it."},
   {'type': 'h2', 'text': 'Questions worth asking about your results'},
   {'type': 'ul',
    'items': ['Is this result new, or has it been like this before?',
              'Could a medicine, a recent illness or not fasting explain it?',
              'Does it need repeating, and when?',
              'What would change in my care if it stays this way?']},
   {'type': 'p',
    'text': "Call your doctor promptly, rather than waiting for a routine visit, if a result is marked critical or "
            "if you are told a value is far out of range and you feel unwell."},
   {'type': 'p',
    'text': "At Legacy Medical, Dr. Shtern goes over results with you and explains what they mean for your own "
            "health, with an internist's and a nephrologist's eye on the kidney numbers in particular. The "
            "[labs and tests](/labs-and-tests) page explains how testing works at the practice. If you would "
            "like to meet her, start with a complimentary [meet and greet](/meet-and-greet)."}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'er-urgent-care-or-call-your-doctor',
  'title': 'ER, urgent care or call your doctor: how to decide',
  'seo_title': 'ER, Urgent Care or Your Doctor? How to Decide | Legacy Medical',
  'date': '2026-10-17T09:20:00',
  'modified': '2026-10-17T09:20:00',
  'category': 'Everyday health',
  'excerpt': 'When to call 911, when the emergency room is the right place, when urgent care will do, and when a '
             'call to your own doctor comes first. Stroke and heart attack signs included.',
  'blocks': [
   {'type': 'p',
    'text': "**If you think you or someone near you is having a medical emergency, call 911 now.** Do not read "
            "further, do not drive yourself, and do not wait to call your doctor first."},
   {'type': 'p',
    'text': "For everything else, the choice between the emergency department, urgent care and your own "
            "doctor is not always obvious. This guide uses the National Library of Medicine's MedlinePlus "
            "guidance and CDC warning signs to make it a little clearer."},
   {'type': 'h2', 'text': 'Call 911 for these'},
   {'type': 'p',
    'text': "MedlinePlus lists situations where someone [cannot wait and you should call 911 right "
            "away](https://medlineplus.gov/ency/patientinstructions/000593.htm), including:"},
   {'type': 'ul',
    'items': ['Choking, or a person who has stopped breathing.',
              'Severe chest pain or pressure.',
              'A seizure lasting more than one minute, or one after which the person does not quickly wake up.',
              'Sudden inability to speak, see, walk or move.',
              'Sudden weakness or drooping on one side of the body.']},
   {'type': 'p',
    'text': "**Stroke.** The CDC teaches [B.E. F.A.S.T.](https://www.cdc.gov/stroke/signs-symptoms/index.html): "
            "**B**alance loss or dizziness; **E**yes, trouble seeing; **F**ace, one side droops when the person "
            "smiles; **A**rms, one arm drifts down when both are raised; **S**peech, slurred or strange; **T**ime "
            "to call 911. Other sudden signs include numbness or weakness of the face, arm or leg, confusion, "
            "trouble understanding speech, and a severe headache with no known cause. Note the time symptoms "
            "started, and wait for the ambulance rather than driving, because treatment can begin on the way."},
   {'type': 'p',
    'text': "**Heart attack.** The CDC lists the [major "
            "symptoms](https://www.cdc.gov/heart-disease/about/heart-attack.html) as chest pain or discomfort; "
            "feeling weak, light-headed or faint; pain or discomfort in the jaw, neck or back; pain or discomfort "
            "in one or both arms or shoulders; and shortness of breath. Unusual tiredness and nausea or vomiting "
            "can also occur, and women are more likely to have these other symptoms. Call 911 immediately."},
   {'type': 'p',
    'text': "If someone is thinking about harming themselves, call or text 988, the Suicide and Crisis Lifeline. "
            "If someone has made an attempt, call 911 and stay with them."},
   {'type': 'h2', 'text': 'Go to the emergency department (or call 911) for these'},
   {'type': 'p',
    'text': "MedlinePlus also lists problems that belong in the emergency department, by ambulance if needed:"},
   {'type': 'ul',
    'items': ['Trouble breathing.',
              'Fainting or passing out.',
              'An unusual or severe headache, especially one that comes on suddenly.',
              'Heavy bleeding.',
              'Sudden confusion.',
              'High fever with headache and a stiff neck.',
              'Vomiting or diarrhea that will not stop.',
              'Poisoning or an overdose of medicine, drugs or alcohol.']},
   {'type': 'p',
    'text': "Cleveland Clinic's physicians give a useful rule of thumb in their [ER versus urgent care "
            "guidance](https://health.clevelandclinic.org/urgent-care-vs-emergency-room): if the word you would "
            "use for a symptom is \"severe,\" the emergency department is the safer choice."},
   {'type': 'h2', 'text': 'When urgent care makes sense'},
   {'type': 'p',
    'text': "Urgent care is for problems that are not life-threatening but need attention sooner than a routine "
            "appointment. MedlinePlus gives examples such as colds, flu, earaches, sore throats, low-grade "
            "fevers, limited rashes, sprains, back pain, minor cuts and burns, minor broken bones and minor eye "
            "injuries."},
   {'type': 'p',
    'text': "MedlinePlus also notes that the same care usually costs much more in an emergency department than "
            "in a doctor's office, and insurance may charge a higher copay. That is a reason to use the "
            "emergency department for emergencies, never a reason to avoid it when you need it."},
   {'type': 'h2', 'text': 'When to call your doctor first'},
   {'type': 'p',
    'text': "If the problem is not on the 911 or emergency lists and you are unsure, MedlinePlus suggests calling "
            "your own doctor. Your doctor knows your history and medicines, which matters with problems such as:"},
   {'type': 'ul',
    'items': ['A new symptom that is bothering you but is not severe.',
              'A possible side effect from a new medicine.',
              'Home blood pressure or blood sugar readings that are higher or lower than usual, without '
              'emergency symptoms.',
              'A flare of a known condition, such as a urinary infection you have had before.',
              'Questions about whether something you saw in urgent care needs follow-up.']},
   {'type': 'p',
    'text': "MedlinePlus also suggests saving a few numbers in your phone now, before you need them: your "
            "doctor, the nearest emergency department, the nearest urgent care, and your insurer's nurse "
            "line."},
   {'type': 'h2', 'text': 'After an ER or urgent care visit'},
   {'type': 'p',
    'text': "Ask for a copy of the discharge summary and any test results, and send them to your regular "
            "doctor. Bring the paperwork and any new prescriptions to your follow-up so your medication list "
            "stays accurate. Our article on [having a concierge doctor during a hospital "
            "stay](/blog/concierge-doctor-hospital-stay) covers what coordination looks like after a "
            "bigger event."},
   {'type': 'p',
    'text': "At Legacy Medical, members can reach the practice by phone at any hour, which often settles the "
            "\"is this urgent?\" question with a short conversation, and [same or next business day "
            "visits](/same-or-next-day-visits) cover many problems that would otherwise mean urgent care. None "
            "of that replaces 911 in an emergency. To learn more, book a complimentary [meet and "
            "greet](/meet-and-greet)."}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'traveling-with-medications',
  'title': 'Traveling with medications: packing, time zones and refills',
  'seo_title': 'Traveling With Medications: Packing and Refills | Legacy Medical',
  'date': '2026-10-17T09:30:00',
  'modified': '2026-10-17T09:30:00',
  'category': 'Seasonal residents',
  'excerpt': 'How to pack prescriptions for a flight, handle doses across time zones and avoid running out when '
             'you split the year between two homes.',
  'blocks': [
   {'type': 'p',
    'text': "For seasonal residents, the trip south in the fall and north in the spring involves more than "
            "closing up a house. It means moving months of prescriptions, sometimes refrigerated ones, and "
            "keeping refills going across two states and two pharmacies. A missed blood pressure pill or a "
            "lost insulin pen is easy to prevent with a little planning."},
   {'type': 'p',
    'text': "The advice below comes from the CDC's travel health pages and the Transportation Security "
            "Administration (TSA)."},
   {'type': 'h2', 'text': 'Packing: carry it on, keep the labels'},
   {'type': 'p',
    'text': "The CDC's guidance on [traveling with "
            "medicine](https://wwwnc.cdc.gov/travel/page/travel-abroad-with-medicine) is straightforward:"},
   {'type': 'ul',
    'items': ['**Pack medicines in your carry-on**, in case your checked luggage is lost or delayed.',
              '**Keep them in their original labeled containers**, showing your name, the prescriber and the '
              'dose. The [CDC Yellow Book](https://www.cdc.gov/yellow-book/hcp/travelers-with-additional-considerations/travelers-with-chronic-illnesses.html) advises against travelling with only a daily pill organizer, because '
              'loose pills can be hard to identify.',
              '**Bring enough for the whole trip plus extra** in case of delays.',
              '**Carry copies of your prescriptions**, including generic names, and leave a copy with someone '
              'at home.']},
   {'type': 'p',
    'text': "TSA allows pills in [both carry-on and checked "
            "bags](https://www.tsa.gov/travel/security-screening/whatcanibring/items/medications-pills), with the "
            "final decision resting with the officer at the checkpoint. For liquid medicines, gels and "
            "injectables, TSA permits [larger amounts of medically necessary liquids in reasonable "
            "quantities](https://www.tsa.gov/travel/tsa-cares/disabilities-and-medical-conditions); tell the "
            "officer at the start of screening and place them in a separate bin. Clear labels make that "
            "screening quicker."},
   {'type': 'h2', 'text': 'Time zones and dose timing'},
   {'type': 'p',
    'text': "A move between Florida and New York does not change the clock, but trips to the West Coast or "
            "overseas do. The CDC's rule is that [medicines should be taken according to the time since your "
            "last dose, not the local time of day](https://wwwnc.cdc.gov/travel/page/travel-abroad-with-medicine), "
            "and it recommends asking your doctor how to adjust if you will cross time zones."},
   {'type': 'p',
    'text': "That conversation matters most for medicines where timing is sensitive, such as insulin and some "
            "other diabetes medicines, blood thinners, seizure medicines and some heart medicines. Ask before "
            "the trip, write the plan down, and keep a watch or phone set to home time if that makes the "
            "schedule easier."},
   {'type': 'h2', 'text': 'Refills when you live in two places'},
   {'type': 'p',
    'text': "Running out is the most common problem we hear about. A few habits help:"},
   {'type': 'ul',
    'items': ['**Count before you go.** Check every bottle two to three weeks before travel, not the night '
              'before.',
              '**Ask your drug plan about an early or travel supply.** Many plans have a process for this; the '
              'rules vary, so call the number on your card.',
              '**Consider a national pharmacy chain or mail order**, so refills can be filled in either state.',
              '**Keep one up-to-date medication list** that both of your doctors see. Our article on [medication '
              'reviews](/blog/medication-review-older-adults) explains why this matters.',
              '**Plan ahead for controlled medicines** such as some pain, sleep and attention medicines, which '
              'have stricter refill and transfer rules. Your prescriber and pharmacist can tell you what applies '
              'to you.']},
   {'type': 'h2', 'text': 'Heat, cold and special items'},
   {'type': 'p',
    'text': "Do not leave medicines in a parked car, which can get very hot in a Florida afternoon. Insulin and "
            "some injectable medicines need cool storage; ask your pharmacist how to carry them for the length "
            "of your trip. Pack supplies such as glucose test strips, a blood pressure cuff, inhalers and "
            "spare batteries for hearing aids with your medicines, not in a checked bag."},
   {'type': 'p',
    'text': "If you are going abroad, the CDC suggests checking with the embassy of your destination, and of any "
            "country where you change planes, because some medicines that are routine in the United States are "
            "restricted elsewhere. For controlled or injectable medicines, a letter from your doctor describing "
            "your condition and treatment is often useful. The CDC also warns against relying on buying "
            "medicine abroad, because counterfeit drugs are common in some countries."},
   {'type': 'h2', 'text': 'A short travel checklist'},
   {'type': 'ol',
    'items': ['Count every medicine and refill early.',
              'Pack medicines in your carry-on, in labeled containers, with extra days.',
              'Bring a printed medication list and copies of prescriptions.',
              'Ask about dose timing if you will cross time zones.',
              'Pack needed devices and supplies alongside the medicines.',
              'Save your doctors\' and pharmacies\' numbers in your phone.']},
   {'type': 'p',
    'text': "For more on splitting the year, see [Medicare when you live in two "
            "states](/blog/medicare-living-in-two-states) and [moving your medical records to a Florida "
            "doctor](/blog/transfer-medical-records-to-florida-doctor)."},
   {'type': 'p',
    'text': "Legacy Medical cares for many patients who spend part of the year away, with video visits through "
            "[telehealth](/telehealth) when you are out of town. The [seasonal residents](/seasonal-residents) "
            "page explains how that works, and a complimentary [meet and greet](/meet-and-greet) is the place "
            "to start."}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'seasonal-allergies-south-florida',
  'title': 'Seasonal allergies in South Florida',
  'seo_title': 'Seasonal Allergies in South Florida | Legacy Medical',
  'date': '2026-10-17T09:40:00',
  'modified': '2026-10-17T09:40:00',
  'category': 'Everyday health',
  'excerpt': "Florida's pollen seasons run longer and overlap more than up north. What triggers allergies here, "
             "how to tell them from a cold, and which treatments work best.",
  'blocks': [
   {'type': 'p',
    'text': "Many people who move to South Florida expect to leave allergy season behind with the snow. Instead "
            "they find that sneezing and itchy eyes arrive in January and do not fully leave. That is not "
            "imagined: Florida's pollen calendar is longer and messier than in much of the country."},
   {'type': 'h2', 'text': "Why Florida's allergy season feels endless"},
   {'type': 'p',
    'text': "The University of Florida's extension service explains that Florida has [more frequent and longer "
            "pollen seasons](https://gardeningsolutions.ifas.ufl.edu/?p=24975) than much of the United States, "
            "where trees, grasses and weeds tend to take turns. Here they overlap for much of the year."},
   {'type': 'ul',
    'items': ['**Trees** produce about 80 percent of Florida\'s airborne pollen. Oaks are among the most '
              'allergenic, with a peak from February to May and high counts in some areas as early as '
              'December.',
              '**Grasses** pollinate in spring, summer and fall. Bahiagrass, the most common grass in the '
              'state, is highly allergenic, and Bermudagrass can pollinate year-round in subtropical areas.',
              '**Weeds** can pollinate in any season, with ragweed the most important.']},
   {'type': 'p',
    'text': "A 2026 UF/IFAS report put the [South Florida peak at February to "
            "May](https://blogs.ifas.ufl.edu/news/2026/03/17/the-unwelcome-dust-that-wont-quit-pollen-season-hits-with-full-force/), "
            "named oaks, pines and melaleucas as major local producers, and noted that rain from summer "
            "thunderstorms naturally knocks pollen out of the air. Mold, which thrives in humidity, can add to "
            "symptoms year-round."},
   {'type': 'h2', 'text': 'Allergy or a cold?'},
   {'type': 'p',
    'text': "Allergic rhinitis, the medical name for hay fever, causes sneezing, a runny or stuffy nose, "
            "itchy eyes, nose or throat, watery eyes and sometimes cough and fatigue. The American College of "
            "Allergy, Asthma and Immunology points out a few [differences from a "
            "cold](https://acaai.org/allergies/allergic-conditions/hay-fever/):"},
   {'type': 'ul',
    'items': ['Allergies start soon after exposure and last as long as the exposure does. Colds usually start a '
              'day or two after catching the virus and improve within about a week.',
              'Allergy drainage is usually thin and clear; a cold can bring thicker or yellowish mucus.',
              'Allergies do not cause fever. A cold may cause a low-grade one.',
              'Allergies are not contagious.']},
   {'type': 'p',
    'text': "If your symptoms never really let up, pollen may not be the only cause. The ACAAI notes that "
            "year-round allergic rhinitis is usually driven by indoor triggers such as dust mites, pet dander, "
            "cockroaches and mold. Allergy testing can sort out which ones matter for you."},
   {'type': 'h2', 'text': 'Treatments that work'},
   {'type': 'p',
    'text': "MedlinePlus describes [nasal corticosteroid sprays as the most effective "
            "treatment](https://medlineplus.gov/ency/article/000813.htm) for allergic rhinitis. They work best "
            "when used every day through your season, rather than only on bad days. Other options include:"},
   {'type': 'ul',
    'items': ['**Antihistamines**, as pills, nasal sprays or eye drops. Newer ones usually cause fewer side effects; '
              'older types can cause drowsiness.',
              '**Saline rinses or sprays**, which wash out pollen and thin mucus.',
              '**Decongestants**, which relieve stuffiness but not itching or sneezing. MedlinePlus advises not '
              'using decongestant nasal sprays for more than 3 days, because of rebound congestion.',
              '**Allergy shots or tablets under the tongue (immunotherapy)**, for symptoms that are hard to '
              'control. Shots typically continue for three to five years.']},
   {'type': 'p',
    'text': "A caution for people with high blood pressure or heart disease: the American Heart Association "
            "notes that [decongestants such as pseudoephedrine and phenylephrine can raise blood "
            "pressure](https://www.heart.org/en/health-topics/high-blood-pressure/changes-you-can-make-to-manage-high-blood-pressure/understanding-overthecounter-otc-medications-and-high-blood-pressure) "
            "and may interfere with blood pressure medicines. They often hide inside combination cold and "
            "sinus products, so read labels and check with your doctor or pharmacist first."},
   {'type': 'h2', 'text': 'Cutting down your exposure'},
   {'type': 'ul',
    'items': ['Keep windows closed at home and in the car, and run the air conditioning.',
              'Check pollen forecasts and plan long outdoor time for after rain when you can.',
              'Shower and change clothes after yard work, golf or tennis, and wash bedding often.',
              'Wear sunglasses outdoors to keep pollen out of your eyes.',
              'Keep indoor humidity between 30 and 50 percent and fix leaks promptly to limit mold, as the '
              'ACAAI recommends.']},
   {'type': 'h2', 'text': 'When to see your doctor'},
   {'type': 'p',
    'text': "MedlinePlus suggests contacting your provider if symptoms are severe, if a treatment that used to "
            "work no longer does, or if symptoms do not respond to treatment. Also call if you have wheezing, "
            "shortness of breath or chest tightness, facial pain with fever, or symptoms that keep you from "
            "sleeping. Antibiotics do not help allergies; our article on [when antibiotics help and "
            "harm](/blog/antibiotics-when-they-help-and-harm) explains why."},
   {'type': 'p',
    'text': "At Legacy Medical, Dr. Shtern can help sort out allergy from infection, choose treatments that fit "
            "your blood pressure and other medicines, and refer you to an allergist when testing or "
            "immunotherapy makes sense. Many allergy questions can be handled by [video visit](/telehealth). "
            "To meet her, book a complimentary [meet and greet](/meet-and-greet)."}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'mosquito-borne-illness-florida',
  'title': 'Mosquito-borne illness in Florida: dengue and West Nile basics',
  'seo_title': 'Dengue and West Nile in Florida: The Basics | Legacy Medical',
  'date': '2026-10-17T09:50:00',
  'modified': '2026-10-17T09:50:00',
  'category': 'Infections and vaccines',
  'excerpt': 'Palm Beach County has had a mosquito-borne illness advisory this year. What dengue and West Nile '
             'look like, who is at higher risk, and how to drain and cover.',
  'blocks': [
   {'type': 'p',
    'text': "Most mosquito bites in Florida are just itchy. A small number carry viruses that can make people "
            "sick, and in some years the risk rises enough for health officials to issue local warnings. On "
            "August 3, 2026, the Florida Department of Health in Palm Beach County [issued a mosquito-borne "
            "illness advisory](https://palmbeach.floridahealth.gov/2026/08/03/doh-palm-beach-issues-mosquito-borne-illness-advisory-3/) "
            "after a confirmed case of locally acquired dengue."},
   {'type': 'p',
    'text': "Here is what to know about the two infections most often in the news, dengue and West Nile virus, "
            "using information from the Florida Department of Health and the CDC."},
   {'type': 'h2', 'text': 'Dengue'},
   {'type': 'p',
    'text': "According to the CDC, [about 1 in 4 people infected with dengue get "
            "sick](https://www.cdc.gov/dengue/signs-symptoms/index.html). The most common symptom is fever, "
            "usually with aches and pains (including eye pain), nausea or vomiting, or a rash. "
            "Symptoms typically last two to seven days, and most people recover in about a week."},
   {'type': 'p',
    'text': "About 1 in 20 people who get sick develop severe dengue, which can cause shock, internal bleeding "
            "and death. The CDC's warning signs usually begin in the 24 to 48 hours **after the fever goes "
            "away**, which is why people sometimes relax too early. Go to an emergency room right away for:"},
   {'type': 'ul',
    'items': ['Belly pain or tenderness.',
              'Vomiting at least three times in 24 hours.',
              'Bleeding from the nose or gums.',
              'Vomiting blood, or blood in the stool.',
              'Feeling extremely tired or restless.']},
   {'type': 'p',
    'text': "For fever and pain, the CDC advises [taking acetaminophen and avoiding aspirin and "
            "ibuprofen](https://www.cdc.gov/dengue/treatment/index.html), because of the bleeding risk. Rest "
            "and drink plenty of fluids. If you take a blood thinner or have kidney or liver disease, call your "
            "doctor for advice specific to you."},
   {'type': 'h2', 'text': 'West Nile virus'},
   {'type': 'p',
    'text': "West Nile spreads mainly through the bite of a mosquito that has fed on an infected bird. The CDC "
            "estimates that [about 80 percent of infections cause no "
            "symptoms](https://www.cdc.gov/west-nile-virus/hcp/clinical-signs/index.html). Most people who do "
            "get sick have a mild illness, such as fever with headache or body aches. Fewer "
            "than 1 percent develop serious illness affecting the brain or spinal cord, such as encephalitis "
            "or meningitis."},
   {'type': 'p',
    'text': "The CDC notes that [older adults, people with certain chronic conditions and people with weakened "
            "immune systems are at higher risk](https://www.cdc.gov/west-nile-virus/about/index.html) of severe "
            "illness. There is no licensed vaccine or specific antiviral medicine for West Nile in people; "
            "severe cases are treated with supportive care in the hospital. Seek care urgently for a high "
            "fever with severe headache, a stiff neck, confusion, weakness or trouble walking."},
   {'type': 'h2', 'text': 'Drain and cover'},
   {'type': 'p',
    'text': "Florida's public health message is to [drain standing water and cover your skin and "
            "home](https://www.floridahealth.gov/diseases-and-conditions/mosquito-borne-diseases/prevention.html). "
            "In practice:"},
   {'type': 'ul',
    'items': ['**Drain.** Empty anything that collects rain or sprinkler water: buckets, plant saucers, toys, '
              'trash can lids, tarps and old tires. Refresh birdbaths and pet bowls at least once or twice a '
              'week, and keep pools clean and chlorinated.',
              '**Cover your skin.** When mosquitoes are out, wear long sleeves, long pants, socks and closed '
              'shoes, and use repellent on exposed skin.',
              '**Cover your home.** Keep screens on windows, doors, porches and patios, and repair tears.']},
   {'type': 'p',
    'text': "After a summer storm, take a few minutes to walk around the house and tip out anything holding "
            "water, which is exactly what the state health department asked Floridians to do in its "
            "[September 2026 dengue reminder](https://www.floridahealth.gov/2026/09/04/florida-surgeon-general-reminds-floridians-to-take-precautions-against-dengue-ahead-of-labor-day-weekend/). "
            "The Palm Beach County advisory also asks residents to report dead birds to the Florida Fish and "
            "Wildlife Conservation Commission, since birds help health officials track West Nile activity."},
   {'type': 'p',
    'text': "The CDC lists [EPA-registered repellent ingredients](https://www.cdc.gov/mosquitoes/prevention/index.html) "
            "that work: DEET, picaridin, IR3535, oil of lemon eucalyptus, para-menthane-diol (PMD) and "
            "2-undecanone. Follow the label. Permethrin is for "
            "clothing and gear only, never directly on skin."},
   {'type': 'h2', 'text': 'Travel and when to call your doctor'},
   {'type': 'p',
    'text': "Dengue is common in many parts of the Caribbean and Latin America. If you develop a fever after "
            "travel to one of those areas, or during a local advisory, tell your doctor where you "
            "have been. The CDC notes that a blood test is the only way to confirm dengue, but care can start "
            "based on symptoms. Anyone with the warning signs above should go to an emergency room, and anyone "
            "with signs of a stroke or severe confusion should call 911."},
   {'type': 'p',
    'text': "For other seasonal Florida concerns, see the [hurricane season health "
            "checklist](/blog/hurricane-season-health-checklist) and [skin cancer checks in "
            "Florida](/blog/skin-cancer-checks-florida)."},
   {'type': 'p',
    'text': "At Legacy Medical, members can reach the practice by phone at any hour about a new fever, and "
            "[same or next business day visits](/same-or-next-day-visits) allow a prompt exam and testing when "
            "needed. To meet Dr. Shtern, book a complimentary [meet and greet](/meet-and-greet)."}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'mens-health-checkups-after-50',
  'title': "Men's health after 50: the checkups that matter",
  'seo_title': "Men's Health After 50: The Checkups That Matter | Legacy Medical",
  'date': '2026-10-17T10:00:00',
  'modified': '2026-10-17T10:00:00',
  'category': 'Prevention and screening',
  'excerpt': 'The screenings and vaccines that national guidelines recommend for men over 50, with the year each '
             'recommendation was issued, and the ones that call for a conversation first.',
  'blocks': [
   {'type': 'p',
    'text': "Heart disease is the [leading cause of death for men in the United "
            "States](https://www.cdc.gov/heart-disease/about/men-and-heart-disease.html), and many of the "
            "conditions that lead to it, such as high blood pressure, diabetes and high cholesterol, cause no "
            "symptoms for years. That is the case for regular checkups after 50: finding problems while they "
            "are still quiet and easy to treat."},
   {'type': 'p',
    'text': "The list below follows the U.S. Preventive Services Task Force (USPSTF), an independent panel that "
            "reviews the evidence on screening, and the CDC's vaccine recommendations. Each item notes the "
            "year of the current guidance. Your own history may call for more, or less."},
   {'type': 'p',
    'text': "A quick key to the Task Force's language: an **A** or **B** grade means the service is "
            "recommended; a **C** means it should be offered selectively, based on your situation and "
            "preferences; a **D** means the Task Force recommends against it; and an **I** means the evidence is "
            "not yet good enough to decide. Grades describe people of average risk, so a strong family history "
            "or a past abnormal result can change the plan."},
   {'type': 'h2', 'text': 'Heart and metabolic health'},
   {'type': 'ul',
    'items': ['**Blood pressure.** The USPSTF (2021) recommends screening all adults and suggests [checking '
              'yearly from age 40](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hypertension-in-adults-screening), '
              'with a high office reading confirmed by home or ambulatory readings before treatment. See [home '
              'blood pressure monitoring](/blog/home-blood-pressure-monitoring).',
              '**Blood sugar.** Screening for prediabetes and type 2 diabetes is recommended for adults 35 to 70 '
              'who have overweight or obesity ([USPSTF, '
              '2021](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes)), '
              'about every three years if results are normal.',
              '**Cholesterol and statins.** For adults 40 to 75 with at least one risk factor and a 10-year '
              'cardiovascular risk of 10 percent or more, the USPSTF (2022) [recommends a '
              'statin](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/statin-use-in-adults-preventive-medication); '
              'between 7.5 and 10 percent, it is an individual decision. Some men benefit from extra tests such '
              'as [ApoB and Lp(a)](/blog/apob-and-lipoprotein-a) or a [coronary calcium '
              'score](/blog/coronary-artery-calcium-score).']},
   {'type': 'h2', 'text': 'Cancer screening'},
   {'type': 'ul',
    'items': ['**Colorectal cancer.** Recommended from 45 through 75, with a selective decision from 76 to 85 '
              '([USPSTF, 2021](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/colorectal-cancer-screening)). '
              'Colonoscopy and stool-based tests are both options.',
              '**Lung cancer.** A yearly low-dose CT is recommended for adults 50 to 80 with at least a '
              '20 pack-year smoking history who still smoke or quit within the past 15 years ([USPSTF, '
              '2021](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/lung-cancer-screening)). '
              'More in [low-dose CT for lung cancer](/blog/low-dose-ct-lung-cancer-screening).',
              '**Skin.** Florida sun makes regular skin checks worth discussing; see [skin cancer checks in '
              'Florida](/blog/skin-cancer-checks-florida).']},
   {'type': 'h2', 'text': 'Two checks specific to men'},
   {'type': 'p',
    'text': "**Prostate cancer.** The current USPSTF recommendation (2018) says that for men 55 to 69, [the "
            "decision to have PSA screening should be an individual "
            "one](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/prostate-cancer-screening), "
            "made after talking through the possible benefit (a small reduction in the chance of dying from "
            "prostate cancer) and the harms (false positives, biopsies, and treatment of cancers that would "
            "never have caused trouble). It recommends against routine PSA screening from age 70. The Task "
            "Force lists this topic as being updated, so the guidance may change. It also asks clinicians to tell "
            "Black men and men with a family history of prostate cancer about their higher risk, since they may "
            "have more to gain from screening."},
   {'type': 'p',
    'text': "**Abdominal aortic aneurysm.** For men 65 to 75 who have ever smoked (usually defined as 100 or more "
            "cigarettes in a lifetime), the USPSTF (2019) recommends [a one-time ultrasound of the "
            "aorta](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/abdominal-aortic-aneurysm-screening). "
            "For men in that age group who never smoked, it is a selective decision based on family history "
            "and other risks."},
   {'type': 'h2', 'text': 'Vaccines, falls and the rest'},
   {'type': 'ul',
    'items': ['**Shingles.** Two doses of Shingrix, two to six months apart, for [adults 50 and '
              'older](https://www.cdc.gov/shingles/vaccines/index.html), with no upper age limit.',
              '**Pneumococcal.** The CDC now recommends pneumococcal vaccination for [all adults 50 and '
              'older](https://www.cdc.gov/pneumococcal/vaccines/index.html).',
              '**RSV.** Recommended for [all adults 75 and older, and for those 50 to 74 at increased '
              'risk](https://www.cdc.gov/rsv/vaccines/index.html). See [RSV in adults](/blog/rsv-infection-in-adults).',
              '**Flu and COVID-19.** Discussed each fall; see [the yearly flu '
              'vaccine](/blog/yearly-flu-vaccine-benefits).',
              '**Falls.** For adults 65 and older at increased risk of falling, the USPSTF (2024) recommends '
              '[exercise programs to prevent '
              'falls](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/falls-prevention-community-dwelling-older-adults-interventions). '
              'See [balance and fall prevention](/blog/balance-and-fall-prevention).',
              '**Hearing, mood, sleep and alcohol** deserve a few minutes too. See [hearing loss and '
              'memory](/blog/hearing-loss-and-memory) and [alcohol after 50](/blog/alcohol-after-50).']},
   {'type': 'p',
    'text': "Bone density testing in men is a gray area: the USPSTF (2025) found the evidence insufficient to "
            "recommend for or against routine screening, so it is a judgment call based on risk factors such as "
            "long-term steroid use or a prior fracture. Our article on [bone density "
            "screening](/blog/bone-density-screening) has more."},
   {'type': 'p',
    'text': "At Legacy Medical, the annual [executive physical](/preventive-care) is where Dr. Shtern puts this list "
            "together for you, keeps track of what is due, and talks through the judgment calls such as PSA "
            "testing. To meet her first, book a complimentary [meet and greet](/meet-and-greet)."}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'womens-health-checkups-after-50',
  'title': "Women's health after 50: the checkups that matter",
  'seo_title': "Women's Health After 50: Checkups That Matter | Legacy Medical",
  'date': '2026-10-17T10:10:00',
  'modified': '2026-10-17T10:10:00',
  'category': 'Prevention and screening',
  'excerpt': 'Mammograms, bone density, the heart, and when cervical screening can stop: the checkups national '
             'guidelines recommend for women over 50, with the year of each.',
  'blocks': [
   {'type': 'p',
    'text': "After 50, the focus of a woman's preventive care shifts. Menopause changes heart and bone risk, some "
            "screenings become more important, and one, the Pap test, can often stop. Heart disease is the "
            "[leading cause of death for women in the United "
            "States](https://www.cdc.gov/heart-disease/about/women-and-heart-disease.html), yet it is often "
            "the risk women think about least."},
   {'type': 'p',
    'text': "The list below follows the U.S. Preventive Services Task Force (USPSTF) and the CDC, with the year "
            "of each current recommendation. Your history may call for a different schedule."},
   {'type': 'p',
    'text': "A quick key to the Task Force's language: an **A** or **B** grade means the service is "
            "recommended; a **C** means it should be offered selectively, based on your situation and "
            "preferences; a **D** means the Task Force recommends against it; and an **I** means the evidence is "
            "not yet good enough to decide. Grades describe people of average risk, so a strong family history "
            "or a past abnormal result can change the plan."},
   {'type': 'h2', 'text': 'Heart and metabolic health'},
   {'type': 'ul',
    'items': ['**Blood pressure.** Checked at least yearly from age 40, with a high office reading confirmed at '
              'home before treatment ([USPSTF, '
              '2021](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hypertension-in-adults-screening)).',
              '**Blood sugar.** Screening for adults 35 to 70 with overweight or obesity ([USPSTF, '
              '2021](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes)).',
              '**Cholesterol and statins.** Recommended for adults 40 to 75 with a risk factor and a 10-year '
              'risk of 10 percent or more ([USPSTF, '
              '2022](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/statin-use-in-adults-preventive-medication)).']},
   {'type': 'p',
    'text': "Heart symptoms in women can be less obvious. Along with chest discomfort, the CDC lists pain in the "
            "neck, jaw, throat, upper abdomen or back, nausea, and unusual tiredness. If those come on "
            "suddenly, call 911. Our article on [menopause and heart health](/blog/menopause-and-heart-health) "
            "covers why risk rises after menopause."},
   {'type': 'h2', 'text': 'Breast and cervical cancer'},
   {'type': 'p',
    'text': "**Mammograms.** The USPSTF (2024) recommends [a mammogram every two years from age 40 through "
            "74](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/breast-cancer-screening). "
            "For women 75 and older, it found the evidence insufficient, so the decision depends on health and "
            "preferences. If you have dense breasts or a strong family history, ask whether extra imaging makes sense for you. See [breast cancer "
            "screening from 40](/blog/breast-cancer-screening-mammogram-age-40)."},
   {'type': 'p',
    'text': "**Cervical cancer.** Screening continues to 65. After that, the current USPSTF recommendation "
            "(2018) is [no further screening for women who have had adequate prior "
            "screening](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/cervical-cancer-screening) "
            "and are not at high risk. \"Adequate\" means three normal Pap tests in a row, or two normal "
            "co-tests, within the ten years before stopping, with the most recent in the past five years. If "
            "your records are incomplete, screening may still be worth doing. The Task Force is updating this "
            "recommendation; a 2024 draft added HPV tests that women can collect themselves."},
   {'type': 'h2', 'text': 'Bones and other cancer screening'},
   {'type': 'ul',
    'items': ['**Bone density.** The USPSTF (2025) recommends [osteoporosis screening for women 65 and '
              'older](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/osteoporosis-screening), '
              'and for younger postmenopausal women with risk factors such as a parent who broke a hip, '
              'smoking, low body weight or heavy drinking. See [bone density '
              'screening](/blog/bone-density-screening).',
              '**Colorectal cancer.** From 45 through 75, with a selective decision from 76 to 85 ([USPSTF, '
              '2021](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/colorectal-cancer-screening)).',
              '**Lung cancer.** Yearly low-dose CT for adults 50 to 80 with at least a 20 pack-year history who '
              'smoke now or quit within 15 years ([USPSTF, '
              '2021](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/lung-cancer-screening)).',
              '**Skin.** Worth discussing in Florida; see [skin cancer checks](/blog/skin-cancer-checks-florida).']},
   {'type': 'h2', 'text': 'Vaccines, falls and the conversations to have'},
   {'type': 'ul',
    'items': ['**Shingles:** two doses of Shingrix for [adults 50 and '
              'older](https://www.cdc.gov/shingles/vaccines/index.html).',
              '**Pneumococcal:** recommended for [all adults 50 and '
              'older](https://www.cdc.gov/pneumococcal/vaccines/index.html).',
              '**RSV:** for [all adults 75 and older and those 50 to 74 at increased '
              'risk](https://www.cdc.gov/rsv/vaccines/index.html).',
              '**Falls:** exercise programs for adults 65 and older at increased risk ([USPSTF, '
              '2024](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/falls-prevention-community-dwelling-older-adults-interventions)). '
              'Strength work helps both bones and balance; see [strength training after '
              '50](/blog/strength-training-after-50).']},
   {'type': 'p',
    'text': "Some topics do not appear on screening lists but belong in the visit: menopause symptoms and "
            "whether treatment makes sense for you, bladder control, sleep, mood, memory and hearing. Many "
            "women do not raise these because they assume nothing can be done. Often something can."},
   {'type': 'p',
    'text': "One practical habit helps more than any single test: keep a short record of when you last had a "
            "mammogram, colon screening, bone density scan and each vaccine, and where it was done. Results "
            "scattered across several offices, or across two states for seasonal residents, are the most "
            "common reason a screening is repeated too soon or quietly missed."},
   {'type': 'p',
    'text': "At Legacy Medical, the annual [executive physical](/preventive-care) is where Dr. Shtern keeps track of "
            "what is due and when, coordinates with your gynecologist and other specialists, and makes time "
            "for the questions that do not fit a checklist. To meet her first, book a complimentary [meet and "
            "greet](/meet-and-greet)."}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'hydration-for-older-adults',
  'title': 'Hydration for older adults: how much is enough',
  'seo_title': 'Hydration for Older Adults: How Much Is Enough | Legacy Medical',
  'date': '2026-10-17T10:20:00',
  'modified': '2026-10-17T10:20:00',
  'category': 'Nutrition',
  'excerpt': 'Thirst fades with age, and Florida heat raises the stakes. What the reference numbers say, the '
             'early signs of dehydration, and when drinking more is the wrong advice.',
  'blocks': [
   {'type': 'p',
    'text': "\"Eight glasses a day\" is the rule most people know, but it does not fit everyone. How much fluid you need depends on your size, activity, the weather, "
            "your health and your medicines. For older adults in South Florida, a few of those factors line up "
            "in the wrong direction."},
   {'type': 'h2', 'text': 'Why it gets harder with age'},
   {'type': 'p',
    'text': "MedlinePlus notes that [some people lose their sense of thirst as they "
            "age](https://medlineplus.gov/dehydration.html), so they do not drink enough. The National "
            "Institute on Aging makes the same point and adds that [some medicines make plenty of fluids even "
            "more important](https://order.nia.nih.gov/sites/default/files/2022-12/whats-on-your-plate-nia.pdf). "
            "Its advice: do not wait until you feel thirsty, and spread fluids through the day."},
   {'type': 'p',
    'text': "Other common reasons older adults run low include water pills (diuretics), diabetes with high blood "
            "sugar, illness with fever, vomiting or diarrhea, and cutting back on drinks to avoid trips to the "
            "bathroom. Our article on [how often you should urinate](/blog/how-often-should-you-urinate) "
            "covers the bladder side of that trade-off."},
   {'type': 'h2', 'text': 'What the reference numbers say'},
   {'type': 'p',
    'text': "The most cited figures come from the National Academies, which set an [adequate intake of total "
            "water of about 3.7 liters a day for men and 2.7 liters for "
            "women](https://www.nationalacademies.org/news/report-sets-dietary-intake-levels-for-water-salt-and-potassium-to-maintain-health-and-reduce-chronic-disease-risk). "
            "Two details are often missed:"},
   {'type': 'ul',
    'items': ['**That total includes food.** About 80 percent comes from drinking water and other beverages, '
              'and about 20 percent from food. Fruit, vegetables, soup and yogurt all count.',
              '**Coffee and tea count too.** The panel concluded that caffeinated drinks contribute to daily '
              'fluid intake, because the diuretic effect of caffeine is short-lived.']},
   {'type': 'p',
    'text': "The same report said most healthy people meet their needs by letting thirst be their guide, and "
            "that people who are very active or live in hot climates may need more. For older adults whose "
            "thirst signal is weaker, a routine works better than waiting to feel thirsty. The figures are "
            "averages from a 2004 report, not a personal target."},
   {'type': 'h2', 'text': 'Signs you are running low'},
   {'type': 'p',
    'text': "MedlinePlus lists the [common signs of "
            "dehydration](https://medlineplus.gov/dehydration.html) in adults as feeling very thirsty, a dry "
            "mouth, urinating and sweating less than usual, dark urine, dry skin, fatigue and dizziness."},
   {'type': 'p',
    'text': "Seek medical help right away if dehydration comes with confusion, fainting, very little urine, a "
            "racing heartbeat, fast breathing or signs of shock. Call 911 if someone is confused and cannot "
            "keep fluids down, or if you see signs of a stroke or heat stroke."},
   {'type': 'p',
    'text': "Because dark urine is one of the signs on that list, urine color makes a rough everyday check. It "
            "is not perfect: some vitamins and medicines change the color, so ask your doctor if yours looks "
            "unusual."},
   {'type': 'h2', 'text': 'Easy ways to drink more'},
   {'type': 'ul',
    'items': ['Have a full glass of water with each medicine and each meal.',
              'Keep a filled bottle where you sit, in the car and in your golf or beach bag. The CDC suggests a '
              '[reusable bottle and a slice of lemon or '
              'lime](https://www.cdc.gov/healthy-weight-growth/water-healthy-drinks/index.html) for flavor.',
              'Front-load the day: drink more in the morning and early afternoon, less in the evening if night '
              'trips to the bathroom are a problem.',
              'Eat water-rich foods such as melon, citrus, cucumbers, tomatoes and soup.',
              'Drink more on hot days, during exercise and when you are sick.',
              'Go easy on alcohol, which adds to fluid loss in the heat.']},
   {'type': 'p',
    'text': "For family members helping a parent, the National Institute on Aging suggests offering [other "
            "drinks if plain water is not "
            "appealing](https://www.nia.nih.gov/health/alzheimers-caregiving/common-medical-problems-alzheimers-disease-information-caregivers), "
            "such as juice, flavored water, broth, milk, or decaffeinated coffee or tea, and asking the doctor "
            "how much fluid to aim for each day. A filled glass within reach does more than a reminder."},
   {'type': 'h2', 'text': 'When more is not better'},
   {'type': 'p',
    'text': "Some people need to limit fluids. That includes many people with heart failure, advanced kidney "
            "disease, certain liver conditions, or a low blood sodium level. The National Institute on Aging's "
            "[advice for hot weather](https://www.nia.nih.gov/health/safety/hot-weather-safety-older-adults) is that if your doctor has told you to limit liquids, ask what to do when "
            "it is very hot. The same applies to sports drinks and electrolyte packets, which can carry "
            "sodium, sugar or potassium you may need to watch."},
   {'type': 'p',
    'text': "As a nephrologist, Dr. Shtern sees both sides of this: kidney strain from too little fluid in the "
            "heat, and fluid overload when the heart or kidneys cannot keep up. Our article on [heat, hydration "
            "and kidney health](/blog/heat-hydration-kidney-health) goes further into the kidney side, and "
            "[kidney care](/kidney-care) explains her approach. To meet her, book a complimentary [meet and "
            "greet](/meet-and-greet)."}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'fiber-why-it-matters',
  'title': 'Fiber: why it matters and how to get more',
  'seo_title': 'Fiber: Why It Matters and How to Get More | Legacy Medical',
  'date': '2026-10-17T10:30:00',
  'modified': '2026-10-17T10:30:00',
  'category': 'Nutrition',
  'excerpt': 'Fiber is linked to lower risk of heart disease, diabetes and colorectal cancer. How much to aim for, '
             'the two kinds, and simple ways to add it without discomfort.',
  'blocks': [
   {'type': 'p',
    'text': "Fiber is the part of plant foods that your body does not digest. That sounds like a reason to skip "
            "it, but it is the opposite. Fiber shapes digestion, blood sugar, cholesterol and the bacteria that "
            "live in the gut, and most adults eat far less than recommended."},
   {'type': 'h2', 'text': 'What the research shows'},
   {'type': 'p',
    'text': "The largest look at the question, a 2019 series of reviews in The Lancet covering 185 long-term "
            "studies and 58 clinical trials, found that people who ate the most fiber had [a 15 to 30 percent "
            "lower risk](https://pubmed.ncbi.nlm.nih.gov/30638909/) of death from any cause and from heart "
            "disease, and of coronary heart disease, stroke, type 2 diabetes and colorectal cancer, compared "
            "with those who ate the least. In the clinical trials, higher fiber intake lowered body weight, "
            "systolic blood pressure and total cholesterol."},
   {'type': 'p',
    'text': "The benefits were greatest at about 25 to 29 grams a day, and the authors suggested more could "
            "help further. Most of the evidence is observational, but the dose-response pattern was strong "
            "enough that the authors judged the links could be causal."},
   {'type': 'h2', 'text': 'Two kinds, two jobs'},
   {'type': 'p',
    'text': "MedlinePlus describes [two types of fiber](https://medlineplus.gov/ency/article/002136.htm), and "
            "most plant foods contain some of each:"},
   {'type': 'ul',
    'items': ['**Soluble fiber** attracts water and turns to gel during digestion, which slows things down. It '
              'is linked to lower cholesterol. Good sources are oats and oat bran, barley, beans, lentils, peas, '
              'nuts, seeds, some fruits and psyllium.',
              '**Insoluble fiber** adds bulk to stool and helps food move through the gut. Good sources are '
              'wheat bran, whole grains and vegetables.']},
   {'type': 'h2', 'text': 'How much to aim for'},
   {'type': 'p',
    'text': "The standard recommendation is [14 grams of fiber for every 1,000 calories you "
            "eat](https://pmc.ncbi.nlm.nih.gov/articles/PMC8634306/). Because calorie needs drop with age, "
            "that works out to roughly 28 grams a day for men over 50 and 22 grams for women over 50. On food "
            "labels, the FDA uses a [Daily Value of 28 grams](https://www.fda.gov/food/nutrition-facts-label/how-understand-and-use-nutrition-facts-label); "
            "a serving with 20 percent or more of the Daily Value counts as high in fiber, and 5 percent or less "
            "as low."},
   {'type': 'p',
    'text': "Most people fall well short. An analysis of national survey data presented at the American Society "
            "for Nutrition's 2021 meeting found that [fewer than 1 in 10 U.S. adults meet the "
            "recommendation](https://nutrition.org/most-americans-are-not-getting-enough-fiber-in-our-diets/). "
            "The 2025 to 2030 Dietary Guidelines for Americans ask people to [prioritize fiber-rich whole "
            "grains](https://realfood.gov/) alongside daily vegetables and fruit."},
   {'type': 'h2', 'text': 'Easy ways to get more'},
   {'type': 'ul',
    'items': ['**Start the day with oats or a high-fiber cereal**, topped with berries or sliced fruit.',
              '**Add beans or lentils** to soups, salads and grain bowls a few times a week.',
              '**Swap refined grains for whole ones:** whole wheat bread and pasta, brown rice, barley, quinoa.',
              '**Keep the skin on** apples, pears and potatoes.',
              '**Snack on nuts, seeds or fruit** instead of chips or crackers.',
              '**Fill half the plate with vegetables** at lunch and dinner.']},
   {'type': 'p',
    'text': "When you shop, check the grams of dietary fiber on the Nutrition Facts label and compare similar "
            "products, such as two loaves of bread or two boxes of cereal. The differences are often larger "
            "than you would guess, and the higher-fiber choice usually costs no more."},
   {'type': 'p',
    'text': "These fit easily into the [Mediterranean diet](/blog/mediterranean-diet-heart-health), which is "
            "built around the same foods. Whole foods also bring vitamins, minerals and other plant compounds "
            "that a supplement does not."},
   {'type': 'h2', 'text': 'Adding fiber without discomfort'},
   {'type': 'p',
    'text': "The NIDDK advises [adding fiber a little at a "
            "time](https://www.niddk.nih.gov/health-information/digestive-diseases/constipation/eating-diet-nutrition) "
            "so your body can adjust, and drinking plenty of liquids to help it work. Going from very little to "
            "a lot in one week is the usual reason for gas and bloating. Increase over a few weeks, and see "
            "[hydration for older adults](/blog/hydration-for-older-adults) for the fluid side."},
   {'type': 'p',
    'text': "Talk with your doctor before a big change if you have a bowel condition, a history of bowel "
            "obstruction, trouble swallowing, or kidney disease with a potassium limit, since beans, lentils "
            "and some fruits are high in potassium. If you are thinking about a fiber supplement, ask whether "
            "to space it from your medicines. Our article on [constipation](/blog/constipation-and-squatty-potty) "
            "has more on bowel habits."},
   {'type': 'p',
    'text': "At Legacy Medical, Dr. Shtern can look at your diet alongside your cholesterol, blood sugar and "
            "kidney numbers and suggest changes that fit your health and your kitchen. The annual [executive "
            "physical](/preventive-care) is a natural time for that conversation, and a complimentary [meet "
            "and greet](/meet-and-greet) is the way to start."}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},
]
