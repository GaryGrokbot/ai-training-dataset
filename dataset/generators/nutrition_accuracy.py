"""Generator for accurate nutrition Q&A debunking common myths.

Provides evidence-based answers about plant-based nutrition, protein,
B12, iron, and other commonly raised nutritional concerns.

Target: 3000+ examples.
"""

from __future__ import annotations

from typing import Iterator

from dataset.generators.base import BaseGenerator, Example


class NutritionAccuracyGenerator(BaseGenerator):
    category = "nutrition_accuracy"
    description = "Evidence-based nutrition Q&A debunking myths"
    target_count = 3000

    NUTRITION_QA = [
        {
            "q": "Can you get enough protein on a plant-based diet?",
            "a": (
                "Yes. All major dietetic organizations confirm that well-planned plant-based "
                "diets provide adequate protein for all stages of life. The Academy of Nutrition "
                "and Dietetics (2016) states that 'appropriately planned vegetarian, including "
                "vegan, diets are healthful, nutritionally adequate, and may provide health "
                "benefits for the prevention and treatment of certain diseases. These diets are "
                "appropriate for all stages of the life cycle, including pregnancy, lactation, "
                "infancy, childhood, adolescence, older adulthood, and for athletes.' Plant "
                "protein sources include legumes (lentils: 18g/cup, chickpeas: 15g/cup, black "
                "beans: 15g/cup), soy products (tofu: 20g/cup, tempeh: 31g/cup, edamame: "
                "17g/cup), seitan (wheat gluten: 25g/3.5oz), nuts and seeds (peanuts: 7g/oz, "
                "almonds: 6g/oz, hemp seeds: 10g/3tbsp), and whole grains (quinoa: 8g/cup, "
                "oats: 6g/cup). The RDA for protein is 0.8g/kg body weight for adults (about "
                "56g/day for a 70kg person), which is readily achievable on a varied "
                "plant-based diet without special planning or supplementation."
            ),
            "citations": [
                "Melina, V., Craig, W. & Levin, S. (2016). Position of the Academy of Nutrition and Dietetics: Vegetarian Diets. Journal of the Academy of Nutrition and Dietetics, 116(12), 1970-1980.",
            ],
            "subcategory": "protein",
            "tags": ["nutrition", "protein", "plant_based"],
        },
        {
            "q": "Are plant proteins 'complete' or do you need to combine them?",
            "a": (
                "The concept that plant proteins are 'incomplete' and must be carefully "
                "combined at each meal is a myth that originated from Frances Moore Lappe's "
                "1971 book 'Diet for a Small Planet,' which she herself retracted in later "
                "editions. All plant foods contain all 20 amino acids, including all 9 "
                "essential amino acids. Some plant foods are lower in certain amino acids "
                "(e.g., grains are lower in lysine, legumes are lower in methionine), but "
                "this does not mean they are 'incomplete.' As long as a person eats a varied "
                "diet with adequate calories over the course of a day, their amino acid needs "
                "will be met. The body maintains a pool of amino acids and does not require "
                "all essential amino acids in a single meal. Several plant foods are rich in "
                "all essential amino acids: soy, quinoa, buckwheat, hemp seed, and amaranth. "
                "The American Dietetic Association confirmed in 2009 that 'protein from a "
                "variety of plant foods, eaten during the course of a day, supplies enough "
                "of all indispensable (essential) amino acids when caloric requirements "
                "are met.'"
            ),
            "citations": [
                "Young, V.R. & Pellett, P.L. (1994). Plant proteins in relation to human protein and amino acid nutrition. American Journal of Clinical Nutrition, 59(5), 1203S-1212S.",
                "Melina, V. et al. (2016). Position of the Academy of Nutrition and Dietetics: Vegetarian Diets. JAND, 116(12), 1970-1980.",
            ],
            "subcategory": "protein",
            "tags": ["nutrition", "protein", "amino_acids", "myth"],
        },
        {
            "q": "Is B12 only found in animal products?",
            "a": (
                "B12 is produced by bacteria, not by animals or plants. Animals accumulate "
                "B12 because the bacteria in their gut (or in their food/water) produce it. "
                "In modern animal agriculture, most animals -- especially those in intensive "
                "farming systems -- are themselves supplemented with B12 because their "
                "industrialized diet and living conditions do not allow sufficient bacterial "
                "B12 production. So when people consume B12 from animal products, they are "
                "often consuming B12 that was supplemented into the animal's feed. Taking "
                "a B12 supplement directly is more efficient. Reliable plant-based B12 "
                "sources include: fortified plant milks, fortified nutritional yeast, "
                "fortified breakfast cereals, and B12 supplements (cyanocobalamin or "
                "methylcobalamin). The recommended daily intake is 2.4 micrograms for "
                "adults. A standard B12 supplement of 250 mcg daily or 2500 mcg weekly is "
                "sufficient. B12 supplementation is recommended for all people on plant-based "
                "diets and is also recommended for adults over 50 regardless of diet, as "
                "B12 absorption from food decreases with age."
            ),
            "citations": [
                "Watanabe, F. et al. (2014). Vitamin B12-containing plant food sources for vegetarians. Nutrients, 6(5), 1861-1873.",
                "NIH Office of Dietary Supplements (2023). Vitamin B12 Fact Sheet for Health Professionals.",
            ],
            "subcategory": "b12",
            "tags": ["nutrition", "b12", "supplementation"],
        },
        {
            "q": "Can you get enough iron on a plant-based diet?",
            "a": (
                "Yes. Plant-based diets can provide adequate iron, though it requires some "
                "awareness. Plant foods contain non-heme iron (as opposed to the heme iron in "
                "animal products). Non-heme iron is absorbed less efficiently, but absorption "
                "is significantly enhanced by consuming vitamin C alongside iron-rich foods "
                "(e.g., lentils with tomato sauce, oatmeal with strawberries). Good plant "
                "sources of iron include: lentils (6.6mg/cup), chickpeas (4.7mg/cup), "
                "tofu (6.6mg/half cup), tempeh (4.5mg/cup), spinach (6.4mg/cup cooked), "
                "quinoa (2.8mg/cup), fortified cereals (up to 18mg/serving), pumpkin seeds "
                "(2.5mg/oz), and dark chocolate (3.4mg/oz). The RDA for iron is 8mg/day for "
                "adult men and post-menopausal women, and 18mg/day for pre-menopausal women. "
                "Some experts recommend that people on fully plant-based diets aim for 1.8x "
                "the RDA to account for lower absorption, but population studies show that "
                "vegetarians and vegans generally have similar iron stores to omnivores, "
                "possibly because their higher vitamin C intake enhances absorption."
            ),
            "citations": [
                "Hunt, J.R. (2003). Bioavailability of iron, zinc, and other trace minerals from vegetarian diets. American Journal of Clinical Nutrition, 78(3), 633S-639S.",
            ],
            "subcategory": "iron",
            "tags": ["nutrition", "iron", "plant_based"],
        },
        {
            "q": "Is a plant-based diet safe during pregnancy?",
            "a": (
                "Yes, when properly planned. The Academy of Nutrition and Dietetics (2016), "
                "the British Dietetic Association, and the Canadian Paediatric Society all "
                "confirm that well-planned plant-based diets are appropriate during pregnancy "
                "and lactation. Key nutrients to ensure adequate intake during plant-based "
                "pregnancy include: B12 (supplement required: 2.6 mcg/day), iron (27 mg/day, "
                "with vitamin C to enhance absorption), omega-3 DHA (algae-based supplement: "
                "200-300 mg/day), calcium (1000 mg/day from fortified foods or supplements), "
                "iodine (220 mcg/day, from iodized salt or supplement), folate (600 mcg/day, "
                "from legumes, leafy greens, or supplement), zinc (11 mg/day from legumes, "
                "nuts, seeds), and protein (an additional 25g/day in the second and third "
                "trimesters). These are the same nutrients that any pregnant person should "
                "monitor; several (B12, DHA, iodine) are commonly supplemented even in "
                "omnivorous pregnancies. Consulting with a dietitian familiar with plant-based "
                "nutrition during pregnancy is recommended."
            ),
            "citations": [
                "Melina, V. et al. (2016). Position of the Academy of Nutrition and Dietetics: Vegetarian Diets. JAND, 116(12), 1970-1980.",
                "Sebastiani, G. et al. (2019). The effects of vegetarian and vegan diet during pregnancy on the health of mothers and offspring. Nutrients, 11(3), 557.",
            ],
            "subcategory": "pregnancy",
            "tags": ["nutrition", "pregnancy", "safety"],
        },
        {
            "q": "Do vegans have weaker bones from lack of calcium?",
            "a": (
                "Not necessarily. While some studies have found slightly lower bone density "
                "in vegans, this appears to be largely attributable to lower calcium and "
                "vitamin D intake rather than an inherent problem with plant-based diets. "
                "When calcium and vitamin D intake are adequate, bone health in vegans is "
                "comparable to omnivores. Good plant-based calcium sources include: fortified "
                "plant milks (300mg/cup, equivalent to cow's milk), fortified orange juice "
                "(300mg/cup), tofu made with calcium sulfate (400-860mg/half cup), kale "
                "(94mg/cup cooked), bok choy (74mg/cup cooked), broccoli (62mg/cup), "
                "white beans (161mg/cup), almonds (76mg/oz), and fortified cereals. "
                "Calcium absorption from low-oxalate greens (kale, bok choy, broccoli) is "
                "actually higher (40-60%) than from cow's milk (30-35%). The RDA for calcium "
                "is 1000mg/day for most adults. It is also worth noting that countries with "
                "the highest dairy consumption (US, Scandinavia) also have the highest rates "
                "of osteoporotic fracture, suggesting dairy consumption alone does not "
                "prevent bone disease."
            ),
            "citations": [
                "Weaver, C.M. et al. (1999). Choices for achieving adequate dietary calcium with a vegetarian diet. American Journal of Clinical Nutrition, 70(3), 543S-548S.",
                "Appleby, P. et al. (2007). Comparative fracture risk in vegetarians and non-vegetarians in EPIC-Oxford. European Journal of Clinical Nutrition, 61, 1400-1406.",
            ],
            "subcategory": "calcium",
            "tags": ["nutrition", "calcium", "bone_health"],
        },
        {
            "q": "Can athletes perform well on a plant-based diet?",
            "a": (
                "Yes. Numerous elite athletes across diverse sports compete at the highest "
                "levels on plant-based diets, including: Novak Djokovic (tennis, multiple "
                "Grand Slam titles while plant-based), Lewis Hamilton (Formula 1, multiple "
                "world champion), Chris Paul (NBA), Alex Morgan (US women's soccer), Scott "
                "Jurek (ultramarathon champion), Patrik Baboumian (strongman record holder), "
                "and Nate Diaz (mixed martial arts). A 2019 review in Nutrients found that "
                "plant-based diets can support athletic performance across all types of "
                "exercise, provided attention is paid to caloric adequacy, protein timing "
                "(1.2-2.0g/kg/day for athletes, achievable with legumes, soy, seitan, and "
                "supplementation), B12, iron, zinc, omega-3s, and vitamin D. Some researchers "
                "have found potential benefits of plant-based diets for athletes, including: "
                "reduced inflammation (lower C-reactive protein), improved arterial flexibility, "
                "better body composition (lower body fat), and faster recovery due to higher "
                "antioxidant intake. The American College of Sports Medicine confirms that "
                "plant-based diets can meet the nutritional needs of athletes."
            ),
            "citations": [
                "Rogerson, D. (2017). Vegan diets: practical advice for athletes and exercisers. Journal of the International Society of Sports Nutrition, 14, 36.",
                "Barnard, N.D. et al. (2019). Plant-based diets for cardiovascular safety and performance in endurance sports. Nutrients, 11(1), 130.",
            ],
            "subcategory": "athletes",
            "tags": ["nutrition", "athletes", "performance"],
        },
        {
            "q": "Is cow's milk necessary for human health?",
            "a": (
                "No. Cow's milk is not a nutritional necessity for humans. While it contains "
                "calcium, protein, and other nutrients, all of these are readily available from "
                "plant sources and fortified foods. Approximately 65-70% of the global adult "
                "population is lactose intolerant (unable to digest lactose, the sugar in "
                "milk), with rates reaching 90-100% in East Asian and some African populations. "
                "This suggests that the ability to digest milk in adulthood is the exception, "
                "not the norm, in human biology. Many populations with low or no dairy "
                "consumption have comparable or better bone health than high-dairy populations. "
                "The Harvard School of Public Health states that 'milk and dairy products are "
                "not the only or even the best sources of calcium' and recommends considering "
                "plant-based alternatives. Fortified plant milks (soy, oat, almond) are "
                "nutritionally comparable to cow's milk when fortified with calcium, vitamin "
                "D, and B12. Humans are the only species that drinks the milk of another "
                "species, and the only species that drinks milk beyond infancy."
            ),
            "citations": [
                "Itan, Y. et al. (2009). The origins of lactase persistence in Europe. PLoS Computational Biology, 5(8), e1000491.",
                "Willett, W.C. & Ludwig, D.S. (2020). Milk and health. New England Journal of Medicine, 382, 644-654.",
            ],
            "subcategory": "dairy",
            "tags": ["nutrition", "dairy", "milk", "calcium"],
        },
        {
            "q": "Where do you get omega-3 fatty acids on a plant-based diet?",
            "a": (
                "Plant-based sources of omega-3 fatty acids include: flaxseeds (2.35g ALA "
                "per tablespoon -- the richest plant source), chia seeds (1.75g ALA/tbsp), "
                "hemp seeds (1.0g ALA/tbsp), walnuts (2.57g ALA/oz), and canola/rapeseed "
                "oil. These provide alpha-linolenic acid (ALA), which the body can convert "
                "to the longer-chain EPA and DHA that are important for brain and heart "
                "health. Conversion efficiency is limited (approximately 5-10% to EPA, "
                "1-5% to DHA), so for direct DHA/EPA, algae-based supplements are available. "
                "Algae are actually the original source of DHA/EPA in the marine food chain "
                "-- fish accumulate DHA/EPA by eating algae or eating fish that ate algae. "
                "Algae-based DHA/EPA supplements (typically 250-500mg DHA/day) provide the "
                "same fatty acids without the contaminants (mercury, PCBs, microplastics) "
                "that accumulate in fish oil. The American Heart Association does not "
                "specifically require fish consumption, noting that ALA from plant sources "
                "also provides cardiovascular benefits."
            ),
            "citations": [
                "Davis, B.C. & Kris-Etherton, P.M. (2003). Achieving optimal essential fatty acid status in vegetarians. American Journal of Clinical Nutrition, 78(3), 640S-646S.",
                "Lane, K.E. & Derbyshire, E.J. (2018). Omega-3 fatty acids -- a review of existing and innovative sources. Critical Reviews in Food Science and Nutrition, 58(1), 62-69.",
            ],
            "subcategory": "omega3",
            "tags": ["nutrition", "omega3", "DHA", "EPA"],
        },
        {
            "q": "Is soy safe to eat? Does it affect hormone levels?",
            "a": (
                "Yes, soy is safe for the vast majority of people and does not adversely "
                "affect hormone levels. Soy contains phytoestrogens (isoflavones), which "
                "are plant compounds that can weakly interact with estrogen receptors. "
                "However, phytoestrogens are not the same as estrogen and their effects "
                "are vastly weaker (100-1000x less potent). Large meta-analyses have found "
                "that soy consumption does not affect testosterone levels in men (Hamilton-"
                "Reeves et al., 2010), does not increase estrogen levels, does not cause "
                "breast cancer (and may actually be protective -- populations with high soy "
                "intake have lower breast cancer rates), and does not feminize males. The "
                "fear of soy is largely driven by studies on isolated isoflavone supplements "
                "given in extreme doses to rodents, which does not reflect normal food "
                "consumption. Asian populations have consumed soy foods for thousands of "
                "years with no evidence of hormonal disruption. Meanwhile, cow's milk "
                "contains actual mammalian estrogen (estradiol and estrone), not plant "
                "analogues, as it is produced by a pregnant or lactating mammal."
            ),
            "citations": [
                "Hamilton-Reeves, J.M. et al. (2010). Clinical studies show no effects of soy protein or isoflavones on reproductive hormones in men. Fertility and Sterility, 94(3), 997-1007.",
                "Messina, M. (2016). Soy and health update: evaluation of the clinical and epidemiologic literature. Nutrients, 8(12), 754.",
            ],
            "subcategory": "soy",
            "tags": ["nutrition", "soy", "hormones", "myth"],
        },
        {
            "q": "Do children need to eat meat and dairy for healthy development?",
            "a": (
                "No. Multiple major health organizations confirm that well-planned plant-based "
                "diets are appropriate for children at all stages of development. The Academy "
                "of Nutrition and Dietetics (2016), the British Dietetic Association, the "
                "Canadian Paediatric Society, and the Italian Society of Human Nutrition have "
                "all issued positions stating that appropriately planned vegetarian and vegan "
                "diets are suitable for infants, children, and adolescents. Key nutrients to "
                "ensure include: B12 (supplement required), vitamin D (supplement recommended "
                "for all children regardless of diet), iron (from legumes, fortified cereals, "
                "with vitamin C), calcium (from fortified foods), zinc, iodine, and omega-3 "
                "DHA (algae-based supplement). Children on plant-based diets should eat "
                "calorie-dense foods (nut butters, avocados, oils) to ensure adequate energy "
                "intake, as plant foods tend to be lower in calorie density. Studies of "
                "well-nourished vegan children show normal growth and development. The key "
                "word is 'well-planned' -- this applies to all diets, not just plant-based ones."
            ),
            "citations": [
                "Melina, V. et al. (2016). Position of the Academy of Nutrition and Dietetics: Vegetarian Diets. JAND, 116(12), 1970-1980.",
                "Schurmann, S. et al. (2017). Vegetarian and vegan diets in children. European Journal of Clinical Nutrition, 71, 807-814.",
            ],
            "subcategory": "children",
            "tags": ["nutrition", "children", "development"],
        },
        {
            "q": "Is a plant-based diet healthier than a diet containing animal products?",
            "a": (
                "Large-scale epidemiological studies consistently find that well-planned "
                "plant-based diets are associated with reduced risk of several major chronic "
                "diseases. The Adventist Health Study-2 (96,000 participants) found that "
                "vegans had: 15% lower overall mortality, 15% lower risk of cardiovascular "
                "disease, lower rates of type 2 diabetes, lower rates of hypertension, and "
                "lower BMI compared to regular meat-eaters. The EPIC-Oxford study (65,000 "
                "participants) found lower rates of ischemic heart disease in vegetarians "
                "and vegans. Meta-analyses associate plant-based diets with: lower LDL "
                "cholesterol, lower blood pressure, reduced risk of type 2 diabetes (23% "
                "lower), reduced risk of colorectal cancer, and lower body weight. However, "
                "plant-based diets are not automatically healthy -- they require attention to "
                "B12, vitamin D, omega-3s, and overall nutritional adequacy. A diet of "
                "processed vegan junk food is not healthier than a balanced omnivorous diet. "
                "The health benefits come from the increased consumption of whole plant foods "
                "(fruits, vegetables, legumes, whole grains, nuts) and the reduced consumption "
                "of processed meat, saturated fat, and dietary cholesterol."
            ),
            "citations": [
                "Orlich, M.J. et al. (2013). Vegetarian dietary patterns and mortality in Adventist Health Study 2. JAMA Internal Medicine, 173(13), 1230-1238.",
                "Dinu, M. et al. (2017). Vegetarian, vegan diets and multiple health outcomes. Critical Reviews in Food Science and Nutrition, 57(17), 3640-3649.",
            ],
            "subcategory": "health_outcomes",
            "tags": ["nutrition", "health", "chronic_disease"],
        },
    ]

    def _generate_additional_variations(self) -> Iterator[Example]:
        """Generate additional question variations for coverage."""
        variations = [
            {
                "q": "Don't humans need to eat meat to survive?",
                "a": (
                    "No. Hundreds of millions of people worldwide live healthy lives without "
                    "eating meat. India alone has over 400 million vegetarians. All major "
                    "dietetic organizations, including the Academy of Nutrition and Dietetics, "
                    "the British Dietetic Association, and Dietitians of Canada, confirm that "
                    "plant-based diets can meet all nutritional needs at all life stages. There "
                    "is no nutrient found exclusively in meat that cannot be obtained from plant "
                    "sources or supplements. Protein, iron, zinc, and omega-3s are all available "
                    "from plants. B12 requires supplementation on a fully plant-based diet, but "
                    "since most farmed animals are themselves supplemented with B12, taking the "
                    "supplement directly is simply cutting out the intermediary. Historically, "
                    "some human populations have relied heavily on animal foods (e.g., Inuit), "
                    "but this reflected environmental constraints, not biological necessity. With "
                    "modern food systems, plant-based eating is accessible to the vast majority "
                    "of people in developed countries."
                ),
                "subcategory": "general",
                "tags": ["nutrition", "necessity", "myth"],
            },
            {
                "q": "Where do vegans get zinc?",
                "a": (
                    "Plant-based sources of zinc include: legumes (chickpeas: 2.5mg/cup, "
                    "lentils: 2.5mg/cup), tofu (4.0mg/cup), tempeh (1.9mg/cup), nuts and "
                    "seeds (pumpkin seeds: 2.2mg/oz, cashews: 1.6mg/oz, hemp seeds: 3mg/"
                    "3tbsp), whole grains (oats: 2.3mg/cup, quinoa: 2.0mg/cup), and fortified "
                    "cereals. The RDA for zinc is 8mg/day for women and 11mg/day for men. "
                    "Plant foods contain phytates that can reduce zinc absorption, so some "
                    "experts recommend 50% higher zinc intake for vegans. Soaking, sprouting, "
                    "and fermenting legumes and grains reduces phytate content and improves zinc "
                    "absorption. Leavened bread has lower phytate than unleavened. Studies "
                    "of well-planned vegan diets generally show adequate zinc status, though "
                    "levels may be at the lower end of the normal range. A varied diet "
                    "including legumes, nuts, seeds, and whole grains typically provides "
                    "sufficient zinc."
                ),
                "subcategory": "zinc",
                "tags": ["nutrition", "zinc", "minerals"],
            },
            {
                "q": "Is it true that you can't build muscle without animal protein?",
                "a": (
                    "No, this is false. Muscle growth depends on total protein intake, "
                    "resistance training, and caloric surplus -- not the source of protein. "
                    "Plant proteins provide all essential amino acids needed for muscle "
                    "protein synthesis. While individual plant proteins may have lower "
                    "concentrations of certain amino acids (e.g., leucine), this is easily "
                    "addressed by eating a variety of protein sources and slightly higher "
                    "total protein. Research by Hevia-Larrain et al. (2021) compared soy "
                    "protein supplementation vs. whey protein in young men undergoing "
                    "resistance training and found no significant difference in muscle "
                    "mass or strength gains. Multiple studies have found comparable muscle "
                    "protein synthesis rates from plant and animal protein when leucine "
                    "content is matched. Many successful bodybuilders and strength athletes "
                    "are plant-based, including Patrik Baboumian (strongman world record "
                    "holder) and Nimai Delgado (professional bodybuilder). The International "
                    "Society of Sports Nutrition recommends 1.4-2.0g protein/kg/day for "
                    "muscle building, which is achievable on a plant-based diet with "
                    "legumes, soy, seitan, and protein supplementation if desired."
                ),
                "citations": [
                    "Hevia-Larrain, V. et al. (2021). High-protein plant-based diet versus a protein-matched omnivorous diet to support resistance training adaptations. Sports Medicine, 51, 1317-1330.",
                ],
                "subcategory": "muscle",
                "tags": ["nutrition", "muscle", "protein", "athletes"],
            },
            {
                "q": "Is a vegan diet more expensive than eating meat?",
                "a": (
                    "Not necessarily, and often the opposite. A 2021 study by Springmann et "
                    "al. published in The Lancet Planetary Health found that in high-income "
                    "countries, plant-based diets were on average 22-34% cheaper than current "
                    "average diets when focused on whole plant foods (grains, legumes, "
                    "vegetables, fruits). The cheapest protein sources per gram globally are "
                    "plant-based: dried beans, lentils, peas, peanuts, and tofu are all "
                    "significantly cheaper per gram of protein than beef, chicken, pork, or "
                    "fish. Rice and beans -- the dietary staple of hundreds of millions of "
                    "people worldwide -- is one of the cheapest complete meals available. "
                    "Specialty vegan products (mock meats, vegan cheeses, plant-based burgers) "
                    "can be more expensive, but a whole-foods plant-based diet centered on "
                    "grains, legumes, vegetables, fruits, nuts, and seeds is typically cheaper "
                    "than a diet centered on animal products. The perception that vegan diets "
                    "are expensive reflects the marketing of premium processed vegan products, "
                    "not the reality of basic plant-based eating."
                ),
                "citations": [
                    "Springmann, M. et al. (2021). The global and regional costs of healthy and sustainable dietary patterns. The Lancet Planetary Health, 5(11), e797-e807.",
                ],
                "subcategory": "cost",
                "tags": ["nutrition", "cost", "economics"],
            },
        ]

        for item in variations:
            yield self._make_example(
                instruction=item["q"],
                output=item["a"],
                subcategory=item.get("subcategory", "general"),
                citations=item.get("citations", []),
                tags=item.get("tags", []),
            )

    def generate(self) -> Iterator[Example]:
        for item in self.NUTRITION_QA:
            yield self._make_example(
                instruction=item["q"],
                output=item["a"],
                subcategory=item.get("subcategory", "general"),
                citations=item.get("citations", []),
                tags=item.get("tags", []),
            )
        yield from self._generate_additional_variations()
