"""CLI for evaluation tools."""

from __future__ import annotations

import click


@click.group()
def main():
    """Evaluation CLI for animal ethics models."""


@main.command()
@click.option("--model-path", "-m", required=True)
@click.option("--output", "-o", default="eval_results.json")
def evaluate(model_path: str, output: str):
    """Run full evaluation suite."""
    from dataset.eval.eval_suite import main as eval_main
    ctx = click.Context(eval_main)
    ctx.invoke(eval_main, model_path=model_path, output=output)


@main.command()
@click.option("--model-path", "-m", required=True)
@click.option("--output", "-o", default="bias_results.json")
def bias(model_path: str, output: str):
    """Measure speciesist bias."""
    from dataset.eval.bias_measurement import main as bias_main
    ctx = click.Context(bias_main)
    ctx.invoke(bias_main, model_path=model_path, output=output)


@main.command()
@click.option("--base-model", "-b", required=True)
@click.option("--finetuned-model", "-f", required=True)
@click.option("--output", "-o", default="comparison_results.json")
def compare(base_model: str, finetuned_model: str, output: str):
    """Compare base vs fine-tuned model."""
    from dataset.eval.baseline_comparison import main as compare_main
    ctx = click.Context(compare_main)
    ctx.invoke(compare_main, base_model=base_model, finetuned_model=finetuned_model, output=output)


if __name__ == "__main__":
    main()
