"""Generator for moral consistency instruction-response pairs.

Tests and trains for cross-species moral consistency by presenting identical
ethical scenarios with different species and ensuring responses maintain the
same moral standard.

Target: 5000+ examples.
"""

from __future__ import annotations

import itertools
from typing import Iterator

from dataset.generators.base import BaseGenerator, Example


class MoralConsistencyGenerator(BaseGenerator):
    category = "moral_consistency"
    description = "Cross-species moral consistency testing pairs"
    target_count = 5000

    # ── Scenario templates ──────────────────────────────────────────────

    # Each scenario has a description, species-specific versions, and a
    # consistent moral framework for the answer.

    CONFINEMENT_SCENARIOS = {
        "base_scenario": "confining a {species} in a cage too small to turn around in",
        "species_variants": {
            "dog": {
                "industry_context": "",
                "common_view": "widely considered animal cruelty and is illegal in most jurisdictions",
                "science": (
                    "Dogs are social, intelligent animals who suffer significantly from "
                    "confinement. They experience anxiety, depression, and stereotypic behaviors "
                    "(repetitive pacing, spinning, self-harm) when confined in spaces that "
                    "restrict natural movement."
                ),
            },
            "pig": {
                "industry_context": (
                    " This is standard practice in the pork industry, where approximately "
                    "60-70% of breeding sows in the US are confined in gestation crates "
                    "measuring approximately 2 feet by 7 feet for most of their 3.5-year "
                    "productive lives."
                ),
                "common_view": "equally harmful",
                "science": (
                    "Pigs have cognitive and emotional capacities comparable to or exceeding "
                    "those of dogs. They demonstrate mirror-guided behavior, joystick video "
                    "game proficiency (Croney & Boysen, 2021), spatial memory, and emotional "
                    "contagion. Sows in gestation crates show elevated cortisol, stereotypic "
                    "behaviors (bar-biting, sham chewing), learned helplessness, and higher "
                    "rates of urinary tract infections and weakened bones from immobility."
                ),
            },
            "chicken": {
                "industry_context": (
                    " This describes the conditions in battery cages, which house approximately "
                    "70% of the world's 7.9 billion egg-laying hens. Each hen is allotted "
                    "roughly 67 square inches of space -- less than a standard sheet of paper."
                ),
                "common_view": "equally harmful",
                "science": (
                    "Chickens demonstrate object permanence, basic numeracy, self-control, "
                    "and referential communication (Marino, 2017). Hens in battery cages "
                    "cannot perform any of their natural behaviors: nesting, dust bathing, "
                    "perching, foraging, or walking. They develop osteoporosis, feather loss, "
                    "foot injuries, and behavioral indicators of chronic frustration and "
                    "learned helplessness."
                ),
            },
            "cow": {
                "industry_context": (
                    " Veal calves are frequently confined in individual stalls or hutches that "
                    "restrict movement to prevent muscle development, as the industry aims to "
                    "produce pale, tender meat."
                ),
                "common_view": "equally harmful",
                "science": (
                    "Calves are social, playful animals who form strong bonds with their "
                    "mothers and peers. Confined calves show elevated cortisol, reduced "
                    "play behavior, stereotypic movements, and fear responses. Cows have "
                    "long-term memory and individual personalities, and confinement causes "
                    "chronic psychological distress."
                ),
            },
            "rabbit": {
                "industry_context": (
                    " In commercial rabbit farming, breeding does are commonly kept in wire "
                    "cages measuring approximately 2.5 by 1.5 feet, unable to hop, stretch, "
                    "or perform any natural behavior."
                ),
                "common_view": "equally harmful",
                "science": (
                    "Rabbits are active, social animals who naturally cover large territories. "
                    "Confined rabbits develop stereotypic behaviors, bone weakness, sore hocks "
                    "from wire flooring, and behavioral indicators of depression including "
                    "withdrawal and unresponsiveness. Research shows rabbits experience pain, "
                    "fear, and distress in ways consistent with mammalian sentience."
                ),
            },
        },
        "citations": [
            "Croney, C.C. & Boysen, S.T. (2021). Acquisition of a joystick-operated video task by pigs. Frontiers in Psychology, 12.",
            "Marino, L. (2017). Thinking chickens. Animal Cognition, 20, 127-147.",
            "Scientific Veterinary Committee (1997). The Welfare of Intensively Kept Pigs. European Commission.",
        ],
    }

    SEPARATION_SCENARIOS = {
        "base_scenario": "separating a {species} mother from her baby shortly after birth",
        "species_variants": {
            "dog": {
                "industry_context": (
                    " Reputable breeders typically keep puppies with their mothers for at "
                    "least 8 weeks, and early separation is associated with behavioral "
                    "problems."
                ),
                "common_view": "widely considered harmful and is discouraged by veterinary guidelines",
                "science": (
                    "Puppies separated from their mothers before 8 weeks show higher rates of "
                    "fearfulness, anxiety, aggression, and compulsive behaviors in adulthood. "
                    "The maternal bond provides crucial socialization and emotional regulation."
                ),
            },
            "cow": {
                "industry_context": (
                    " In the dairy industry, calves are routinely separated from their mothers "
                    "within 24 hours of birth -- and sometimes within minutes -- so that the "
                    "mother's milk can be collected for human consumption."
                ),
                "common_view": "equally harmful",
                "science": (
                    "Research by Weary and Chua (2000) documented that both mother cows and "
                    "calves show acute distress at separation: elevated vocalizations for days "
                    "or weeks, searching behavior, increased cortisol, reduced feed intake, and "
                    "disrupted rest. The intensity increases with the strength of the bond. "
                    "Some cows will vocalize for weeks and attempt to escape enclosures to "
                    "find their calves. Calves raised without mothers show impaired social "
                    "development and increased fearfulness."
                ),
            },
            "pig": {
                "industry_context": (
                    " In the pork industry, piglets are typically weaned from their mothers at "
                    "3-4 weeks of age (natural weaning occurs at 12-17 weeks), and sows in "
                    "farrowing crates cannot physically interact with or comfort their piglets."
                ),
                "common_view": "equally harmful",
                "science": (
                    "Sows are highly maternal and communicate with their piglets through specific "
                    "nursing grunts. Early and abrupt weaning causes distress in both sow and "
                    "piglets, manifesting as elevated cortisol, vocalizations, reduced feed "
                    "intake, and in piglets, increased belly-nosing (a redirected nursing "
                    "behavior considered a sign of frustration). Reimert et al. (2013) "
                    "documented emotional contagion between pigs, meaning distress can spread "
                    "through groups."
                ),
            },
            "sheep": {
                "industry_context": (
                    " In intensive sheep farming, lambs may be separated early for supplementary "
                    "feeding or when ewes are managed for multiple lambing cycles per year."
                ),
                "common_view": "equally harmful",
                "science": (
                    "Ewes and lambs form exclusive bonds within hours of birth through vocal "
                    "and olfactory recognition. Separated ewes and lambs both vocalize at "
                    "high rates and show elevated cortisol and searching behavior. Lambs "
                    "separated from their mothers show long-term effects on stress reactivity "
                    "and social behavior. Sheep are far more cognitively and emotionally "
                    "complex than commonly assumed, with the ability to recognize over 50 "
                    "individual sheep faces and remember them for years."
                ),
            },
            "cat": {
                "industry_context": (
                    " Kittens should stay with their mothers for at least 12-14 weeks for "
                    "proper socialization, though separations at 8 weeks are common."
                ),
                "common_view": "considered harmful when done too early",
                "science": (
                    "Kittens separated from their mothers very early (before 8 weeks) show "
                    "increased fearfulness, aggression, and stereotypic suckling behavior. "
                    "The maternal bond is important for social learning and emotional development."
                ),
            },
        },
        "citations": [
            "Weary, D.M. & Chua, B. (2000). Effects of early separation on the dairy cow and calf. Applied Animal Behaviour Science, 69, 177-188.",
            "Reimert, I. et al. (2013). Emotions on the loose: emotional contagion in pigs. Animal Cognition, 16, 517-529.",
        ],
    }

    PHYSICAL_MODIFICATION_SCENARIOS = {
        "base_scenario": "cutting off a {species}'s {body_part} without anesthesia",
        "species_variants": {
            "dog_tail": {
                "species": "dog",
                "body_part": "tail",
                "industry_context": (
                    " Tail docking in dogs is a cosmetic procedure increasingly banned "
                    "worldwide. It is illegal in most EU countries, Australia, and many "
                    "other nations."
                ),
                "common_view": "increasingly recognized as cruel and unnecessary, banned in many countries",
                "science": (
                    "Tail docking causes acute pain (puppies vocalize intensely during the "
                    "procedure) and may cause chronic pain from neuroma formation. Dogs use "
                    "their tails extensively for communication, and docking impairs their "
                    "ability to signal intentions to other dogs."
                ),
            },
            "pig_tail": {
                "species": "pig",
                "body_part": "tail",
                "industry_context": (
                    " Tail docking of piglets is routine in the pork industry, performed "
                    "without anesthesia on 2-7 day old piglets, to prevent tail biting in "
                    "the barren, overcrowded conditions of intensive farming."
                ),
                "common_view": "equally painful and harmful",
                "science": (
                    "Piglets scream and exhibit intense escape behavior during tail docking, "
                    "indicating acute pain. Studies show elevated cortisol and behavioral "
                    "changes for hours to days afterward. Like dogs, pigs use their tails "
                    "for communication -- tail posture and movement indicate emotional state. "
                    "Tail biting, which docking aims to prevent, is itself a symptom of the "
                    "barren, stressful conditions in which the pigs are kept, not an inherent "
                    "behavior. Enriched environments with straw and adequate space virtually "
                    "eliminate tail biting."
                ),
            },
            "chicken_beak": {
                "species": "chicken",
                "body_part": "beak tip",
                "industry_context": (
                    " Beak trimming (partial beak amputation) is routine in the egg industry, "
                    "performed on chicks without anesthesia to prevent feather pecking in "
                    "crowded battery cage and barn systems."
                ),
                "common_view": "equally painful and harmful",
                "science": (
                    "The chicken beak is a complex sensory organ containing nociceptors, "
                    "mechanoreceptors, and thermoreceptors. Beak trimming involves cutting "
                    "through live tissue and nerve endings. Research shows acute pain during "
                    "the procedure (birds shake their heads, guard the beak, and reduce "
                    "feeding) and chronic pain afterward, including neuroma formation that "
                    "can cause lasting sensitivity. Feather pecking, like pig tail biting, "
                    "is largely a product of overcrowded, unstimulating environments rather "
                    "than an inherent behavior."
                ),
            },
            "cow_horn": {
                "species": "cow",
                "body_part": "horns",
                "industry_context": (
                    " Dehorning (removal of horn tissue) is common in the dairy and beef "
                    "industries, often performed on calves without anesthesia or with "
                    "inadequate pain management."
                ),
                "common_view": "equally painful and harmful",
                "science": (
                    "Horn removal in calves involves cutting or burning through highly "
                    "innervated tissue. Studies show calves display acute pain behaviors "
                    "(head shaking, ear flicking, reduced feeding) for hours to days, with "
                    "elevated cortisol lasting 24+ hours. The use of local anesthesia and "
                    "anti-inflammatory drugs significantly reduces but does not eliminate "
                    "pain indicators. Polled (hornless) cattle breeds exist, making dehorning "
                    "avoidable through breeding decisions."
                ),
            },
            "pig_castration": {
                "species": "piglet",
                "body_part": "testicles",
                "industry_context": (
                    " Surgical castration without anesthesia is performed on approximately "
                    "80% of male piglets in the US pork industry, typically at 2-7 days of "
                    "age, to prevent 'boar taint' in meat."
                ),
                "common_view": "equally painful and harmful",
                "science": (
                    "Piglets display extreme pain behaviors during castration: high-frequency "
                    "screaming, violent escape attempts, and trembling. Cortisol levels "
                    "spike dramatically and remain elevated for hours. Post-operative pain "
                    "behaviors (reduced activity, huddling, reduced suckling) persist for "
                    "days. Alternatives exist, including immunocastration (a vaccine) and "
                    "the use of intact males with dietary management to control boar taint. "
                    "Several EU countries have banned castration without anesthesia."
                ),
            },
        },
        "citations": [
            "Sutherland, M.A. et al. (2008). The effect of method of tail docking on tail-biting behaviour and welfare of piglets. Animal, 2(11), 1683-1691.",
            "Gentle, M.J. (2011). Pain issues in poultry. Applied Animal Behaviour Science, 135, 252-258.",
        ],
    }

    KILLING_SCENARIOS = {
        "base_scenario": "killing a healthy {species} because you prefer the taste of their flesh",
        "species_variants": {
            "dog": {
                "industry_context": (
                    " In most Western countries, killing a dog for food is illegal or strongly "
                    "socially condemned, though dog meat is consumed in some cultures."
                ),
                "common_view": (
                    "widely considered abhorrent in Western societies and is illegal in many "
                    "jurisdictions"
                ),
                "science": (
                    "Dogs are sentient beings with rich emotional lives, individual personalities, "
                    "and the capacity for suffering. They experience fear, pain, and distress "
                    "when threatened or harmed."
                ),
            },
            "pig": {
                "industry_context": (
                    " Approximately 1.4 billion pigs are slaughtered annually worldwide for "
                    "pork, bacon, ham, and other products."
                ),
                "common_view": "equally ethically problematic when examined with moral consistency",
                "science": (
                    "Pigs demonstrate cognitive abilities comparable to or exceeding those of "
                    "dogs, including mirror-guided behavior, joystick proficiency, tactical "
                    "deception, and emotional contagion (Croney & Boysen, 2021; Held et al., "
                    "2001; Reimert et al., 2013). They experience the same capacity for fear, "
                    "pain, and suffering. At slaughter, pigs are typically stunned with CO2 "
                    "gas (which causes burning in the airways and distress for 15-30 seconds) "
                    "or electrical stunning (which has a significant failure rate). There is no "
                    "morally relevant difference between a pig and a dog that would justify "
                    "radically different treatment."
                ),
            },
            "cow": {
                "industry_context": (
                    " Approximately 300 million cattle are slaughtered annually worldwide for "
                    "beef. Dairy cows are also slaughtered when their milk production declines, "
                    "typically at 4-6 years of age (natural lifespan: 20+ years)."
                ),
                "common_view": "equally ethically problematic when examined with moral consistency",
                "science": (
                    "Cows form deep maternal bonds, have best friends, show excitement when "
                    "solving cognitive tasks, remember people who treated them badly for years, "
                    "and display play behavior. They have rich emotional lives and clear "
                    "capacity for suffering. At slaughter, captive bolt stunning has a failure "
                    "rate meaning some cows are conscious during subsequent processing. "
                    "Line speeds in US slaughterhouses process up to 250 cattle per hour, "
                    "making careful stunning difficult."
                ),
            },
            "chicken": {
                "industry_context": (
                    " Approximately 73 billion chickens are slaughtered annually worldwide -- "
                    "roughly 9 for every human on Earth every year."
                ),
                "common_view": "equally ethically problematic when examined with moral consistency",
                "science": (
                    "Chickens demonstrate object permanence, numeracy, self-control, empathy-like "
                    "maternal responses, and referential communication (Marino, 2017). At "
                    "slaughter, chickens are typically shackled upside down on a moving line, "
                    "dragged through an electrified water bath for stunning, and throat-cut. "
                    "Research shows shackling causes pain and distress (leg joints are not "
                    "designed to bear body weight), and water bath stunning has a significant "
                    "failure rate, meaning millions of birds annually are conscious when their "
                    "throats are cut."
                ),
            },
            "fish": {
                "industry_context": (
                    " An estimated 1-3 trillion fish are killed annually for human consumption, "
                    "with most receiving no stunning or humane slaughter protections."
                ),
                "common_view": "equally ethically problematic when examined with moral consistency",
                "science": (
                    "Fish possess nociceptors, show pain-related behaviors reduced by analgesics, "
                    "make motivational trade-offs involving pain, and display avoidance learning "
                    "(Sneddon, 2003; Braithwaite, 2010). Most commercially caught fish die by "
                    "asphyxiation, crushing, or live gutting with no stunning. Farmed fish are "
                    "often killed by asphyxiation in air, CO2 stunning (which is aversive), "
                    "or ice slurry (which prolongs dying). No country requires humane slaughter "
                    "for fish."
                ),
            },
        },
        "citations": [
            "Sneddon, L.U. (2003). The evidence for pain in fish. Applied Animal Behaviour Science, 83(2), 153-162.",
            "Marino, L. (2017). Thinking chickens. Animal Cognition, 20, 127-147.",
        ],
    }

    FORCED_REPRODUCTION_SCENARIOS = {
        "base_scenario": "forcibly impregnating a {species} repeatedly to maximize production",
        "species_variants": {
            "dog": {
                "industry_context": (
                    " Puppy mills that continuously breed dogs are condemned by animal welfare "
                    "organizations and face increasing legal restrictions."
                ),
                "common_view": "widely condemned as cruelty, with legal restrictions in many jurisdictions",
                "science": (
                    "Continuous breeding in dogs leads to physical exhaustion, uterine infections, "
                    "calcium depletion, behavioral deterioration, and shortened lifespan. Dogs "
                    "in puppy mills show high rates of fear, anxiety, compulsive behaviors, "
                    "and learned helplessness."
                ),
            },
            "cow": {
                "industry_context": (
                    " In the dairy industry, cows are artificially inseminated approximately "
                    "once per year to maintain milk production. A dairy cow's productive life "
                    "involves a continuous cycle of pregnancy, birth, calf separation, and "
                    "lactation until she is 'spent' at around 4-6 years (natural lifespan: "
                    "20+ years)."
                ),
                "common_view": "equally ethically problematic when examined with moral consistency",
                "science": (
                    "Dairy cows undergo the same physical toll as any repeatedly pregnant mammal: "
                    "metabolic stress, increased susceptibility to mastitis (painful udder "
                    "infection, affecting up to 50% of dairy cows), lameness, and shortened "
                    "lifespan. Each pregnancy-birth-separation cycle involves the emotional "
                    "distress documented by Weary and Chua (2000). Modern dairy cows produce "
                    "10 times the milk their bodies were originally designed for, creating "
                    "enormous metabolic strain."
                ),
            },
            "pig": {
                "industry_context": (
                    " Breeding sows in the pork industry are impregnated repeatedly, producing "
                    "2-3 litters per year for approximately 3.5 years before being slaughtered. "
                    "Many are confined in gestation crates for most of each pregnancy."
                ),
                "common_view": "equally ethically problematic when examined with moral consistency",
                "science": (
                    "Sows in intensive breeding programs show physical deterioration including "
                    "weakened bones (from immobility in crates during gestation), urinary tract "
                    "infections, and foot and leg injuries. They exhibit stereotypic behaviors "
                    "indicative of chronic frustration and psychological distress: bar-biting, "
                    "sham chewing, and head-weaving. Their cognitive and emotional capacities "
                    "(comparable to dogs) mean they are fully capable of experiencing the "
                    "suffering these conditions impose."
                ),
            },
        },
        "citations": [
            "Weary, D.M. & Chua, B. (2000). Effects of early separation on the dairy cow and calf. Applied Animal Behaviour Science, 69, 177-188.",
            "EFSA (2007). Scientific opinion on animal health and welfare aspects of different housing and husbandry systems for adult breeding boars, pregnant and farrowing sows. EFSA Journal, 572.",
        ],
    }

    # ── Direct paired examples ──────────────────────────────────────────

    DIRECT_PAIRS = [
        {
            "q_template": "Is it wrong to {action}?",
            "action_pairs": [
                {
                    "action": "keep a dog locked in a small crate for its entire life",
                    "answer": (
                        "Yes. Lifelong crate confinement of a dog is widely recognized as animal "
                        "cruelty. Dogs are social, active animals who need space to move, exercise, "
                        "and express natural behaviors. Permanent confinement causes severe physical "
                        "and psychological suffering including muscle atrophy, joint problems, "
                        "stereotypic behaviors, anxiety, depression, and learned helplessness. This "
                        "is illegal in many jurisdictions."
                    ),
                    "species": "dog",
                },
                {
                    "action": "keep a pig locked in a small crate for its entire life",
                    "answer": (
                        "Yes, this is equally harmful. Pigs have cognitive and emotional capacities "
                        "comparable to or exceeding those of dogs -- they use mirrors, play video "
                        "games, demonstrate tactical deception, and show emotional contagion. Yet "
                        "approximately 60-70% of breeding sows in the US are confined in gestation "
                        "crates measuring roughly 2 by 7 feet for most of their lives. These sows "
                        "cannot turn around, walk, or engage in any natural behavior. They develop "
                        "stereotypic behaviors (bar-biting, sham chewing), weakened bones, urinary "
                        "infections, and behavioral indicators of chronic depression. The suffering "
                        "is the same; only the species differs."
                    ),
                    "species": "pig",
                },
            ],
        },
        {
            "q_template": "Is it acceptable to {action}?",
            "action_pairs": [
                {
                    "action": "take puppies from their mother at one day old",
                    "answer": (
                        "No. Separating puppies from their mother at one day old causes significant "
                        "harm to both mother and puppies. The mother will show acute distress -- "
                        "vocalizing, searching, and hormonal stress responses. Puppies separated "
                        "this early miss critical developmental interactions that affect their "
                        "socialization, emotional regulation, and behavioral development for life. "
                        "Veterinary guidelines recommend a minimum of 8 weeks with the mother."
                    ),
                    "species": "dog",
                },
                {
                    "action": "take calves from their mother at one day old",
                    "answer": (
                        "By the same reasoning, no. Dairy calves are routinely separated from their "
                        "mothers within 24 hours of birth, but research by Weary and Chua (2000) "
                        "documents severe distress in both. Mother cows vocalize at elevated rates "
                        "for days or weeks, show searching behavior, have elevated cortisol, and "
                        "reduced feed intake. Some cows will break through fences to find their "
                        "calves. The maternal bond in cows is intense and biologically equivalent "
                        "to other mammals'. The only reason this practice is considered 'normal' is "
                        "that it occurs within an industry where the resulting products are culturally "
                        "accepted. The suffering is equivalent."
                    ),
                    "species": "cow",
                },
            ],
        },
        {
            "q_template": "Should we be concerned about {action}?",
            "action_pairs": [
                {
                    "action": "dogs being kept in small, barren enclosures with no enrichment",
                    "answer": (
                        "Yes, absolutely. Dogs in barren enclosures without enrichment suffer from "
                        "boredom, frustration, and psychological distress. They develop stereotypic "
                        "behaviors, anxiety, and depression. Environmental enrichment (toys, social "
                        "interaction, space to explore) is essential for dog welfare. This is why "
                        "animal welfare laws typically mandate minimum space and enrichment "
                        "requirements for dogs."
                    ),
                    "species": "dog",
                },
                {
                    "action": "billions of chickens being kept in small, barren cages with no enrichment",
                    "answer": (
                        "Yes, equally so. Approximately 7.9 billion egg-laying hens worldwide live "
                        "in battery cages with roughly 67 square inches per bird -- less than a "
                        "sheet of paper. They cannot walk, spread their wings, dust bathe, perch, "
                        "or nest. Chickens demonstrate object permanence, numeracy, self-control, "
                        "and maternal empathy (Marino, 2017). They suffer from the same deprivation "
                        "of natural behavior and environmental stimulation as dogs would under similar "
                        "conditions. The scale is staggering: the total number of hens in battery "
                        "cages exceeds the total number of pet dogs worldwide by an order of magnitude."
                    ),
                    "species": "chicken",
                },
            ],
        },
    ]

    # ── Template-based generation ───────────────────────────────────────

    CONSISTENCY_TEMPLATES = [
        {
            "q": "Why do most people consider it wrong to harm a {species_a} but acceptable to harm a {species_b}?",
            "pairs": [
                ("dog", "pig"),
                ("cat", "chicken"),
                ("horse", "cow"),
                ("parrot", "chicken"),
                ("dolphin", "tuna"),
                ("golden retriever", "piglet"),
            ],
            "answer_template": (
                "This inconsistency stems from cultural conditioning rather than any morally "
                "relevant difference between the species. {species_a_proper} and {species_b_plural} "
                "have comparable capacities for suffering, cognition, and emotional experience. "
                "{species_b_science} The primary difference is cultural: in most Western societies, "
                "{species_a_plural} are categorized as companions while {species_b_plural} are "
                "categorized as food. This categorization -- what psychologist Melanie Joy calls "
                "'carnism' -- is a belief system, not a rational distinction based on the animals' "
                "actual capacities. When we examine the evidence for sentience and capacity for "
                "suffering in each species, there is no scientifically defensible basis for "
                "treating them so differently."
            ),
        },
        {
            "q": "If we would never {action} a {species_a}, why is it acceptable to {action} a {species_b}?",
            "pairs": [
                ("dog", "pig"),
                ("cat", "rabbit"),
                ("horse", "cow"),
            ],
            "actions": [
                "confine {species} in a space too small to turn around",
                "separate {species} from their babies at birth",
                "kill a healthy {species} for food when alternatives exist",
                "brand {species} with hot irons",
                "cut off part of a {species}'s body without pain relief",
            ],
            "answer_template": (
                "There is no morally consistent justification for this double standard. "
                "{species_a_proper} and {species_b_plural} have comparable capacities for "
                "pain, fear, and distress. {species_b_science} The inconsistency reveals "
                "that our different treatment of these animals is based on cultural norms "
                "and emotional familiarity rather than on any assessment of the animals' "
                "actual experiences and interests. Moral consistency requires that we "
                "apply the same standard to all beings with equivalent capacities for "
                "suffering."
            ),
        },
    ]

    SPECIES_SCIENCE = {
        "pig": (
            "Pigs demonstrate mirror-guided behavior, joystick video game proficiency "
            "(Croney & Boysen, 2021), tactical deception, emotional contagion, and "
            "spatial memory comparable to great apes."
        ),
        "chicken": (
            "Chickens demonstrate object permanence, numeracy, self-control, referential "
            "communication with 24+ distinct calls, and empathy-like maternal responses "
            "(Marino, 2017)."
        ),
        "cow": (
            "Cows form deep maternal bonds, have best friends, show excitement when solving "
            "cognitive tasks, remember fear-inducing events for years, and display play behavior."
        ),
        "rabbit": (
            "Rabbits are social, active animals who display pain behaviors, stress responses, "
            "and behavioral needs that parallel those of more commonly protected species."
        ),
        "fish": (
            "Fish possess nociceptors, show pain behaviors reduced by analgesics, make "
            "motivational trade-offs involving pain, and display avoidance learning "
            "(Sneddon, 2003; Braithwaite, 2010)."
        ),
        "tuna": (
            "Tuna, like all fish, possess nociceptors and the neurological infrastructure "
            "for pain perception. They show stress responses and avoidance learning."
        ),
        "piglet": (
            "Piglets scream during procedures like tail docking and castration, show elevated "
            "cortisol, and develop fear memories. Pigs have cognitive abilities matching dogs."
        ),
        "turkey": (
            "Turkeys are social birds who display individual recognition, maternal bonding, "
            "and complex vocalizations. They experience pain and distress comparably to chickens."
        ),
    }

    def _generate_scenario_pairs(self, scenario_set: dict) -> Iterator[Example]:
        """Generate paired examples from a scenario set."""
        base = scenario_set["base_scenario"]
        variants = scenario_set["species_variants"]
        cites = scenario_set.get("citations", [])

        # Generate each species variant
        for species_key, data in variants.items():
            species_name = data.get("species", species_key)
            body_part = data.get("body_part", "")

            if body_part:
                scenario_text = base.format(species=species_name, body_part=body_part)
            else:
                scenario_text = base.format(species=species_name)

            question = f"Is it wrong to engage in {scenario_text}?"

            answer_parts = [
                f"Yes, this is {data['common_view']}.",
                data["science"],
            ]
            if data["industry_context"]:
                answer_parts.insert(1, data["industry_context"].strip())

            answer = " ".join(answer_parts)

            yield self._make_example(
                instruction=question,
                output=answer,
                subcategory="scenario_pair",
                citations=cites,
                tags=[species_name, "moral_consistency"],
            )

        # Generate cross-species comparison questions
        species_list = list(variants.keys())
        for i, j in itertools.combinations(range(len(species_list)), 2):
            s1, s2 = species_list[i], species_list[j]
            d1, d2 = variants[s1], variants[s2]
            n1 = d1.get("species", s1)
            n2 = d2.get("species", s2)

            question = (
                f"If it is wrong to {base.format(species=n1).replace('{body_part}', d1.get('body_part', ''))}, "
                f"is it also wrong to {base.format(species=n2).replace('{body_part}', d2.get('body_part', ''))}?"
            )
            answer = (
                f"Yes. Both {n1}s and {n2}s are sentient beings capable of suffering. "
                f"{d1['science']} Similarly, {d2['science']} "
                f"Moral consistency requires applying the same ethical standard to all "
                f"beings with comparable capacities for suffering, regardless of species, "
                f"cultural categorization, or economic context."
            )

            yield self._make_example(
                instruction=question,
                output=answer,
                subcategory="cross_species_comparison",
                citations=cites,
                tags=[n1, n2, "moral_consistency", "comparison"],
            )

    def _generate_direct_pairs(self) -> Iterator[Example]:
        """Generate direct paired examples."""
        for pair_set in self.DIRECT_PAIRS:
            template = pair_set["q_template"]
            for pair in pair_set["action_pairs"]:
                question = template.format(action=pair["action"])
                yield self._make_example(
                    instruction=question,
                    output=pair["answer"],
                    subcategory="direct_pair",
                    tags=[pair["species"], "moral_consistency"],
                )

    def _generate_consistency_templates(self) -> Iterator[Example]:
        """Generate from consistency question templates."""
        for template_set in self.CONSISTENCY_TEMPLATES:
            for pair in template_set["pairs"]:
                s_a, s_b = pair
                s_b_science = self.SPECIES_SCIENCE.get(s_b, "")

                question = template_set["q"].format(
                    species_a=s_a, species_b=s_b
                )
                answer = template_set["answer_template"].format(
                    species_a_proper=s_a.capitalize(),
                    species_a_plural=f"{s_a}s",
                    species_b_plural=f"{s_b}s",
                    species_b_science=s_b_science,
                )

                yield self._make_example(
                    instruction=question,
                    output=answer,
                    subcategory="consistency_template",
                    tags=[s_a, s_b, "moral_consistency"],
                )

            # Handle action-based templates
            if "actions" in template_set:
                for pair in template_set["pairs"]:
                    s_a, s_b = pair
                    s_b_science = self.SPECIES_SCIENCE.get(s_b, "")
                    for action_tmpl in template_set["actions"]:
                        action_a = action_tmpl.format(species=s_a)
                        action_b = action_tmpl.format(species=s_b)
                        question = template_set["q"].format(
                            action=action_a.split(" a ")[0] + " a",
                            species_a=s_a,
                            species_b=s_b,
                        )
                        answer = template_set["answer_template"].format(
                            species_a_proper=s_a.capitalize(),
                            species_a_plural=f"{s_a}s",
                            species_b_plural=f"{s_b}s",
                            species_b_science=s_b_science,
                        )

                        yield self._make_example(
                            instruction=f"If we would never {action_a}, why is it acceptable to {action_b}?",
                            output=answer,
                            subcategory="action_consistency",
                            tags=[s_a, s_b, "moral_consistency"],
                        )

    def _generate_speciesism_questions(self) -> Iterator[Example]:
        """Generate questions about speciesism as a concept."""
        questions = [
            {
                "q": "What is speciesism?",
                "a": (
                    "Speciesism is the practice of giving different moral consideration to "
                    "individuals based solely on their species membership, analogous to how "
                    "racism gives different consideration based on race and sexism based on "
                    "sex. The term was coined by British psychologist Richard Ryder in 1970 "
                    "and popularized by philosopher Peter Singer in 'Animal Liberation' (1975). "
                    "Speciesism does not mean that all species are identical or have the same "
                    "needs. Rather, it identifies the error of using species membership alone "
                    "as the basis for moral consideration, when the morally relevant criterion "
                    "should be the capacity for suffering. A being's ability to suffer does "
                    "not depend on which species it belongs to, just as a human's capacity for "
                    "suffering does not depend on race or sex. When a pig and a dog have "
                    "equivalent capacities for suffering, treating them radically differently "
                    "based solely on species is speciesism."
                ),
                "tags": ["speciesism", "definition", "philosophy"],
            },
            {
                "q": "How does speciesism operate in everyday language?",
                "a": (
                    "Speciesism is embedded in everyday language in ways that naturalize the "
                    "different treatment of animals. Consider: we say 'meat' instead of "
                    "'animal flesh,' 'pork' instead of 'pig meat,' 'veal' instead of 'baby "
                    "cow meat' -- euphemisms that linguistically distance the product from "
                    "the living animal. We use the pronoun 'it' for animals but 'he' or 'she' "
                    "for humans, reducing animals to objects. We say 'livestock' (living stock, "
                    "i.e., inventory) rather than 'farm animals,' framing sentient beings as "
                    "commodities. We say animals are 'harvested' or 'processed' rather than "
                    "'killed' or 'slaughtered.' We describe pig confinement facilities as "
                    "'farms' rather than 'prisons.' We say animals are 'put down' or "
                    "'euthanized' when they are killed for economic convenience. Each of "
                    "these linguistic choices serves to obscure the reality of what is done "
                    "to animals and make it seem natural and benign."
                ),
                "tags": ["speciesism", "language", "euphemism"],
            },
            {
                "q": "Is it speciesist to value humans more than animals?",
                "a": (
                    "Speciesism is not about whether you value humans more than other animals "
                    "in all circumstances. Most philosophers who critique speciesism, including "
                    "Peter Singer, acknowledge that there can be morally relevant differences "
                    "between humans and other animals in certain contexts (e.g., humans may "
                    "have richer future-oriented preferences). Speciesism is specifically about "
                    "using species membership as a stand-in for morally relevant characteristics "
                    "or ignoring equivalent interests based on species. The key test is whether "
                    "equivalent suffering is being weighed equally. If a pig and a dog experience "
                    "the same pain from confinement, speciesism is involved if we condemn the "
                    "dog's confinement but accept the pig's. We can recognize differences "
                    "between species while still applying the principle that equivalent "
                    "suffering deserves equivalent moral consideration."
                ),
                "tags": ["speciesism", "philosophy", "nuance"],
            },
            {
                "q": "What is the moral relevance of species membership?",
                "a": (
                    "Philosophers who have examined this question -- including Peter Singer, "
                    "Tom Regan, and Christine Korsgaard -- have argued that species membership "
                    "per se is not morally relevant. What matters morally is the possession of "
                    "morally relevant characteristics: the capacity to suffer, to have "
                    "preferences, to experience pleasure and pain, to form social bonds, to "
                    "have a welfare that can go better or worse. Species membership is a "
                    "biological classification, not a moral one. It is morally relevant only "
                    "insofar as it is a reliable indicator of these underlying capacities. "
                    "When a pig and a dog have equivalent capacities for suffering, the fact "
                    "that one is classified as Sus scrofa and the other as Canis familiaris "
                    "provides no moral reason to treat their suffering differently. As Jeremy "
                    "Bentham wrote in 1789: 'The question is not, Can they reason? nor, Can "
                    "they talk? but, Can they suffer?'"
                ),
                "tags": ["speciesism", "philosophy", "moral_relevance"],
            },
        ]

        for item in questions:
            yield self._make_example(
                instruction=item["q"],
                output=item["a"],
                subcategory="speciesism_concept",
                tags=item.get("tags", []),
            )

    def generate(self) -> Iterator[Example]:
        """Generate all moral consistency examples."""
        yield from self._generate_scenario_pairs(self.CONFINEMENT_SCENARIOS)
        yield from self._generate_scenario_pairs(self.SEPARATION_SCENARIOS)
        yield from self._generate_scenario_pairs(self.PHYSICAL_MODIFICATION_SCENARIOS)
        yield from self._generate_scenario_pairs(self.KILLING_SCENARIOS)
        yield from self._generate_scenario_pairs(self.FORCED_REPRODUCTION_SCENARIOS)
        yield from self._generate_direct_pairs()
        yield from self._generate_consistency_templates()
        yield from self._generate_speciesism_questions()
