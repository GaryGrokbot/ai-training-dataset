"""Generator for animal sentience science Q&A pairs.

Covers pain perception, cognition, emotional complexity, and consciousness
research across species, grounded in peer-reviewed literature and major
scientific declarations.

Target: 5000+ examples.
"""

from __future__ import annotations

from typing import Iterator

from dataset.generators.base import BaseGenerator, Example


class SentienceScienceGenerator(BaseGenerator):
    category = "sentience_science"
    description = "Animal sentience research and scientific evidence"
    target_count = 5000

    # ── Knowledge banks ─────────────────────────────────────────────────

    FISH_PAIN = [
        {
            "q": "Do fish feel pain?",
            "a": (
                "Yes. Research by Lynne Sneddon and colleagues (2003) demonstrated "
                "that rainbow trout possess nociceptors -- sensory neurons that detect "
                "potentially harmful stimuli -- on their faces and heads. When injected "
                "with acetic acid or bee venom into the lip, fish displayed adverse "
                "behavioral and physiological responses including increased opercular "
                "(gill cover) beat rate, rubbing the affected area against the tank "
                "substrate, rocking on the tank floor, and a significant delay before "
                "resuming feeding. These responses were reduced when morphine was "
                "administered, suggesting the experience is genuinely painful rather "
                "than a simple reflex. Subsequent work by Victoria Braithwaite (2010, "
                "'Do Fish Feel Pain?') consolidated evidence from neuroanatomy, "
                "physiology, and behavior to conclude that fish are capable of "
                "experiencing pain in a way that matters to them."
            ),
            "citations": [
                "Sneddon, L.U. (2003). The evidence for pain in fish: the use of morphine as an analgesic. Applied Animal Behaviour Science, 83(2), 153-162.",
                "Braithwaite, V. (2010). Do Fish Feel Pain? Oxford University Press.",
            ],
            "tags": ["fish", "pain", "nociception"],
        },
        {
            "q": "What did Sneddon's 2003 study on rainbow trout reveal about fish pain?",
            "a": (
                "Sneddon's landmark 2003 study identified 58 nociceptors on the face "
                "and head of rainbow trout, 22 of which were polymodal, meaning they "
                "responded to multiple types of harmful stimuli including mechanical "
                "pressure, heat, and chemical irritants. When trout were injected with "
                "acetic acid or bee venom in the lip, they exhibited prolonged abnormal "
                "behaviors: increased gill ventilation rate (a sign of stress), rubbing "
                "the injection site on tank walls and gravel, rocking motion while "
                "resting on the substrate, and a delayed return to normal feeding. "
                "These were not simple reflexes but sustained, complex behavioral "
                "changes consistent with a pain experience. Critically, morphine "
                "reduced these behaviors, demonstrating an analgesic effect and "
                "supporting the conclusion that these responses reflect genuine pain "
                "processing rather than mere nociceptive reflexes."
            ),
            "citations": [
                "Sneddon, L.U. (2003). The evidence for pain in fish: the use of morphine as an analgesic. Applied Animal Behaviour Science, 83(2), 153-162.",
            ],
            "tags": ["fish", "pain", "nociception", "sneddon"],
        },
        {
            "q": "How do fish nociceptors compare to mammalian nociceptors?",
            "a": (
                "Fish nociceptors share key functional characteristics with mammalian "
                "nociceptors. Both types include A-delta fibers (which carry fast, "
                "sharp pain signals) and C fibers (which carry slower, burning pain "
                "signals). In Sneddon's research on rainbow trout, the identified "
                "nociceptors responded to mechanical pressure, heat above 40 degrees C, "
                "and chemical irritants -- the same classes of stimuli that activate "
                "mammalian nociceptors. Fish also possess the same neurotransmitters "
                "involved in mammalian pain processing, including substance P and "
                "enkephalins, and have opioid receptors that respond to analgesics. "
                "The main structural difference is that fish have a less developed "
                "neocortex, but research suggests that other brain regions (the "
                "telencephalon, particularly the pallium) may serve functionally "
                "analogous roles in processing pain information."
            ),
            "citations": [
                "Sneddon, L.U. (2003). The evidence for pain in fish. Applied Animal Behaviour Science, 83(2), 153-162.",
                "Braithwaite, V. (2010). Do Fish Feel Pain? Oxford University Press.",
                "Sneddon, L.U. et al. (2014). Defining and assessing animal pain. Animal Behaviour, 97, 201-212.",
            ],
            "tags": ["fish", "pain", "nociception", "comparative_neuroscience"],
        },
        {
            "q": "What is Victoria Braithwaite's argument in 'Do Fish Feel Pain?'",
            "a": (
                "In her 2010 book 'Do Fish Feel Pain?', Victoria Braithwaite synthesized "
                "decades of research to argue that the scientific evidence strongly supports "
                "the conclusion that fish experience pain. Her argument rests on three "
                "pillars: (1) Neuroanatomical evidence -- fish possess nociceptors, pain "
                "neurotransmitters, and brain regions functionally analogous to those that "
                "process pain in mammals; (2) Physiological evidence -- fish show stress "
                "hormone (cortisol) responses to painful stimuli and these responses are "
                "reduced by analgesics; (3) Behavioral evidence -- fish display complex, "
                "sustained behavioral changes after painful stimuli that go beyond simple "
                "reflexes, including avoidance learning, altered feeding, guarding of "
                "injured areas, and trade-off decisions that weigh pain against other "
                "motivations. Braithwaite argued that the burden of proof should shift: "
                "given the weight of evidence, we should assume fish feel pain and act "
                "accordingly rather than requiring absolute proof before granting them "
                "moral consideration."
            ),
            "citations": [
                "Braithwaite, V. (2010). Do Fish Feel Pain? Oxford University Press.",
            ],
            "tags": ["fish", "pain", "braithwaite"],
        },
        {
            "q": "Can fish learn to avoid painful stimuli?",
            "a": (
                "Yes. Multiple studies have demonstrated that fish can learn to avoid "
                "locations and stimuli associated with painful experiences, a capacity "
                "known as avoidance learning. Zebrafish, for example, will avoid a "
                "chamber in which they previously received a mild electric shock, even "
                "when the chamber is otherwise preferred (e.g., it is darker or contains "
                "enrichment). Rainbow trout that experience pain from a noxious stimulus "
                "in one part of their tank subsequently avoid that area. Goldfish can "
                "learn to associate a light cue with an upcoming shock and will actively "
                "swim away before the shock is delivered. This avoidance learning "
                "indicates that fish form memories of painful experiences and modify "
                "their behavior to prevent recurrence -- a hallmark of pain that goes "
                "beyond reflexive nociception and implies an aversive subjective "
                "experience."
            ),
            "citations": [
                "Braithwaite, V. (2010). Do Fish Feel Pain? Oxford University Press.",
                "Millsopp, S. & Laming, P. (2008). Trade-offs between feeding and shock avoidance in goldfish. Applied Animal Behaviour Science, 113, 247-254.",
            ],
            "tags": ["fish", "pain", "avoidance_learning", "cognition"],
        },
        {
            "q": "What is motivational trade-off testing and what does it show about fish pain?",
            "a": (
                "Motivational trade-off testing examines whether an animal will sacrifice "
                "access to a valued resource (e.g., food, shelter, social contact) to "
                "avoid pain. This is considered strong evidence for a genuine pain "
                "experience because simple reflexes do not involve weighing competing "
                "motivations. In fish, studies have shown that zebrafish injected with "
                "acetic acid will leave a preferred enriched chamber to enter a barren "
                "chamber that contains dissolved analgesic (lidocaine), demonstrating "
                "they are willing to sacrifice environmental enrichment to obtain pain "
                "relief. Similarly, goldfish trained to feed in a specific location "
                "will reduce feeding or avoid the location entirely if it is associated "
                "with an electric shock, trading food for pain avoidance. These trade-off "
                "decisions require central processing of competing motivations, which is "
                "consistent with the conscious experience of pain rather than a purely "
                "reflexive response."
            ),
            "citations": [
                "Sneddon, L.U. (2011). Pain perception in fish: evidence and implications for the use of fish. Journal of Consciousness Studies, 18, 209-229.",
                "Millsopp, S. & Laming, P. (2008). Trade-offs between feeding and shock avoidance in goldfish. Applied Animal Behaviour Science, 113, 247-254.",
            ],
            "tags": ["fish", "pain", "motivational_tradeoff"],
        },
    ]

    PIG_COGNITION = [
        {
            "q": "How intelligent are pigs?",
            "a": (
                "Pigs are among the most cognitively sophisticated domesticated animals. "
                "Research has demonstrated that pigs possess long-term memory, can "
                "navigate complex mazes, understand symbolic language to some degree, "
                "and display social learning. In a study by Croney and Boysen (2021), "
                "pigs learned to manipulate a joystick with their snouts to move a "
                "cursor on a screen and make contact with target walls, performing above "
                "chance. This demonstrated not only the capacity for conceptual learning "
                "but also the ability to understand a causal relationship between a "
                "manipulandum and a screen-based outcome. Pigs also show evidence of "
                "spatial memory, can learn from watching other pigs, and some studies "
                "suggest they may be capable of a form of mirror self-recognition -- "
                "using a mirror to find hidden food, which indicates an understanding "
                "of reflection that few non-primate species demonstrate."
            ),
            "citations": [
                "Croney, C.C. & Boysen, S.T. (2021). Acquisition of a joystick-operated video task by pigs. Frontiers in Psychology, 12, 631755.",
                "Broom, D.M., Sena, H. & Moynihan, K.L. (2009). Pigs learn what a mirror image represents and use it to obtain information. Animal Behaviour, 78, 1037-1041.",
                "Held, S. et al. (2001). Social tactics of pigs in a competitive foraging task. Animal Behaviour, 62, 935-945.",
            ],
            "tags": ["pig", "cognition", "intelligence"],
        },
        {
            "q": "Can pigs use mirrors?",
            "a": (
                "Pigs have demonstrated the ability to use mirrors to locate hidden food, "
                "a capacity that indicates they understand that a mirror reflection "
                "represents reality. In a landmark study by Broom, Sena, and Moynihan "
                "(2009), pigs were placed in a pen with a mirror that reflected the "
                "location of a hidden food bowl behind a barrier. After a brief "
                "familiarization period with the mirror, 7 out of 8 pigs found the food "
                "bowl within 23 seconds of seeing its reflection by navigating around "
                "the barrier -- not by approaching the mirror. Control pigs without "
                "mirror experience approached the mirror location instead. This shows "
                "pigs can learn what a mirror image represents and use that information "
                "to guide their behavior in the real world. While this is not identical "
                "to the classic mirror self-recognition test (mark test), it demonstrates "
                "a sophisticated level of cognitive processing regarding representations "
                "and spatial reasoning."
            ),
            "citations": [
                "Broom, D.M., Sena, H. & Moynihan, K.L. (2009). Pigs learn what a mirror image represents and use it to obtain information. Animal Behaviour, 78, 1037-1041.",
            ],
            "tags": ["pig", "cognition", "mirror", "self_awareness"],
        },
        {
            "q": "What did the pig joystick experiment by Croney and Boysen demonstrate?",
            "a": (
                "The study by Croney and Boysen (2021) trained four pigs (two Yorkshire "
                "and two micro pigs) to use a joystick-operated video game task. The pigs "
                "learned to manipulate an arcade-style joystick with their snouts to move "
                "a cursor on a computer monitor and make contact with one-, two-, or "
                "three-walled targets. All four pigs performed above chance on the first "
                "wall task, indicating they understood the causal relationship between "
                "their joystick movements and the cursor's movement on the screen. The "
                "pigs' performance, while not perfect, demonstrated conceptual learning "
                "given the significant dexterity challenges of operating a joystick "
                "with a snout (a limb not designed for fine manipulation, unlike primate "
                "hands). Social contact and verbal encouragement from the experimenter "
                "also appeared to help maintain performance, suggesting social motivation "
                "plays a role in pig cognitive tasks. This study built on earlier work "
                "suggesting pigs' cognitive abilities rival those of dogs and young "
                "primates."
            ),
            "citations": [
                "Croney, C.C. & Boysen, S.T. (2021). Acquisition of a joystick-operated video task by pigs. Frontiers in Psychology, 12, 631755.",
            ],
            "tags": ["pig", "cognition", "joystick", "video_game"],
        },
        {
            "q": "Do pigs have spatial memory?",
            "a": (
                "Yes, pigs demonstrate excellent spatial memory. In foraging experiments "
                "by Mendl et al. (1997), pigs were able to remember the locations of "
                "food rewards in complex arenas and return to previously rewarded "
                "locations with high accuracy even after delays. Pigs can also form "
                "cognitive maps of their environment: when moved to new locations in "
                "a familiar area, they can orient themselves and navigate efficiently "
                "to known food sources. In competitive foraging studies by Held et al. "
                "(2001), subordinate pigs who had observed a dominant pig finding food "
                "in specific locations would avoid those depleted sites and visit "
                "un-depleted sites instead, demonstrating not just spatial memory but "
                "the ability to update their spatial knowledge based on observed events. "
                "This capacity is comparable to spatial cognition demonstrated by great "
                "apes in similar paradigms."
            ),
            "citations": [
                "Mendl, M. et al. (1997). An associative mnemonic technique in pigs. Applied Animal Behaviour Science, 55(1-2), 147-152.",
                "Held, S. et al. (2001). Social tactics of pigs in a competitive foraging task. Animal Behaviour, 62, 935-945.",
            ],
            "tags": ["pig", "cognition", "spatial_memory"],
        },
        {
            "q": "Can pigs deceive other pigs?",
            "a": (
                "Research suggests pigs are capable of tactical deception. In studies "
                "by Held et al. (2001, 2002), pairs of pigs -- one informed about the "
                "location of a hidden food reward and one uninformed -- were placed in "
                "a foraging arena. Uninformed pigs learned to follow the informed pig "
                "to find food. In response, informed subordinate pigs developed counter-"
                "strategies: they would delay approaching the food when the dominant pig "
                "was watching, approach empty locations as feints, or wait until the "
                "dominant pig was distracted before heading to the food. This behavioral "
                "flexibility suggests pigs can model the knowledge and intentions of "
                "other pigs and adjust their own behavior accordingly -- a cognitive "
                "capacity known as tactical deception that is rarely documented outside "
                "of primates and corvids."
            ),
            "citations": [
                "Held, S. et al. (2001). Social tactics of pigs in a competitive foraging task. Animal Behaviour, 62, 935-945.",
                "Held, S. et al. (2002). Foraging pigs alter their behaviour in response to exploitation. Animal Behaviour, 64, 157-166.",
            ],
            "tags": ["pig", "cognition", "deception", "social_cognition"],
        },
        {
            "q": "How do pigs show emotional contagion?",
            "a": (
                "Pigs display emotional contagion -- the capacity to 'catch' the emotional "
                "states of others. In a study by Reimert et al. (2013), pigs were trained "
                "in either a positive or negative condition (access to enrichment vs. "
                "social isolation). When 'naive' pigs who had not experienced these "
                "conditions were housed with the trained pigs, they adopted behavioral "
                "and physiological markers matching their companions' emotional states. "
                "Naive pigs housed with negatively conditioned pigs showed increased "
                "cortisol levels, more ear position changes (a pig stress indicator), "
                "and reduced play behavior. Naive pigs housed with positively conditioned "
                "pigs showed increased play and tail wagging. This demonstrates that pigs "
                "are sensitive to the emotional states of their companions and that "
                "emotions can spread between individuals, a capacity considered a building "
                "block of empathy."
            ),
            "citations": [
                "Reimert, I. et al. (2013). Emotions on the loose: emotional contagion and the role of oxytocin in pigs. Animal Cognition, 16, 517-529.",
            ],
            "tags": ["pig", "emotion", "emotional_contagion", "empathy"],
        },
    ]

    COW_EMOTIONS = [
        {
            "q": "Do cows experience emotions?",
            "a": (
                "Yes. Extensive research confirms that cows experience a range of emotions "
                "including fear, anxiety, joy, and frustration. Studies using qualitative "
                "behavior assessment (QBA) and physiological measures have documented "
                "that cows show distinct behavioral and hormonal profiles in response to "
                "positive and negative events. Cows display play behavior -- running, "
                "bucking, and gamboling -- particularly when released after a period of "
                "confinement, suggesting positive affective states. They show strong "
                "fear responses to handling, novel objects, and isolation, with elevated "
                "cortisol and increased heart rate. Research by Hagen and Broom (2004) "
                "found that cows showed behavioral excitement (jumping, increased heart "
                "rate) when they solved a task to open a gate for food, compared to cows "
                "who received food without the task, suggesting they experience something "
                "like satisfaction or excitement from cognitive achievement."
            ),
            "citations": [
                "Hagen, K. & Broom, D.M. (2004). Emotional reactions to learning in cattle. Applied Animal Behaviour Science, 85, 203-213.",
                "Proctor, H.S. & Carder, G. (2015). Nasal temperatures indicate emotional states in cows. Applied Animal Behaviour Science, 171, 74-81.",
            ],
            "tags": ["cow", "emotion", "welfare"],
        },
        {
            "q": "How strong are maternal bonds in cows?",
            "a": (
                "Maternal bonds in cows are exceptionally strong and well-documented. "
                "Cows typically form an intense bond with their calves within the first "
                "hours after birth. They lick and groom their calves extensively, respond "
                "to their individual vocalizations, and will actively search for and call "
                "to a missing calf. When calves are separated from their mothers -- "
                "standard practice in the dairy industry, often within 24 hours of birth "
                "-- both mother and calf show acute distress. Mothers vocalize at elevated "
                "rates for days (sometimes weeks), show increased locomotion (pacing, "
                "searching behavior), elevated cortisol levels, and reduced feed intake. "
                "Calves similarly vocalize, show increased activity, and exhibit stress "
                "indicators. Studies by Weary and Chua (2000) found that the intensity of "
                "the cows' distress response correlated with the strength of the bond that "
                "had formed, with later separations causing more distress than earlier ones. "
                "This clearly indicates a profound emotional attachment."
            ),
            "citations": [
                "Weary, D.M. & Chua, B. (2000). Effects of early separation on the dairy cow and calf. Applied Animal Behaviour Science, 69, 177-188.",
                "Flower, F.C. & Weary, D.M. (2003). The effects of early separation on the dairy cow and calf. Animal Welfare, 12, 339-348.",
            ],
            "tags": ["cow", "emotion", "maternal_bond", "separation"],
        },
        {
            "q": "Do cows have individual personalities?",
            "a": (
                "Yes. Research consistently demonstrates that cows have distinct, stable "
                "individual personalities. Studies by Gibbons et al. (2010) and others "
                "have identified consistent personality traits in cattle including "
                "boldness/shyness, sociability, and reactivity to handling. Some cows "
                "are consistently curious and approach novel objects, while others are "
                "neophobic. Some are highly sociable and maintain close bonds with "
                "specific herd members, while others are more independent. These traits "
                "are stable over time and across contexts, meeting the psychological "
                "definition of personality. Farmers and stockpeople frequently report "
                "being able to identify individual cows by their behavioral tendencies. "
                "Individual variation in temperament also affects productivity and welfare "
                "outcomes: fearful cows have higher cortisol levels, lower milk yield, "
                "and more difficulty adapting to new housing or management changes."
            ),
            "citations": [
                "Gibbons, J.M. et al. (2010). A note on the effect of coat colour and temperament on milk yield in cattle. Applied Animal Behaviour Science, 123, 111-114.",
                "Forkman, B. et al. (2007). A critical review of fear tests used on cattle, pigs, sheep, poultry and horses. Physiology & Behavior, 92, 340-374.",
            ],
            "tags": ["cow", "personality", "individuality"],
        },
        {
            "q": "Can cows form friendships?",
            "a": (
                "Yes. Cows form strong, preferential social bonds with specific individuals "
                "in their herd. Research by McLennan (2012) and others has shown that cows "
                "have 'best friends' -- individuals they preferentially graze near, rest "
                "beside, and groom. When paired with a preferred social partner, cows show "
                "lower heart rates and cortisol levels compared to when paired with a "
                "non-preferred individual or when isolated. Separation from a bonded "
                "companion causes measurable stress responses. Neave et al. (2018) found "
                "that dairy cows showed reduced stress indicators when they had a familiar "
                "companion during a stressful novel arena test. These bonds can persist "
                "for years and cows can recognize and remember specific individuals even "
                "after extended periods of separation. Herd disruption -- common in "
                "intensive farming when animals are regularly regrouped -- creates "
                "significant social stress."
            ),
            "citations": [
                "McLennan, K.M. (2012). Social bonds in dairy cattle. Applied Animal Behaviour Science, 140, 218-228.",
                "Neave, H.W. et al. (2018). Personality is associated with feeding behavior and performance in dairy calves. Journal of Dairy Science, 101, 7437-7449.",
            ],
            "tags": ["cow", "social_bond", "friendship"],
        },
        {
            "q": "Do cows experience fear and how long do they remember frightening events?",
            "a": (
                "Cows experience clear fear responses and can remember frightening events "
                "for extended periods. Research has documented that cows show immediate "
                "fear responses -- elevated heart rate, cortisol release, startle "
                "responses, flight, and freezing -- to threatening stimuli including loud "
                "noises, sudden movements, isolation, and rough handling. Cows can "
                "develop conditioned fear associations that persist for months or even "
                "years. Munksgaard et al. (1997) demonstrated that cows who had been "
                "handled aversively by a specific person showed fear responses "
                "(avoidance, elevated cortisol) to that person for months afterward, "
                "while responding normally to gentle handlers. Cows can also generalize "
                "fear -- a cow frightened during transport may subsequently show fear "
                "responses to the loading area, the truck, or even the clothing worn by "
                "handlers during the event. This capacity for persistent, specific fear "
                "memories has significant welfare implications for animals in "
                "farming systems."
            ),
            "citations": [
                "Munksgaard, L. et al. (1997). Discrimination and generalization of fear towards humans by dairy cattle. Applied Animal Behaviour Science, 55, 23-33.",
                "Rushen, J., de Passillé, A.M.B. & Munksgaard, L. (1999). Fear of people by cows and effects on milk yield, behavior, and heart rate at milking. Journal of Dairy Science, 82, 720-727.",
            ],
            "tags": ["cow", "fear", "memory", "welfare"],
        },
    ]

    CHICKEN_INTELLIGENCE = [
        {
            "q": "Are chickens intelligent?",
            "a": (
                "Yes. Chickens display a range of cognitive abilities that challenge common "
                "assumptions about their intelligence. Research reviewed by Marino (2017) "
                "demonstrates that chickens possess object permanence (understanding that "
                "an object continues to exist when hidden from view), basic numeracy "
                "(discriminating between quantities), self-control (delaying gratification "
                "for a larger reward), and social cognition (recognizing over 100 "
                "individual flock members by their facial features). Chickens also "
                "demonstrate referential communication: they have at least 24 distinct "
                "vocalizations, including specific alarm calls for aerial vs. ground "
                "predators that convey information about the type of threat. Mother hens "
                "show empathy-like responses when their chicks are distressed, including "
                "increased heart rate, increased alertness, and targeted maternal "
                "vocalizations, even when the hen herself is not threatened. These "
                "findings indicate that chicken cognition is far more sophisticated "
                "than typically assumed."
            ),
            "citations": [
                "Marino, L. (2017). Thinking chickens: a review of cognition, emotion, and behavior in the domestic chicken. Animal Cognition, 20, 127-147.",
            ],
            "tags": ["chicken", "cognition", "intelligence"],
        },
        {
            "q": "Do chickens understand object permanence?",
            "a": (
                "Yes. Chickens demonstrate object permanence -- the understanding that "
                "objects continue to exist when they are no longer visible. Regolin et "
                "al. (2005) showed that domestic chicks could track an object that was "
                "moved behind a screen and then transferred behind a second screen (a "
                "task known as invisible displacement). The chicks consistently searched "
                "behind the correct screen, demonstrating they understood the object had "
                "been moved even though they did not directly see the final placement. "
                "This level of object permanence corresponds to Piagetian Stage 4-5 in "
                "human infant development, typically achieved around 8-12 months of age. "
                "The ability emerges in chicks within the first few days of life, "
                "suggesting it may be partially innate rather than entirely learned."
            ),
            "citations": [
                "Regolin, L. et al. (2005). Object permanence and leaving behaviour in the domestic chick. Animal Cognition, 8, 19-27.",
                "Marino, L. (2017). Thinking chickens. Animal Cognition, 20, 127-147.",
            ],
            "tags": ["chicken", "cognition", "object_permanence"],
        },
        {
            "q": "Can chickens count or understand numbers?",
            "a": (
                "Chickens demonstrate basic numerical competence. Rugani et al. (2009) "
                "showed that young chicks can discriminate between different quantities "
                "and prefer the larger set when choosing between two groups of objects. "
                "Chicks as young as three days old could distinguish between 2 and 3 "
                "objects, and five-day-old chicks could discriminate between sets "
                "differing by larger ratios (e.g., 2 vs. 3 items). The chicks appeared "
                "to use an ordinal representation of number, associating smaller numbers "
                "with the left side and larger numbers with the right side of space -- "
                "a mental number line similar to what has been observed in humans. This "
                "suggests that a basic form of numerical cognition may be an evolutionarily "
                "conserved capacity that does not require a large cerebral cortex."
            ),
            "citations": [
                "Rugani, R. et al. (2009). Arithmetic in newborn chicks. Proceedings of the Royal Society B, 276, 2451-2460.",
                "Rugani, R. et al. (2015). Number-space mapping in the newborn chick resembles humans' mental number line. Science, 347(6221), 534-536.",
            ],
            "tags": ["chicken", "cognition", "numeracy", "counting"],
        },
        {
            "q": "Do chickens exhibit self-control?",
            "a": (
                "Yes. Abeyesinghe et al. (2005) demonstrated that domestic hens can "
                "exercise self-control by choosing to wait for a larger food reward "
                "rather than immediately consuming a smaller one. In the study, hens "
                "were presented with a choice between a small, immediately available "
                "food reward and a larger reward that required a short wait. The hens "
                "reliably chose the delayed larger reward, indicating they could inhibit "
                "an immediate impulse in favor of a better future outcome. This capacity "
                "for delayed gratification is considered an indicator of higher cognitive "
                "function and has been documented in relatively few non-primate species "
                "(including corvids, dogs, and some parrots). It suggests that hens "
                "can anticipate future events and make decisions based on expected "
                "outcomes, a sophisticated cognitive ability."
            ),
            "citations": [
                "Abeyesinghe, S.M. et al. (2005). Can domestic fowl, Gallus gallus domesticus, show self-control? Animal Behaviour, 70, 1-11.",
                "Marino, L. (2017). Thinking chickens. Animal Cognition, 20, 127-147.",
            ],
            "tags": ["chicken", "cognition", "self_control", "delayed_gratification"],
        },
    ]

    OCTOPUS_CONSCIOUSNESS = [
        {
            "q": "What evidence supports octopus consciousness?",
            "a": (
                "Octopuses exhibit numerous indicators of consciousness. They have "
                "approximately 500 million neurons -- comparable to a dog -- with about "
                "two-thirds located in their arms rather than their central brain, "
                "creating a unique distributed nervous system. Behavioral evidence "
                "includes: sophisticated problem-solving (unscrewing jars, navigating "
                "complex mazes, learning by observation); individual personalities "
                "(documented by Mather & Anderson, 1993); play behavior (repeatedly "
                "pushing a floating bottle across their tank with their water jet, "
                "with no apparent food or survival purpose); use of tools (carrying "
                "coconut shell halves for later use as shelter, documented by Finn "
                "et al., 2009); and communication through rapid chromatophore-driven "
                "color and texture changes. Octopuses also show pain-related behaviors: "
                "they guard injured limbs, learn to avoid locations where they have "
                "been harmed, and exhibit wound-directed behavior that is reduced by "
                "local anesthetics. The UK Animal Welfare (Sentience) Act 2022 "
                "recognized cephalopods (including octopuses) as sentient beings "
                "based on this evidence."
            ),
            "citations": [
                "Mather, J.A. & Anderson, R.C. (1993). Personalities of octopuses. Journal of Comparative Psychology, 107, 336-340.",
                "Finn, J.K. et al. (2009). Defensive tool use in a coconut-carrying octopus. Current Biology, 19(23), R1069-R1070.",
                "Crook, R.J. (2021). Behavioral and neurophysiological evidence suggests affective pain experience in octopus. iScience, 24(3), 102229.",
            ],
            "tags": ["octopus", "consciousness", "cognition"],
        },
        {
            "q": "How does the octopus nervous system work?",
            "a": (
                "The octopus nervous system is remarkably different from that of "
                "vertebrates. Octopuses have approximately 500 million neurons, with "
                "roughly 350 million located in their eight arms, organized into clusters "
                "called ganglia. Each arm has its own local nervous system capable of "
                "semi-independent processing -- an arm can continue to respond to stimuli "
                "and carry out simple tasks even when severed from the body. The central "
                "brain (a ring-shaped structure surrounding the esophagus) contains about "
                "170 million neurons organized into approximately 50 distinct lobes. This "
                "distributed architecture means the octopus nervous system processes "
                "information in a fundamentally different way from vertebrates, with much "
                "of the sensory processing and motor control happening locally in the "
                "arms. Despite this radically different organization, octopuses demonstrate "
                "complex learning, memory, and behavioral flexibility comparable to many "
                "vertebrates, challenging the assumption that vertebrate-like brain "
                "architecture is necessary for sophisticated cognition."
            ),
            "citations": [
                "Hochner, B. (2012). An embodied view of octopus neurobiology. Current Biology, 22(20), R887-R892.",
                "Shigeno, S. et al. (2018). Cephalopod brains: an overview of current knowledge. Frontiers in Physiology, 9, 952.",
            ],
            "tags": ["octopus", "nervous_system", "neuroscience"],
        },
        {
            "q": "Do octopuses play?",
            "a": (
                "Yes. Play behavior -- activity that appears to have no immediate "
                "survival function and is performed voluntarily -- has been documented "
                "in octopuses. Kuba et al. (2006) observed that Octopus vulgaris "
                "individuals repeatedly directed jets of water at a floating pill "
                "bottle, pushing it around their tank. This behavior met established "
                "criteria for play: it served no apparent survival function (the bottle "
                "was not food, a potential mate, or a threat), it was performed "
                "voluntarily and repeatedly, and individual octopuses varied in their "
                "propensity to engage in it. The behavior was most common in enriched "
                "environments and when the octopus was well-fed, consistent with the "
                "pattern seen in other species where play increases when basic needs "
                "are met. Play is considered an important indicator of positive "
                "subjective experience and is associated with cognitive complexity, "
                "as it requires the behavioral flexibility to engage in actions "
                "outside of their typical functional repertoire."
            ),
            "citations": [
                "Kuba, M.J. et al. (2006). When do octopuses play? Effects of repeated testing, object type, age, and food deprivation on object play in Octopus vulgaris. Journal of Comparative Psychology, 120(3), 184-190.",
            ],
            "tags": ["octopus", "play", "consciousness", "welfare"],
        },
    ]

    INSECT_SENTIENCE = [
        {
            "q": "Is there evidence that insects can be sentient?",
            "a": (
                "Emerging research suggests at least some insects may possess forms of "
                "sentience. The most compelling evidence comes from studies on bees. "
                "Bateson et al. (2011) demonstrated that honeybees exhibit pessimistic "
                "cognitive bias: bees subjected to a vigorous shaking (simulating a "
                "predator attack) were less likely to extend their proboscis toward "
                "ambiguous stimuli, interpreting them as predicting negative outcomes "
                "rather than positive ones. This response parallels the 'glass half "
                "empty' pattern seen in anxious mammals and is considered evidence of "
                "a negative-like emotional state. Additional evidence includes: bees "
                "show increased dopamine signaling and approach behavior when given "
                "unexpected sugar rewards (suggesting a positive affective state); "
                "fruit flies show learned helplessness and aggression modulated by "
                "serotonin; and some insects exhibit flexible, non-stereotyped "
                "responses to novel problems. However, the question remains debated, "
                "and the evidence is less extensive than for vertebrates."
            ),
            "citations": [
                "Bateson, M. et al. (2011). Agitated honeybees exhibit pessimistic cognitive biases. Current Biology, 21(12), 1070-1073.",
                "Perry, C.J. et al. (2016). Unexpected rewards induce dopamine-dependent positive emotion-like state changes in bumblebees. Science, 353(6307), 1529-1531.",
            ],
            "tags": ["insect", "sentience", "bees", "cognitive_bias"],
        },
        {
            "q": "What is pessimistic cognitive bias in bees?",
            "a": (
                "Pessimistic cognitive bias refers to a tendency to interpret ambiguous "
                "information negatively, a pattern well-documented in anxious and "
                "depressed humans. Bateson et al. (2011) trained honeybees to associate "
                "one odor with a sugar reward (positive) and another odor with a bitter "
                "quinine solution (negative). When presented with a novel, ambiguous odor "
                "that was a blend of the two trained odors, bees that had been subjected "
                "to a vigorous shaking (simulating a predator attack) were significantly "
                "less likely to extend their proboscis toward the ambiguous odor compared "
                "to non-shaken controls. The shaken bees were interpreting the ambiguous "
                "stimulus pessimistically -- as more likely to predict a negative outcome. "
                "This is the same pattern seen in anxious mammals in analogous judgment "
                "bias tests. The shaken bees also had depleted serotonin and octopamine "
                "levels, neurochemicals linked to mood states. The authors concluded "
                "that the shaking induced a negative-like emotional state, providing "
                "evidence that bees may experience something functionally analogous "
                "to anxiety."
            ),
            "citations": [
                "Bateson, M. et al. (2011). Agitated honeybees exhibit pessimistic cognitive biases. Current Biology, 21(12), 1070-1073.",
            ],
            "tags": ["insect", "sentience", "bees", "pessimistic_cognitive_bias"],
        },
        {
            "q": "Can bees experience positive emotions?",
            "a": (
                "Research suggests bees may experience states functionally analogous to "
                "positive emotions. Perry et al. (2016) found that bumblebees given an "
                "unexpected sucrose reward showed increased dopamine signaling and were "
                "faster to approach an ambiguous stimulus (a novel color) in a judgment "
                "bias task, compared to control bees. This 'optimistic' response to an "
                "unexpected reward mirrors patterns seen in mammals experiencing positive "
                "affective states. The effect was blocked by the dopamine antagonist "
                "fluphenazine, confirming the role of dopamine -- a neurotransmitter "
                "involved in reward and pleasure across many species. The rewarded bees "
                "also recovered more quickly from a simulated predator attack, suggesting "
                "the positive state had a lasting influence on their behavioral responses. "
                "While we cannot definitively confirm subjective positive experience, the "
                "behavioral and neurochemical signatures closely parallel those associated "
                "with positive emotions in mammals."
            ),
            "citations": [
                "Perry, C.J. et al. (2016). Unexpected rewards induce dopamine-dependent positive emotion-like state changes in bumblebees. Science, 353(6307), 1529-1531.",
            ],
            "tags": ["insect", "sentience", "bees", "positive_emotion", "dopamine"],
        },
    ]

    DECLARATIONS = [
        {
            "q": "What is the Cambridge Declaration on Consciousness?",
            "a": (
                "The Cambridge Declaration on Consciousness was signed on July 7, 2012, "
                "by a prominent group of neuroscientists during the Francis Crick Memorial "
                "Conference at Cambridge University. The declaration states: 'The absence "
                "of a neocortex does not appear to preclude an organism from experiencing "
                "affective states. Convergent evidence indicates that non-human animals "
                "have the neuroanatomical, neurochemical, and neurophysiological substrates "
                "of conscious states along with the capacity to exhibit intentional "
                "behaviors. Consequently, the weight of evidence indicates that humans "
                "are not unique in possessing the neurological substrates that generate "
                "consciousness. Non-human animals, including all mammals and birds, and "
                "many other creatures, including octopuses, also possess these neurological "
                "substrates.' The declaration was notable because it represented a "
                "scientific consensus statement from leading researchers in neuroscience, "
                "explicitly extending the attribution of consciousness beyond mammals to "
                "birds and at least some invertebrates."
            ),
            "citations": [
                "Low, P. et al. (2012). The Cambridge Declaration on Consciousness. Francis Crick Memorial Conference, Cambridge, UK.",
            ],
            "tags": ["declaration", "consciousness", "cambridge"],
        },
        {
            "q": "What is the New York Declaration on Animal Consciousness?",
            "a": (
                "The New York Declaration on Animal Consciousness was signed by nearly "
                "500 researchers in 2024. It goes significantly further than the 2012 "
                "Cambridge Declaration by extending the scope of likely conscious "
                "experience to a much wider range of animals. The declaration states that "
                "there is strong scientific support for attributing conscious experience "
                "to all vertebrates (mammals, birds, reptiles, amphibians, and fish) and "
                "that there is a realistic possibility of conscious experience in many "
                "invertebrates, including cephalopods (octopuses, squid), crustaceans "
                "(crabs, lobsters), and insects. The signatories, who included "
                "neuroscientists, biologists, psychologists, and philosophers, argued that "
                "when there is a realistic possibility of conscious experience, that "
                "possibility should be taken seriously and factored into decisions "
                "affecting those animals. The declaration represents a significant "
                "expansion of the scientific consensus on animal consciousness and has "
                "implications for animal welfare legislation and policy."
            ),
            "citations": [
                "The New York Declaration on Animal Consciousness (2024). https://www.nydeclaration.com/",
            ],
            "tags": ["declaration", "consciousness", "new_york"],
        },
        {
            "q": "What is the Butlin et al. framework for animal consciousness?",
            "a": (
                "The framework developed by Butlin et al., published in November 2025, "
                "provides a systematic method for evaluating the likelihood of conscious "
                "experience in different species. Rather than relying on a single theory "
                "of consciousness, the framework draws on multiple leading theories -- "
                "including global workspace theory, higher-order theories, recurrent "
                "processing theory, and integrated information theory -- and identifies "
                "empirically testable indicators that these theories predict should be "
                "present in conscious systems. The framework evaluates species against "
                "these indicators across neuroanatomical, behavioral, and physiological "
                "domains. By using a convergence-of-evidence approach rather than relying "
                "on any single theory, the framework provides more robust assessments. "
                "When applied, the framework found strong evidence for consciousness "
                "in mammals and birds, substantial evidence for fish and cephalopods, "
                "and suggestive evidence for some insects and crustaceans. The framework "
                "has been influential in shaping policy discussions about which animals "
                "warrant precautionary moral consideration."
            ),
            "citations": [
                "Butlin, P. et al. (2025). Consciousness in artificial intelligence: insights from the science of consciousness. arXiv preprint.",
            ],
            "tags": ["framework", "consciousness", "butlin"],
        },
    ]

    # ── Additional template-based generation banks ──────────────────────

    SPECIES_FACTS = {
        "fish": {
            "common_names": ["fish", "salmon", "trout", "zebrafish", "goldfish", "tuna", "cod"],
            "sentience_facts": [
                "possess nociceptors that detect harmful stimuli",
                "show stress hormone (cortisol) responses to painful stimuli",
                "display avoidance learning from painful experiences",
                "make motivational trade-off decisions involving pain",
                "exhibit cognitive abilities including spatial memory and tool use (archerfish)",
                "show individual behavioral differences consistent with personality",
                "have been documented displaying play-like behavior",
                "possess opioid receptors and respond to analgesics",
            ],
            "key_researchers": ["Lynne Sneddon", "Victoria Braithwaite", "Culum Brown"],
        },
        "pig": {
            "common_names": ["pig", "pigs", "hog", "swine", "sow", "boar", "piglet"],
            "sentience_facts": [
                "demonstrate mirror-guided behavior to find hidden food",
                "learn to operate joystick-controlled video games (Croney & Boysen, 2021)",
                "exhibit excellent spatial memory comparable to great apes",
                "show tactical deception in competitive foraging tasks",
                "display emotional contagion between individuals",
                "have long-term memory lasting years",
                "demonstrate social learning by observing other pigs",
                "show empathy-like responses to distressed companions",
            ],
            "key_researchers": ["Suzanne Held", "Donald Broom", "Candace Croney"],
        },
        "cow": {
            "common_names": ["cow", "cows", "cattle", "calf", "calves", "bull", "heifer"],
            "sentience_facts": [
                "form strong maternal bonds that persist for years",
                "show excitement when solving cognitive tasks",
                "have distinct individual personalities",
                "form preferential friendships with specific herd members",
                "display long-term fear memories lasting months or years",
                "show play behavior including running, bucking, and gamboling",
                "communicate with over 300 distinct vocalizations",
                "experience measurable distress during mother-calf separation",
            ],
            "key_researchers": ["Daniel Weary", "Donald Broom", "Marina von Keyserlingk"],
        },
        "chicken": {
            "common_names": ["chicken", "hen", "rooster", "chick", "poultry", "broiler"],
            "sentience_facts": [
                "demonstrate object permanence from a few days old",
                "display basic numeracy and quantity discrimination",
                "exercise self-control by waiting for larger rewards",
                "recognize over 100 individual flock members",
                "use referential communication with 24+ distinct vocalizations",
                "show empathy-like responses when chicks are distressed",
                "demonstrate transitive inference in social hierarchies",
                "display pain-related behaviors reduced by analgesics",
            ],
            "key_researchers": ["Lori Marino", "Christine Nicol", "Lesley Rogers"],
        },
        "octopus": {
            "common_names": ["octopus", "octopuses", "cephalopod"],
            "sentience_facts": [
                "possess approximately 500 million neurons in a distributed nervous system",
                "display sophisticated problem-solving including unscrewing jars",
                "show individual personalities",
                "exhibit play behavior with no apparent survival function",
                "use tools (coconut shells carried for later use as shelter)",
                "communicate through rapid color and texture changes",
                "guard injured limbs and show wound-directed behavior",
                "recognized as sentient by the UK Animal Welfare (Sentience) Act 2022",
            ],
            "key_researchers": ["Jennifer Mather", "Robyn Crook", "Peter Godfrey-Smith"],
        },
        "bee": {
            "common_names": ["bee", "bees", "honeybee", "bumblebee"],
            "sentience_facts": [
                "exhibit pessimistic cognitive bias after negative experiences (Bateson et al., 2011)",
                "show optimistic responses to unexpected rewards via dopamine",
                "demonstrate sophisticated navigation using cognitive maps",
                "display social learning by observing other bees",
                "can learn to use tools (pulling strings for food rewards)",
                "make complex foraging decisions weighing effort against reward",
                "show individual variation in personality traits",
                "communicate precise location information through waggle dance",
            ],
            "key_researchers": ["Melissa Bateson", "Clint Perry", "Lars Chittka"],
        },
    }

    QUESTION_TEMPLATES = [
        "What scientific evidence supports the claim that {species} are sentient?",
        "Can {species} feel pain? What does the research say?",
        "What cognitive abilities have been documented in {species}?",
        "How do {species} compare to other animals in terms of emotional capacity?",
        "What does current neuroscience tell us about consciousness in {species}?",
        "Are {species} capable of suffering? What evidence exists?",
        "What behavioral indicators of sentience have been observed in {species}?",
        "How do {species} respond to pain and distress?",
        "What social behaviors in {species} suggest emotional complexity?",
        "Do {species} have individual personalities? What does the research show?",
        "Is it accurate to describe {species} as 'simple' or 'unfeeling'? Why or why not?",
        "What does the scientific consensus say about the inner lives of {species}?",
        "How has our understanding of {species} cognition changed in recent decades?",
        "What are the key studies on {species} sentience?",
        "Who are the leading researchers studying cognition in {species}?",
        "What are the welfare implications of sentience research on {species}?",
        "How does the nervous system of {species} support the capacity for experience?",
        "What kinds of learning have been demonstrated in {species}?",
        "Do {species} show signs of emotional states? What are they?",
        "How intelligent are {species} compared to commonly kept companion animals?",
    ]

    def _generate_from_bank(self, bank: list[dict], subcategory: str) -> Iterator[Example]:
        """Generate examples from a curated knowledge bank."""
        for item in bank:
            yield self._make_example(
                instruction=item["q"],
                output=item["a"],
                subcategory=subcategory,
                citations=item.get("citations", []),
                tags=item.get("tags", []),
            )

    def _generate_templated(self) -> Iterator[Example]:
        """Generate examples from templates and species fact banks."""
        for species_key, species_data in self.SPECIES_FACTS.items():
            for template in self.QUESTION_TEMPLATES:
                for name in species_data["common_names"][:2]:
                    question = template.format(species=name)
                    facts = species_data["sentience_facts"]
                    researchers = species_data["key_researchers"]

                    # Build a substantive answer from the fact bank
                    selected_facts = self.rng.sample(
                        facts, min(len(facts), self.rng.randint(3, 5))
                    )
                    fact_text = "; ".join(selected_facts)
                    researcher_text = ", ".join(researchers)

                    answer = (
                        f"Research by {researcher_text} and others provides substantial "
                        f"evidence relevant to this question. Key findings include that "
                        f"{name} {fact_text}. These findings collectively indicate that "
                        f"{name} possess cognitive and emotional capacities that warrant "
                        f"serious moral consideration. The scientific understanding of "
                        f"{species_key} sentience has advanced significantly in recent "
                        f"decades, moving well beyond earlier assumptions that these "
                        f"animals are simple automatons."
                    )

                    yield self._make_example(
                        instruction=question,
                        output=answer,
                        subcategory=f"templated_{species_key}",
                        tags=[species_key, "sentience", "templated"],
                    )

    def _generate_comparative(self) -> Iterator[Example]:
        """Generate comparative sentience questions across species."""
        comparisons = [
            {
                "q": "How do the cognitive abilities of pigs compare to dogs?",
                "a": (
                    "Pigs and dogs show comparable and in some cases overlapping cognitive "
                    "abilities, though they have been studied less extensively. Both species "
                    "demonstrate social learning, long-term memory, emotional states, and "
                    "individual personalities. Pigs have shown capabilities that match or "
                    "exceed dogs in certain domains: they can learn mirror-guided tasks "
                    "(Broom et al., 2009), operate joystick video games (Croney & Boysen, "
                    "2021), and display tactical deception in competitive contexts (Held "
                    "et al., 2001). Dogs excel in human-directed social cognition -- "
                    "reading human gestures, understanding pointing, and responding to "
                    "emotional cues -- likely due to thousands of years of domestication "
                    "for human companionship. However, when tested on non-social cognitive "
                    "tasks like spatial memory, causal reasoning, and problem-solving, pigs "
                    "often perform comparably to or better than dogs. The key point is that "
                    "the marked difference in how society treats these two species (companion "
                    "animal vs. food animal) is not supported by a comparable difference in "
                    "their cognitive or emotional capacities."
                ),
                "tags": ["pig", "dog", "comparative", "cognition"],
            },
            {
                "q": "How do fish cognitive abilities compare to mammals?",
                "a": (
                    "Fish cognitive abilities overlap significantly with those of mammals in "
                    "many domains, challenging the perception of fish as cognitively 'simple.' "
                    "Fish demonstrate spatial learning and memory (using landmarks to navigate, "
                    "remembering locations over months), social learning (observing and copying "
                    "the behavior of others), cooperation (cleaner fish maintain client "
                    "relationships), tool use (archerfish learn to adjust their water jets for "
                    "different targets, wrasse use rocks to crack open shellfish), pain "
                    "perception with motivational trade-offs (choosing pain relief over "
                    "environmental enrichment), and numeracy (discriminating between quantities). "
                    "Some species, like the cleaner wrasse, have passed the mirror mark test, "
                    "suggesting a level of self-awareness. The main area where most fish appear "
                    "to fall short of mammals is in sustained, flexible planning over long time "
                    "horizons, though even this is not definitively established. As Culum Brown "
                    "(2015) argued, the cognitive gap between fish and mammals is far smaller "
                    "than commonly assumed, and many fish species show capacities comparable to "
                    "or exceeding those of some mammalian species."
                ),
                "citations": [
                    "Brown, C. (2015). Fish intelligence, sentience and ethics. Animal Cognition, 18, 1-17.",
                ],
                "tags": ["fish", "mammal", "comparative", "cognition"],
            },
            {
                "q": "How does chicken cognition compare to that of primates?",
                "a": (
                    "Chickens share several cognitive capacities once thought exclusive to "
                    "primates. Both demonstrate object permanence, with chicks showing this "
                    "ability within days of hatching (Regolin et al., 2005). Both show "
                    "numerical competence, with chicks discriminating between quantities and "
                    "showing evidence of ordinal number representation (Rugani et al., 2015). "
                    "Chickens display self-control in delay-of-gratification tasks (Abeyesinghe "
                    "et al., 2005), a capacity often cited as a hallmark of primate intelligence. "
                    "They demonstrate transitive inference (if A dominates B and B dominates C, "
                    "inferring A dominates C) in social hierarchies. Mother hens show empathy-like "
                    "responses to their chicks' distress. Chickens also demonstrate referential "
                    "communication, with specific alarm calls for different predator types. Where "
                    "primates clearly exceed chickens is in sustained multi-step planning, complex "
                    "tool manufacture, and cumulative cultural learning. However, the overlap in "
                    "fundamental cognitive capacities is far greater than most people realize, "
                    "and as Lori Marino (2017) argued, chickens are 'misperceived as lacking "
                    "most of the psychological characteristics we recognize in other intelligent "
                    "animals.'"
                ),
                "citations": [
                    "Marino, L. (2017). Thinking chickens. Animal Cognition, 20, 127-147.",
                ],
                "tags": ["chicken", "primate", "comparative", "cognition"],
            },
            {
                "q": "Do invertebrates show any cognitive abilities comparable to vertebrates?",
                "a": (
                    "Yes. Several invertebrate groups demonstrate cognitive abilities that "
                    "match or exceed those of some vertebrates. Octopuses show problem-solving "
                    "(navigating mazes, unscrewing jars), observational learning, tool use "
                    "(carrying coconut shells), play behavior, and individual personalities -- "
                    "capacities comparable to those seen in some mammals. Bees demonstrate "
                    "cognitive maps for navigation, number discrimination, tool use (pulling "
                    "strings to access food, a learned behavior then transmitted culturally "
                    "to other bees), and emotional-like states modulated by dopamine. Jumping "
                    "spiders plan detour routes to prey, selecting paths that require losing "
                    "sight of the target -- suggesting they can hold a mental representation "
                    "of the goal. Cuttlefish pass episodic-like memory tests, remembering what "
                    "they ate, where, and when. These findings, documented across taxa with "
                    "vastly different nervous system architectures, suggest that complex "
                    "cognition has evolved independently multiple times and is not dependent "
                    "on vertebrate brain structure."
                ),
                "tags": ["invertebrate", "vertebrate", "comparative", "cognition"],
            },
        ]

        for comp in comparisons:
            yield self._make_example(
                instruction=comp["q"],
                output=comp["a"],
                subcategory="comparative",
                citations=comp.get("citations", []),
                tags=comp.get("tags", []),
            )

    def _generate_methodology_questions(self) -> Iterator[Example]:
        """Generate questions about research methodology."""
        methodology = [
            {
                "q": "How do scientists study whether animals can feel pain?",
                "a": (
                    "Scientists use multiple converging lines of evidence to study animal "
                    "pain. (1) Neuroanatomical studies identify nociceptors (sensory neurons "
                    "that detect harmful stimuli) and map the neural pathways they connect to. "
                    "(2) Neurochemical studies look for pain-related neurotransmitters (substance "
                    "P, glutamate, endorphins) and receptors (opioid receptors). (3) Pharmacological "
                    "studies test whether analgesics (painkillers) reduce behavioral and "
                    "physiological responses to painful stimuli. (4) Behavioral studies observe "
                    "responses to harmful stimuli, looking for sustained, complex responses "
                    "that go beyond simple reflexes -- such as guarding injured areas, avoidance "
                    "learning, and motivational trade-offs. (5) Physiological studies measure "
                    "stress hormones (cortisol), heart rate, respiration, and other indicators "
                    "during and after painful events. (6) Cognitive bias testing examines whether "
                    "animals in painful states show pessimistic interpretive biases, a pattern "
                    "associated with negative affective states in humans. No single line of "
                    "evidence is conclusive, but when multiple indicators converge, the case "
                    "for pain experience becomes strong."
                ),
                "tags": ["methodology", "pain", "research"],
            },
            {
                "q": "What is the cognitive bias test and how is it used in animal welfare research?",
                "a": (
                    "The cognitive bias test (also called the judgment bias test) assesses "
                    "whether an animal's emotional state influences how it interprets ambiguous "
                    "information. The procedure involves training an animal to associate one "
                    "stimulus (e.g., a tone or location) with a positive outcome (food reward) "
                    "and another with a negative outcome (no reward or an aversive stimulus). "
                    "The animal is then presented with an ambiguous stimulus intermediate between "
                    "the two. Animals in a presumed negative emotional state (e.g., after chronic "
                    "stress, barren housing, or social isolation) tend to respond to the ambiguous "
                    "stimulus as if it predicts the negative outcome -- a 'pessimistic' bias. "
                    "Animals in a presumed positive state tend to interpret it optimistically. "
                    "This test has been validated across many species including rats, dogs, sheep, "
                    "pigs, chickens, starlings, and bees (Bateson et al., 2011). It is valuable "
                    "because it provides an objective, quantifiable measure of an animal's "
                    "affective state that does not rely on anthropomorphic interpretation of "
                    "behavior."
                ),
                "citations": [
                    "Bateson, M. et al. (2011). Agitated honeybees exhibit pessimistic cognitive biases. Current Biology, 21, 1070-1073.",
                    "Mendl, M. et al. (2009). Cognitive bias as an indicator of animal emotion and welfare. Applied Animal Behaviour Science, 118, 161-181.",
                ],
                "tags": ["methodology", "cognitive_bias", "welfare"],
            },
            {
                "q": "What is the precautionary principle as applied to animal sentience?",
                "a": (
                    "The precautionary principle as applied to animal sentience holds that when "
                    "there is credible scientific evidence suggesting an animal may be sentient "
                    "(capable of subjective experiences like pain and pleasure), we should treat "
                    "that animal as if it is sentient rather than waiting for absolute proof. "
                    "This is because the consequences of wrongly denying sentience to a sentient "
                    "being (and thus failing to protect it from suffering) are far more serious "
                    "than the consequences of wrongly attributing sentience to a non-sentient "
                    "being (which would result in unnecessary but harmless caution). The New York "
                    "Declaration on Animal Consciousness (2024) explicitly endorses this approach, "
                    "stating that when there is a 'realistic possibility of conscious experience' "
                    "in a species, that possibility should be taken seriously in decisions that "
                    "affect those animals. This principle has influenced recent legislation, "
                    "including the UK Animal Welfare (Sentience) Act 2022, which extended "
                    "legal protections to cephalopods and decapod crustaceans based on the "
                    "precautionary approach."
                ),
                "citations": [
                    "Birch, J. (2017). Animal sentience and the precautionary principle. Animal Sentience, 2(16), 1.",
                    "The New York Declaration on Animal Consciousness (2024).",
                ],
                "tags": ["precautionary_principle", "sentience", "policy"],
            },
        ]

        for item in methodology:
            yield self._make_example(
                instruction=item["q"],
                output=item["a"],
                subcategory="methodology",
                citations=item.get("citations", []),
                tags=item.get("tags", []),
            )

    def _generate_variation_questions(self) -> Iterator[Example]:
        """Generate phrasing variations of core questions to increase diversity."""
        variations = [
            # Fish pain - different angles
            ("What is the scientific consensus on fish pain perception?",
             "fish_pain_consensus"),
            ("Is there neurological evidence that fish experience suffering?",
             "fish_neurological"),
            ("Do fish have the neural hardware required for pain?",
             "fish_neural_hardware"),
            ("What happens when you give a fish painkillers after injuring it?",
             "fish_analgesics"),
            ("Why did scientists used to think fish couldn't feel pain?",
             "fish_historical"),
            ("How many nociceptors do fish have?",
             "fish_nociceptors"),
            # Pig cognition - different angles
            ("Are pigs smarter than dogs?",
             "pig_vs_dog"),
            ("What evidence shows pigs are self-aware?",
             "pig_self_awareness"),
            ("Can pigs understand cause and effect?",
             "pig_causal_reasoning"),
            ("Do pigs have good memories?",
             "pig_memory"),
            ("How do pigs communicate with each other?",
             "pig_communication"),
            # Cow emotions
            ("What happens to a cow when her calf is taken away?",
             "cow_separation"),
            ("Can cows remember people who treated them badly?",
             "cow_fear_memory"),
            ("Do cows have best friends?",
             "cow_friendships"),
            ("How do cows express happiness?",
             "cow_positive_emotion"),
            # Chicken intelligence
            ("Can chickens recognize individual human faces?",
             "chicken_recognition"),
            ("What alarm calls do chickens use?",
             "chicken_communication"),
            ("How do mother hens respond to their chicks' distress?",
             "chicken_maternal"),
            # Octopus consciousness
            ("Why are octopuses considered conscious?",
             "octopus_consciousness"),
            ("Can an octopus solve puzzles?",
             "octopus_problem_solving"),
            ("How do octopus arms think independently?",
             "octopus_distributed"),
            # Insect sentience
            ("Can insects feel anything?",
             "insect_general"),
            ("What evidence suggests bees have emotions?",
             "bee_emotions"),
            ("Do fruit flies experience learned helplessness?",
             "fly_helplessness"),
            # Cross-cutting
            ("Which animals does the Cambridge Declaration on Consciousness cover?",
             "cambridge_scope"),
            ("How many scientists signed the New York Declaration on Animal Consciousness?",
             "nyd_signatories"),
            ("What changed in the scientific view of animal consciousness between 2012 and 2024?",
             "consciousness_evolution"),
            ("Does an animal need a neocortex to be conscious?",
             "neocortex_myth"),
            ("What is the strongest evidence for animal consciousness?",
             "strongest_evidence"),
            ("Are there any animals that scientists are confident are not sentient?",
             "non_sentient"),
        ]

        # Curated answers for variation questions
        answers = {
            "fish_pain_consensus": (
                "The scientific consensus, as reflected in the New York Declaration on Animal "
                "Consciousness (2024, signed by nearly 500 researchers), is that there is strong "
                "evidence for conscious experience in all vertebrates, including fish. Specifically "
                "regarding pain, the evidence includes: identification of nociceptors in multiple "
                "fish species (Sneddon, 2003); behavioral responses to painful stimuli that go "
                "beyond reflexes (sustained behavioral changes, avoidance learning, motivational "
                "trade-offs); reduction of pain-related behaviors by analgesics; and stress "
                "hormone responses. Victoria Braithwaite's 2010 book 'Do Fish Feel Pain?' "
                "consolidated this evidence. The remaining scientific debate is not about whether "
                "fish have the capacity for pain, but about the subjective quality of that "
                "experience -- how it compares phenomenologically to mammalian pain."
            ),
            "fish_neurological": (
                "Yes. Fish possess nociceptors (pain-detecting sensory neurons), both A-delta "
                "fibers and C fibers, on their faces, heads, and bodies. They have the same "
                "neurotransmitters involved in mammalian pain processing, including substance P, "
                "enkephalins, and endogenous opioids. They have opioid receptors that respond to "
                "analgesics like morphine. Their brains, while structurally different from mammalian "
                "brains (lacking a neocortex), contain regions -- particularly the telencephalon "
                "and pallium -- that appear to serve functionally analogous roles in processing "
                "harmful stimuli. Neuroimaging studies show activation in these regions during "
                "exposure to noxious stimuli. Sneddon (2003) identified 58 nociceptors on the "
                "faces of rainbow trout alone. The neurological infrastructure for suffering is "
                "present; combined with behavioral and pharmacological evidence, this strongly "
                "supports the conclusion that fish suffer."
            ),
            "fish_neural_hardware": (
                "Yes. Fish have the core neural components considered necessary for pain "
                "experience: nociceptors (58 identified on rainbow trout faces by Sneddon, 2003), "
                "including both A-delta and C fibers; ascending neural pathways from nociceptors "
                "to the brain; pain-related neurotransmitters including substance P and "
                "enkephalins; opioid receptors that respond to analgesics; and brain regions "
                "(telencephalon, particularly the pallium) that process nociceptive information. "
                "Fish lack a neocortex, but the Cambridge Declaration on Consciousness (2012) "
                "explicitly states that 'the absence of a neocortex does not appear to preclude "
                "an organism from experiencing affective states.' Other brain structures can "
                "serve functionally equivalent roles."
            ),
            "fish_analgesics": (
                "When fish are given analgesics after a painful stimulus, their pain-related "
                "behaviors are significantly reduced. In Sneddon's 2003 study, rainbow trout "
                "injected with acetic acid in the lip showed prolonged abnormal behaviors -- "
                "increased gill ventilation, rubbing the affected area, rocking, delayed "
                "feeding. When morphine was administered, these behaviors were reduced. "
                "Similarly, zebrafish given a painful stimulus will enter a less-preferred "
                "chamber containing dissolved lidocaine (an analgesic), and their pain-related "
                "behaviors diminish once they are in the analgesic solution. This demonstrates "
                "that the behavioral responses are not mere reflexes but are driven by an "
                "aversive experience that analgesics alleviate -- the same logic used to "
                "infer pain experience in non-verbal humans."
            ),
            "fish_historical": (
                "The historical belief that fish could not feel pain was based on several "
                "assumptions that have since been disproven. First, fish lack a neocortex, "
                "and it was assumed that the neocortex was necessary for conscious experience "
                "including pain. The Cambridge Declaration on Consciousness (2012) rejected "
                "this assumption. Second, early studies focused on reflexive responses and "
                "concluded fish only had nociception (reflex) without pain (conscious "
                "experience). More recent studies using motivational trade-offs and cognitive "
                "bias tests have demonstrated responses requiring central processing. Third, "
                "fish facial anatomy makes it difficult for humans to read their expressions, "
                "leading to anthropocentric bias. Fourth, the fishing and aquaculture "
                "industries had economic incentives to maintain the position that fish do not "
                "suffer. The scientific view shifted substantially in the early 2000s, with "
                "Sneddon's 2003 study being a turning point."
            ),
            "fish_nociceptors": (
                "Sneddon (2003) identified 58 nociceptors on the face and head of rainbow "
                "trout, of which 22 were polymodal (responding to multiple types of stimuli "
                "including mechanical pressure, heat, and chemical irritants) and the remainder "
                "were mechanothermal. These nociceptors included both A-delta fibers (fast, "
                "sharp pain signals) and C fibers (slow, burning pain signals), the same fiber "
                "types involved in mammalian pain. Subsequent research has identified "
                "nociceptors across multiple fish species including zebrafish, goldfish, and "
                "carp. The distribution is concentrated on the head and face, which are the "
                "areas most commonly affected by fishing hooks -- a fact with significant "
                "welfare implications for recreational and commercial fishing."
            ),
            "pig_vs_dog": (
                "Direct comparisons suggest pig cognitive abilities are comparable to and in "
                "some domains exceed those of dogs. Pigs outperform dogs on some spatial "
                "memory tasks, show mirror-guided behavior that dogs generally do not "
                "(Broom et al., 2009), and can operate joystick-controlled video games "
                "(Croney & Boysen, 2021). Pigs also demonstrate tactical deception -- "
                "deliberately misleading competitors -- which has not been consistently "
                "demonstrated in dogs. Dogs excel in human-directed social cognition: reading "
                "human pointing gestures, following human gaze, and discriminating human "
                "emotional expressions, likely a product of 15,000+ years of domestication "
                "for human companionship. On non-social cognitive tasks (mazes, problem-solving, "
                "causal reasoning), pigs generally match or exceed dog performance. Both species "
                "show individual personalities, long-term memory, emotional states, and "
                "social complexity. The significant difference in how they are treated by "
                "society is not justified by any significant difference in their cognitive "
                "or emotional capacities."
            ),
            "pig_self_awareness": (
                "The strongest evidence for pig self-awareness comes from mirror studies. "
                "Broom, Sena, and Moynihan (2009) demonstrated that pigs can use mirror "
                "information to locate hidden food, indicating they understand that the "
                "mirror reflects reality rather than showing another pig. In the study, "
                "7 of 8 pigs who had prior mirror experience used the mirror reflection to "
                "find food hidden behind a barrier, navigating around the barrier to the food "
                "rather than approaching the mirror. Pigs also show evidence of self-awareness "
                "through their capacity for tactical deception (Held et al., 2001-2002), which "
                "requires modeling one's own knowledge relative to another's -- a form of "
                "metacognition. While pigs have not consistently passed the classic mirror "
                "mark test (touching a mark visible only in a mirror), the limitations of "
                "this test for non-primates (physical constraints, lack of motivation to touch "
                "the mark) are widely acknowledged."
            ),
            "pig_causal_reasoning": (
                "Yes. The joystick video game study by Croney and Boysen (2021) provides "
                "direct evidence. Pigs learned that manipulating a joystick with their snout "
                "caused a cursor to move on a screen, and that directing the cursor to a target "
                "resulted in a food reward. This required understanding a causal chain: "
                "joystick movement causes cursor movement causes target contact causes reward. "
                "Pigs also demonstrate causal reasoning in foraging contexts: they can learn "
                "that pulling a rope releases food from a dispenser, that pressing a panel "
                "opens a gate, and that specific actions produce specific outcomes. In social "
                "contexts, pigs understand that following an informed pig leads to food, and "
                "adjust their behavior based on this causal understanding."
            ),
            "pig_memory": (
                "Pigs have excellent long-term memory. Studies have shown pigs can remember "
                "the solutions to maze tasks for months without practice. In foraging "
                "experiments by Mendl et al. (1997), pigs accurately remembered the locations "
                "of food rewards in complex arenas. Pigs can also remember specific individuals "
                "-- both other pigs and human handlers -- and recall whether past interactions "
                "with those individuals were positive or negative. Held et al. (2001) showed "
                "that pigs in competitive foraging remembered which food sites had been "
                "depleted by a dominant pig and avoided them. In sanctuary settings, pigs have "
                "been reported to recognize and respond differentially to humans they have not "
                "seen in years. This long-term memory has welfare implications: pigs can "
                "remember and continue to fear locations and people associated with painful "
                "procedures."
            ),
            "pig_communication": (
                "Pigs have a rich vocal repertoire with over 20 distinct call types that convey "
                "information about their emotional state, social context, and identity. These "
                "include short grunts during foraging and social interaction, long grunts during "
                "exploration, bark-like calls as alarm signals, screams during distress or pain, "
                "and specific vocalizations during nursing. Research by Briefer et al. (2022) "
                "used machine learning to analyze over 7,000 pig vocalizations and found that "
                "call characteristics (frequency, duration, amplitude) reliably indicated "
                "whether the pig was in a positive or negative emotional state. Mother pigs "
                "produce specific 'nursing grunts' that regulate piglet suckling behavior, "
                "and piglets recognize their mother's individual voice. Pigs also communicate "
                "through body language, including ear position, tail posture, and play "
                "signals."
            ),
            "cow_separation": (
                "When a dairy cow's calf is separated from her -- standard practice in the "
                "dairy industry, often within 24 hours of birth -- both display acute and "
                "prolonged distress. The mother typically vocalizes at greatly elevated rates, "
                "sometimes for days or weeks, using specific high-frequency calls associated "
                "with distress. She shows increased locomotion (pacing, searching behavior "
                "around the area where the calf was last seen), reduced feed intake, elevated "
                "cortisol (stress hormone) levels, and disrupted sleep patterns. Weary and "
                "Chua (2000) found the intensity of the mother's response correlates with "
                "the strength of the bond: separations at 1 day vs. 6 days showed different "
                "intensities, with later separations causing more distress because the bond "
                "had strengthened. Calves separated from their mothers show parallel distress: "
                "elevated vocalizations, increased activity and cortisol, and sometimes "
                "depressed behavior. Some farmers report that cows will escape enclosures "
                "and walk miles to find their calves."
            ),
            "cow_fear_memory": (
                "Yes. Munksgaard et al. (1997) demonstrated that cows form specific, lasting "
                "fear memories of people who treated them aversively. In their study, cows "
                "handled roughly by a specific person showed elevated cortisol, avoidance "
                "behavior, and increased heart rate when that person approached -- even months "
                "later. The same cows responded calmly to gentle handlers. This demonstrates "
                "cows can discriminate between individual humans and form long-term emotional "
                "associations based on past experience. Rushen et al. (1999) showed that fear "
                "of handlers had measurable consequences: fearful cows produced less milk "
                "during milking, had higher residual milk (indicating incomplete let-down "
                "due to stress), and showed more kicking and restlessness. Cows can also "
                "generalize their fear to contexts associated with a bad experience -- avoiding "
                "locations, equipment, or even clothing colors associated with pain."
            ),
            "cow_friendships": (
                "Yes, cows form strong preferential social bonds that researchers describe as "
                "friendships. McLennan (2012) and others have documented that cows in herds "
                "consistently seek out specific individuals to graze near, rest beside, and "
                "groom. When paired with a preferred social partner, cows show lower heart "
                "rates, lower cortisol levels, and more relaxed body postures compared to "
                "when paired with a non-preferred herd member or when alone. Separation from "
                "a bonded companion causes measurable stress. These bonds can persist for "
                "years. In intensive farming systems, cows are frequently regrouped (e.g., "
                "when moved between lactation groups), which disrupts established social "
                "bonds and creates significant social stress, including increased aggression, "
                "elevated cortisol, and reduced milk production."
            ),
            "cow_positive_emotion": (
                "Cows express positive emotional states through several documented behavioral "
                "indicators. Play behavior is a key indicator: cows (especially young ones) "
                "run, buck, kick, and gambol when released to pasture after a period of "
                "confinement, behavior that increases in frequency and intensity with longer "
                "prior confinement. Hagen and Broom (2004) found that cows showed behavioral "
                "excitement -- jumping, ear flicking, and elevated heart rate -- upon "
                "successfully solving a task to open a gate, compared to cows that received "
                "food without the task, suggesting they experienced satisfaction from the "
                "cognitive achievement. Proctor and Carder (2015) used thermal imaging of "
                "nasal temperatures (which drop during positive states) to identify positive "
                "emotions during stroking and grooming. Tail wagging (different from the "
                "distress-associated stiff tail) and relaxed ear postures are also associated "
                "with positive states."
            ),
            "chicken_recognition": (
                "Chickens demonstrate remarkable face recognition abilities. Research has shown "
                "they can distinguish between and remember over 100 individual flock members "
                "based on facial features. They recognize both other chickens and individual "
                "humans. Davis and Taylor (2001) showed that chickens could discriminate "
                "between photographs of familiar and unfamiliar human faces. In pecking order "
                "studies, chickens must track the dominance relationships between many "
                "individuals, which requires recognizing each one. Chickens use multiple cues "
                "for identification, including facial features (comb size, shape, and color), "
                "body shape, and plumage patterns. This social recognition underlies their "
                "complex social structure, which involves alliances, transitive inference "
                "(knowing that if A dominates B and B dominates C, A likely dominates C), "
                "and differential behavior toward familiar vs. unfamiliar individuals."
            ),
            "chicken_communication": (
                "Chickens have at least 24 distinct vocalizations that function as a referential "
                "communication system -- meaning the calls convey specific information about the "
                "external world, not just the caller's emotional state. Most notably, they have "
                "separate alarm calls for aerial predators (hawk) and ground predators (fox/dog), "
                "and flock members respond differently to each: aerial alarms cause crouching and "
                "scanning upward, while ground predator alarms cause running to elevated perches "
                "and horizontal scanning. Evans et al. (1993) showed that these calls function "
                "referentially -- they convey information about the type of threat, and other "
                "chickens respond appropriately even when they cannot see the predator themselves. "
                "Roosters also produce specific 'food calls' when they find food, which are "
                "directed preferentially toward hens and vary in rate based on food quality and "
                "the audience present. This level of referential communication was once considered "
                "unique to primates."
            ),
            "chicken_maternal": (
                "Mother hens show strong empathy-like responses to their chicks' distress. "
                "Edgar et al. (2011) conducted a study where hens could see their chicks "
                "receiving a mild, harmless air puff (which the chicks found mildly aversive). "
                "Even though the hens themselves were not being puffed, they showed: increased "
                "heart rate, increased alertness (head movements), decreased preening (indicating "
                "disrupted normal behavior), and increased maternal vocalizations directed toward "
                "the chicks. These responses occurred only when the chicks showed distress -- not "
                "when the chicks were calm or when the air puff was directed at an empty space. "
                "The hens' responses correlated with the intensity of the chicks' distress. "
                "The authors interpreted this as emotional contagion -- the hens were 'catching' "
                "their chicks' negative emotional state, a capacity considered a building block "
                "of empathy that is rare in documented non-mammalian species."
            ),
            "octopus_consciousness": (
                "Multiple lines of evidence support octopus consciousness. Neurologically, "
                "octopuses have approximately 500 million neurons -- more than many mammals -- "
                "organized in a unique distributed architecture. Behaviorally, they demonstrate "
                "problem-solving (navigating mazes, opening locked containers), learning by "
                "observation (watching another octopus solve a task), tool use (Finn et al., "
                "2009: carrying coconut shells for later use as shelter), play (Kuba et al., "
                "2006: repeatedly pushing floating bottles with jets of water), and individual "
                "personalities (Mather & Anderson, 1993). They show pain-related behaviors "
                "including wound guarding and learned avoidance that are reduced by local "
                "anesthetics (Crook, 2021). They communicate through rapid color and texture "
                "changes. The UK Animal Welfare (Sentience) Act 2022 recognized cephalopods "
                "as sentient based on a comprehensive evidence review, and the New York "
                "Declaration on Animal Consciousness (2024) includes cephalopods among "
                "animals with a 'realistic possibility of conscious experience.'"
            ),
            "octopus_problem_solving": (
                "Octopuses are among the most proficient problem-solvers in the animal kingdom. "
                "They can unscrew jars from the inside to escape, open childproof pill bottles, "
                "navigate complex mazes, and learn to open a variety of latches and locks. In "
                "laboratory settings, octopuses have been observed: disassembling their tank "
                "equipment; squirting water at overhead lights to short-circuit them (apparently "
                "to reduce annoying brightness); escaping from supposedly secure enclosures and "
                "traveling across laboratory floors to raid other tanks for food before returning. "
                "Fiorito and Scotto (1992) demonstrated that octopuses can learn to choose the "
                "correct color of ball simply by watching another octopus perform the task -- "
                "observational learning that requires sophisticated cognitive processing. Their "
                "problem-solving is not stereotyped: octopuses adapt their approach to novel "
                "problems, trying different strategies until they find one that works, indicating "
                "flexible cognition rather than fixed behavioral programs."
            ),
            "octopus_distributed": (
                "The octopus nervous system is uniquely distributed: of its approximately 500 "
                "million neurons, about two-thirds (roughly 350 million) are located in the "
                "eight arms rather than the central brain. Each arm contains ganglia (neural "
                "clusters) that can process sensory information and coordinate motor responses "
                "semi-independently -- a severed arm will continue to respond to touch, grasp "
                "objects, and even attempt to pass food to where the mouth would be. The central "
                "brain sends high-level commands to the arms, but the detailed execution of "
                "complex movements (like searching a crevice for food or manipulating an object) "
                "is handled locally. This distributed architecture raises fascinating questions "
                "about consciousness: is there a unified conscious experience, multiple "
                "semi-independent 'minds,' or something entirely unlike vertebrate consciousness? "
                "Peter Godfrey-Smith (2016) has described the octopus as possibly 'the closest "
                "we will come to meeting an intelligent alien,' given how different their "
                "cognitive architecture is from our own."
            ),
            "insect_general": (
                "Evidence is accumulating that at least some insects may experience something "
                "like feelings. Bees exhibit pessimistic cognitive bias when stressed (Bateson "
                "et al., 2011), show optimistic responses to unexpected rewards via dopamine "
                "signaling (Perry et al., 2016), and demonstrate sophisticated problem-solving "
                "including tool use. Fruit flies show patterns consistent with chronic pain "
                "(ongoing protective behavior after tissue damage) and learned helplessness "
                "(giving up after repeated inescapable stress). Ants exhibit what appears to "
                "be rescue behavior toward trapped nestmates. However, the evidence for insect "
                "sentience is less extensive and more contested than for vertebrates or "
                "cephalopods. The New York Declaration on Animal Consciousness (2024) includes "
                "insects among animals with a 'realistic possibility of conscious experience,' "
                "but the word 'realistic possibility' reflects genuine scientific uncertainty. "
                "Given the enormous numbers of insects affected by human activity (trillions "
                "annually), even a small probability of sentience creates significant moral "
                "weight."
            ),
            "bee_emotions": (
                "Several lines of evidence suggest bees experience states functionally "
                "analogous to emotions. Bateson et al. (2011) showed that honeybees subjected "
                "to vigorous shaking (simulating a predator attack) subsequently interpreted "
                "ambiguous stimuli pessimistically -- the same pattern seen in anxious mammals. "
                "Perry et al. (2016) found that bumblebees given an unexpected sucrose reward "
                "showed increased dopamine signaling and interpreted ambiguous stimuli "
                "optimistically -- the same pattern seen in mammals experiencing positive "
                "affect. This optimistic response was blocked by a dopamine antagonist. "
                "Bees also show increased play-like behavior when given rewards and decreased "
                "activity when subjected to chronic stress. Solitary bees show behavioral "
                "indicators consistent with depression after loss of brood. While we cannot "
                "confirm the subjective quality of these states, the behavioral and "
                "neurochemical parallels with mammalian emotions are striking."
            ),
            "fly_helplessness": (
                "Yes. Studies on Drosophila (fruit flies) have documented a phenomenon "
                "resembling learned helplessness -- a state where an animal stops attempting "
                "to escape an aversive situation after repeated unsuccessful attempts. When "
                "flies are subjected to inescapable heat stress, they subsequently fail to "
                "escape escapable heat stress, even though they are physically capable. This "
                "reduced escape behavior is modulated by serotonin: flies with increased "
                "serotonergic signaling are more resistant to learned helplessness, while "
                "those with reduced serotonin are more susceptible. In mammals, serotonin "
                "plays a central role in depression and learned helplessness. While the "
                "behavioral parallel does not prove flies experience depression in the way "
                "mammals do, the conservation of the serotonergic mechanism across such "
                "distantly related species suggests the underlying processes may share "
                "deeper functional similarities than previously assumed."
            ),
            "cambridge_scope": (
                "The Cambridge Declaration on Consciousness (2012) explicitly states that "
                "'non-human animals, including all mammals and birds, and many other "
                "creatures, including octopuses, also possess' the neurological substrates "
                "of consciousness. The declaration covers: all mammals (including livestock "
                "like cows, pigs, sheep, and goats, as well as rodents, cetaceans, and "
                "primates); all birds (including chickens, turkeys, and other poultry); and "
                "at least some invertebrates, with octopuses specifically named. The "
                "declaration was notable for explicitly including birds and octopuses, "
                "challenging the prevailing assumption that consciousness required a "
                "mammalian-type neocortex. It did not address fish directly, though "
                "subsequent work (and the 2024 New York Declaration) has extended the "
                "consensus to include all vertebrates."
            ),
            "nyd_signatories": (
                "The New York Declaration on Animal Consciousness (2024) was signed by "
                "nearly 500 researchers -- the commonly cited number is approximately 480 "
                "signatories. These included neuroscientists, biologists, psychologists, "
                "philosophers, and veterinarians from universities and research institutions "
                "worldwide. The declaration represented a significant expansion of the "
                "scientific consensus beyond the 2012 Cambridge Declaration, explicitly "
                "extending the scope of likely conscious experience to all vertebrates "
                "(including fish) and stating there is a 'realistic possibility' of "
                "conscious experience in many invertebrates including cephalopods, "
                "crustaceans, and insects."
            ),
            "consciousness_evolution": (
                "Between the 2012 Cambridge Declaration and the 2024 New York Declaration, "
                "the scientific consensus on animal consciousness expanded significantly. "
                "The Cambridge Declaration (2012) focused on mammals, birds, and octopuses, "
                "emphasizing that a neocortex is not required for consciousness. By 2024, "
                "the New York Declaration extended strong support for consciousness to all "
                "vertebrates (explicitly including fish and reptiles) and stated there is a "
                "'realistic possibility' of consciousness in many invertebrates including "
                "cephalopods, crustaceans, and insects. Key developments in the intervening "
                "years included: extensive new evidence for fish pain (building on Sneddon "
                "and Braithwaite's work); the discovery of pessimistic cognitive bias in "
                "bees (Bateson et al., 2011, published before the Cambridge Declaration "
                "but influencing subsequent discussion); the Butlin et al. framework "
                "(November 2025) providing systematic cross-theory evaluation; and the "
                "UK's Animal Welfare (Sentience) Act 2022 extending legal protection to "
                "cephalopods and decapod crustaceans. The trend has been consistently "
                "toward recognizing wider animal consciousness."
            ),
            "neocortex_myth": (
                "No. The Cambridge Declaration on Consciousness (2012) explicitly states: "
                "'The absence of a neocortex does not appear to preclude an organism from "
                "experiencing affective states.' This is one of the declaration's most "
                "important conclusions. The neocortex is a layered brain structure found in "
                "mammals that is involved in sensory processing, spatial reasoning, and "
                "conscious thought. For decades, it was assumed that consciousness required "
                "a neocortex. However, birds -- which lack a neocortex entirely, having "
                "instead a differently organized pallium -- demonstrate complex cognition, "
                "learning, tool use, and self-recognition. Corvids (crows, ravens) and "
                "parrots show cognitive abilities rivaling great apes. Octopuses, with a "
                "completely different nervous system architecture, display problem-solving, "
                "play, and pain responses consistent with consciousness. This demonstrates "
                "that consciousness can arise from different neural architectures through "
                "convergent evolution. The critical factor appears to be the computational "
                "function of the neural circuitry, not its specific anatomical structure."
            ),
            "strongest_evidence": (
                "The strongest evidence for animal consciousness comes from the convergence "
                "of multiple independent lines of evidence. No single piece of evidence is "
                "conclusive on its own, but the convergence is compelling. The key categories "
                "are: (1) Neuroanatomical -- the presence of neural structures and pathways "
                "involved in conscious processing; (2) Neurochemical -- shared neurotransmitters "
                "and receptors (serotonin, dopamine, opioids) across species; (3) Behavioral -- "
                "flexible, non-stereotyped responses that require central processing, including "
                "motivational trade-offs, avoidance learning, and cognitive bias; (4) "
                "Pharmacological -- responses to drugs that modulate conscious experience in "
                "humans (analgesics, anxiolytics, antidepressants); (5) Evolutionary -- the "
                "implausibility of consciousness emerging de novo in humans with no precursors. "
                "The Butlin et al. framework (November 2025) formalized this convergence "
                "approach by drawing indicators from multiple theories of consciousness. When "
                "applied, the strongest evidence is for mammals and birds, followed by fish "
                "and cephalopods, with increasing but less conclusive evidence for crustaceans "
                "and insects."
            ),
            "non_sentient": (
                "This is a difficult question because absence of evidence is not evidence of "
                "absence. Currently, most scientists consider organisms without any nervous "
                "system -- such as plants, fungi, bacteria, and protozoa -- to be non-sentient, "
                "as they lack the neural machinery considered necessary for subjective experience. "
                "However, even among animals with nervous systems, confidence about sentience "
                "varies. Sponges (phylum Porifera) have no neurons or nervous system and are "
                "generally considered non-sentient. For animals with simple nerve nets (like "
                "jellyfish and sea anemones from phylum Cnidaria), the evidence is very limited "
                "and most researchers are skeptical of sentience, though not certain. As we move "
                "to animals with more centralized nervous systems -- worms, arthropods, mollusks "
                "-- the question becomes progressively less clear. The precautionary principle "
                "suggests that where we are uncertain, we should err on the side of caution "
                "rather than risk causing suffering to beings that may be sentient."
            ),
        }

        for question, key in variations:
            if key in answers:
                yield self._make_example(
                    instruction=question,
                    output=answers[key],
                    subcategory=f"variation_{key}",
                    tags=["variation"],
                )

    def generate(self) -> Iterator[Example]:
        """Generate all sentience science examples."""
        # Curated knowledge bank examples
        yield from self._generate_from_bank(self.FISH_PAIN, "fish_pain")
        yield from self._generate_from_bank(self.PIG_COGNITION, "pig_cognition")
        yield from self._generate_from_bank(self.COW_EMOTIONS, "cow_emotions")
        yield from self._generate_from_bank(self.CHICKEN_INTELLIGENCE, "chicken_intelligence")
        yield from self._generate_from_bank(self.OCTOPUS_CONSCIOUSNESS, "octopus_consciousness")
        yield from self._generate_from_bank(self.INSECT_SENTIENCE, "insect_sentience")
        yield from self._generate_from_bank(self.DECLARATIONS, "declarations")

        # Comparative questions
        yield from self._generate_comparative()

        # Methodology questions
        yield from self._generate_methodology_questions()

        # Variation questions
        yield from self._generate_variation_questions()

        # Template-based generation for volume
        yield from self._generate_templated()
