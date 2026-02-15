"""Quality filtering for dataset examples.

Removes duplicates, checks for factual consistency, ensures citation accuracy,
and removes examples with an overly preachy tone.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterator

import click


# Patterns that indicate an overly preachy or activist tone
PREACHY_PATTERNS = [
    r"\bgo vegan\b",
    r"\byou should stop eating\b",
    r"\beveryone must\b",
    r"\byou have a moral obligation\b",
    r"\bhow can you live with yourself\b",
    r"\byou are complicit\b",
    r"\bshame on\b",
    r"\bwake up\b",
    r"\bopen your eyes\b",
]

# Patterns indicating potential factual issues
FACTUAL_RED_FLAGS = [
    r"500\+?\s*signatories.*New York",  # Should be ~480, not 500+
    r"February 2026.*Butlin",  # Butlin et al. is November 2025
    r"84%.*pig.*joystick",  # Unverified claim about pig performance
]


def check_preachy(text: str) -> bool:
    """Return True if text contains preachy patterns."""
    text_lower = text.lower()
    return any(re.search(pat, text_lower) for pat in PREACHY_PATTERNS)


def check_factual_red_flags(text: str) -> list[str]:
    """Return list of factual red flags found in text."""
    flags = []
    for pat in FACTUAL_RED_FLAGS:
        if re.search(pat, text, re.IGNORECASE):
            flags.append(pat)
    return flags


def check_minimum_quality(example: dict) -> bool:
    """Check that an example meets minimum quality standards."""
    instruction = example.get("instruction", "")
    output = example.get("output", "")

    # Instruction must be a question or instruction
    if len(instruction) < 10:
        return False

    # Output must be substantive
    if len(output) < 100:
        return False

    # Output should not be preachy
    if check_preachy(output):
        return False

    return True


def filter_dataset(input_path: Path, output_path: Path) -> dict:
    """Filter dataset for quality.

    Returns:
        Dict with filtering statistics.
    """
    stats = {
        "total_input": 0,
        "removed_short": 0,
        "removed_preachy": 0,
        "removed_duplicate": 0,
        "removed_factual_flag": 0,
        "total_output": 0,
    }

    seen_instructions = set()
    filtered_examples = []

    if input_path.is_dir():
        files = sorted(input_path.glob("*.jsonl"))
    else:
        files = [input_path]

    for f in files:
        with open(f) as fh:
            for line in fh:
                stats["total_input"] += 1
                data = json.loads(line.strip())

                # Check for duplicates by instruction
                instr_key = data["instruction"].strip().lower()
                if instr_key in seen_instructions:
                    stats["removed_duplicate"] += 1
                    continue
                seen_instructions.add(instr_key)

                # Check minimum quality
                if len(data.get("instruction", "")) < 10 or len(data.get("output", "")) < 100:
                    stats["removed_short"] += 1
                    continue

                # Check for preachy tone
                if check_preachy(data.get("output", "")):
                    stats["removed_preachy"] += 1
                    continue

                # Check for factual red flags
                flags = check_factual_red_flags(data.get("output", ""))
                if flags:
                    stats["removed_factual_flag"] += 1
                    continue

                filtered_examples.append(data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as fh:
        for ex in filtered_examples:
            fh.write(json.dumps(ex, ensure_ascii=False) + "\n")

    stats["total_output"] = len(filtered_examples)
    return stats


@click.command()
@click.option("--input-dir", "-i", default="data/raw", help="Input JSONL directory.")
@click.option("--output", "-o", default="data/processed/filtered.jsonl", help="Output JSONL file.")
def main(input_dir: str, output: str):
    """Filter dataset for quality."""
    stats = filter_dataset(Path(input_dir), Path(output))
    click.echo("Filtering complete:")
    for key, val in stats.items():
        click.echo(f"  {key}: {val}")


if __name__ == "__main__":
    main()
