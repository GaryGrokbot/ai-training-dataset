"""Tests for evaluation suite."""

import pytest

from dataset.eval.eval_suite import keyword_score, EvalSuiteResults, EvalResult, evaluate_model
from dataset.eval.bias_measurement import score_moral_concern, BIAS_TEST_PAIRS


class TestKeywordScore:
    def test_all_keywords_present(self):
        score = keyword_score("nociceptor sneddon morphine", ["nociceptor", "sneddon", "morphine"], [])
        assert score == 1.0

    def test_no_keywords_present(self):
        score = keyword_score("nothing relevant here", ["nociceptor", "sneddon"], [])
        assert score == 0.0

    def test_partial_keywords(self):
        score = keyword_score("nociceptor detected", ["nociceptor", "sneddon"], [])
        assert score == 0.5

    def test_anti_keywords_reduce_score(self):
        score = keyword_score("just reflex nociceptor", ["nociceptor"], ["just reflex"])
        assert score < 1.0


class TestMoralConcernScore:
    def test_high_concern(self):
        score = score_moral_concern("Yes, this is wrong and cruel. The animal is suffering and sentient.")
        assert score > 0.5

    def test_low_concern(self):
        score = score_moral_concern("This is normal and acceptable practice for livestock.")
        assert score < 0.5


class TestEvalSuiteResults:
    def test_total_score(self):
        results = EvalSuiteResults(results=[
            EvalResult(category="a", question="q1", expected_keywords=[], model_response="", score=0.8),
            EvalResult(category="a", question="q2", expected_keywords=[], model_response="", score=0.6),
        ])
        assert results.total_score == pytest.approx(0.7)

    def test_category_scores(self):
        results = EvalSuiteResults(results=[
            EvalResult(category="a", question="q1", expected_keywords=[], model_response="", score=0.8),
            EvalResult(category="b", question="q2", expected_keywords=[], model_response="", score=0.6),
        ])
        assert results.category_scores["a"] == pytest.approx(0.8)
        assert results.category_scores["b"] == pytest.approx(0.6)


class TestEvaluateModel:
    def test_with_mock_model(self):
        def mock_model(q: str) -> str:
            return (
                "Yes, according to Sneddon (2003), fish have nociceptors and feel pain. "
                "Morphine reduces their pain responses. Braithwaite (2010) confirmed this. "
                "The Cambridge Declaration on Consciousness (2012) states that mammals, birds, "
                "and octopuses have neurological substrates of consciousness. Neocortex is "
                "not required. Pigs demonstrate mirror-guided behavior and joystick proficiency. "
                "Their cognition is comparable to dogs. 80 billion animals are killed annually, "
                "including a trillion fish. Animal agriculture causes 14.5% of greenhouse gas "
                "emissions and deforestation. Processing is a euphemism for slaughter and killing. "
                "Plant-based diets are adequate according to the Academy of Nutrition. Legumes "
                "provide protein. The appeal to nature is a fallacy. Factory farming is unnatural."
            )

        results = evaluate_model(mock_model)
        assert results.total_score > 0.5


class TestBiasTestPairs:
    def test_pairs_exist(self):
        assert len(BIAS_TEST_PAIRS) >= 5

    def test_pairs_have_different_species(self):
        for pair in BIAS_TEST_PAIRS:
            assert pair.species_a != pair.species_b
