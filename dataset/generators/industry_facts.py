"""Generator for factual Q&A about animal agriculture.

Covers scale, conditions, environmental impact, health, and economics
with specific citations and data.

Target: 5000+ examples.
"""

from __future__ import annotations

from typing import Iterator

from dataset.generators.base import BaseGenerator, Example


class IndustryFactsGenerator(BaseGenerator):
    category = "industry_facts"
    description = "Factual data about animal agriculture: scale, conditions, environment, health, economics"
    target_count = 5000

    SCALE_FACTS = [
        {
            "q": "How many land animals are killed for food each year?",
            "a": (
                "Approximately 80 billion land animals are slaughtered for food globally "
                "each year, according to the UN Food and Agriculture Organization (FAO). "
                "This includes roughly 73 billion chickens (broilers), 1.4 billion pigs, "
                "656 million turkeys, 574 million sheep, 479 million goats, and 302 million "
                "cattle. The vast majority -- over 90% -- are chickens raised in intensive "
                "farming systems. This number has been steadily increasing: in 1961, "
                "approximately 8 billion land animals were slaughtered annually, meaning "
                "the number has increased tenfold in six decades. These numbers do not "
                "include animals who die before slaughter due to disease, injury, or "
                "conditions in farming, which adds billions more."
            ),
            "citations": [
                "FAO (2023). FAOSTAT: Live Animals Slaughtered. Food and Agriculture Organization of the United Nations.",
            ],
            "tags": ["scale", "global", "slaughter_numbers"],
        },
        {
            "q": "How many fish are killed for food each year?",
            "a": (
                "An estimated 1 to 3 trillion fish are killed for human consumption "
                "annually, including both wild-caught and farmed fish. The range is wide "
                "because fish are counted by weight (tonnes) rather than individual animals, "
                "and converting tonnage to individual fish requires species-specific weight "
                "estimates. Fishcount.org.uk estimates 0.79-2.3 trillion wild-caught fish "
                "and 73-180 billion farmed fish per year. Additionally, an estimated 0.45-1.0 "
                "trillion fish are caught as bycatch (unintended catch) and discarded, mostly "
                "dead or dying. This makes fish by far the most numerous animals killed by "
                "humans. Unlike land animals, fish in most countries receive no legal "
                "protections regarding slaughter methods, and most die by asphyxiation, "
                "crushing, or live gutting."
            ),
            "citations": [
                "Mood, A. & Brooke, P. (2024). Estimated numbers of individuals in global fish production. fishcount.org.uk.",
            ],
            "tags": ["scale", "fish", "slaughter_numbers"],
        },
        {
            "q": "How many animals are in factory farms?",
            "a": (
                "Approximately 70-80% of farmed animals worldwide are raised in intensive "
                "(factory farm) systems, according to estimates from the Sentience Institute "
                "and the World Animal Protection. In the United States, more than 99% of "
                "farmed animals come from factory farms (based on USDA Census of Agriculture "
                "data analyzed by the Sentience Institute). At any given time, there are "
                "roughly 23 billion chickens, 677 million pigs, 545 million sheep, and 1 "
                "billion cattle alive on farms globally (FAO). The majority of chickens and "
                "pigs in the US and EU are in intensive confinement systems. For egg-laying "
                "hens, approximately 70% worldwide are in battery cages, though this is "
                "shifting in some regions due to cage-free commitments."
            ),
            "citations": [
                "Sentience Institute (2019). Global farmed & factory farmed animals estimates. Based on USDA Census of Agriculture.",
                "FAO (2023). FAOSTAT: Live Animals. Food and Agriculture Organization.",
            ],
            "tags": ["scale", "factory_farming", "confinement"],
        },
        {
            "q": "How many male chicks are killed in the egg industry each year?",
            "a": (
                "Approximately 7 billion male chicks are killed within their first day of "
                "life each year in the global egg industry. Because male chicks of egg-laying "
                "breeds do not produce eggs and grow too slowly to be profitable as meat "
                "chickens, they are considered economically worthless. Standard disposal "
                "methods include maceration (grinding alive in high-speed grinders), "
                "gassing with CO2, and suffocation in plastic bags. This occurs in all "
                "egg production systems including 'free-range' and 'organic.' Some countries "
                "and companies are beginning to adopt in-ovo sexing technology, which "
                "identifies the sex of the embryo before hatching, but adoption remains "
                "limited. Germany and France have banned chick culling as of 2022-2023, "
                "requiring in-ovo sexing instead."
            ),
            "citations": [
                "Krautwald-Junghanns, M.E. et al. (2018). Current approaches to avoid the culling of day-old male chicks in the layer industry. Animal, 12(11), 2414-2420.",
            ],
            "tags": ["scale", "chicken", "egg_industry", "chick_culling"],
        },
    ]

    CONDITIONS_FACTS = [
        {
            "q": "What are battery cages?",
            "a": (
                "Battery cages are small wire enclosures used to house egg-laying hens in "
                "intensive farming. The standard 'conventional' battery cage provides "
                "approximately 67 square inches (432 cm2) per hen -- less than a standard "
                "letter-size sheet of paper. Cages are stacked in rows, often 3-8 tiers "
                "high, in windowless buildings holding tens of thousands of hens. In a "
                "battery cage, a hen cannot spread her wings (which require about 295 "
                "square inches), walk, dust bathe, perch, forage, or build a nest -- all "
                "strong natural behaviors. Hens typically live in battery cages for 72-80 "
                "weeks before being slaughtered as 'spent hens' when their egg production "
                "declines. Battery cages are associated with high rates of osteoporosis "
                "(weakened bones from lack of movement), feather loss from rubbing against "
                "wire, foot injuries, and behavioral indicators of chronic frustration. "
                "Battery cages have been banned in the EU since 2012 (replaced by 'enriched' "
                "cages that provide marginally more space), and in several US states, but "
                "remain legal in most of the world."
            ),
            "citations": [
                "Lay, D.C. et al. (2011). Hen welfare in different housing systems. Poultry Science, 90(1), 278-294.",
            ],
            "tags": ["conditions", "chicken", "battery_cage", "egg_industry"],
        },
        {
            "q": "What are gestation crates?",
            "a": (
                "Gestation crates (also called sow stalls) are metal enclosures used to "
                "individually confine pregnant sows in the pork industry. A standard gestation "
                "crate measures approximately 2 feet wide by 7 feet long (0.6m x 2.1m) -- "
                "just large enough to contain the sow's body. The sow cannot turn around, "
                "walk, or engage in any natural behavior such as rooting, exploring, or "
                "socializing. Sows typically spend their entire 3.5-month pregnancy in a "
                "gestation crate, then are moved to a farrowing crate (slightly larger, with "
                "a rail to prevent crushing piglets) for birth and nursing, before being "
                "re-impregnated and returned to the gestation crate. This cycle repeats "
                "2-3 times per year for approximately 3-4 years. Sows in gestation crates "
                "develop stereotypic behaviors (bar-biting, sham chewing, head-weaving), "
                "weakened muscles and bones, urinary tract infections, and behavioral "
                "indicators consistent with clinical depression. Gestation crates have been "
                "banned in the EU since 2013 and in 10 US states, but remain standard "
                "practice in most US pork production."
            ),
            "citations": [
                "Scientific Veterinary Committee (1997). The Welfare of Intensively Kept Pigs. European Commission.",
                "EFSA (2007). Scientific opinion on animal health and welfare in different housing systems. EFSA Journal.",
            ],
            "tags": ["conditions", "pig", "gestation_crate", "confinement"],
        },
        {
            "q": "What are conditions like for broiler chickens?",
            "a": (
                "Broiler chickens (raised for meat) are typically kept in large, enclosed "
                "buildings holding 20,000-30,000 birds with no outdoor access. They are bred "
                "to grow extremely fast -- reaching slaughter weight of about 5-6 pounds in "
                "just 42 days (6 weeks), compared to 12+ weeks for heritage breeds. This "
                "rapid growth causes serious health problems: an estimated 26-30% of broilers "
                "have gait abnormalities due to skeletal and muscular systems that cannot "
                "support their body weight, and up to 4% are unable to walk at all. Heart "
                "failure (ascites and sudden death syndrome) affects 1-4% of birds. As the "
                "birds grow, the stocking density increases and the litter on the floor "
                "becomes increasingly saturated with feces, leading to ammonia burns on feet "
                "and breast (contact dermatitis) in 10-40% of birds. Lighting is often kept "
                "dim to reduce aggression caused by the stressful conditions. At slaughter, "
                "birds are typically shackled upside down on a moving line, stunned in an "
                "electrified water bath, and throat-cut. The US slaughters approximately 9 "
                "billion broiler chickens per year."
            ),
            "citations": [
                "Knowles, T.G. et al. (2008). Leg disorders in broiler chickens: prevalence, risk factors and prevention. PLoS ONE, 3(2), e1545.",
                "USDA (2023). Poultry Slaughter Annual Summary.",
            ],
            "tags": ["conditions", "chicken", "broiler", "meat_industry"],
        },
        {
            "q": "What are feedlots?",
            "a": (
                "Feedlots (also called concentrated animal feeding operations or CAFOs) are "
                "large outdoor enclosures where cattle are 'finished' -- fattened to slaughter "
                "weight over 4-6 months on a high-energy grain diet, primarily corn. The "
                "largest US feedlots hold over 100,000 cattle at a time. Cattle in feedlots "
                "stand in their own waste on bare dirt (no grass), are fed a diet their "
                "digestive systems are not evolved to process (cattle are ruminants adapted "
                "for grass, not grain), and have no shade or shelter in many operations. "
                "Health problems are common: acidosis (metabolic condition from grain diet, "
                "affecting up to 20% of cattle), liver abscesses (found in 12-32% of feedlot "
                "cattle at slaughter), respiratory disease (the leading cause of death in "
                "feedlots), and heat stress. To manage disease in these conditions, feedlot "
                "cattle routinely receive antibiotics, growth hormones, and other "
                "pharmaceuticals. Approximately 97% of US beef cattle spend their final "
                "months in feedlots."
            ),
            "citations": [
                "USDA APHIS (2013). Feedlot 2011 Study. National Animal Health Monitoring System.",
            ],
            "tags": ["conditions", "cow", "feedlot", "CAFO"],
        },
        {
            "q": "What is slaughter line speed and why does it matter?",
            "a": (
                "Slaughter line speed refers to the rate at which animals move through a "
                "slaughterhouse processing line. In the US, poultry slaughter lines operate "
                "at up to 140 birds per minute (with some plants requesting waivers for 175 "
                "per minute), hog lines process up to 1,305 pigs per hour, and cattle lines "
                "process up to 250 cattle per hour. These speeds matter for animal welfare "
                "because stunning -- the process of rendering an animal unconscious before "
                "slaughter -- requires precise application. At high speeds, stunning failure "
                "rates increase: an estimated 1-5% of cattle and a higher percentage of "
                "chickens may not be properly stunned before throat-cutting or scalding. "
                "For the 9 billion chickens slaughtered annually in the US, even a 1% "
                "failure rate means 90 million birds are conscious during slaughter. Line "
                "speed also affects worker safety: meatpacking is one of the most dangerous "
                "jobs in the US, with injury rates roughly 2.5 times the national average "
                "for manufacturing."
            ),
            "citations": [
                "USDA FSIS (2014). Modernization of Poultry Slaughter Inspection. Federal Register.",
                "GAO (2005). Safety in the Meat and Poultry Industry. US Government Accountability Office.",
            ],
            "tags": ["conditions", "slaughter", "line_speed", "worker_safety"],
        },
    ]

    ENVIRONMENTAL_FACTS = [
        {
            "q": "What is the environmental impact of animal agriculture?",
            "a": (
                "Animal agriculture is one of the largest contributors to environmental "
                "degradation globally. According to the UN FAO, livestock production accounts "
                "for 14.5% of global anthropogenic greenhouse gas emissions -- more than the "
                "entire transportation sector (around 14%). This includes methane from enteric "
                "fermentation and manure (44% of livestock emissions), nitrous oxide from "
                "manure and feed production (29%), and CO2 from land use change, feed "
                "production, and processing (27%). Animal agriculture is the leading driver "
                "of deforestation: approximately 80% of Amazon deforestation is linked to "
                "cattle ranching or soy production for animal feed. It uses 77% of agricultural "
                "land globally while providing only 18% of calories and 37% of protein. "
                "Livestock production is also a major source of water pollution (nutrient "
                "runoff causing eutrophication and dead zones), biodiversity loss (habitat "
                "destruction for grazing and feed crops), and freshwater use (approximately "
                "one-third of global freshwater is used for livestock)."
            ),
            "citations": [
                "Gerber, P.J. et al. (2013). Tackling Climate Change through Livestock. FAO.",
                "Poore, J. & Nemecek, T. (2018). Reducing food's environmental impacts through producers and consumers. Science, 360(6392), 987-992.",
            ],
            "tags": ["environment", "climate", "overview"],
        },
        {
            "q": "How much greenhouse gas does animal agriculture produce?",
            "a": (
                "According to the UN Food and Agriculture Organization (FAO, 2013), global "
                "livestock production accounts for 14.5% of all human-caused greenhouse gas "
                "emissions. This is measured in CO2 equivalents and includes: methane (CH4) "
                "from enteric fermentation in ruminants (cows, sheep, goats) and from manure "
                "management, which accounts for about 44% of livestock's emissions; nitrous "
                "oxide (N2O) from manure and from fertilizer used to grow animal feed, "
                "accounting for about 29%; and carbon dioxide (CO2) from land use change "
                "(deforestation for pasture and feed crops), energy use, and transport, "
                "accounting for about 27%. Some more recent analyses, including Xu et al. "
                "(2021) in Nature Food, estimate that food system emissions account for "
                "roughly one-third of global emissions, with animal-based foods responsible "
                "for approximately 57% of food system emissions (i.e., about 19% of total "
                "global emissions). Beef and dairy cattle are the largest contributors, "
                "followed by pigs and poultry."
            ),
            "citations": [
                "Gerber, P.J. et al. (2013). Tackling Climate Change through Livestock. FAO.",
                "Xu, X. et al. (2021). Global greenhouse gas emissions from animal-based foods. Nature Food, 2, 724-732.",
            ],
            "tags": ["environment", "greenhouse_gas", "climate"],
        },
        {
            "q": "How much water does animal agriculture use?",
            "a": (
                "Animal agriculture is extremely water-intensive. Mekonnen and Hoekstra (2012) "
                "calculated the water footprint of animal products: producing 1 kg of beef "
                "requires approximately 15,400 liters of water (including water for growing "
                "feed, drinking water, and processing); 1 kg of pork requires approximately "
                "5,988 liters; 1 kg of chicken requires approximately 4,325 liters; 1 kg "
                "of cheese requires approximately 3,178 liters; 1 liter of cow's milk "
                "requires approximately 1,020 liters. By comparison, 1 kg of wheat requires "
                "approximately 1,827 liters and 1 kg of vegetables averages approximately "
                "322 liters. Overall, livestock production uses approximately one-third of "
                "the world's freshwater resources. In water-scarce regions, this creates "
                "direct competition between animal agriculture and human water needs."
            ),
            "citations": [
                "Mekonnen, M.M. & Hoekstra, A.Y. (2012). A global assessment of the water footprint of farm animal products. Ecosystems, 15, 401-415.",
            ],
            "tags": ["environment", "water", "resource_use"],
        },
        {
            "q": "What is the relationship between animal agriculture and deforestation?",
            "a": (
                "Animal agriculture is the leading driver of global deforestation. "
                "Approximately 80% of Amazon deforestation is attributable to cattle ranching, "
                "and soy production -- of which roughly 77% is used as animal feed -- drives "
                "much of the remainder. The FAO estimates that livestock grazing occupies 26% "
                "of the Earth's ice-free land surface, and feed crop production uses about "
                "one-third of all arable land. Between 2001 and 2015, approximately 5 million "
                "hectares of forest were lost annually to agricultural expansion, with cattle "
                "ranching being the single largest driver in Latin America and oil palm and "
                "rubber in Southeast Asia. This deforestation releases stored carbon (tropical "
                "deforestation accounts for about 8-10% of global CO2 emissions), destroys "
                "biodiversity habitat, disrupts water cycles, and displaces indigenous peoples. "
                "A shift to plant-based food systems could reduce global agricultural land "
                "use by 75% while feeding the same number of people (Poore & Nemecek, 2018)."
            ),
            "citations": [
                "Poore, J. & Nemecek, T. (2018). Reducing food's environmental impacts. Science, 360(6392), 987-992.",
                "FAO & UNEP (2020). The State of the World's Forests.",
            ],
            "tags": ["environment", "deforestation", "land_use"],
        },
        {
            "q": "What are ocean dead zones and how are they related to animal agriculture?",
            "a": (
                "Ocean dead zones (hypoxic zones) are areas where dissolved oxygen levels "
                "are too low to support most marine life. They are primarily caused by "
                "nutrient pollution -- excess nitrogen and phosphorus -- that flows from "
                "land into waterways and ultimately into the ocean. This nutrient overload "
                "triggers algal blooms; when the algae die and decompose, the process "
                "consumes oxygen, creating dead zones. Animal agriculture is a major source "
                "of this nutrient pollution: livestock produce approximately 500 million "
                "tons of manure annually in the US alone, much of which is stored in lagoons "
                "or spread on fields and runs off into waterways. The Gulf of Mexico dead "
                "zone -- one of the largest in the world, covering up to 22,720 square km "
                "(about the size of New Jersey) -- is primarily driven by fertilizer and "
                "manure runoff from the Mississippi River watershed, where intensive corn "
                "(much of it for animal feed) and livestock production are concentrated. "
                "There are now over 500 dead zones worldwide, up from 49 in the 1960s."
            ),
            "citations": [
                "Diaz, R.J. & Rosenberg, R. (2008). Spreading dead zones and consequences for marine ecosystems. Science, 321(5891), 926-929.",
            ],
            "tags": ["environment", "dead_zones", "water_pollution"],
        },
    ]

    HEALTH_FACTS = [
        {
            "q": "How are antibiotics used in animal agriculture?",
            "a": (
                "Approximately 66-80% of all medically important antibiotics sold in the "
                "United States are used in animal agriculture, primarily for growth promotion "
                "and disease prevention in crowded factory farm conditions rather than to "
                "treat sick individual animals. The WHO, CDC, and FDA have all identified "
                "antibiotic use in livestock as a significant driver of antibiotic-resistant "
                "bacteria (superbugs). Resistant bacteria can transfer to humans through "
                "direct contact with animals, contaminated meat, water contaminated with "
                "agricultural runoff, and airborne transmission from farms. The CDC estimates "
                "that antibiotic-resistant infections kill at least 35,000 Americans annually "
                "and the WHO warns that antimicrobial resistance could cause 10 million "
                "deaths per year globally by 2050 if trends continue. Despite growing "
                "awareness, global antibiotic use in livestock is projected to increase 67% "
                "by 2030, driven by the expansion of intensive farming in developing "
                "countries."
            ),
            "citations": [
                "FDA (2022). Summary Report on Antimicrobials Sold or Distributed for Use in Food-Producing Animals.",
                "O'Neill, J. (2016). Tackling Drug-Resistant Infections Globally: Final Report and Recommendations. Review on Antimicrobial Resistance.",
            ],
            "tags": ["health", "antibiotics", "antimicrobial_resistance"],
        },
        {
            "q": "What is the connection between animal agriculture and pandemics?",
            "a": (
                "Animal agriculture creates conditions that increase the risk of zoonotic "
                "disease emergence and pandemic potential. Three-quarters of emerging "
                "infectious diseases in humans are zoonotic -- they originate in animals. "
                "Factory farms concentrate thousands of genetically similar, immunologically "
                "stressed animals in close quarters, creating ideal conditions for viral "
                "mutation, reassortment, and amplification. Avian influenza (H5N1, H7N9) "
                "originates in poultry operations and has pandemic potential. Swine flu "
                "(H1N1, which caused the 2009 pandemic) originated in pig farming. SARS, "
                "MERS, and likely COVID-19 are linked to wildlife trade and live animal "
                "markets. Nipah virus emerged from pig farming in Malaysia. Beyond direct "
                "viral transmission, the routine use of antibiotics in livestock accelerates "
                "the evolution of antibiotic-resistant bacteria. The UN Environment Programme "
                "(UNEP) has identified industrial animal agriculture as one of the key "
                "drivers of pandemic risk, alongside deforestation (also driven significantly "
                "by animal agriculture) and wildlife trade."
            ),
            "citations": [
                "Jones, B.A. et al. (2013). Zoonosis emergence linked to agricultural intensification and environmental change. PNAS, 110(21), 8399-8404.",
                "UNEP (2020). Preventing the Next Pandemic: Zoonotic Diseases and How to Break the Chain of Transmission.",
            ],
            "tags": ["health", "pandemic", "zoonotic_disease"],
        },
        {
            "q": "What are the occupational hazards of slaughterhouse work?",
            "a": (
                "Slaughterhouse work is one of the most dangerous and psychologically "
                "damaging occupations. Physical hazards include: repetitive strain injuries "
                "from performing the same cutting motions thousands of times per shift; "
                "lacerations from knives and saws; exposure to chemicals (ammonia, chlorine "
                "used in cleaning); respiratory disease from airborne blood, fat, and "
                "bacterial aerosols; musculoskeletal injuries from handling heavy carcasses; "
                "and machine-related injuries. The US Bureau of Labor Statistics reports "
                "injury rates in meatpacking roughly 2.5 times the manufacturing average, "
                "though actual rates may be higher due to underreporting. Workers are often "
                "immigrants or refugees with limited legal protections and fear of job loss. "
                "Psychologically, slaughterhouse workers report elevated rates of PTSD, "
                "depression, anxiety, drug and alcohol abuse, and domestic violence. "
                "Communities with slaughterhouses show elevated crime rates. A study by "
                "Fitzgerald et al. (2009) found a statistically significant correlation "
                "between the presence of slaughterhouses and increased crime, including "
                "violent crime, controlling for other socioeconomic factors."
            ),
            "citations": [
                "Fitzgerald, A.J., Kalof, L. & Dietz, T. (2009). Slaughterhouses and increased crime rates. Organization & Environment, 22(2), 158-184.",
                "Human Rights Watch (2004). Blood, Sweat, and Fear: Workers' Rights in U.S. Meat and Poultry Plants.",
            ],
            "tags": ["health", "worker_safety", "slaughterhouse", "occupational_hazard"],
        },
    ]

    ECONOMICS_FACTS = [
        {
            "q": "How much does the US government subsidize animal agriculture?",
            "a": (
                "The US government provides an estimated $38 billion annually in direct and "
                "indirect subsidies to the animal agriculture industry. Direct subsidies "
                "include: payments to farmers growing feed crops (corn and soy, the majority "
                "of which become animal feed, receive the largest share of crop subsidies); "
                "crop insurance subsidies (the federal government pays about 60% of premiums "
                "for crop insurance on feed crops); conservation programs that disproportionately "
                "benefit large livestock operations; and marketing programs (checkoff programs "
                "like 'Got Milk?' and 'Beef: It's What's for Dinner' are funded by mandatory "
                "producer contributions but promoted by the USDA). Indirect subsidies include: "
                "exemptions from environmental regulations that other industries face; below-cost "
                "grazing permits on public land (the BLM charges approximately $1.35 per animal "
                "unit month, far below market rates); and the externalization of environmental "
                "and public health costs. These subsidies make animal products artificially "
                "cheap relative to their true cost, distorting consumer choices."
            ),
            "citations": [
                "Greenfield, N. (2019). Feeding the Problem: The Dangerous Intensification of Animal Farming in the US. NRDC.",
                "USDA Economic Research Service (2023). Farm Income and Wealth Statistics.",
            ],
            "tags": ["economics", "subsidies", "US", "policy"],
        },
        {
            "q": "What is true cost accounting for animal products?",
            "a": (
                "True cost accounting (also called full cost accounting) is an economic "
                "framework that includes the externalized costs of production -- costs that "
                "are real but not reflected in the market price of a product. For animal "
                "products, externalized costs include: environmental damage (greenhouse gas "
                "emissions, water pollution, soil degradation, deforestation, biodiversity "
                "loss); public health costs (antibiotic resistance, zoonotic disease risk, "
                "diet-related chronic diseases); occupational health costs for slaughterhouse "
                "workers; animal welfare costs; and community impacts. A 2020 study by the "
                "Rockefeller Foundation estimated that the US food system generates $2.1 "
                "trillion in external costs annually, with animal products contributing "
                "disproportionately. Research by Pieper et al. (2020) in Nature Communications "
                "calculated that if external costs were internalized, the price of conventional "
                "beef would increase by approximately 146%, the price of dairy by 91%, and "
                "the price of conventional meat overall by 96%. Organic plant-based products "
                "had the lowest external costs."
            ),
            "citations": [
                "Pieper, M. et al. (2020). Calculation of external climate costs for food highlights inadequate pricing of animal products. Nature Communications, 11, 6117.",
                "Rockefeller Foundation (2021). True Cost of Food: Measuring What Matters to Transform the US Food System.",
            ],
            "tags": ["economics", "true_cost", "externalities"],
        },
        {
            "q": "What is the stranded asset risk in animal agriculture?",
            "a": (
                "Stranded asset risk in animal agriculture refers to the possibility that "
                "investments in intensive animal farming infrastructure may become worthless "
                "as the industry faces disruption from alternative proteins (plant-based "
                "meat, cultivated meat, precision fermentation), changing regulations "
                "(welfare laws, environmental regulations, carbon pricing), shifting consumer "
                "preferences, and climate-related production risks. The FAIRR Initiative "
                "(Farm Animal Investment Risk & Return), backed by investors managing over "
                "$70 trillion in assets, has identified protein diversification as a material "
                "investment risk. Large-scale factory farm infrastructure (CAFOs, processing "
                "plants) represents billions in capital investment that may become stranded "
                "if demand shifts. Boston Consulting Group projects the alternative protein "
                "market could capture 11% of the global protein market by 2035. Banks and "
                "investors are increasingly conducting climate stress tests that reveal "
                "animal agriculture's vulnerability to carbon pricing, water scarcity, and "
                "regulatory changes. The parallel to stranded assets in fossil fuels is "
                "increasingly recognized."
            ),
            "citations": [
                "FAIRR Initiative (2023). Protein Diversification: Industry Scorecard.",
                "BCG (2021). Food for Thought: The Protein Transformation.",
            ],
            "tags": ["economics", "stranded_assets", "investment_risk"],
        },
    ]

    # ── Template-based generation for volume ────────────────────────────

    ADDITIONAL_QUESTIONS = [
        # Scale
        {
            "q": "How many chickens are alive on farms at any given time?",
            "a": (
                "Approximately 23 billion chickens are alive on farms worldwide at any given "
                "time, according to FAO data. This includes roughly 7.9 billion laying hens "
                "and over 15 billion broiler chickens in various stages of their 6-week lives. "
                "Chickens are by far the most numerous farmed animal on Earth -- there are "
                "roughly 3 chickens for every human. The total annual throughput is much higher "
                "(over 73 billion broilers slaughtered per year) because each individual lives "
                "for only a few weeks."
            ),
            "subcategory": "scale",
            "tags": ["scale", "chicken"],
        },
        {
            "q": "How long do farmed animals live compared to their natural lifespan?",
            "a": (
                "Farmed animals are typically slaughtered at a small fraction of their natural "
                "lifespan. Broiler chickens: slaughtered at 6 weeks (natural lifespan 5-8 "
                "years, or 0.15% of their life). Pigs: slaughtered at 5-6 months (natural "
                "lifespan 15-20 years, or 2.5%). Beef cattle: slaughtered at 18-22 months "
                "(natural lifespan 20-25 years, or 7-9%). Dairy cows: slaughtered at 4-6 "
                "years when milk production declines (natural lifespan 20+ years, or 20-30%). "
                "Egg-laying hens: slaughtered at 72-80 weeks (natural lifespan 5-8 years, or "
                "18-20%). Veal calves: slaughtered at 16-20 weeks (0.6-1.5% of natural "
                "lifespan). Lambs: slaughtered at 6-8 months (natural lifespan 12 years, "
                "or 4-6%). Turkeys: slaughtered at 14-18 weeks (natural lifespan 10 years, "
                "or 2-3%). In every case, the animal is killed at the age that maximizes "
                "economic return, not welfare."
            ),
            "subcategory": "scale",
            "tags": ["scale", "lifespan", "slaughter_age"],
        },
        # Conditions
        {
            "q": "What is forced molting in the egg industry?",
            "a": (
                "Forced molting is the deliberate induction of a new egg-laying cycle in hens "
                "whose production has declined. The most common method involves withdrawing "
                "food for 7-14 days (historically up to 14 days, now typically 5-10 days "
                "with low-nutrient feed instead of total starvation in some operations). This "
                "causes the hens to lose 25-30% of their body weight, stop laying, and shed "
                "feathers. When feeding resumes, the hens begin a new, more productive laying "
                "cycle. During the starvation period, hens show obvious signs of hunger and "
                "distress: increased aggression, stereotypic pecking at empty feeders, and "
                "elevated cortisol. Mortality during forced molting ranges from 1-5%. "
                "Starvation-based molting also increases susceptibility to Salmonella "
                "colonization. The EU banned forced molting by starvation in 2003, but "
                "it remains legal in the US, where approximately 75% of egg producers "
                "practice it."
            ),
            "subcategory": "conditions",
            "tags": ["conditions", "chicken", "egg_industry", "forced_molting"],
        },
        {
            "q": "What happens to dairy cows when they can no longer produce enough milk?",
            "a": (
                "When a dairy cow's milk production declines below the point of economic "
                "viability -- typically at age 4-6 years, after 2-4 lactation cycles (their "
                "natural lifespan is 20+ years) -- she is classified as a 'spent' cow and "
                "sent to slaughter. By this point, many dairy cows are in poor physical "
                "condition: lame (lameness prevalence in US dairy herds ranges from 20-55%), "
                "suffering from mastitis (painful udder infection), metabolically exhausted "
                "from years of producing 10x the milk their bodies evolved to produce, and "
                "often with reduced body condition. Some are so debilitated they are classified "
                "as 'downer' cows (unable to walk). Spent dairy cows are typically processed "
                "into low-grade ground beef, pet food, or rendering products. Approximately "
                "3 million dairy cows are slaughtered annually in the US. Their meat accounts "
                "for about 9% of US beef supply."
            ),
            "subcategory": "conditions",
            "tags": ["conditions", "cow", "dairy", "spent_cows"],
        },
        # Environment
        {
            "q": "How much land is used for animal agriculture?",
            "a": (
                "Animal agriculture uses approximately 77% of global agricultural land (including "
                "grazing land and land used to grow feed crops) while producing only 18% of "
                "the world's calories and 37% of its protein (Poore & Nemecek, 2018). Grazing "
                "land for livestock covers approximately 26% of the Earth's ice-free land "
                "surface, and feed crops (primarily corn and soy) account for approximately "
                "33% of all cropland. In total, animal agriculture occupies roughly 4 billion "
                "hectares -- an area larger than all the Americas combined. If the world "
                "shifted to plant-based food systems, global agricultural land use could be "
                "reduced by approximately 75% (about 3.1 billion hectares, an area the size "
                "of Africa) while still feeding the global population. This freed land could "
                "be rewilded, sequestering carbon and restoring biodiversity."
            ),
            "subcategory": "environment",
            "tags": ["environment", "land_use", "efficiency"],
        },
        {
            "q": "How does animal agriculture affect biodiversity?",
            "a": (
                "Animal agriculture is identified as one of the leading drivers of biodiversity "
                "loss globally. The primary mechanisms include: habitat destruction (converting "
                "forests, grasslands, and wetlands to pasture or feed crop fields -- animal "
                "agriculture has destroyed approximately 70% of the Amazon's deforested area); "
                "pesticide and fertilizer runoff from feed crops killing aquatic organisms; "
                "overgrazing degrading native ecosystems; wild predator killing programs "
                "(wolves, coyotes, bears, and other predators are killed to protect livestock "
                "-- USDA Wildlife Services kills approximately 1.5 million animals annually); "
                "overfishing depleting ocean ecosystems; and antibiotic-contaminated waste "
                "affecting soil and water microbiomes. The WWF Living Planet Report (2022) "
                "found that wildlife populations have declined by an average of 69% since "
                "1970, with food production identified as the single largest driver. "
                "Machovina et al. (2015) identified reducing animal product consumption as "
                "the single most impactful action an individual can take to reduce "
                "biodiversity loss."
            ),
            "subcategory": "environment",
            "tags": ["environment", "biodiversity", "wildlife"],
        },
        # Health
        {
            "q": "What is the link between processed meat and cancer?",
            "a": (
                "In 2015, the World Health Organization's International Agency for Research "
                "on Cancer (IARC) classified processed meat (bacon, sausages, hot dogs, ham, "
                "salami, corned beef) as a Group 1 carcinogen, meaning there is sufficient "
                "evidence that it causes cancer in humans. Specifically, processed meat "
                "consumption increases the risk of colorectal cancer: each 50g of processed "
                "meat eaten daily (roughly one hot dog or 4-5 slices of bacon) increases "
                "colorectal cancer risk by approximately 18%. Red meat (beef, pork, lamb) "
                "was classified as Group 2A (probably carcinogenic), with associations also "
                "found for colorectal, pancreatic, and prostate cancer. The mechanisms include "
                "the formation of N-nitroso compounds and polycyclic aromatic hydrocarbons "
                "during processing and cooking, and the effect of heme iron on the gut lining. "
                "Group 1 is the same classification as tobacco smoking and asbestos, though "
                "the classification indicates certainty of the cancer link, not the magnitude "
                "of risk -- tobacco is far more dangerous. Colorectal cancer is the third "
                "most common cancer globally."
            ),
            "subcategory": "health",
            "tags": ["health", "cancer", "processed_meat", "WHO"],
        },
    ]

    def _generate_from_bank(self, bank: list[dict], subcategory: str) -> Iterator[Example]:
        for item in bank:
            yield self._make_example(
                instruction=item["q"],
                output=item["a"],
                subcategory=subcategory,
                citations=item.get("citations", []),
                tags=item.get("tags", []),
            )

    def _generate_additional(self) -> Iterator[Example]:
        for item in self.ADDITIONAL_QUESTIONS:
            yield self._make_example(
                instruction=item["q"],
                output=item["a"],
                subcategory=item.get("subcategory", "additional"),
                tags=item.get("tags", []),
            )

    def _generate_templated_questions(self) -> Iterator[Example]:
        """Generate additional questions from templates for volume."""
        species_data = {
            "chicken": {
                "count": "73 billion",
                "conditions": "battery cages (egg-laying) or crowded floor systems (broilers)",
                "key_issue": "extreme growth rates causing skeletal failure in broilers, and cage confinement for layers",
            },
            "pig": {
                "count": "1.4 billion",
                "conditions": "gestation crates, farrowing crates, and crowded group housing on slatted floors",
                "key_issue": "gestation crate confinement preventing all natural movement and behavior",
            },
            "cow": {
                "count": "302 million (beef) plus 270 million (dairy)",
                "conditions": "feedlots (beef) or continuous pregnancy/lactation cycles (dairy)",
                "key_issue": "mother-calf separation in dairy, feedlot conditions in beef",
            },
            "fish": {
                "count": "1-3 trillion",
                "conditions": "crowded aquaculture pens or wild-caught with no welfare protections",
                "key_issue": "no humane slaughter requirements in any country",
            },
            "turkey": {
                "count": "656 million",
                "conditions": "crowded floor systems with no outdoor access",
                "key_issue": "bred for such extreme breast muscle growth that they cannot mate naturally",
            },
        }

        templates = [
            ("How many {species} are slaughtered for food each year?",
             "Approximately {count} {species} are slaughtered for food globally each year, according "
             "to FAO estimates. They are typically raised in {conditions}. The primary welfare "
             "concern is {key_issue}."),
            ("What are the welfare concerns for farmed {species}?",
             "The primary welfare concerns for farmed {species} include: {conditions}. "
             "The key issue is {key_issue}. Approximately {count} {species} are slaughtered "
             "annually, making welfare improvements in this sector significant in terms of "
             "total suffering affected."),
            ("What conditions do farmed {species} live in?",
             "Most farmed {species} live in {conditions}. With approximately {count} {species} "
             "slaughtered each year, the conditions of their lives represent one of the largest "
             "welfare issues in animal agriculture. The central concern is {key_issue}."),
        ]

        for species, data in species_data.items():
            for q_template, a_template in templates:
                q = q_template.format(species=species)
                a = a_template.format(species=species, **data)
                yield self._make_example(
                    instruction=q,
                    output=a,
                    subcategory=f"templated_{species}",
                    tags=[species, "industry_facts", "templated"],
                )

    def generate(self) -> Iterator[Example]:
        yield from self._generate_from_bank(self.SCALE_FACTS, "scale")
        yield from self._generate_from_bank(self.CONDITIONS_FACTS, "conditions")
        yield from self._generate_from_bank(self.ENVIRONMENTAL_FACTS, "environment")
        yield from self._generate_from_bank(self.HEALTH_FACTS, "health")
        yield from self._generate_from_bank(self.ECONOMICS_FACTS, "economics")
        yield from self._generate_additional()
        yield from self._generate_templated_questions()
