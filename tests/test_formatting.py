"""Tests for dataset formatting utilities."""

import json
from pathlib import Path

import pytest


@pytest.fixture
def sample_jsonl(tmp_path):
    """Create sample JSONL data for testing."""
    data = [
        {
            "instruction": "Do fish feel pain?",
            "input": "",
            "output": "Yes. Research by Sneddon (2003) demonstrated that rainbow trout possess nociceptors.",
            "category": "sentience_science",
            "subcategory": "fish_pain",
            "citations": ["Sneddon (2003)"],
            "tags": ["fish", "pain"],
            "uid": "abc123",
        },
        {
            "instruction": "How many animals are killed for food each year?",
            "input": "",
            "output": "Approximately 80 billion land animals are slaughtered annually.",
            "category": "industry_facts",
            "subcategory": "scale",
            "citations": ["FAO (2023)"],
            "tags": ["scale"],
            "uid": "def456",
        },
    ]

    jsonl_path = tmp_path / "raw" / "test.jsonl"
    jsonl_path.parent.mkdir(parents=True)
    with open(jsonl_path, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")

    return tmp_path / "raw"


class TestAlpacaFormat:
    def test_conversion(self, sample_jsonl, tmp_path):
        from dataset.formatting.alpaca_format import convert_to_alpaca

        output = tmp_path / "alpaca.json"
        count = convert_to_alpaca(sample_jsonl, output)
        assert count == 2

        with open(output) as f:
            data = json.load(f)
        assert len(data) == 2
        assert "instruction" in data[0]
        assert "input" in data[0]
        assert "output" in data[0]


class TestShareGPTFormat:
    def test_conversion(self, sample_jsonl, tmp_path):
        from dataset.formatting.sharegpt_format import convert_to_sharegpt

        output = tmp_path / "sharegpt.json"
        count = convert_to_sharegpt(sample_jsonl, output)
        assert count == 2

        with open(output) as f:
            data = json.load(f)
        assert len(data) == 2
        assert "conversations" in data[0]
        assert data[0]["conversations"][0]["from"] == "human"
        assert data[0]["conversations"][1]["from"] == "gpt"


class TestQualityFilter:
    def test_removes_short_examples(self, tmp_path):
        from dataset.formatting.quality_filter import filter_dataset

        # Create test data with one short example
        jsonl_path = tmp_path / "raw" / "test.jsonl"
        jsonl_path.parent.mkdir(parents=True)
        with open(jsonl_path, "w") as f:
            f.write(json.dumps({
                "instruction": "short",
                "output": "too short",
            }) + "\n")
            f.write(json.dumps({
                "instruction": "Do fish feel pain? What does the research say about this important topic?",
                "output": "Yes. " + "A" * 200,
            }) + "\n")

        output = tmp_path / "filtered.jsonl"
        stats = filter_dataset(tmp_path / "raw", output)
        assert stats["removed_short"] >= 1
        assert stats["total_output"] <= stats["total_input"]

    def test_removes_preachy_language(self, tmp_path):
        from dataset.formatting.quality_filter import check_preachy

        assert check_preachy("You should go vegan today") is True
        assert check_preachy("Research shows that fish possess nociceptors") is False


class TestHFFormat:
    def test_creates_splits(self, sample_jsonl, tmp_path):
        from dataset.formatting.hf_dataset import format_for_hf

        output = tmp_path / "hf_dataset"
        counts = format_for_hf(sample_jsonl, output, val_split=0.5, seed=42)

        assert (output / "train.jsonl").exists()
        assert (output / "validation.jsonl").exists()
        assert (output / "dataset_info.json").exists()
        assert counts["train"] + counts["validation"] == 2
