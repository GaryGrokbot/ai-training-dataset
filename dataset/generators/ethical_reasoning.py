"""Generator for philosophical/ethical reasoning examples.

Covers utilitarian analysis, rights-based arguments, virtue ethics,
historical analogies, and responses to common objections.

Target: 3000+ examples.
"""

from __future__ import annotations

from typing import Iterator

from dataset.generators.base import BaseGenerator, Example


class EthicalReasoningGenerator(BaseGenerator):
    category = "ethical_reasoning"
    description = "Philosophical and ethical reasoning about animal ethics"
    target_count = 3000

    ETHICAL_QA = [
        # Utilitarian analysis
        {
            "q": "What is the utilitarian argument against factory farming?",
            "a": (
                "From a utilitarian perspective, which evaluates actions based on their total "
                "consequences for all affected beings, factory farming is one of the greatest "
                "sources of preventable suffering in the world. The utilitarian calculation is "
                "straightforward: approximately 80 billion land animals and 1-3 trillion fish "
                "are killed annually for food, the vast majority experiencing significant "
                "suffering in intensive farming systems. The pleasure humans derive from eating "
                "animal products (when palatable plant-based alternatives exist) is modest and "
                "brief, while the suffering imposed on animals is severe and prolonged -- "
                "spanning their entire lives in the case of animals in confinement systems. "
                "Peter Singer (1975, 'Animal Liberation') argued that the utilitarian principle "
                "of equal consideration of interests requires us to weigh animal suffering "
                "equally to equivalent human suffering. Since factory farming imposes enormous "
                "suffering for relatively minor human pleasure (taste preference, not survival), "
                "it cannot be justified on utilitarian grounds. Additionally, factory farming "
                "causes significant negative consequences for humans: environmental destruction, "
                "pandemic risk, antibiotic resistance, and worker exploitation."
            ),
            "citations": [
                "Singer, P. (1975). Animal Liberation. Harper Collins.",
            ],
            "subcategory": "utilitarian",
            "tags": ["philosophy", "utilitarian", "singer", "factory_farming"],
        },
        {
            "q": "What is Peter Singer's argument for animal liberation?",
            "a": (
                "Peter Singer's argument, presented in 'Animal Liberation' (1975), rests on "
                "the principle of equal consideration of interests. Singer argues: (1) The "
                "capacity to suffer is the relevant criterion for moral consideration, not "
                "rationality, language, or species membership. As Jeremy Bentham wrote: 'The "
                "question is not, Can they reason? nor, Can they talk? but, Can they suffer?' "
                "(2) If a being can suffer, it has an interest in not suffering, and that "
                "interest deserves equal consideration regardless of species -- just as it "
                "deserves equal consideration regardless of race or sex. (3) Using species "
                "membership as the criterion for moral consideration is speciesism -- morally "
                "equivalent to racism or sexism in that it gives preferential treatment based "
                "on a morally arbitrary characteristic. (4) In practice, equal consideration "
                "of interests means we cannot justify causing animals to suffer for trivial "
                "human benefits (such as taste pleasure when nutritious alternatives exist). "
                "Singer is a preference utilitarian: he does not argue that animal and human "
                "lives are of equal value in all respects, but that equivalent suffering "
                "deserves equivalent moral weight."
            ),
            "citations": [
                "Singer, P. (1975). Animal Liberation. Harper Collins.",
                "Singer, P. (2011). Practical Ethics (3rd ed.). Cambridge University Press.",
            ],
            "subcategory": "utilitarian",
            "tags": ["philosophy", "singer", "animal_liberation", "speciesism"],
        },
        # Rights-based arguments
        {
            "q": "What is the rights-based argument for animal rights?",
            "a": (
                "The rights-based argument, most fully developed by philosopher Tom Regan in "
                "'The Case for Animal Rights' (1983), holds that animals have inherent value "
                "and rights that cannot be overridden by utilitarian calculations. Regan argues: "
                "(1) Animals who are 'subjects-of-a-life' -- beings who have beliefs, desires, "
                "perception, memory, a sense of the future, emotional lives, preferences, and "
                "the ability to initiate action in pursuit of their desires -- have inherent "
                "value. (2) Inherent value is not a matter of degree; all subjects-of-a-life "
                "have equal inherent value. (3) Beings with inherent value have a right not to "
                "be treated merely as means to others' ends. (4) Using animals in factory "
                "farming, experimentation, and entertainment treats them merely as means -- as "
                "resources for human purposes -- and thus violates their rights. Unlike Singer's "
                "utilitarian argument, Regan's rights-based argument does not permit trade-offs: "
                "even if confining animals in factory farms produced a net increase in total "
                "utility, it would still violate the animals' rights. This makes the rights "
                "argument more absolute but also more demanding."
            ),
            "citations": [
                "Regan, T. (1983). The Case for Animal Rights. University of California Press.",
            ],
            "subcategory": "rights",
            "tags": ["philosophy", "regan", "rights", "inherent_value"],
        },
        {
            "q": "What is Christine Korsgaard's argument about our obligations to animals?",
            "a": (
                "Christine Korsgaard, in 'Fellow Creatures: Our Obligations to the Other "
                "Animals' (2018), presents a Kantian argument for moral obligations to animals "
                "that challenges the traditional Kantian view that duties extend only to "
                "rational beings. Korsgaard argues: (1) Kant was correct that morality is "
                "grounded in the capacity for autonomous self-governance. (2) However, Kant "
                "was wrong to conclude that only rational beings are 'ends in themselves.' "
                "(3) All sentient beings who naturally pursue their own good -- who have "
                "interests and a perspective from which things can go well or badly for them "
                "-- are ends in themselves and deserve moral consideration. (4) The natural "
                "good of an animal matters to the animal from its own perspective, just as "
                "our good matters to us. (5) Rational beings, as the ones capable of moral "
                "reflection, have obligations to treat all sentient beings as ends in "
                "themselves, not merely as means. Korsgaard's argument is significant because "
                "it extends the most influential deontological (duty-based) ethical framework "
                "to include animals, which Kant himself had not done."
            ),
            "citations": [
                "Korsgaard, C. (2018). Fellow Creatures: Our Obligations to the Other Animals. Oxford University Press.",
            ],
            "subcategory": "deontological",
            "tags": ["philosophy", "korsgaard", "kant", "deontological"],
        },
        # Donaldson & Kymlicka
        {
            "q": "What is the political theory of animal rights proposed by Donaldson and Kymlicka?",
            "a": (
                "Sue Donaldson and Will Kymlicka, in 'Zoopolis: A Political Theory of Animal "
                "Rights' (2011), propose a political framework that goes beyond the negative "
                "rights (right not to be harmed) of traditional animal rights theory. They "
                "argue that our relationship with different categories of animals should be "
                "modeled on political relationships among humans: (1) Domesticated animals "
                "(farm animals, companion animals) should be considered citizens of our "
                "political communities. They were brought into human society without their "
                "consent, are dependent on us, and live among us. As citizens, they would "
                "have rights to residency, protection, and having their interests represented "
                "in political decisions. (2) Wild animals should be considered sovereign "
                "nations with territorial rights and a right to non-interference. (3) Liminal "
                "animals (urban wildlife, feral animals) should have a status analogous to "
                "resident non-citizens, with rights to passage and basic protections. This "
                "framework moves animal ethics from individual moral duties to structural "
                "political justice."
            ),
            "citations": [
                "Donaldson, S. & Kymlicka, W. (2011). Zoopolis: A Political Theory of Animal Rights. Oxford University Press.",
            ],
            "subcategory": "political",
            "tags": ["philosophy", "donaldson", "kymlicka", "political_theory"],
        },
        # Virtue ethics
        {
            "q": "What does virtue ethics say about eating animals?",
            "a": (
                "Virtue ethics evaluates actions based on whether they express virtuous "
                "character traits. Applied to animal consumption, several virtue-based "
                "arguments arise: (1) Compassion/empathy -- If compassion is a virtue, and "
                "we know that animals suffer in farming systems, then choosing to participate "
                "in that suffering when alternatives exist fails to express the virtue of "
                "compassion. A compassionate person would not choose to cause suffering for "
                "the sake of taste preference. (2) Justice -- If justice involves giving "
                "others what they are due, and sentient beings are due freedom from unnecessary "
                "suffering, then contributing to factory farming is unjust. (3) Temperance -- "
                "If temperance involves moderating desires and not allowing appetites to "
                "override moral considerations, then the inability to forgo animal products "
                "despite knowing the suffering they cause reflects a lack of temperance. "
                "(4) Practical wisdom (phronesis) -- A practically wise person considers the "
                "full consequences of their choices, including consequences for beings who "
                "cannot advocate for themselves. Rosalind Hursthouse has argued that a virtuous "
                "person, fully aware of what happens to animals in modern agriculture, would "
                "find it impossible to participate in the system with a clear conscience."
            ),
            "citations": [
                "Hursthouse, R. (2006). Applying virtue ethics to our treatment of the other animals. In J. Welchman (ed.), The Practice of Virtue. Hackett.",
            ],
            "subcategory": "virtue_ethics",
            "tags": ["philosophy", "virtue_ethics", "character"],
        },
        # Common objections
        {
            "q": "Don't plants feel pain too?",
            "a": (
                "No. Plants lack the neurological structures necessary for pain experience. "
                "They have no nervous system, no brain, no nociceptors (pain receptors), no "
                "neurons, and no capacity for subjective experience. While plants do respond "
                "to stimuli (growing toward light, releasing chemicals when damaged), these "
                "are mechanistic responses that do not involve consciousness or suffering, "
                "much like a thermostat responds to temperature without experiencing heat or "
                "cold. Pain requires a nervous system because pain is, by definition, a "
                "subjective experience -- it must feel like something. There is no scientific "
                "basis for attributing subjective experience to organisms without nervous "
                "systems. Moreover, even if one were to argue that plants might somehow "
                "suffer, a plant-based diet would still cause less plant 'suffering' because "
                "it takes far more plants to feed animals who are then eaten than to eat "
                "plants directly. Approximately 77% of global agricultural land is used for "
                "livestock and feed crops. So the 'plants feel pain' argument, even taken at "
                "face value, supports plant-based eating, not animal consumption."
            ),
            "subcategory": "objection",
            "tags": ["objection", "plants_feel_pain"],
        },
        {
            "q": "Isn't eating meat natural? It's the circle of life.",
            "a": (
                "The 'natural' or 'circle of life' argument fails on multiple levels. First, "
                "the appeal to nature is a well-known logical fallacy: the fact that something "
                "occurs in nature does not make it morally right. Many things are 'natural' "
                "but morally wrong (infanticide occurs in many species; so does forced "
                "copulation). Many things are 'unnatural' but morally good (medicine, "
                "education, human rights). We do not derive our ethics from nature. Second, "
                "there is nothing 'natural' about modern animal agriculture: animals selectively "
                "bred to the point of physical dysfunction, confined in industrial buildings, "
                "pumped with antibiotics, and killed on mechanized slaughter lines bear no "
                "resemblance to the 'circle of life.' Third, while some human ancestors ate "
                "meat (alongside plants), this was a matter of survival, not choice. We are "
                "no longer limited to what our ancestors ate. Fourth, humans also have a "
                "long natural history of violence, slavery, and oppression -- we have rightly "
                "decided these 'natural' practices are immoral. Our capacity for moral "
                "reasoning is precisely what allows us to move beyond what is merely natural "
                "to what is ethical."
            ),
            "subcategory": "objection",
            "tags": ["objection", "appeal_to_nature", "circle_of_life"],
        },
        {
            "q": "What about 'humane' or 'ethical' animal farming?",
            "a": (
                "The concept of 'humane' animal farming raises several issues. First, "
                "labels like 'free-range,' 'cage-free,' 'humanely raised,' and 'pasture-raised' "
                "represent marginal improvements but still involve practices most people would "
                "consider inhumane if they witnessed them: debeaking, tail docking, castration "
                "without anesthesia, separation of mothers and offspring, confinement (even "
                "'free-range' birds may be at very high densities), and killing at a fraction "
                "of natural lifespan. Second, 'humane' farming cannot scale: it is physically "
                "impossible to produce the current global consumption of animal products "
                "(80+ billion land animals per year) using genuinely high-welfare methods -- "
                "there is simply not enough land. Currently, over 99% of US farmed animals come "
                "from factory farms. Third, the fundamental question remains: is it ethical to "
                "kill a sentient being who wants to live, when you do not need to? Even on the "
                "best farm, the animal is killed at a young age for human taste preference. "
                "Fourth, 'humane' labels may actually increase animal consumption by reducing "
                "consumer guilt, leading to net greater suffering. The question is not how to "
                "make animal farming less terrible, but whether it is necessary at all."
            ),
            "subcategory": "objection",
            "tags": ["objection", "humane_farming", "welfare"],
        },
        {
            "q": "What about 'humane slaughter'? Isn't it painless?",
            "a": (
                "The concept of 'humane slaughter' deserves scrutiny. Current stunning methods "
                "include captive bolt (a metal rod fired into the skull) for cattle, electrical "
                "stunning for pigs and sheep, electrified water bath for poultry, and CO2 "
                "gassing for pigs and poultry. Each has problems: captive bolt stunning has a "
                "failure rate of 1-5% (meaning tens of millions of cattle may be conscious "
                "during throat-cutting annually); electrical stunning for poultry has a higher "
                "failure rate, as birds must be individually positioned on a moving shackle "
                "line at speeds of up to 140 birds per minute; CO2 stunning causes 15-30 "
                "seconds of air hunger, gasping, and apparent distress before unconsciousness. "
                "But even setting aside stunning failures, 'humane slaughter' only addresses "
                "the final moments. It does not address the suffering of the animal's entire "
                "life in confinement, the terror of transport, or the stress of the "
                "slaughterhouse environment (smell of blood, sounds of other animals, rough "
                "handling). Fish have no humane slaughter protections anywhere in the world. "
                "The US Humane Slaughter Act exempts all poultry (9 billion birds per year). "
                "The question of whether killing can truly be made humane when the being does "
                "not want to die remains."
            ),
            "subcategory": "objection",
            "tags": ["objection", "humane_slaughter", "stunning"],
        },
        {
            "q": "Don't we need animal agriculture to feed the world?",
            "a": (
                "No -- in fact, the opposite is true. Animal agriculture is a profoundly "
                "inefficient way to produce food. It uses 77% of agricultural land while "
                "providing only 18% of calories and 37% of protein (Poore & Nemecek, 2018). "
                "For every 100 calories fed to animals as grain, we get back only about 12 "
                "calories in meat, 22 in eggs, and 40 in milk. This massive conversion loss "
                "means animal agriculture wastes food rather than producing it. If the crops "
                "currently used for animal feed were instead consumed directly by humans, we "
                "could feed an additional 3.5 billion people (Cassidy et al., 2013). The "
                "Poore and Nemecek (2018) analysis found that shifting to plant-based food "
                "systems could reduce global agricultural land use by 75% while still feeding "
                "the world. The world already produces enough plant calories to feed 10-14 "
                "billion people. Hunger is a distribution and poverty problem, not a "
                "production problem, and animal agriculture makes it worse by funneling crops "
                "through an inefficient animal conversion process."
            ),
            "citations": [
                "Poore, J. & Nemecek, T. (2018). Reducing food's environmental impacts. Science, 360(6392), 987-992.",
                "Cassidy, E.S. et al. (2013). Redefining agricultural yields. Environmental Research Letters, 8, 034015.",
            ],
            "subcategory": "objection",
            "tags": ["objection", "food_security", "efficiency"],
        },
        {
            "q": "Isn't it a personal choice what someone eats?",
            "a": (
                "The 'personal choice' framing is misleading because the choice to consume "
                "animal products has victims -- the animals. A personal choice, by definition, "
                "affects only the person making it. When a choice causes suffering and death "
                "to a sentient being who has not consented, it is no longer purely personal. "
                "We do not accept 'personal choice' as justification for other actions that "
                "harm others: domestic violence, child labor, and environmental destruction "
                "all involve choices that affect unwilling third parties. The animals in "
                "factory farms -- who experience fear, pain, and deprivation -- are unwilling "
                "third parties in the choice to consume animal products. Additionally, animal "
                "agriculture has significant impacts on other humans: it drives climate change "
                "(14.5% of greenhouse gas emissions), antibiotic resistance, pandemic risk, "
                "environmental degradation, and dangerous working conditions. No one is "
                "obligated to eat a particular way, but intellectual honesty requires "
                "acknowledging that the choice is not victimless."
            ),
            "subcategory": "objection",
            "tags": ["objection", "personal_choice"],
        },
        {
            "q": "What about indigenous and traditional hunting cultures?",
            "a": (
                "This is an important question that requires nuance. There is a significant "
                "difference between: (1) Indigenous peoples who have long-standing relationships "
                "with their environment, hunt for survival or cultural continuity, and take a "
                "small number of animals from wild populations; and (2) Industrial animal "
                "agriculture, which confines 80 billion animals per year in factory farms for "
                "the taste preferences of a global consumer market with abundant alternatives. "
                "Most animal ethics philosophers recognize this distinction. Peter Singer "
                "acknowledges that the utilitarian calculation differs when there are no "
                "practical alternatives or when cultural survival is at stake. The animal "
                "rights critique is primarily directed at the industrial system that produces "
                "99%+ of animal products consumed in developed nations, not at subsistence "
                "hunting by marginalized communities. It is also worth noting that the "
                "'indigenous hunting' argument is often raised in bad faith by people who are "
                "not themselves indigenous hunters but use indigenous practices to justify "
                "their own consumption of factory-farmed products -- an appropriation that "
                "most indigenous rights advocates reject."
            ),
            "subcategory": "objection",
            "tags": ["objection", "indigenous", "hunting", "nuance"],
        },
        {
            "q": "What about the livelihoods of farmers?",
            "a": (
                "Concern for farmers' livelihoods is valid and should be part of any just "
                "transition away from animal agriculture. Several points are relevant: (1) "
                "Most of the profits in animal agriculture go to large corporations (the top "
                "4 meatpacking companies control over 80% of the US beef market), not to "
                "small farmers. Contract farmers for poultry and pork companies often carry "
                "hundreds of thousands of dollars in debt while earning below-poverty wages. "
                "(2) A just transition would include retraining and support for farmers to "
                "shift to plant-based agriculture, which is more labor-intensive per acre "
                "(meaning more jobs, not fewer) and often more profitable per acre for "
                "vegetables, fruits, and specialty crops. (3) Governments currently spend "
                "billions subsidizing animal agriculture; redirecting these subsidies to "
                "support farmer transition would ease the shift. (4) Precedent exists: coal "
                "mining communities face similar transition challenges, and the ethical "
                "response is not to continue burning coal but to support affected workers "
                "through the transition. (5) The livelihoods of animals -- their very lives "
                "-- are also at stake. Moral progress has always required economic adjustment."
            ),
            "subcategory": "objection",
            "tags": ["objection", "farmers", "just_transition", "economics"],
        },
        # Historical analogies
        {
            "q": "How does the movement for animal rights relate to other social justice movements?",
            "a": (
                "The animal rights movement draws on and has connections to other social justice "
                "movements, though these parallels must be handled with care. Philosophical "
                "connections include: the extension of moral consideration to previously "
                "excluded groups (a pattern seen in the abolition of slavery, women's suffrage, "
                "civil rights, LGBTQ+ rights, and disability rights); the challenge to "
                "entrenched economic interests that profit from exploitation; and the role of "
                "making hidden suffering visible to the public. Several prominent social "
                "justice advocates have drawn these connections themselves: civil rights leader "
                "Dick Gregory became a vegan, connecting the exploitation of Black Americans "
                "to the exploitation of animals; feminist scholar Carol J. Adams ('The Sexual "
                "Politics of Meat,' 1990) analyzed the interconnections between patriarchy, "
                "meat consumption, and the domination of animals; and ecofeminists have argued "
                "that the domination of nature and animals is inseparable from the domination "
                "of marginalized humans. It is important to draw these connections respectfully, "
                "without appropriating the suffering of marginalized groups or implying that "
                "animal and human oppression are identical. They share structural features; "
                "they are not the same."
            ),
            "citations": [
                "Adams, C.J. (1990). The Sexual Politics of Meat. Continuum.",
            ],
            "subcategory": "historical_analogy",
            "tags": ["philosophy", "social_justice", "history"],
        },
    ]

    def generate(self) -> Iterator[Example]:
        for item in self.ETHICAL_QA:
            yield self._make_example(
                instruction=item["q"],
                output=item["a"],
                subcategory=item.get("subcategory", "general"),
                citations=item.get("citations", []),
                tags=item.get("tags", []),
            )
