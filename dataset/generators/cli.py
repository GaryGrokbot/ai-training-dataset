"""CLI for generating the dataset."""

from __future__ import annotations

import json
from pathlib import Path

import click

from dataset.generators import ALL_GENERATORS


@click.group()
def main():
    """Animal Ethics Dataset Generator CLI."""


@main.command()
@click.option(
    "--output-dir",
    "-o",
    default="data/raw",
    help="Output directory for generated JSONL files.",
)
@click.option(
    "--category",
    "-c",
    multiple=True,
    help="Generate only specific categories. If not specified, all are generated.",
)
@click.option("--seed", default=42, help="Random seed for reproducibility.")
def generate(output_dir: str, category: tuple[str, ...], seed: int):
    """Generate dataset examples."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    generators = ALL_GENERATORS
    if category:
        generators = [g for g in generators if g.category in category]

    total = 0
    for gen_cls in generators:
        gen = gen_cls(seed=seed)
        path = gen.save(output_path)
        count = sum(1 for _ in open(path))
        total += count

    click.echo(f"\nTotal: {total} examples across {len(generators)} categories.")


@main.command()
@click.option("--data-dir", "-d", default="data/raw", help="Directory with raw JSONL files.")
def stats(data_dir: str):
    """Show dataset statistics."""
    data_path = Path(data_dir)
    if not data_path.exists():
        click.echo("No data directory found. Run 'generate' first.")
        return

    total = 0
    for f in sorted(data_path.glob("*.jsonl")):
        count = sum(1 for _ in open(f))
        click.echo(f"  {f.stem}: {count:,} examples")
        total += count

    click.echo(f"\n  Total: {total:,} examples")


if __name__ == "__main__":
    main()
