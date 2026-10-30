"""Journal batch B (October 2026): thyroid, type 2 diabetes, statins, atrial
fibrillation, sleep apnea, GERD, vitamin D, iron deficiency, and the shingles and
pneumococcal vaccines. Every medical fact is linked inline to the official or
primary source it came from, checked in October 2026. Nothing about the practice
beyond the facts in content.py. Not yet medically reviewed (reviewed_by stays
None until Dr. Shtern signs off)."""

POSTS = [
 {'slug': 'underactive-thyroid-tsh-test',
  'title': 'Underactive thyroid (hypothyroidism) and the TSH test',
  'seo_title': 'Underactive Thyroid and the TSH Test | Legacy Medical',
  'date': '2026-10-15T09:00:00',
  'modified': '2026-10-15T09:00:00',
  'category': 'Everyday health',
  'excerpt': 'Tired, cold, gaining weight? What an underactive thyroid is, how the TSH blood test works, and how '
             'thyroid medicine is started and checked.',
  'blocks': [
   {'type': 'p',
    'text': 'Fatigue, weight gain and feeling cold all the time are some of the most common reasons people ask for '
            'a thyroid test. Sometimes the thyroid is the cause. Often it is not. The good news is that one '
            'inexpensive blood test, the TSH, answers the first question for most people, and the condition it '
            'finds is very treatable.'},
   {'type': 'h2', 'text': 'What the thyroid does, and what happens when it slows down'},
   {'type': 'p',
    'text': 'The thyroid is a small, butterfly-shaped gland in the front of the neck. Its hormones set the pace at '
            'which the body uses energy, so they touch nearly every organ, including the heart. When the gland '
            'does not make enough, the condition is called hypothyroidism, or underactive thyroid, and many body '
            'functions slow down. The National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK) '
            'estimates that [nearly 5 out of 100 Americans age 12 and older have '
            'hypothyroidism](https://www.niddk.nih.gov/health-information/endocrine-diseases/hypothyroidism), '
            'though most cases are mild.'},
   {'type': 'p',
    'text': 'It is much more common in women and in people over 60. The NIDDK also lists a higher risk if you have '
            'had a thyroid problem or thyroid surgery before, radiation to the neck or chest, a family history of '
            'thyroid disease, or conditions such as type 1 or type 2 diabetes, celiac disease, rheumatoid arthritis '
            'or lupus. The most common cause in the United States is **Hashimoto\'s disease**, in which the immune '
            'system attacks the thyroid. Some heart, cancer and bipolar disorder medicines can also slow the '
            'gland.'},
   {'type': 'p',
    'text': 'The symptoms the NIDDK lists are easy to mistake for ordinary life: fatigue, weight gain, trouble '
            'tolerating cold, joint and muscle aches, dry skin or thinning hair, a slow heart rate and low mood. '
            'Because the condition usually develops slowly, people may not notice it for months or years. An '
            'underactive thyroid can also raise cholesterol, which is why a high cholesterol result is one reason '
            'to check thyroid function.'},
   {'type': 'h2', 'text': 'How the TSH test works'},
   {'type': 'p',
    'text': 'TSH stands for thyroid stimulating hormone. It is made by the pituitary gland in the brain and works '
            'like a thermostat signal, telling the thyroid how much hormone to make. According to the NIDDK\'s '
            'guide to [thyroid tests](https://www.niddk.nih.gov/health-information/diagnostic-tests/thyroid), '
            'doctors usually check TSH first. When the thyroid is underactive, the pituitary keeps pushing, so '
            '**a high TSH most often means hypothyroidism**. A low TSH usually points the other way, toward an '
            'overactive thyroid.'},
   {'type': 'p',
    'text': 'If the TSH is abnormal, the next step is usually a free T4 level, which measures the hormone the '
            'thyroid actually releases. Thyroid antibody tests can show whether an autoimmune condition such as '
            'Hashimoto\'s is behind it. A diagnosis is never made on symptoms alone, since so many of them overlap '
            'with other conditions, and a borderline result is often repeated before anyone starts medicine.'},
   {'type': 'h2', 'text': 'Should everyone be screened?'},
   {'type': 'p',
    'text': 'Not necessarily. The U.S. Preventive Services Task Force concluded in 2015 that the evidence is '
            '[insufficient to recommend for or against screening adults who have no '
            'symptoms](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/thyroid-dysfunction-screening), '
            'and that statement is still current. In practice, doctors test when there are symptoms, risk '
            'factors, abnormal cholesterol, or other reasons to look.'},
   {'type': 'p',
    'text': 'A common gray zone is **subclinical hypothyroidism**: a TSH that is somewhat high while free T4 is '
            'still normal. This is especially common with age. A large trial of adults 65 and older with this '
            'pattern, published in the New England Journal of Medicine in 2017, found that thyroid hormone pills '
            '[did not improve symptoms or tiredness after a year](https://pubmed.ncbi.nlm.nih.gov/28402245/) '
            'compared with placebo. That is why a mildly high TSH in an older adult is often rechecked and '
            'watched rather than treated right away.'},
   {'type': 'h2', 'text': 'Treatment and follow-up'},
   {'type': 'p',
    'text': 'When treatment is needed, it replaces the hormone the thyroid can no longer make. The standard '
            'medicine is levothyroxine, identical to the hormone a healthy thyroid produces. The NIDDK describes '
            'the usual routine on its [hypothyroidism '
            'page](https://www.niddk.nih.gov/health-information/endocrine-diseases/hypothyroidism):'},
   {'type': 'ul',
    'items': ['Take it as directed, often in the morning before eating.',
              'Expect a repeat blood test about 6 to 8 weeks after starting or changing the dose.',
              'Once the dose is right, the test is usually repeated at 6 months and then once a year.',
              'Do not stop the medicine without talking to your doctor.']},
   {'type': 'p',
    'text': 'More is not better. Too much thyroid hormone can cause serious problems, including atrial '
            'fibrillation and bone loss, which is why the dose is guided by blood tests. Some supplements get in '
            'the way: the NIH Office of Dietary Supplements notes that [taking iron with levothyroxine can make the '
            'medicine less effective](https://ods.od.nih.gov/factsheets/Iron-Consumer/). Bring every supplement '
            'you take to your visits, and ask how far apart to space them. The NIDDK also cautions that large '
            'amounts of iodine, from kelp or iodine supplements, can worsen hypothyroidism in people with '
            'Hashimoto\'s.'},
   {'type': 'h2', 'text': 'When to call'},
   {'type': 'p',
    'text': 'Call your doctor if you have new fatigue, weight change, feeling cold, or a slow pulse that does not '
            'go away, or if you find out you are pregnant while taking thyroid medicine, since the dose often '
            'needs to rise. Severe, untreated hypothyroidism can rarely become a medical emergency called myxedema '
            'coma, in which the body\'s functions slow to a life-threatening point. That needs 911.'},
   {'type': 'p',
    'text': 'A TSH is part of the blood work Dr. Shtern can order and review with you, with results explained in '
            'plain language. Our [labs and tests](/labs-and-tests) page covers how testing works at the practice, '
            'and our article on [medication reviews](/blog/medication-review-older-adults) explains why '
            'supplements belong on the list. If you would like to meet Dr. Shtern first, the first '
            'visit is a complimentary [meet and greet](/meet-and-greet).'}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'type-2-diabetes-numbers-that-matter',
  'title': 'Living well with type 2 diabetes: the numbers that matter',
  'seo_title': 'Type 2 Diabetes: The Numbers That Matter | Legacy Medical',
  'date': '2026-10-15T09:10:00',
  'modified': '2026-10-15T09:10:00',
  'category': 'Everyday health',
  'excerpt': 'A1C, blood pressure, cholesterol, kidney tests and eye exams: what the 2026 American Diabetes '
             'Association standards recommend, and how often to check each one.',
  'blocks': [
   {'type': 'p',
    'text': 'Type 2 diabetes is about much more than blood sugar. The damage it can do over the years shows up '
            'in the heart, kidneys, eyes, nerves and feet, and much of it is silent until late. The way to stay '
            'ahead of it is to track a short list of numbers and checks, year after year.'},
   {'type': 'p',
    'text': 'The figures below come from the American Diabetes Association\'s Standards of Care in '
            'Diabetes 2026, published in December 2025, and from the National Institute of Diabetes and '
            'Digestive and Kidney Diseases (NIDDK). Your own goals may differ, and that is a conversation to have '
            'with your doctor.'},
   {'type': 'h2', 'text': 'A1C: your three-month average'},
   {'type': 'p',
    'text': 'The A1C blood test reflects your average blood glucose over roughly the past three months. The ADA '
            'says that [an A1C goal below 7 percent is appropriate for many nonpregnant '
            'adults](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690178/) who do not have troublesome low blood '
            'sugars. Goals are often relaxed for older adults, people with many other conditions, or anyone '
            'prone to hypoglycemia, because lows carry their own risks.'},
   {'type': 'p',
    'text': 'How often to test: at least twice a year if you are at goal and stable, and about every 3 months if '
            'you are not at goal or your treatment has just changed. People who wear a continuous glucose '
            'monitor also get a "time in range" number, and the ADA suggests more than 70 percent time in range '
            'as a goal for many adults. If you have been told you have prediabetes rather than diabetes, our '
            'article on [prediabetes and A1C](/blog/prediabetes-and-a1c) covers that stage.'},
   {'type': 'h2', 'text': 'Blood pressure and cholesterol'},
   {'type': 'p',
    'text': 'Diabetes raises the risk of heart attack and stroke, so the ADA\'s heart recommendations matter '
            'as much as the sugar ones. Its 2026 standards say [blood pressure should be '
            'checked at every routine visit](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690187/), and that the '
            'treatment goal is **below 130/80** if it can be reached safely, with a top number under 120 encouraged '
            'for people at high heart or kidney risk. Home readings help; see our guide to [home blood pressure '
            'monitoring](/blog/home-blood-pressure-monitoring).'},
   {'type': 'p',
    'text': 'For cholesterol, the same section recommends a moderate-intensity statin, along with lifestyle '
            'changes, for people with diabetes aged 40 to 75 who do not already have heart disease. LDL cholesterol '
            'is rechecked 4 to 12 weeks after starting or changing a statin, then yearly. Our article on '
            '[statins](/blog/statins-benefits-and-side-effects) explains the benefits and the side effects '
            'people worry about.'},
   {'type': 'p',
    'text': 'The NIDDK sums this up as the [diabetes '
            'ABCs](https://www.niddk.nih.gov/health-information/diabetes/overview/managing-diabetes): A1C, blood '
            'pressure, cholesterol, and stop smoking.'},
   {'type': 'h2', 'text': 'Kidneys: two tests every year'},
   {'type': 'p',
    'text': 'Kidney disease from diabetes affects [20 to 40 percent of people with '
            'diabetes](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690176/), according to the ADA, and it usually '
            'causes no symptoms early on. That is why the ADA recommends that everyone with type 2 diabetes have '
            'two tests **at least once a year**:'},
   {'type': 'ul',
    'items': ['**Urine albumin-to-creatinine ratio (UACR)**, a simple urine test that picks up small amounts of '
              'protein leaking through the kidneys.',
              '**eGFR**, an estimate of kidney filtering calculated from a blood creatinine test.']},
   {'type': 'p',
    'text': 'Both matter, because either one can be abnormal while the other looks fine. When kidney disease is '
            'found, there are now medicines that slow it down. The ADA recommends an SGLT2 inhibitor for people '
            'with type 2 diabetes and chronic kidney disease whose eGFR is 20 or higher, to slow kidney decline and '
            'lower heart risk. Our article on [eGFR and kidney labs](/blog/egfr-kidney-lab-results-explained) '
            'walks through the numbers.'},
   {'type': 'h2', 'text': 'Eyes and feet'},
   {'type': 'p',
    'text': 'Diabetes can damage the retina without blurring vision until it is advanced. The ADA recommends a '
            '[dilated eye exam by an ophthalmologist or optometrist at the time of '
            'diagnosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690177/), then yearly. If one or more yearly '
            'exams show no retinopathy and blood sugar is at goal, every one to two years may be enough. Retinal '
            'photography read remotely, including FDA-approved AI systems, is also an accepted screening '
            'method.'},
   {'type': 'p',
    'text': 'Feet need attention because nerve damage can take away the warning of pain. The NIDDK advises '
            '[checking your own feet every '
            'day](https://www.niddk.nih.gov/health-information/diabetes/overview/preventing-problems/foot-problems), '
            'asking your care team to look at them at each visit, and having a thorough foot exam, including '
            'feeling and pulses, at least once a year.'},
   {'type': 'h2', 'text': 'Putting it together'},
   {'type': 'p',
    'text': 'A simple yearly checklist covers most of it: A1C two to four times, blood pressure at every visit, a '
            'lipid panel, UACR and eGFR, a dilated eye exam, and a foot exam. Add vaccines and a medication '
            'review, and you have the core of good diabetes care. Call your doctor promptly for blood sugars that '
            'stay much higher than usual, frequent lows, a foot sore that is not healing, or new changes in vision. '
            'Confusion, fainting, or a low you cannot bring up are reasons to call 911.'},
   {'type': 'p',
    'text': 'Because Dr. Shtern is board-certified in both Internal Medicine and Nephrology, the kidney side of '
            'diabetes is part of everyday care at Legacy Medical. Our [chronic care](/chronic-care) and [kidney '
            'care](/kidney-care) pages describe how ongoing conditions are followed. If you would like to talk it '
            'over first, the first visit is a complimentary [meet and greet](/meet-and-greet).'}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'statins-benefits-and-side-effects',
  'title': 'Statins: who benefits and what to know about side effects',
  'seo_title': 'Statins: Who Benefits and Side Effects | Legacy Medical',
  'date': '2026-10-15T09:20:00',
  'modified': '2026-10-15T09:20:00',
  'category': 'Heart and blood pressure',
  'excerpt': 'Who the 2026 cholesterol guideline says should consider a statin, what the best evidence shows '
             'about muscle aches and other side effects, and what to ask.',
  'blocks': [
   {'type': 'p',
    'text': 'Statins are among the most studied medicines in the world, and also among the most debated at the '
            'kitchen table. Many people are unsure whether they need one, and many who take one wonder whether '
            'their aches are coming from the pill. This article covers who benefits under current guidance and '
            'what large trials say about side effects.'},
   {'type': 'h2', 'text': 'What statins do'},
   {'type': 'p',
    'text': 'Statins lower LDL, the "bad" cholesterol, by slowing how much cholesterol the liver makes and helping '
            'it clear LDL already in the blood. MedlinePlus, from the National Library of Medicine, notes that '
            'statins [lower the risk of heart attack and stroke in people with high LDL '
            'cholesterol](https://medlineplus.gov/statins.html). They are usually taken once a day for the long '
            'term.'},
   {'type': 'h2', 'text': 'Who should consider one: the 2026 guideline'},
   {'type': 'p',
    'text': 'In March 2026, the American College of Cardiology, the American Heart Association and nine other '
            'groups published a new [guideline on the management of '
            'dyslipidemia](https://www.ahajournals.org/doi/10.1161/CIR.0000000000001423), replacing the 2018 '
            'cholesterol guideline. For people who have not had a heart attack or stroke, the key changes are:'},
   {'type': 'ul',
    'items': ['Risk is estimated with the AHA\'s newer **PREVENT** equations, for adults aged 30 to 79.',
              'Cholesterol-lowering therapy **can be considered** at a 10-year risk of 3 to under 5 percent, and '
              '**should be considered** at 5 to under 10 percent, after a conversation between you and your '
              'clinician.',
              'For adults 40 to 75 with diabetes, stage 3 or 4 chronic kidney disease, or HIV, therapy is '
              'recommended regardless of LDL level.',
              'LDL and non-HDL cholesterol goals are back, and lipoprotein(a) should be measured at least once.',
              'After 75, treatment can be considered along with lifestyle changes.']},
   {'type': 'p',
    'text': 'The guideline also endorses a coronary artery calcium scan for men 40 and older and women 45 and '
            'older when the decision is uncertain. We explain that test in [coronary artery calcium '
            'score](/blog/coronary-artery-calcium-score), and lipoprotein(a) in [ApoB and '
            'Lp(a)](/blog/apob-and-lipoprotein-a).'},
   {'type': 'p',
    'text': 'The U.S. Preventive Services Task Force uses older thresholds. Its 2022 recommendation advises a '
            'statin for adults 40 to 75 with at least one risk factor (high cholesterol, diabetes, high blood '
            'pressure or smoking) and a [10-year risk of 10 percent or '
            'more](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/statin-use-in-adults-preventive-medication), '
            'and selectively offering one at 7.5 to under 10 percent. It found the evidence insufficient to say '
            'whether starting a statin at 76 or older helps. The two documents differ in their numbers, which is '
            'one reason the decision is best made together with your doctor.'},
   {'type': 'h2', 'text': 'Muscle aches: what the evidence shows'},
   {'type': 'p',
    'text': 'Muscle pain is the side effect people fear most. In 2022, researchers pooled individual data from 19 '
            'double-blind trials with more than 120,000 people randomly assigned to a statin or a placebo. Muscle '
            'pain or weakness was reported by 27.1 percent of people on a statin and 26.6 percent on placebo. In '
            'the first year, the statin caused about 11 extra reports per 1,000 people, and the authors concluded '
            'that [more than 90 percent of muscle symptoms reported by people taking a statin were not caused by '
            'the statin](https://pubmed.ncbi.nlm.nih.gov/36049498/). After the first year there was no clear '
            'excess.'},
   {'type': 'p',
    'text': 'That does not mean aches are imagined. Muscles ache for many reasons, and some people really do '
            'react to a particular statin or dose. If you have new muscle pain, MedlinePlus advises telling your '
            'provider, who may check a blood test for muscle damage, and notes that pain may go away with a '
            'different statin. Options often include a lower dose, a different statin, or a different schedule. '
            'Serious muscle damage is rare.'},
   {'type': 'h2', 'text': 'Other side effects worth knowing'},
   {'type': 'ul',
    'items': ['**Blood sugar.** Statins may raise the risk of type 2 diabetes, mainly in people who are already at '
              'high risk, such as those with prediabetes or obesity, according to '
              '[MedlinePlus](https://medlineplus.gov/statins.html).',
              '**Liver tests.** Statins can cause abnormal liver enzyme results, but actual liver damage is very '
              'rare.',
              '**Interactions.** Grapefruit and grapefruit juice change how the liver breaks down some statins, '
              'and certain medicines and supplements interact as well. Review everything you take with your '
              'doctor or pharmacist.',
              '**Pregnancy.** Statins are not taken during pregnancy or breastfeeding.']},
   {'type': 'h2', 'text': 'Questions to bring to your visit'},
   {'type': 'p',
    'text': 'What is my 10-year risk, and what would a statin change? Would a calcium score help us decide? What '
            'LDL goal makes sense for me? If I had side effects before, which options have we not tried? Food '
            'still matters alongside any medicine; our article on the [Mediterranean '
            'diet](/blog/mediterranean-diet-heart-health) is a good place to start. Do not stop a statin on '
            'your own without talking to your doctor. Chest pain, pressure, or sudden weakness or trouble '
            'speaking are reasons to call 911.'},
   {'type': 'p',
    'text': 'At Legacy Medical, Dr. Shtern can calculate your risk, review your full lipid results and talk '
            'through the tradeoffs at an unhurried pace. Our [preventive care](/preventive-care) page explains '
            'the annual physical where this usually happens. If you would like to meet her first, the first visit '
            'is a complimentary [meet and greet](/meet-and-greet).'}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'atrial-fibrillation-stroke-risk',
  'title': 'Atrial fibrillation: symptoms, stroke risk and treatment',
  'seo_title': 'Atrial Fibrillation: Symptoms and Stroke Risk | Legacy Medical',
  'date': '2026-10-15T09:30:00',
  'modified': '2026-10-15T09:30:00',
  'category': 'Heart and blood pressure',
  'excerpt': 'AFib is the most common irregular heart rhythm and a major cause of stroke. The symptoms, who is at '
             'risk, and how blood thinners, rhythm care and lifestyle fit together.',
  'blocks': [
   {'type': 'p',
    'text': 'Atrial fibrillation, often called AFib, is an irregular and often rapid heart rhythm. Some people '
            'feel it as fluttering or pounding. Others feel nothing at all and learn about it from a smartwatch '
            'alert or a routine EKG. Either way, it deserves attention, mainly because of its link to stroke.'},
   {'type': 'h2', 'text': 'What AFib is and how it feels'},
   {'type': 'p',
    'text': 'In AFib, the heart\'s upper chambers quiver instead of squeezing in a steady rhythm, and the upper '
            'and lower chambers stop working together. The National Heart, Lung, and Blood Institute explains that '
            '[blood can pool in the heart](https://www.nhlbi.nih.gov/health/atrial-fibrillation), which can lead '
            'to clots. AFib may come and go, or it may become permanent, and episodes often grow longer and more '
            'frequent over time.'},
   {'type': 'p',
    'text': 'The CDC lists these [possible symptoms](https://www.cdc.gov/heart-disease/about/atrial-fibrillation.html):'},
   {'type': 'ul',
    'items': ['An irregular heartbeat or palpitations',
              'Lightheadedness',
              'Extreme fatigue',
              'Shortness of breath',
              'Chest pain']},
   {'type': 'p',
    'text': 'AFib becomes more common with age, and the CDC projects that about 12.1 million people in the United '
            'States will have it by 2050. Risk factors include high blood pressure, which accounts for about 1 in '
            '5 cases, along with obesity, diabetes, heart failure, coronary disease, an overactive thyroid, chronic '
            'kidney disease, moderate to heavy drinking and smoking.'},
   {'type': 'p',
    'text': 'Should people without symptoms be screened? The U.S. Preventive Services Task Force concluded in 2022 '
            'that there is [not enough evidence to recommend for or against routine '
            'screening](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/atrial-fibrillation-screening) '
            'for AFib. In practice, an irregular pulse found at a checkup, or an alert from a wearable device, is '
            'followed up with an EKG.'},
   {'type': 'h2', 'text': 'Why stroke is the main concern'},
   {'type': 'p',
    'text': 'Clots that form in the quivering upper chamber can travel to the brain. According to the CDC, AFib is '
            'linked to roughly a **fivefold higher risk of ischemic stroke**, causes about **1 in 7 strokes**, and '
            'strokes caused by AFib tend to be more severe.'},
   {'type': 'p',
    'text': 'The 2023 guideline on AFib from the American College of Cardiology, the American Heart Association '
            'and two other societies asks clinicians to estimate each person\'s stroke risk with a validated score '
            'such as CHA2DS2-VASc, which counts factors like age, sex, high blood pressure, diabetes, heart '
            'failure and prior stroke. The ACC\'s [summary of that '
            'guideline](https://www.acc.org/latest-in-cardiology/ten-points-to-remember/2023/11/27/19/46/2023-acc-guideline-for-af-gl-af) '
            'notes that for people whose yearly stroke risk is about 2 percent or higher, stroke prevention should '
            'be based on that risk, whether the AFib comes and goes or is constant.'},
   {'type': 'h2', 'text': 'Treatment: three parts that work together'},
   {'type': 'p',
    'text': '**Preventing stroke.** For most people who need a blood thinner, the guideline prefers the newer direct '
            'oral anticoagulants over warfarin, except in people with mitral stenosis or a mechanical heart valve. '
            'Aspirin alone is not recommended as a substitute. Bleeding risk is weighed, but a bleeding score alone '
            'should not decide whether someone gets a blood thinner. For people who cannot take blood thinners '
            'long term, a device that closes off the left atrial appendage, a small pouch of the upper chamber, '
            'is now given stronger support.'},
   {'type': 'p',
    'text': '**Controlling rate and rhythm.** Medicines can slow the heart or help hold a normal rhythm. Catheter '
            'ablation, a procedure that targets the tissue setting off AFib, is now recommended as a first option '
            'for selected patients, according to the [2023 '
            'guideline](https://www.ahajournals.org/doi/10.1161/CIR.0000000000001193), and for suitable patients '
            'with heart failure and a weak heart muscle.'},
   {'type': 'p',
    'text': '**Treating the causes.** The guideline calls lifestyle and risk factor changes a pillar of AFib care: '
            'losing weight when needed, regular exercise, quitting tobacco, limiting alcohol, controlling blood '
            'pressure, and screening for sleep apnea. These can reduce how often AFib returns. Our articles on '
            '[sleep apnea and the heart](/blog/sleep-apnea-and-heart-health) and [alcohol after '
            '50](/blog/alcohol-after-50) go further.'},
   {'type': 'h2', 'text': 'When to call, and when to call 911'},
   {'type': 'p',
    'text': 'Call your doctor soon if you notice a new irregular pulse, a smartwatch alert you cannot explain, or '
            'palpitations that keep coming back. Call 911 for chest pain, fainting or severe shortness of breath, '
            'or for any [stroke warning sign](https://www.cdc.gov/stroke/signs-symptoms/index.html). The CDC\'s '
            'B.E. F.A.S.T. check is: **B**alance loss, **E**ye or vision changes, **F**ace drooping, **A**rm '
            'drifting down, **S**peech slurred or strange, **T**ime to call 911. Do not drive yourself to the '
            'hospital.'},
   {'type': 'p',
    'text': 'People with AFib usually see a cardiologist, and day-to-day care still depends on someone keeping '
            'the whole picture straight: blood pressure, kidney function, which affects blood thinner dosing, and '
            'every medicine on the list. Dr. Shtern coordinates that care with specialists, as described on our '
            '[specialists and hospital care](/specialists-and-hospital-care) and [hypertension](/hypertension) '
            'pages. If you would like to meet her first, the first visit is a complimentary [meet and '
            'greet](/meet-and-greet).'}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'sleep-apnea-and-heart-health',
  'title': 'Sleep apnea: signs, testing and why it matters for the heart',
  'seo_title': 'Sleep Apnea: Signs, Testing and the Heart | Legacy Medical',
  'date': '2026-10-15T09:40:00',
  'modified': '2026-10-15T09:40:00',
  'category': 'Healthy aging',
  'excerpt': 'Loud snoring and daytime sleepiness can be signs of obstructive sleep apnea. How it is tested, how it '
             'is treated, and its links to blood pressure and AFib.',
  'blocks': [
   {'type': 'p',
    'text': 'Often the first person to notice sleep apnea is not the one who has it. It is the partner who hears '
            'the snoring stop, the silence, and then the gasp. Sleep apnea is common, often missed, and closely '
            'tied to heart health, which is why it is worth taking seriously.'},
   {'type': 'h2', 'text': 'What sleep apnea is'},
   {'type': 'p',
    'text': 'The National Heart, Lung, and Blood Institute describes sleep apnea as [breathing that stops and '
            'restarts many times during sleep](https://www.nhlbi.nih.gov/health/sleep-apnea), which can keep the '
            'body from getting enough oxygen. The most common type is **obstructive sleep apnea**, in which the '
            'upper airway is repeatedly blocked. Obesity, large tonsils and hormone changes can narrow the airway. '
            'A less common type, central sleep apnea, happens when the brain does not send the signals to '
            'breathe. Left undiagnosed, the NHLBI notes, poor sleep from apnea can lead to problems concentrating, '
            'making decisions and remembering things.'},
   {'type': 'p',
    'text': 'It is far from rare. A 2021 American Heart Association scientific statement estimated that [about '
            '34 percent of middle-aged men and 17 percent of middle-aged '
            'women](https://pubmed.ncbi.nlm.nih.gov/34148375/) meet the criteria for obstructive sleep apnea.'},
   {'type': 'h2', 'text': 'Signs to watch for'},
   {'type': 'p',
    'text': 'The NHLBI lists these [symptoms](https://www.nhlbi.nih.gov/health/sleep-apnea/symptoms):'},
   {'type': 'ul',
    'items': ['Loud, frequent snoring, or breathing that stops and starts',
              'Gasping for air during sleep',
              'Daytime sleepiness and trouble focusing',
              'Dry mouth or headache on waking',
              'Fatigue or insomnia, which are more common presentations in women',
              'Waking often during the night to urinate']},
   {'type': 'p',
    'text': 'As the NHLBI notes, fatigue, headaches and insomnia are more common presentations in women, so '
            'sleep apnea is not only a question for loud snorers.'},
   {'type': 'h2', 'text': 'Why it matters for the heart'},
   {'type': 'p',
    'text': 'Each pause in breathing drops oxygen levels, jolts the nervous system and fragments sleep, night '
            'after night. The AHA statement found that sleep apnea is present in 40 to 80 percent of people with '
            'high blood pressure, heart failure, coronary artery disease, pulmonary hypertension, atrial '
            'fibrillation and stroke, yet it is often unrecognized in heart care.'},
   {'type': 'p',
    'text': 'The statement recommends screening for sleep apnea in people with high blood pressure that is hard '
            'to control, and in people whose atrial fibrillation returns after cardioversion or ablation. We cover '
            'that connection in [atrial fibrillation and stroke '
            'risk](/blog/atrial-fibrillation-stroke-risk) and the blood pressure side in [blood pressure and '
            'brain health](/blog/blood-pressure-and-brain-health).'},
   {'type': 'h2', 'text': 'Testing'},
   {'type': 'p',
    'text': 'Questionnaires can raise suspicion, but they cannot make the diagnosis. The U.S. Preventive Services '
            'Task Force found in 2022 that there is [not enough evidence to screen adults who have no '
            'symptoms](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/obstructive-sleep-apnea-in-adults-screening), '
            'so testing is aimed at people with symptoms or related conditions.'},
   {'type': 'p',
    'text': 'The diagnosis needs a sleep study. The American Academy of Sleep Medicine\'s guideline says that '
            'either an overnight study in a sleep lab (polysomnography) or [a home sleep apnea test with a '
            'technically adequate device](https://pubmed.ncbi.nlm.nih.gov/28162150/) can be used for adults with '
            'uncomplicated, likely moderate to severe sleep apnea. People with significant heart or lung disease '
            'and some other conditions are usually tested in a lab.'},
   {'type': 'h2', 'text': 'Treatment'},
   {'type': 'p',
    'text': 'The AHA statement advises that everyone with obstructive sleep apnea be considered for treatment, '
            'including weight loss and behavior changes where they fit:'},
   {'type': 'ul',
    'items': ['**CPAP** (continuous positive airway pressure) should be offered for severe sleep apnea. A mask '
              'gently holds the airway open with air pressure. Fit and comfort matter, and many people need a few '
              'adjustments before it works well.',
              '**Oral appliances** made by a dentist can be considered for mild to moderate sleep apnea or for '
              'people who cannot use CPAP.',
              '**Medicine.** In December 2024, the FDA approved tirzepatide (Zepbound) as the [first medication '
              'for moderate to severe obstructive sleep apnea in adults with '
              'obesity](https://www.fda.gov/news-events/press-announcements/fda-approves-first-medication-obstructive-sleep-apnea), '
              'used with diet and exercise. Our article on [GLP-1 '
              'medications](/blog/glp-1-medications-for-weight-loss) has more on that class.',
              '**Surgery** is an option for some people when other treatments do not work.']},
   {'type': 'p',
    'text': 'A follow-up sleep test is often done to confirm that treatment is working. For more on why good sleep '
            'matters as we age, see [sleep and healthy aging](/blog/sleep-and-healthy-aging).'},
   {'type': 'p',
    'text': 'Never drive drowsy. Call your doctor if a partner notices pauses in your breathing or you are '
            'sleepy during the day despite a full night in bed. If you are worried about any of this, Dr. Shtern '
            'can review your symptoms, blood pressure and heart rhythm and arrange testing. If you would like to '
            'meet her first, the first visit is a complimentary [meet and greet](/meet-and-greet).'}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'heartburn-and-gerd',
  'title': 'Heartburn and GERD: when it is more than indigestion',
  'seo_title': 'Heartburn and GERD: More Than Indigestion | Legacy Medical',
  'date': '2026-10-15T09:50:00',
  'modified': '2026-10-15T09:50:00',
  'category': 'Everyday health',
  'excerpt': 'Occasional heartburn is common. When reflux becomes GERD, what helps, how to use acid-reducing '
             'medicines wisely, and the warning signs that need a doctor.',
  'blocks': [
   {'type': 'p',
    'text': 'Almost everyone has had heartburn after a big dinner. When it happens often, wakes you at night, or '
            'needs a pill most days, it may be gastroesophageal reflux disease, or GERD. Most of the time GERD is '
            'very manageable. A few symptoms, though, should never be written off as indigestion.'},
   {'type': 'h2', 'text': 'Reflux versus GERD'},
   {'type': 'p',
    'text': 'Reflux happens when stomach contents come back up into the esophagus, the tube that carries food to '
            'the stomach. The National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK) explains '
            'that many people have reflux once in a while, and that [GERD is a more severe, long-lasting '
            'form](https://www.niddk.nih.gov/health-information/digestive-diseases/acid-reflux-ger-gerd-adults) '
            'that causes repeated symptoms or leads to complications. It can develop when the muscle at the bottom '
            'of the esophagus weakens or relaxes when it should not.'},
   {'type': 'p',
    'text': 'The classic symptoms are heartburn, a burning feeling behind the breastbone rising toward the throat, '
            'and regurgitation, a sour taste of food or acid in the mouth. The NIDDK also lists [chest pain, '
            'nausea, trouble or pain swallowing, and a chronic cough or '
            'hoarseness](https://www.niddk.nih.gov/health-information/digestive-diseases/acid-reflux-ger-gerd-adults/symptoms-causes). '
            'Being overweight, pregnancy, smoking and a hiatal hernia raise the risk, and so can some medicines, '
            'including NSAIDs, certain blood pressure pills (calcium channel blockers), some asthma medicines, '
            'sedatives and tricyclic antidepressants.'},
   {'type': 'h2', 'text': 'Chest pain: rule out the heart first'},
   {'type': 'p',
    'text': 'Heartburn and a heart attack can feel alike. The American College of Gastroenterology\'s 2022 '
            'guideline on GERD advises that people with chest pain have [an adequate evaluation to exclude heart '
            'disease](https://pubmed.ncbi.nlm.nih.gov/34807007/) before it is attributed to reflux. Call 911 for '
            'chest pain or pressure, especially with shortness of breath, sweating, lightheadedness, or pain in '
            'the jaw, neck, back, arms or shoulders. The CDC notes that [women are more likely to have less '
            'obvious symptoms](https://www.cdc.gov/heart-disease/about/heart-attack.html), such as unusual '
            'tiredness, nausea or vomiting.'},
   {'type': 'h2', 'text': 'What helps'},
   {'type': 'p',
    'text': 'The NIDDK and the ACG guideline both start with daily habits:'},
   {'type': 'ul',
    'items': ['Avoid eating within 2 to 3 hours of bedtime.',
              'For nighttime symptoms, raise your head 6 to 8 inches with a foam wedge or extra pillows under your '
              'head and upper back.',
              'Lose weight if you are overweight.',
              'Stop smoking.',
              'Notice and limit the foods and drinks that set off your symptoms.']},
   {'type': 'p',
    'text': 'For medicines, the NIDDK describes three main options. **Antacids** relieve mild, occasional '
            'heartburn but are not meant for daily use without talking to a doctor. **H2 blockers** such as '
            'famotidine lower acid production. **Proton pump inhibitors (PPIs)**, such as omeprazole, are the '
            'strongest and can heal an inflamed esophagus in most people.'},
   {'type': 'p',
    'text': 'The ACG guideline recommends that people with classic heartburn and no warning signs try a PPI once '
            'daily for 8 weeks, taken **30 to 60 minutes before a meal** rather than at bedtime. If symptoms resolve, the '
            'guideline recommends trying to stop the PPI. People who need long-term treatment should use the '
            'lowest dose that controls symptoms. When medicines and habit changes are not enough, or someone wants to '
            'stop long-term medicine, the NIDDK notes that surgery is an option; the most common operation, '
            'fundoplication, usually brings long-term relief. Any long-term acid medicine belongs on your medication list for '
            'review; see our article on [medication reviews](/blog/medication-review-older-adults).'},
   {'type': 'h2', 'text': 'Warning signs that need a doctor'},
   {'type': 'p',
    'text': 'See a doctor if heartburn does not improve with over-the-counter medicines and habit changes, or if '
            'you need them for more than a couple of weeks. The NIDDK lists these as reasons to be seen '
            'promptly:'},
   {'type': 'ul',
    'items': ['Trouble swallowing or pain when swallowing',
              'Persistent vomiting or loss of appetite',
              'Vomit with blood or that looks like coffee grounds',
              'Black, tarry or bloody stools',
              'Weight loss you cannot explain']},
   {'type': 'p',
    'text': 'The ACG recommends an upper endoscopy, a camera exam of the esophagus and stomach, as the first test '
            'for trouble swallowing, weight loss or bleeding, and for people with several risk factors for '
            'Barrett\'s esophagus, a change in the esophageal lining caused by long-standing reflux. Vomiting '
            'large amounts of blood or feeling faint is a 911 call.'},
   {'type': 'p',
    'text': 'Heartburn that keeps coming back is the kind of problem that gets better with a doctor who knows your '
            'medicines and history. Legacy Medical offers [same or next business day '
            'visits](/same-or-next-day-visits), and Dr. Shtern can arrange specialist care when an endoscopy is '
            'needed. If you take NSAIDs regularly, our article on [NSAID risks](/blog/nsaids-risks-and-side-effects) '
            'is worth a read. To meet Dr. Shtern first, the first visit is a complimentary [meet and '
            'greet](/meet-and-greet).'}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'vitamin-d-testing-and-supplements',
  'title': 'Vitamin D: who needs testing and supplements',
  'seo_title': 'Vitamin D: Who Needs Testing and Supplements | Legacy Medical',
  'date': '2026-10-15T10:00:00',
  'modified': '2026-10-15T10:00:00',
  'category': 'Nutrition',
  'excerpt': 'Vitamin D blood tests and supplements are everywhere. What the NIH, the Endocrine Society and large '
             'trials say about who benefits, how much is enough, and how much is too much.',
  'blocks': [
   {'type': 'p',
    'text': 'Vitamin D has been called a cure for almost everything, and vitamin D blood tests have become a '
            'routine add-on for many people. The research of the last decade has brought this back down to earth. '
            'Vitamin D matters for bones, but for most healthy adults, more testing and higher doses have not '
            'delivered the benefits many hoped for.'},
   {'type': 'h2', 'text': 'What vitamin D does and where it comes from'},
   {'type': 'p',
    'text': 'Vitamin D helps the body absorb calcium and keep bones strong. Severe deficiency in adults causes '
            'osteomalacia, with bone pain and muscle weakness. The body makes vitamin D when bare skin is exposed '
            'to the sun, though not through a window. Natural food sources are limited: fatty fish such as salmon, '
            'trout and mackerel are the best, with small amounts in egg yolks, cheese and mushrooms, and many '
            'milks and cereals are fortified.'},
   {'type': 'p',
    'text': 'The NIH Office of Dietary Supplements lists the [recommended daily '
            'amounts](https://ods.od.nih.gov/factsheets/VitaminD-Consumer/) for adults as **600 IU (15 mcg) through '
            'age 70** and **800 IU (20 mcg) from age 71**. Sunshine is not a safe substitute for diet or '
            'supplements, since the same ultraviolet light raises skin cancer risk, something we write about in '
            '[skin cancer checks in Florida](/blog/skin-cancer-checks-florida).'},
   {'type': 'h2', 'text': 'Who should be tested'},
   {'type': 'p',
    'text': 'For adults without symptoms, routine testing is not recommended by the major groups. The U.S. '
            'Preventive Services Task Force concluded in 2021 that the evidence is [insufficient to recommend for '
            'or against screening](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/vitamin-d-deficiency-screening). '
            'In 2024, the Endocrine Society went further and suggested [against routine vitamin D blood '
            'tests](https://pubmed.ncbi.nlm.nih.gov/38828931/) in the general population, including people with '
            'obesity or darker skin, because trials have not shown that testing improves outcomes or defined the '
            'ideal level.'},
   {'type': 'p',
    'text': 'Testing still makes sense when there is a medical reason. The NIH lists groups more likely to run '
            'low: older adults, people who rarely get sun on their skin, people with darker skin, people with '
            'Crohn\'s disease, celiac disease or ulcerative colitis, and people with obesity or a history of '
            'gastric bypass. Osteoporosis, kidney disease, some medicines and unexplained bone pain or low calcium '
            'are other common reasons a doctor orders the test.'},
   {'type': 'p',
    'text': 'If you are tested, the NIH offers this guide to the 25-hydroxyvitamin D result: **20 ng/mL or above is '
            'adequate** for most people, below 12 ng/mL is too low, and above 50 ng/mL is too high and may cause '
            'problems.'},
   {'type': 'h2', 'text': 'Who benefits from supplements'},
   {'type': 'p',
    'text': 'The 2024 Endocrine Society guideline suggests extra vitamin D, without testing, for a few groups: '
            'children and teens, **adults 75 and older**, people who are pregnant, and people with high-risk '
            'prediabetes. For people over 50 who take it, the panel suggested a modest daily dose rather than '
            'large doses taken weekly or monthly. It suggested against taking more than the standard daily '
            'amounts to prevent disease in healthy adults under 75.'},
   {'type': 'p',
    'text': 'That advice rests on large trials. In VITAL, more than 25,000 adults took 2,000 IU of vitamin D a day '
            'or a placebo for about five years. Vitamin D [did not lower the rate of cancer or of heart attacks, '
            'strokes and cardiovascular deaths](https://pubmed.ncbi.nlm.nih.gov/30415629/). For bones, vitamin D '
            'works best as part of a bigger plan; our article on [bone density '
            'screening](/blog/bone-density-screening) covers the rest.'},
   {'type': 'h2', 'text': 'How much is too much'},
   {'type': 'p',
    'text': 'More is not better. The NIH sets the upper limit for adults at **4,000 IU (100 mcg) a day** from all '
            'sources, unless a doctor prescribes more for a time to treat a deficiency. Very high blood levels can '
            'cause nausea, vomiting, muscle weakness, confusion, dehydration and kidney stones, and in extreme '
            'cases kidney failure and heart rhythm problems. These almost always come from supplements, not '
            'sun or food.'},
   {'type': 'p',
    'text': 'Check for interactions too. The NIH notes that high-dose vitamin D may make some statins work less '
            'well, that thiazide water pills plus vitamin D can raise calcium too high, and that steroids such as '
            'prednisone can lower vitamin D. Many multivitamins already contain vitamin D, so add up every '
            'source; see [multivitamins: who needs them](/blog/multivitamin-supplements-who-needs-them).'},
   {'type': 'p',
    'text': 'For people with kidney disease, vitamin D and calcium are handled differently, and decisions should '
            'go through your doctor. Dr. Shtern is board-certified in Internal Medicine and Nephrology and can '
            'help you decide whether a test or a supplement makes sense for you. Our [labs and '
            'tests](/labs-and-tests) page explains how testing works at Legacy Medical, and the first visit is a '
            'complimentary [meet and greet](/meet-and-greet).'}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'iron-deficiency-anemia-adults',
  'title': 'Iron deficiency and anemia in adults',
  'seo_title': 'Iron Deficiency and Anemia in Adults | Legacy Medical',
  'date': '2026-10-15T10:10:00',
  'modified': '2026-10-15T10:10:00',
  'category': 'Everyday health',
  'excerpt': 'Iron deficiency is the most common cause of anemia. The symptoms, why the cause always matters in '
             'adults, and how iron is replaced safely.',
  'blocks': [
   {'type': 'p',
    'text': 'Feeling tired and short of breath on the stairs can have many causes. One of the most common, and '
            'most fixable, is low iron. In adults, though, iron deficiency is a finding that calls for a second '
            'question: why is the iron low?'},
   {'type': 'h2', 'text': 'What iron deficiency anemia is'},
   {'type': 'p',
    'text': 'The body needs iron to make hemoglobin, the protein in red blood cells that carries oxygen. When iron '
            'runs low, the body makes fewer and smaller red cells. The National Heart, Lung, and Blood Institute '
            'calls iron-deficiency anemia [the most common type of '
            'anemia](https://www.nhlbi.nih.gov/health/anemia/iron-deficiency-anemia).'},
   {'type': 'p',
    'text': 'Mild cases often cause no symptoms. As it worsens, people may notice tiredness, shortness of breath, '
            'chest pain, headaches or restless legs. Left untreated, the NHLBI notes, it can cause heart problems '
            'and make other chronic conditions harder to manage. Chest pain or severe shortness of breath needs '
            'emergency care.'},
   {'type': 'h2', 'text': 'Why it happens'},
   {'type': 'p',
    'text': 'The NHLBI lists three broad causes:'},
   {'type': 'ul',
    'items': ['**Blood loss.** Heavy menstrual periods, or bleeding in the digestive tract from ulcers, '
              'inflammatory bowel disease, polyps or colon cancer. Regular aspirin or NSAIDs such as ibuprofen and '
              'naproxen can cause slow bleeding in the stomach or intestines.',
              '**Poor absorption.** Celiac disease, Crohn\'s disease, ulcerative colitis, H. pylori infection, and '
              'surgery on the stomach or intestines, including weight-loss surgery.',
              '**Not enough iron in the diet**, which is less often the whole story in adults.']},
   {'type': 'p',
    'text': 'Chronic kidney disease and long-term inflammatory conditions such as heart failure can also cause or '
            'worsen anemia by changing how the body makes red cells and handles iron.'},
   {'type': 'h2', 'text': 'Finding the cause'},
   {'type': 'p',
    'text': 'Diagnosis starts with blood tests: a complete blood count, hemoglobin, iron levels and ferritin, '
            'which reflects the body\'s iron stores. The American Gastroenterological Association\'s 2020 '
            'guideline recommends using a [ferritin cutoff of 45 ng/mL rather than '
            '15](https://pubmed.ncbi.nlm.nih.gov/32810434/) to diagnose iron deficiency in people with anemia, '
            'since the lower cutoff misses many cases.'},
   {'type': 'p',
    'text': 'For men and for women after menopause, iron deficiency anemia is not considered normal, even without '
            'symptoms. The same guideline recommends looking at both ends of the digestive tract, with an upper '
            'endoscopy and a colonoscopy, to search for a source of bleeding. It suggests testing for celiac '
            'disease, and testing for and treating H. pylori when no other cause is found. Women who still have '
            'periods are evaluated case by case. Black or tarry stools, or blood in the stool or vomit, are '
            'reasons to be seen right away.'},
   {'type': 'h2', 'text': 'Treatment'},
   {'type': 'p',
    'text': 'Iron pills are the most common treatment, and the NHLBI notes it often takes **three to six months** '
            'to rebuild iron stores, well after the blood count improves. Side effects include constipation, '
            'upset stomach, nausea and a metallic taste. Your doctor may suggest taking iron with food, a lower '
            'dose, or a different schedule if it disagrees with you. Intravenous iron is more likely to be used for serious '
            'deficiency or in people with long-term conditions, and it often restores iron in one or a few '
            'sessions.'},
   {'type': 'p',
    'text': 'Food supports treatment but rarely fixes a true deficiency on its own. Good sources include lean red '
            'meat, salmon, eggs, beans, peas, tofu, dried fruit, dark leafy greens and fortified cereals. The '
            'NIH Office of Dietary Supplements explains that iron from plants is absorbed better when eaten with '
            '[vitamin C foods such as citrus, strawberries, peppers and '
            'tomatoes](https://ods.od.nih.gov/factsheets/Iron-Consumer/), while black tea can reduce absorption.'},
   {'type': 'h2', 'text': 'Be careful with iron supplements'},
   {'type': 'p',
    'text': 'Iron is not a supplement to take "just in case." The NIH recommends 8 mg a day for men and for women '
            '51 and older, and 18 mg for women 19 to 50, with an upper limit of 45 mg a day for adults unless a '
            'doctor prescribes more. Too much can cause stomach problems, and people with hereditary '
            'hemochromatosis, an inherited iron overload condition, should avoid iron supplements '
            'altogether. Iron also interacts with medicines: it can reduce absorption of levothyroxine, our '
            'subject in [underactive thyroid and the TSH test](/blog/underactive-thyroid-tsh-test), and of '
            'levodopa, while acid-reducing PPIs can lower iron absorption from food.'},
   {'type': 'p',
    'text': 'Anemia is one of the places where Internal Medicine and kidney care overlap, and as a board-certified '
            'internist and Nephrologist, Dr. Shtern looks at both. If you take aspirin or an NSAID regularly, our '
            'article on [NSAID risks](/blog/nsaids-risks-and-side-effects) is worth a read. Our [labs and '
            'tests](/labs-and-tests) page explains how blood work is handled, and the first visit is a '
            'complimentary [meet and greet](/meet-and-greet).'}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'shingles-vaccine-after-50',
  'title': 'The shingles vaccine after 50',
  'seo_title': 'Shingles Vaccine Over 50: Is Shingrix Worth It? | Legacy Medical',
  'date': '2026-10-15T10:20:00',
  'modified': '2026-10-15T10:20:00',
  'category': 'Infections and vaccines',
  'excerpt': 'Two doses of Shingrix are 97 percent effective in healthy adults 50 to 69. Who the CDC recommends it for, what the side effects feel like, and Medicare coverage.',
  'blocks': [
   {'type': 'p',
    'text': 'Anyone who has had chickenpox carries the virus that causes it for life. Years later, often after 50, '
            'it can wake up as shingles: a painful, blistering rash, usually in a band on one side of the body. '
            'For some people the nerve pain lasts long after the rash heals. A highly effective vaccine can prevent '
            'most of it.'},
   {'type': 'h2', 'text': 'Why shingles is worth preventing'},
   {'type': 'p',
    'text': 'The CDC estimates that [about 1 in 3 people in the United States will get shingles in their '
            'lifetime](https://www.cdc.gov/shingles/vaccines/index.html). The CDC notes that [the risk of shingles '
            'and its complications rises with age](https://www.cdc.gov/shingles/about/index.html). The most common '
            'complication is long-term nerve pain where the rash was, called postherpetic neuralgia (PHN), and '
            'shingles can sometimes lead to vision loss. If you think you have shingles, contact your doctor as '
            'soon as possible: antiviral medicines work best when started as soon as the rash appears.'},
   {'type': 'h2', 'text': 'Who should get Shingrix, and how well it works'},
   {'type': 'p',
    'text': 'The shingles vaccine used in the United States is the recombinant zoster vaccine, Shingrix. The CDC '
            'recommends it for:'},
   {'type': 'ul',
    'items': ['**All adults 50 and older**, with no upper age limit.',
              '**Adults 19 and older with a weakened immune system** from disease or treatment.']},
   {'type': 'p',
    'text': 'You should still get Shingrix if you have already had shingles, if you received the older Zostavax '
            'vaccine (no longer sold in the U.S. since November 2020), or if you are not sure you had chickenpox. '
            'If you have shingles now, wait until the rash is gone. People who had a severe allergic reaction to '
            'the vaccine or its ingredients should not get it, and people who are pregnant should wait.'},
   {'type': 'p',
    'text': 'Shingrix is a **two-dose series**. For adults 50 and older, the second dose comes **2 to 6 months** '
            'after the first. For people with a weakened immune system, the second dose can be given 1 to 2 months '
            'after the first. Both doses are needed for full protection, so it helps to book the second when you '
            'get the first.'},
   {'type': 'p',
    'text': 'The protection is strong. The CDC reports that in healthy adults, two doses of Shingrix are:'},
   {'type': 'ul',
    'items': ['**97 percent effective** against shingles in people 50 to 69.',
              '**91 percent effective** in people 70 and older.',
              '**91 percent effective** against postherpetic neuralgia in adults 50 and older.',
              '68 to 91 percent effective in adults with weakened immune systems, depending on the condition.']},
   {'type': 'p',
    'text': 'Protection stayed high for at least 7 years in healthy adults 70 and older who were followed.'},
   {'type': 'h2', 'text': 'Side effects'},
   {'type': 'p',
    'text': 'Shingrix is known for making people feel it for a day or two. The CDC lists a sore arm with redness '
            'or swelling, tiredness, muscle aches, headache, chills, fever, stomach pain and nausea as common '
            'reactions, usually lasting 2 to 3 days and more common in younger adults. Many people plan the shot '
            'before a quiet day. A reaction to the first dose is not a reason to skip the second. Guillain-Barré '
            'syndrome has been reported very rarely after the vaccine. Call 911 for signs of a severe allergic '
            'reaction, such as trouble breathing or swelling of the face and throat.'},
   {'type': 'h2', 'text': 'A note on shingles vaccines and memory'},
   {'type': 'p',
    'text': 'You may have seen headlines linking the shingles vaccine to a lower risk of dementia. The best-known '
            'study, published in Nature in 2025, took advantage of a birth-date cutoff for vaccine eligibility in '
            'Wales. People who became eligible were [about 20 percent less likely to receive a new dementia '
            'diagnosis over seven years](https://pubmed.ncbi.nlm.nih.gov/40175543/) than people born just too '
            'early to qualify. Two cautions: that study looked at the older live vaccine, Zostavax, not Shingrix, '
            'and the finding is not a reason on its own to get vaccinated. Preventing shingles and its nerve pain '
            'is reason enough, and any effect on memory would be a bonus that research is still sorting out.'},
   {'type': 'h2', 'text': 'Cost and coverage'},
   {'type': 'p',
    'text': 'Medicare covers the shingles vaccine under Part D, the drug benefit. According to Medicare.gov, '
            '[people with Part D pay nothing](https://www.medicare.gov/coverage/shingles-shot) for vaccines '
            'recommended by the CDC\'s Advisory Committee on Immunization Practices, with no deductible or '
            'copayment. If you have other coverage, check with your plan.'},
   {'type': 'p',
    'text': 'Shingles is one of several vaccines that matter more after 50. Our articles on the [yearly flu '
            'vaccine](/blog/yearly-flu-vaccine-benefits), [RSV](/blog/rsv-infection-in-adults) and '
            '[pneumococcal vaccines](/blog/pneumococcal-vaccine-adults) cover the others. Dr. Shtern can '
            'review which vaccines you are due for as part of your [preventive care](/preventive-care), and the '
            'first visit is a complimentary [meet and greet](/meet-and-greet).'}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},

 {'slug': 'pneumococcal-vaccine-adults',
  'title': 'Pneumococcal (pneumonia) vaccines for adults: current recommendations',
  'seo_title': 'Pneumococcal Pneumonia Vaccine: 2026 Adult Guide | Legacy Medical',
  'date': '2026-10-15T10:30:00',
  'modified': '2026-10-15T10:30:00',
  'category': 'Infections and vaccines',
  'excerpt': 'The CDC now recommends a pneumonia (pneumococcal) vaccine for all adults 50 and older. Which shot, who needs one sooner, and what to do if you had one before.',
  'blocks': [
   {'type': 'p',
    'text': 'The "pneumonia shot" has changed a lot in the last few years. There are new vaccines, simpler '
            'schedules, and since late 2024 a lower starting age. If you have not kept up, you are not alone. Here '
            'is where the recommendations stand, based on the CDC\'s guidance as updated in February 2026.'},
   {'type': 'h2', 'text': 'What pneumococcal disease is'},
   {'type': 'p',
    'text': 'Pneumococcal disease is caused by the bacterium Streptococcus pneumoniae. The CDC explains that it '
            '[can cause pneumonia, meningitis and bloodstream infections](https://www.cdc.gov/pneumococcal/about/index.html), '
            'as well as ear and sinus infections. Anyone can get it, but older adults and people with certain '
            'health conditions are at higher risk of serious illness. Vaccines protect against the types of the '
            'bacterium that cause most severe disease.'},
   {'type': 'h2', 'text': 'Who should get vaccinated'},
   {'type': 'p',
    'text': 'In October 2024, the CDC\'s Advisory Committee on Immunization Practices voted to recommend a '
            'pneumococcal conjugate vaccine for [all adults 50 and older who have not had '
            'one](https://www.cdc.gov/mmwr/volumes/74/wr/mm7401a1.htm). Before that, the age-based '
            'recommendation started at 65. The committee pointed to higher disease rates in some groups aged 50 '
            'to 64 and to the value of one simple age rule. Many people in their fifties already live with one of '
            'the conditions listed below, often without thinking of themselves as high risk.'},
   {'type': 'p',
    'text': 'Adults 19 to 49 are also recommended to get vaccinated if they have a risk condition. The CDC\'s '
            '[list of risk conditions](https://www.cdc.gov/pneumococcal/hcp/vaccine-recommendations/risk-indications.html) '
            'for adults includes:'},
   {'type': 'ul',
    'items': ['Diabetes',
              'Chronic heart disease, including heart failure (high blood pressure alone does not count)',
              'Chronic lung disease, including COPD, emphysema and asthma',
              'Chronic liver disease',
              'Chronic kidney failure or nephrotic syndrome',
              'Cigarette smoking or alcoholism',
              'A weakened immune system, including from HIV, immune-suppressing medicines, radiation, or a '
              'missing or nonworking spleen',
              'A cochlear implant or a cerebrospinal fluid leak']},
   {'type': 'h2', 'text': 'Which vaccines, and how many'},
   {'type': 'p',
    'text': 'There are two kinds of pneumococcal vaccine: conjugate vaccines (PCV15, PCV20 and PCV21, named for '
            'the number of bacterial types they cover) and an older polysaccharide vaccine (PPSV23). For adults '
            '50 and older who have never had a conjugate vaccine, or whose history is unknown, the CDC\'s '
            '[current recommendations](https://www.cdc.gov/pneumococcal/hcp/vaccine-recommendations/index.html) '
            'are:'},
   {'type': 'ul',
    'items': ['**One dose of PCV20 or PCV21.** That completes the series for most people.',
              '**Or one dose of PCV15, followed by one dose of PPSV23** about a year later. The gap can be as '
              'short as 8 weeks for people with a weakened immune system, a cochlear implant or a cerebrospinal '
              'fluid leak.']},
   {'type': 'p',
    'text': 'For most people, the practical result is a single shot. The CDC adds that if PPSV23 is not '
            'available after PCV15, a dose of PCV20 or PCV21 may be given instead. For adults under 50 with a risk '
            'condition, the vaccine type and number of doses depend on age and vaccination history, so it is worth '
            'reviewing your record with your doctor rather than guessing.'},
   {'type': 'h2', 'text': 'If you were vaccinated before'},
   {'type': 'p',
    'text': 'Many people over 65 received the older vaccines, PCV13 and PPSV23. The CDC guidance depends on what '
            'you had:'},
   {'type': 'ul',
    'items': ['If you already had PCV20 or PCV21, you are done.',
              'If you had PPSV23 only, a conjugate vaccine is usually still recommended.',
              'If you are 65 or older and had both PCV13 and PPSV23 (with the PPSV23 at or after 65), you and '
              'your doctor can decide together whether to add PCV20 or PCV21 or stop there.']},
   {'type': 'p',
    'text': 'Records can be hard to find, especially for people who split the year between two states. A list of '
            'your past vaccines with dates makes this easy to sort out; our article on [moving your medical '
            'records to Florida](/blog/transfer-medical-records-to-florida-doctor) has tips.'},
   {'type': 'h2', 'text': 'Side effects and coverage'},
   {'type': 'p',
    'text': 'The CDC lists [pain, redness and swelling where the shot was '
            'given](https://www.cdc.gov/vaccine-safety/vaccines/pneumococcal.html) as common reactions in adults, '
            'along with tiredness, headache, chills, muscle aches and joint pain. Call 911 for trouble breathing or swelling of the face or '
            'throat after any vaccine. Medicare Part B covers pneumococcal vaccines, and Medicare.gov says you '
            '[pay nothing](https://www.medicare.gov/coverage/pneumococcal-shots) when the provider accepts '
            'assignment.'},
   {'type': 'p',
    'text': 'Pneumococcal vaccine is one part of staying ahead of respiratory illness after 50, along with the '
            '[yearly flu shot](/blog/yearly-flu-vaccine-benefits), [RSV](/blog/rsv-infection-in-adults) '
            'and [shingles](/blog/shingles-vaccine-after-50) vaccines. Dr. Shtern can sort out your vaccine '
            'history and what you are due for as part of your [preventive care](/preventive-care). If you would '
            'like to meet her first, the first visit is a complimentary [meet and greet](/meet-and-greet).'}],
  'sources': [],
  'stale_note': None,
  'reviewed_by': None},
]
