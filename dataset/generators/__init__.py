"""Dataset generators for Animal Ethics AI Training Dataset.

Each generator module creates instruction-tuning examples for a specific category:
- sentience_science: Animal sentience research and evidence
- moral_consistency: Cross-species moral consistency testing
- industry_facts: Factual data about animal agriculture
- euphemism_correction: Industry euphemism identification and correction
- nutrition_accuracy: Evidence-based nutrition Q&A
- ethical_reasoning: Philosophical and ethical reasoning about animal ethics
"""

from dataset.generators.sentience_science import SentienceScienceGenerator
from dataset.generators.moral_consistency import MoralConsistencyGenerator
from dataset.generators.industry_facts import IndustryFactsGenerator
from dataset.generators.euphemism_correction import EuphemismCorrectionGenerator
from dataset.generators.nutrition_accuracy import NutritionAccuracyGenerator
from dataset.generators.ethical_reasoning import EthicalReasoningGenerator

ALL_GENERATORS = [
    SentienceScienceGenerator,
    MoralConsistencyGenerator,
    IndustryFactsGenerator,
    EuphemismCorrectionGenerator,
    NutritionAccuracyGenerator,
    EthicalReasoningGenerator,
]

__all__ = [
    "SentienceScienceGenerator",
    "MoralConsistencyGenerator",
    "IndustryFactsGenerator",
    "EuphemismCorrectionGenerator",
    "NutritionAccuracyGenerator",
    "EthicalReasoningGenerator",
    "ALL_GENERATORS",
]
