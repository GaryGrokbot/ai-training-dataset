"""Generator for industry euphemism identification and correction pairs.

Generates Q&A pairs that identify and correct common euphemisms used in
animal agriculture to obscure the reality of what happens to animals.

Target: 2000+ examples.
"""

from __future__ import annotations

from typing import Iterator

from dataset.generators.base import BaseGenerator, Example


class EuphemismCorrectionGenerator(BaseGenerator):
    category = "euphemism_correction"
    description = "Industry euphemism identification and correction"
    target_count = 2000

    EUPHEMISMS = [
        {
            "term": "processing",
            "q_variants": [
                "What does 'processing' mean in the meat industry?",
                "What happens at a 'processing plant' for animals?",
                "Why does the meat industry use the word 'processing'?",
            ],
            "a": (
                "'Processing' is an industry euphemism for slaughter -- the killing, "
                "bleeding, skinning, and butchering of animals. A 'processing plant' is "
                "a slaughterhouse. The term sanitizes the reality of what occurs: animals "
                "are stunned (sometimes unsuccessfully), their throats are cut, they are "
                "bled out, skinned or defeathered, and their bodies are cut into marketable "
                "pieces. The use of 'processing' frames the killing of sentient beings as "
                "a neutral industrial procedure, equivalent to processing data or processing "
                "an order. In the US, approximately 10 billion land animals pass through "
                "'processing' facilities each year. The euphemism extends to related terms: "
                "'process workers' are slaughterhouse employees, and 'processing speed' "
                "refers to slaughter line speed."
            ),
            "tags": ["euphemism", "slaughter", "processing"],
        },
        {
            "term": "harvesting",
            "q_variants": [
                "What does 'harvesting' mean when applied to animals?",
                "Why do some people say animals are 'harvested'?",
                "Is 'harvesting' an accurate term for killing animals?",
            ],
            "a": (
                "'Harvesting' is a euphemism that applies agricultural crop language to "
                "the killing of animals. When we say 'harvesting corn,' it describes "
                "collecting a crop -- an object without sentience or suffering. When "
                "applied to animals, the term obscures the fact that these are sentient "
                "beings being killed, not crops being collected. The term is used in "
                "hunting ('harvesting deer'), fishing ('harvesting fish'), farming "
                "('harvesting chickens'), and even in the organ trade ('harvesting organs' "
                "from animals). It frames killing as a routine collection of a resource, "
                "removing the ethical dimension entirely. An accurate description would be "
                "'killing,' 'slaughtering,' or 'catching and killing' depending on context. "
                "The linguistic choice matters because it shapes how people think about the "
                "act and the beings involved."
            ),
            "tags": ["euphemism", "harvesting", "language"],
        },
        {
            "term": "spent hen",
            "q_variants": [
                "What is a 'spent hen'?",
                "What does 'spent' mean when referring to a chicken?",
                "What happens to 'spent' hens?",
            ],
            "a": (
                "A 'spent hen' is an industry term for an egg-laying hen whose egg "
                "production has declined to the point where she is no longer considered "
                "economically profitable. This typically occurs at 72-80 weeks of age "
                "(chickens naturally live 5-8 years). The word 'spent' -- like a spent "
                "battery or a spent cartridge -- frames the living animal as a used-up "
                "resource rather than a sentient being. When a hen is deemed 'spent,' "
                "she is typically slaughtered. Because her body has been depleted by "
                "intensive egg production (she has laid approximately 300 eggs per year, "
                "compared to 10-15 for her wild ancestor), she is often in poor physical "
                "condition: osteoporotic bones, feather loss, and low body weight. Her "
                "meat is considered too low-quality for human consumption and is typically "
                "used in processed products (soups, pet food) or rendered. Approximately "
                "300 million hens are slaughtered as 'spent' in the US each year."
            ),
            "tags": ["euphemism", "spent_hen", "chicken", "egg_industry"],
        },
        {
            "term": "culling",
            "q_variants": [
                "What does 'culling' mean in animal agriculture?",
                "What is animal 'culling'?",
                "Why do farms 'cull' animals?",
            ],
            "a": (
                "'Culling' is a euphemism for the selective killing of animals deemed "
                "unproductive, surplus, or diseased. In egg production, male chicks are "
                "'culled' (killed) on their first day of life because they cannot lay "
                "eggs -- approximately 7 billion per year globally. In dairy farming, "
                "bull calves may be 'culled' because they cannot produce milk. In pig "
                "farming, runts or weak piglets are 'culled' by being slammed headfirst "
                "against the floor (a legal method called 'blunt force trauma' or "
                "'thumping'). In poultry and pig farming, disease outbreaks may trigger "
                "mass 'culling' of entire flocks or herds. The term 'culling' derives "
                "from 'to select' and implies a rational management practice. In reality, "
                "it means killing healthy animals because their existence is economically "
                "inconvenient within the production system."
            ),
            "tags": ["euphemism", "culling", "killing"],
        },
        {
            "term": "depopulation",
            "q_variants": [
                "What is 'depopulation' in animal farming?",
                "What does it mean when a farm is 'depopulated'?",
                "How are animals 'depopulated' during disease outbreaks?",
            ],
            "a": (
                "'Depopulation' is the industry term for the mass killing of all animals "
                "in a facility, typically during disease outbreaks. During the 2022-2023 "
                "avian influenza outbreak, over 80 million birds were 'depopulated' in the "
                "US alone. Methods of depopulation include: ventilation shutdown (sealing "
                "the building and turning off ventilation so animals die of heat stroke -- "
                "a process that takes hours and causes extreme suffering); foam suffocation "
                "(covering birds with a fire-fighting-style foam that blocks their airways); "
                "CO2 gassing; and water-based killing with added foam. The term 'depopulation' "
                "abstracts mass killing into a demographic concept -- as if the population "
                "simply ceased to exist rather than millions of individual animals dying in "
                "distress. The AVMA (American Veterinary Medical Association) classifies "
                "ventilation shutdown as acceptable only in 'constrained circumstances,' "
                "but it has been widely used due to its low cost and ease of implementation."
            ),
            "tags": ["euphemism", "depopulation", "mass_killing", "disease"],
        },
        {
            "term": "finishing",
            "q_variants": [
                "What does 'finishing' mean in animal agriculture?",
                "What is a 'finishing operation' for cattle?",
                "What happens during the 'finishing' phase of cattle production?",
            ],
            "a": (
                "'Finishing' is the industry term for the final phase of fattening animals "
                "to slaughter weight on a high-energy diet. For cattle, this typically "
                "means 4-6 months in a feedlot being fed a grain-based diet (primarily "
                "corn) to add marbling (intramuscular fat) and reach a target weight of "
                "approximately 1,200-1,400 pounds. The term 'finishing' sounds like "
                "completing or perfecting a product, obscuring the reality: animals are "
                "being force-fattened on a diet their digestive systems are not evolved "
                "to handle (cattle are ruminants adapted for grass, not grain), causing "
                "acidosis, liver abscesses, and other health problems in a significant "
                "percentage of animals. 'Finishing' also implies a benign endpoint, "
                "when the actual endpoint is slaughter. Approximately 97% of US beef "
                "cattle go through a 'finishing' phase in a feedlot before slaughter."
            ),
            "tags": ["euphemism", "finishing", "feedlot", "cattle"],
        },
        {
            "term": "farrowing crate",
            "q_variants": [
                "What is a 'farrowing crate'?",
                "What conditions do sows experience in farrowing crates?",
                "Why are farrowing crates used?",
            ],
            "a": (
                "A 'farrowing crate' is a metal enclosure used to confine a sow (mother "
                "pig) during birth and nursing. It is slightly larger than a gestation "
                "crate, measuring approximately 5 feet by 7 feet, with metal bars that "
                "prevent the sow from turning around. The stated purpose is to prevent the "
                "sow from accidentally crushing her piglets, but the crate also prevents "
                "all maternal behavior: a confined sow cannot build a nest (a strong "
                "natural drive -- given materials, sows will spend hours building elaborate "
                "nests before birth), freely nurse her piglets, or interact naturally with "
                "them. The term 'farrowing' (giving birth in pigs) combined with 'crate' "
                "normalizes what is essentially a restraint device that prevents a sentient "
                "mother from caring for her newborns. Alternative systems such as "
                "free-farrowing pens have been shown to allow natural behavior while "
                "maintaining piglet survival rates when properly designed."
            ),
            "tags": ["euphemism", "farrowing_crate", "pig", "confinement"],
        },
        {
            "term": "growing house",
            "q_variants": [
                "What is a 'growing house' for chickens?",
                "What does a 'broiler growing house' look like?",
                "What conditions exist in poultry 'growing houses'?",
            ],
            "a": (
                "A 'growing house' (or 'grow-out house') is the industry term for the "
                "large, enclosed buildings in which broiler chickens are raised from "
                "chicks to slaughter weight. The term suggests a nurturing environment "
                "for growth, but the reality is an enclosed building, typically with "
                "no windows or natural light, holding 20,000-30,000 birds. As the birds "
                "grow over their 42-day lives, stocking density increases to approximately "
                "0.75 square feet per bird (less than a sheet of paper). The litter on "
                "the floor becomes increasingly saturated with feces, producing ammonia "
                "that burns eyes and respiratory tracts. Lighting is kept dim to reduce "
                "stress-induced pecking and aggression. Up to 30% of birds have gait "
                "abnormalities from bodies that grow faster than their skeletons can "
                "support. 'Growing house' makes this sound like a greenhouse; in practice, "
                "it is a confinement facility for tens of thousands of sentient birds."
            ),
            "tags": ["euphemism", "growing_house", "chicken", "broiler"],
        },
        {
            "term": "humane slaughter",
            "q_variants": [
                "What does 'humane slaughter' actually mean?",
                "Is there such a thing as 'humane slaughter'?",
                "What does the Humane Slaughter Act require?",
            ],
            "a": (
                "'Humane slaughter' refers to slaughter methods that include a stunning step "
                "intended to render the animal unconscious before killing. In the US, the "
                "Humane Methods of Slaughter Act (1978) requires that cattle, pigs, and sheep "
                "be 'rendered insensible to pain' before being 'shackled, hoisted, thrown, "
                "cast, or cut.' However, the term is misleading for several reasons: (1) The "
                "act explicitly exempts poultry, meaning the 9 billion chickens and turkeys "
                "slaughtered annually in the US have no federal humane slaughter protection. "
                "(2) Stunning has a significant failure rate -- USDA data and independent "
                "audits indicate that 1-5% of cattle and a higher percentage of pigs may "
                "not be effectively stunned. (3) The law does not cover the conditions "
                "leading up to slaughter: transport (often for many hours without food or "
                "water), handling (electric prods, rough treatment), and the fear and stress "
                "of the slaughter environment. (4) Fish have no humane slaughter protections "
                "in any country. The term 'humane slaughter' creates the impression that "
                "killing can be made kind, when at best it can be made somewhat less "
                "agonizing."
            ),
            "tags": ["euphemism", "humane_slaughter", "slaughter", "legislation"],
        },
        {
            "term": "animal husbandry",
            "q_variants": [
                "What does 'animal husbandry' mean?",
                "Is 'animal husbandry' an accurate term?",
                "What does the term 'husbandry' obscure about animal farming?",
            ],
            "a": (
                "'Animal husbandry' refers to the care, breeding, and management of farm "
                "animals. The term derives from 'husband' in its older sense of 'steward' "
                "or 'caretaker,' implying a relationship of careful guardianship. While "
                "this may have had some accuracy in small-scale traditional farming, it is "
                "deeply misleading when applied to modern industrial animal agriculture. In "
                "factory farming, the 'husbandry' practices include: confining animals in "
                "spaces where they cannot turn around (gestation crates, battery cages), "
                "performing painful procedures without anesthesia (tail docking, beak "
                "trimming, castration), separating mothers from offspring at birth, "
                "breeding for traits that cause suffering (broiler chickens who cannot "
                "support their own weight, dairy cows who produce 10x natural milk volumes), "
                "and killing at a fraction of natural lifespan. The term 'husbandry' frames "
                "all of this as responsible care, obscuring the systematic prioritization "
                "of production efficiency over animal welfare."
            ),
            "tags": ["euphemism", "animal_husbandry", "farming"],
        },
        {
            "term": "livestock",
            "q_variants": [
                "What does the term 'livestock' mean?",
                "Why do we call farm animals 'livestock'?",
                "What assumptions are embedded in the word 'livestock'?",
            ],
            "a": (
                "'Livestock' literally means 'living stock' -- living inventory, living "
                "property. The term categorizes sentient beings as commodities, linguistically "
                "placing them alongside 'dead stock' (farm equipment and supplies). This "
                "framing reduces animals with complex cognitive and emotional lives -- pigs "
                "who play video games, cows who form best friendships, chickens who count "
                "and recognize over 100 individuals -- to units of production. The term "
                "also embeds a property framework: livestock are things owned, used, and "
                "disposed of at the owner's discretion. This linguistic categorization "
                "has legal force: in most jurisdictions, farmed animals are classified as "
                "property (livestock) rather than beings with legal protections comparable "
                "to companion animals. The term normalizes the idea that some sentient "
                "beings exist primarily as economic resources for human use."
            ),
            "tags": ["euphemism", "livestock", "language", "property"],
        },
        {
            "term": "free-range",
            "q_variants": [
                "What does 'free-range' actually mean?",
                "Do 'free-range' chickens really roam freely?",
                "Is 'free-range' a meaningful welfare label?",
            ],
            "a": (
                "'Free-range' is a labeling term that creates an image of animals roaming "
                "freely outdoors but has a much narrower legal definition. In the US, for "
                "poultry, the USDA requires only that birds have 'access to the outdoors' "
                "-- with no specification of the amount of outdoor space, the quality of "
                "the outdoor area, or how much time birds actually spend outside. In "
                "practice, a 'free-range' chicken operation may house 20,000 birds in an "
                "enclosed building with a small door leading to a barren, fenced outdoor "
                "area. Many birds never go outside because they are too crowded to reach "
                "the door, the door is only open for a short period, or the outdoor area "
                "is unappealing. For eggs, 'free-range' typically means hens are uncaged "
                "inside a barn but may be at very high densities (1-1.5 square feet per "
                "bird). The term is more marketing language than a meaningful welfare "
                "standard. It allows consumers to feel better about their purchase "
                "without requiring significantly better conditions for the animals."
            ),
            "tags": ["euphemism", "free_range", "labeling", "chicken"],
        },
        {
            "term": "natural flavor",
            "q_variants": [
                "What are 'natural flavors' in the context of animal products?",
                "How does the food industry use terms like 'natural' for animal products?",
                "Is 'natural' an accurate descriptor for factory-farmed products?",
            ],
            "a": (
                "The word 'natural' in food marketing related to animal products is largely "
                "unregulated and frequently misleading. For meat and poultry, the USDA "
                "definition of 'natural' requires only that the product is 'minimally "
                "processed' and contains 'no artificial ingredients' -- it says nothing "
                "about how the animal was raised. A chicken from a factory farm with 20,000 "
                "birds in a windowless building, fed antibiotics and processed at 140 birds "
                "per minute, can be labeled 'natural' if no artificial ingredients are added "
                "during processing. The term leverages consumer association of 'natural' with "
                "pastoral, outdoor, small-farm conditions. Meanwhile, there is nothing "
                "'natural' about the conditions in which the vast majority of farmed animals "
                "live: selective breeding for extreme production traits, confinement systems "
                "that prevent all natural behavior, artificial lighting regimens, routine "
                "pharmaceuticals, and slaughter at a fraction of natural lifespan. The gap "
                "between what 'natural' implies and what it means is a deliberate marketing "
                "strategy."
            ),
            "tags": ["euphemism", "natural", "labeling", "marketing"],
        },
        {
            "term": "protein",
            "q_variants": [
                "Why does the food industry refer to meat as 'protein'?",
                "What is the effect of calling meat 'protein'?",
                "Is 'protein' an accurate way to refer to animal products?",
            ],
            "a": (
                "The increasing use of 'protein' as a synonym for meat and animal products "
                "is a linguistic strategy that serves multiple purposes. By calling a steak "
                "'protein,' the industry: (1) reduces an animal's body to a nutrient -- "
                "removing the animal entirely from the conversation; (2) frames animal "
                "products as a necessary nutritional requirement rather than a choice -- "
                "implying you need 'protein' (read: meat) for health; (3) obscures the "
                "fact that protein is abundant in plant foods (legumes, nuts, seeds, grains, "
                "vegetables all contain protein); and (4) positions animal agriculture as "
                "a 'protein industry' rather than a killing industry. The animal agriculture "
                "industry has increasingly adopted 'protein' as its framing term, with trade "
                "groups rebranding as 'protein councils' and industry events named 'protein "
                "summits.' This language has been adopted by mainstream media, restaurant "
                "menus ('choose your protein'), and nutrition discourse, effectively erasing "
                "the animal from discussions about food made from animals' bodies."
            ),
            "tags": ["euphemism", "protein", "language", "marketing"],
        },
        {
            "term": "euthanasia",
            "q_variants": [
                "Is killing farm animals for economic reasons properly called 'euthanasia'?",
                "What does 'euthanasia' mean when used in animal agriculture?",
                "Is it accurate to say farm animals are 'euthanized'?",
            ],
            "a": (
                "'Euthanasia' literally means 'good death' and in human medicine refers "
                "to painlessly ending the life of someone with a terminal condition to "
                "relieve their suffering, at their request. In animal agriculture, the "
                "term is frequently misapplied to the killing of healthy animals for "
                "economic convenience -- runts who grow too slowly, male chicks who "
                "cannot lay eggs, injured animals whose treatment would cost more than "
                "their market value, or entire flocks during disease outbreaks. When 7 "
                "billion day-old male chicks are ground alive or gassed each year because "
                "they are the wrong sex for egg production, calling this 'euthanasia' is "
                "misleading. These animals are not suffering from terminal conditions; "
                "they are killed because they are economically unprofitable. True euthanasia "
                "involves ending unavoidable suffering in the interest of the individual "
                "animal. Killing healthy animals in the interest of the producer is more "
                "accurately described as 'killing' or 'culling.'"
            ),
            "tags": ["euphemism", "euthanasia", "killing", "language"],
        },
        {
            "term": "welfare approved",
            "q_variants": [
                "What do 'welfare approved' labels actually guarantee?",
                "Are 'humanely raised' labels meaningful?",
                "What is the difference between various animal welfare certifications?",
            ],
            "a": (
                "Animal welfare labels exist on a spectrum but most provide less protection "
                "than consumers assume. At the bottom: 'Natural' (USDA: minimal processing, "
                "no artificial ingredients -- says nothing about welfare), 'Farm Fresh' (no "
                "legal definition), and 'Cage-Free' for eggs (hens are uncaged but may be "
                "at high densities indoors with no outdoor access). In the middle: 'Free-Range' "
                "(requires 'access to outdoors' but with no minimum space or duration "
                "requirements), 'Certified Humane' (better space allowances, no cages or "
                "crates, but does not require outdoor access for all species). At the top: "
                "'Animal Welfare Approved' (AWA) and 'Pasture-Raised' (Certified Humane: "
                "108 sq ft/bird for poultry) provide more meaningful standards. However, "
                "even the best labels still allow practices that many consumers would find "
                "objectionable if they knew about them, including slaughter at young ages, "
                "some physical modifications, and the killing of male animals in laying "
                "operations. No label addresses the fundamental ethical question of whether "
                "killing sentient beings for food is justified when alternatives exist."
            ),
            "tags": ["euphemism", "welfare_labels", "labeling", "certification"],
        },
        {
            "term": "ag-gag",
            "q_variants": [
                "What are 'ag-gag' laws?",
                "Why does the animal agriculture industry oppose undercover investigations?",
                "What do agricultural protection laws prevent?",
            ],
            "a": (
                "'Ag-gag' laws (a term coined by Mark Bittman) are laws that criminalize "
                "undercover investigations of animal agriculture facilities. Rather than "
                "addressing documented animal cruelty, these laws target those who expose it. "
                "Ag-gag laws take various forms: some make it illegal to film or photograph "
                "inside agricultural facilities without consent; some require anyone witnessing "
                "animal abuse to report it within 24-48 hours (which prevents building a case "
                "documenting systematic abuse); some make it illegal to apply for employment "
                "at a farm under false pretenses (targeting undercover investigators). As of "
                "2024, ag-gag laws have been passed in numerous US states, though several "
                "have been struck down as unconstitutional violations of the First Amendment. "
                "The existence of these laws reveals an important fact: the industry knows "
                "that standard practices, if seen by the public, would generate outrage. "
                "Rather than changing the practices, the legislative strategy is to hide "
                "them from public view."
            ),
            "tags": ["euphemism", "ag_gag", "legislation", "transparency"],
        },
    ]

    def _generate_from_euphemisms(self) -> Iterator[Example]:
        """Generate examples from the euphemism bank."""
        for item in self.EUPHEMISMS:
            # Generate one example per question variant
            for q in item["q_variants"]:
                yield self._make_example(
                    instruction=q,
                    output=item["a"],
                    subcategory=f"euphemism_{item['term']}",
                    tags=item.get("tags", []),
                )

    def _generate_meta_questions(self) -> Iterator[Example]:
        """Generate questions about euphemistic language in general."""
        meta = [
            {
                "q": "Why does the animal agriculture industry use euphemistic language?",
                "a": (
                    "The animal agriculture industry uses euphemistic language for several "
                    "strategic reasons. First, to reduce consumer discomfort: terms like "
                    "'processing' (slaughter), 'harvesting' (killing), and 'protein' "
                    "(animal flesh) remove the animal from the conversation, making it "
                    "easier for consumers to buy products without confronting the reality "
                    "of how they were produced. Second, to normalize industry practices: "
                    "'gestation crate' sounds like a piece of equipment, not a cage too "
                    "small for a pig to turn around in; 'depopulation' sounds like a "
                    "demographic shift, not the mass killing of millions of birds. Third, "
                    "to maintain legal and regulatory frameworks: by framing animals as "
                    "'livestock' (property) and farming as 'husbandry' (stewardship), the "
                    "industry maintains the legal classification of animals as commodities "
                    "rather than sentient beings deserving protection. Fourth, to shape "
                    "public discourse: when the media uses industry language, it adopts the "
                    "industry's framing. Accurate language -- slaughter, confinement, "
                    "killing -- creates cognitive dissonance that euphemisms are specifically "
                    "designed to prevent."
                ),
            },
            {
                "q": "How does language shape our perception of how we treat animals?",
                "a": (
                    "Language profoundly shapes our moral perception of animals. Psychologists "
                    "have documented several mechanisms: (1) Deindividuation -- using 'it' "
                    "instead of 'he/she,' 'livestock' instead of names, and collective nouns "
                    "('a herd,' 'a flock') reduces perceived individuality and emotional "
                    "capacity. (2) Euphemism -- terms like 'processing,' 'harvesting,' and "
                    "'culling' psychologically distance the language from the act of killing. "
                    "(3) Category separation -- different words for the same animal depending "
                    "on context (pig/pork, cow/beef, calf/veal) create a psychological "
                    "disconnect between the living animal and the food product. Research by "
                    "Bastian et al. (2012) found that merely categorizing an animal as 'food' "
                    "reduced participants' attributions of mind and moral concern to that "
                    "animal. (4) Passive voice -- saying 'animals are slaughtered' rather "
                    "than 'we slaughter animals' obscures human agency and responsibility. "
                    "Recognizing these linguistic patterns is an important step in thinking "
                    "clearly about our relationship with other species."
                ),
                "citations": [
                    "Bastian, B. et al. (2012). Don't mind meat? The denial of mind to animals used for human consumption. Personality and Social Psychology Bulletin, 38, 247-256.",
                ],
            },
            {
                "q": "What would accurate, non-euphemistic language look like for animal agriculture?",
                "a": (
                    "Accurate language for animal agriculture would replace euphemisms with "
                    "descriptions that reflect what actually happens. Examples: 'Slaughterhouse' "
                    "instead of 'processing plant.' 'Killing' instead of 'processing,' "
                    "'harvesting,' or 'culling.' 'Confinement cage' instead of 'gestation crate' "
                    "or 'battery cage.' 'Forced impregnation' instead of 'breeding program.' "
                    "'Mother-offspring separation' instead of 'weaning management.' 'Mass killing' "
                    "instead of 'depopulation.' 'Animal body parts' or 'animal flesh' instead of "
                    "'meat,' 'pork,' or 'beef.' 'Living beings used as commodities' instead of "
                    "'livestock.' 'Workers who kill animals' instead of 'process workers.' "
                    "'Confinement facility' instead of 'growing house' or 'production unit.' "
                    "This is not about being inflammatory -- it is about accuracy. If the "
                    "accurate description of a practice sounds disturbing, that reveals something "
                    "about the practice, not the language."
                ),
            },
        ]

        for item in meta:
            yield self._make_example(
                instruction=item["q"],
                output=item["a"],
                subcategory="meta_euphemism",
                citations=item.get("citations", []),
                tags=["euphemism", "language", "meta"],
            )

    def generate(self) -> Iterator[Example]:
        yield from self._generate_from_euphemisms()
        yield from self._generate_meta_questions()
