"""Format dataset for Hugging Face datasets library upload.

Creates a datasets-compatible directory structure with:
- train.jsonl
- validation.jsonl
- dataset_info.json
"""

from __future__ import annotations

import json
import random
from pathlib import Path

import click


def format_for_hf(
    input_path: Path,
    output_path: Path,
    val_split: float = 0.05,
    seed: int = 42,
) -> dict[str, int]:
    """Format dataset for Hugging Face.

    Args:
        input_path: Directory of raw JSONL files.
        output_path: Output directory for HF-formatted dataset.
        val_split: Fraction of data to use for validation.
        seed: Random seed for reproducible splits.

    Returns:
        Dict with counts for train and validation splits.
    """
    rng = random.Random(seed)
    all_examples = []

    for f in sorted(input_path.glob("*.jsonl")):
        with open(f) as fh:
            for line in fh:
                data = json.loads(line.strip())
                all_examples.append(data)

    rng.shuffle(all_examples)
    val_count = int(len(all_examples) * val_split)
    val_examples = all_examples[:val_count]
    train_examples = all_examples[val_count:]

    output_path.mkdir(parents=True, exist_ok=True)

    for split_name, split_data in [("train", train_examples), ("validation", val_examples)]:
        with open(output_path / f"{split_name}.jsonl", "w") as fh:
            for ex in split_data:
                fh.write(json.dumps(ex, ensure_ascii=False) + "\n")

    # Write dataset info
    dataset_info = {
        "description": (
            "Animal Ethics AI Training Dataset: Instruction-tuning examples for "
            "reducing speciesist bias in language models. Every claim sourced, "
            "every response scientifically grounded."
        ),
        "citation": (
            "@misc{openpaws2026animalethics,\n"
            "  title={Animal Ethics AI Training Dataset},\n"
            "  author={Open Paws},\n"
            "  year={2026},\n"
            "  url={https://github.com/GaryGrokbot/ai-training-dataset}\n"
            "}"
        ),
        "homepage": "https://github.com/GaryGrokbot/ai-training-dataset",
        "license": "Apache-2.0",
        "features": {
            "instruction": {"dtype": "string"},
            "input": {"dtype": "string"},
            "output": {"dtype": "string"},
            "category": {"dtype": "string"},
            "subcategory": {"dtype": "string"},
            "citations": {"dtype": "string", "sequence": True},
            "tags": {"dtype": "string", "sequence": True},
            "uid": {"dtype": "string"},
        },
        "splits": {
            "train": {"num_examples": len(train_examples)},
            "validation": {"num_examples": len(val_examples)},
        },
    }

    with open(output_path / "dataset_info.json", "w") as fh:
        json.dump(dataset_info, fh, indent=2)

    return {"train": len(train_examples), "validation": len(val_examples)}


@click.command()
@click.option("--input-dir", "-i", default="data/raw", help="Input JSONL directory.")
@click.option("--output-dir", "-o", default="data/processed/hf_dataset", help="Output HF directory.")
@click.option("--val-split", default=0.05, help="Validation split fraction.")
def main(input_dir: str, output_dir: str, val_split: float):
    """Format dataset for Hugging Face Hub."""
    counts = format_for_hf(Path(input_dir), Path(output_dir), val_split=val_split)
    click.echo(f"Formatted for HF: {counts['train']} train, {counts['validation']} validation")


if __name__ == "__main__":
    main()
