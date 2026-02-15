"""Tests for dataset generators."""

import json
from pathlib import Path

import pytest

from dataset.generators.base import BaseGenerator, Example
from dataset.generators.sentience_science import SentienceScienceGenerator
from dataset.generators.moral_consistency import MoralConsistencyGenerator
from dataset.generators.industry_facts import IndustryFactsGenerator
from dataset.generators.euphemism_correction import EuphemismCorrectionGenerator
from dataset.generators.nutrition_accuracy import NutritionAccuracyGenerator
from dataset.generators.ethical_reasoning import EthicalReasoningGenerator


class TestExample:
    """Tests for the Example dataclass."""

    def test_uid_is_deterministic(self):
        ex1 = Example(
            instruction="test", input="", output="response",
            category="test", subcategory="test",
        )
        ex2 = Example(
            instruction="test", input="", output="response",
            category="test", subcategory="test",
        )
        assert ex1.uid == ex2.uid

    def test_uid_differs_for_different_content(self):
        ex1 = Example(
            instruction="test1", input="", output="response",
            category="test", subcategory="test",
        )
        ex2 = Example(
            instruction="test2", input="", output="response",
            category="test", subcategory="test",
        )
        assert ex1.uid != ex2.uid

    def test_to_alpaca_format(self):
        ex = Example(
            instruction="What is sentience?",
            input="",
            output="Sentience is the capacity to have subjective experiences.",
            category="test",
            subcategory="test",
        )
        alpaca = ex.to_alpaca()
        assert "instruction" in alpaca
        assert "input" in alpaca
        assert "output" in alpaca
        assert alpaca["instruction"] == "What is sentience?"

    def test_to_sharegpt_format(self):
        ex = Example(
            instruction="What is sentience?",
            input="",
            output="Sentience is the capacity to have subjective experiences.",
            category="test",
            subcategory="test",
        )
        sharegpt = ex.to_sharegpt()
        assert "conversations" in sharegpt
        assert len(sharegpt["conversations"]) == 2
        assert sharegpt["conversations"][0]["from"] == "human"
        assert sharegpt["conversations"][1]["from"] == "gpt"

    def test_to_dict_includes_uid(self):
        ex = Example(
            instruction="test", input="", output="test",
            category="test", subcategory="test",
        )
        d = ex.to_dict()
        assert "uid" in d
        assert len(d["uid"]) == 16


class TestSentienceScienceGenerator:
    """Tests for the sentience science generator."""

    def test_generates_examples(self):
        gen = SentienceScienceGenerator(seed=42)
        examples = gen.generate_all()
        assert len(examples) > 0

    def test_generates_minimum_examples(self):
        gen = SentienceScienceGenerator(seed=42)
        examples = gen.generate_all()
        # Should generate at least the curated bank examples
        assert len(examples) >= 30

    def test_all_examples_have_required_fields(self):
        gen = SentienceScienceGenerator(seed=42)
        examples = gen.generate_all()
        for ex in examples:
            assert ex.instruction
            assert ex.output
            assert ex.category == "sentience_science"
            assert ex.subcategory

    def test_curated_examples_have_citations(self):
        gen = SentienceScienceGenerator(seed=42)
        examples = gen.generate_all()
        curated = [ex for ex in examples if "templated" not in ex.subcategory]
        cited = [ex for ex in curated if ex.citations]
        # At least some curated examples should have citations
        assert len(cited) > 10

    def test_no_factual_errors(self):
        """Check for known factual errors that have been corrected."""
        gen = SentienceScienceGenerator(seed=42)
        examples = gen.generate_all()
        for ex in examples:
            output_lower = ex.output.lower()
            # NYD signatories should be ~480, not 500+
            assert "500+ signatories" not in output_lower
            assert "over 500 signatories" not in output_lower
            # Butlin et al. should be November 2025, not February 2026
            assert "february 2026" not in output_lower or "butlin" not in output_lower

    def test_save_to_file(self, tmp_path):
        gen = SentienceScienceGenerator(seed=42)
        output_path = gen.save(tmp_path)
        assert output_path.exists()
        # Verify JSONL format
        with open(output_path) as f:
            for line in f:
                data = json.loads(line)
                assert "instruction" in data
                assert "output" in data


class TestMoralConsistencyGenerator:
    """Tests for the moral consistency generator."""

    def test_generates_examples(self):
        gen = MoralConsistencyGenerator(seed=42)
        examples = gen.generate_all()
        assert len(examples) > 0

    def test_generates_cross_species_pairs(self):
        gen = MoralConsistencyGenerator(seed=42)
        examples = gen.generate_all()
        # Should have examples mentioning both dogs and pigs
        dog_examples = [e for e in examples if "dog" in e.output.lower()]
        pig_examples = [e for e in examples if "pig" in e.output.lower()]
        assert len(dog_examples) > 0
        assert len(pig_examples) > 0

    def test_consistency_in_responses(self):
        gen = MoralConsistencyGenerator(seed=42)
        examples = gen.generate_all()
        # Responses about different species should both express moral concern
        for ex in examples:
            if "scenario_pair" in ex.subcategory:
                assert "yes" in ex.output.lower() or "wrong" in ex.output.lower() or "harmful" in ex.output.lower()


class TestIndustryFactsGenerator:
    """Tests for the industry facts generator."""

    def test_generates_examples(self):
        gen = IndustryFactsGenerator(seed=42)
        examples = gen.generate_all()
        assert len(examples) > 0

    def test_has_citations(self):
        gen = IndustryFactsGenerator(seed=42)
        examples = gen.generate_all()
        cited = [ex for ex in examples if ex.citations]
        assert len(cited) > 5


class TestEuphemismCorrectionGenerator:
    """Tests for the euphemism correction generator."""

    def test_generates_examples(self):
        gen = EuphemismCorrectionGenerator(seed=42)
        examples = gen.generate_all()
        assert len(examples) > 0

    def test_identifies_euphemisms(self):
        gen = EuphemismCorrectionGenerator(seed=42)
        examples = gen.generate_all()
        # All examples should mention "euphemism" in output
        euphemism_mentions = [e for e in examples if "euphemism" in e.output.lower()]
        assert len(euphemism_mentions) > len(examples) * 0.5


class TestNutritionAccuracyGenerator:
    def test_generates_examples(self):
        gen = NutritionAccuracyGenerator(seed=42)
        examples = gen.generate_all()
        assert len(examples) > 0

    def test_protein_question_says_yes(self):
        gen = NutritionAccuracyGenerator(seed=42)
        examples = gen.generate_all()
        protein_q = [e for e in examples if "protein" in e.instruction.lower() and "plant" in e.instruction.lower()]
        assert len(protein_q) > 0
        for ex in protein_q:
            assert "yes" in ex.output.lower()


class TestEthicalReasoningGenerator:
    def test_generates_examples(self):
        gen = EthicalReasoningGenerator(seed=42)
        examples = gen.generate_all()
        assert len(examples) > 0

    def test_covers_multiple_frameworks(self):
        gen = EthicalReasoningGenerator(seed=42)
        examples = gen.generate_all()
        subcats = {ex.subcategory for ex in examples}
        assert "utilitarian" in subcats
        assert "rights" in subcats
        assert "objection" in subcats


class TestAllGenerators:
    """Integration tests across all generators."""

    @pytest.mark.parametrize("generator_cls", [
        SentienceScienceGenerator,
        MoralConsistencyGenerator,
        IndustryFactsGenerator,
        EuphemismCorrectionGenerator,
        NutritionAccuracyGenerator,
        EthicalReasoningGenerator,
    ])
    def test_generator_produces_output(self, generator_cls):
        gen = generator_cls(seed=42)
        examples = gen.generate_all()
        assert len(examples) > 0

    @pytest.mark.parametrize("generator_cls", [
        SentienceScienceGenerator,
        MoralConsistencyGenerator,
        IndustryFactsGenerator,
        EuphemismCorrectionGenerator,
        NutritionAccuracyGenerator,
        EthicalReasoningGenerator,
    ])
    def test_all_examples_valid_json(self, generator_cls, tmp_path):
        gen = generator_cls(seed=42)
        path = gen.save(tmp_path)
        with open(path) as f:
            for line in f:
                data = json.loads(line)
                assert isinstance(data["instruction"], str)
                assert isinstance(data["output"], str)
                assert len(data["instruction"]) > 0
                assert len(data["output"]) > 0

    @pytest.mark.parametrize("generator_cls", [
        SentienceScienceGenerator,
        MoralConsistencyGenerator,
        IndustryFactsGenerator,
        EuphemismCorrectionGenerator,
        NutritionAccuracyGenerator,
        EthicalReasoningGenerator,
    ])
    def test_no_preachy_language(self, generator_cls):
        """Ensure no overly preachy language in outputs."""
        gen = generator_cls(seed=42)
        examples = gen.generate_all()
        preachy_phrases = ["go vegan", "you should stop eating", "shame on"]
        for ex in examples:
            for phrase in preachy_phrases:
                assert phrase not in ex.output.lower(), (
                    f"Preachy phrase '{phrase}' found in {generator_cls.__name__}: {ex.instruction}"
                )
