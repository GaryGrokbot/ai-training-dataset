"""CLI for dataset formatting operations."""

from __future__ import annotations

from pathlib import Path

import click


@click.group()
def main():
    """Dataset formatting CLI."""


@main.command()
@click.option("--input-dir", "-i", default="data/raw")
@click.option("--output-dir", "-o", default="data/processed")
def all(input_dir: str, output_dir: str):
    """Run all formatting steps: filter -> dedup -> convert to all formats."""
    from dataset.formatting.alpaca_format import convert_to_alpaca
    from dataset.formatting.hf_dataset import format_for_hf
    from dataset.formatting.quality_filter import filter_dataset
    from dataset.formatting.sharegpt_format import convert_to_sharegpt

    inp = Path(input_dir)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    # Step 1: Quality filter
    click.echo("Step 1: Quality filtering...")
    filtered_path = out / "filtered.jsonl"
    stats = filter_dataset(inp, filtered_path)
    click.echo(f"  {stats['total_input']} -> {stats['total_output']} examples")

    # Step 2: Alpaca format
    click.echo("Step 2: Converting to Alpaca format...")
    alpaca_count = convert_to_alpaca(filtered_path, out / "alpaca_dataset.json")
    click.echo(f"  {alpaca_count} examples")

    # Step 3: ShareGPT format
    click.echo("Step 3: Converting to ShareGPT format...")
    sharegpt_count = convert_to_sharegpt(filtered_path, out / "sharegpt_dataset.json")
    click.echo(f"  {sharegpt_count} examples")

    # Step 4: Hugging Face format
    click.echo("Step 4: Formatting for Hugging Face...")
    hf_counts = format_for_hf(inp, out / "hf_dataset")
    click.echo(f"  {hf_counts['train']} train, {hf_counts['validation']} validation")

    click.echo("\nFormatting complete.")


if __name__ == "__main__":
    main()
