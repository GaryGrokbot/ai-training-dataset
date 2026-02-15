"""Convert dataset to ShareGPT conversation format for chat models.

Output format:
{
    "conversations": [
        {"from": "human", "value": "..."},
        {"from": "gpt", "value": "..."}
    ]
}
"""

from __future__ import annotations

import json
from pathlib import Path

import click


def convert_to_sharegpt(input_path: Path, output_path: Path) -> int:
    """Convert JSONL dataset to ShareGPT format.

    Args:
        input_path: Path to input JSONL file or directory of JSONL files.
        output_path: Path to output JSON file.

    Returns:
        Number of examples converted.
    """
    examples = []

    if input_path.is_dir():
        files = sorted(input_path.glob("*.jsonl"))
    else:
        files = [input_path]

    for f in files:
        with open(f) as fh:
            for line in fh:
                data = json.loads(line.strip())

                human_msg = data["instruction"]
                if data.get("input"):
                    human_msg += f"\n\n{data['input']}"

                examples.append({
                    "conversations": [
                        {"from": "human", "value": human_msg},
                        {"from": "gpt", "value": data["output"]},
                    ]
                })

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as fh:
        json.dump(examples, fh, indent=2, ensure_ascii=False)

    return len(examples)


@click.command()
@click.option("--input-dir", "-i", default="data/raw", help="Input JSONL directory.")
@click.option("--output", "-o", default="data/processed/sharegpt_dataset.json", help="Output JSON file.")
def main(input_dir: str, output: str):
    """Convert raw dataset to ShareGPT format."""
    count = convert_to_sharegpt(Path(input_dir), Path(output))
    click.echo(f"Converted {count} examples to ShareGPT format -> {output}")


if __name__ == "__main__":
    main()
