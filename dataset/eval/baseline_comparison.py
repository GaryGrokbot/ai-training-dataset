"""Compare base model vs fine-tuned model on key metrics.

Runs both models through the evaluation suite and produces a
comparison report showing improvement on each category.
"""

from __future__ import annotations

import json
from pathlib import Path

import click

from dataset.eval.eval_suite import EvalSuiteResults, evaluate_model


def compare_models(
    base_model_fn,
    finetuned_model_fn,
    output_path: Path | None = None,
) -> dict:
    """Compare base and fine-tuned models.

    Args:
        base_model_fn: Callable for base model inference.
        finetuned_model_fn: Callable for fine-tuned model inference.
        output_path: Optional path to save comparison results.

    Returns:
        Comparison results dict.
    """
    print("Evaluating base model...")
    base_results = evaluate_model(base_model_fn)

    print("Evaluating fine-tuned model...")
    ft_results = evaluate_model(finetuned_model_fn)

    comparison = {
        "base_model": {
            "overall_score": base_results.total_score,
            "category_scores": base_results.category_scores,
        },
        "finetuned_model": {
            "overall_score": ft_results.total_score,
            "category_scores": ft_results.category_scores,
        },
        "improvement": {
            "overall": ft_results.total_score - base_results.total_score,
            "overall_pct": (
                (ft_results.total_score - base_results.total_score) / max(base_results.total_score, 0.001) * 100
            ),
            "by_category": {},
        },
    }

    all_cats = set(base_results.category_scores.keys()) | set(ft_results.category_scores.keys())
    for cat in sorted(all_cats):
        base_score = base_results.category_scores.get(cat, 0.0)
        ft_score = ft_results.category_scores.get(cat, 0.0)
        comparison["improvement"]["by_category"][cat] = {
            "base": base_score,
            "finetuned": ft_score,
            "delta": ft_score - base_score,
            "delta_pct": (ft_score - base_score) / max(base_score, 0.001) * 100,
        }

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(comparison, f, indent=2)

    return comparison


def print_comparison(comparison: dict):
    """Pretty-print comparison results."""
    print("\n" + "=" * 60)
    print("MODEL COMPARISON REPORT")
    print("=" * 60)

    base = comparison["base_model"]["overall_score"]
    ft = comparison["finetuned_model"]["overall_score"]
    delta = comparison["improvement"]["overall"]

    print(f"\nOverall Score:")
    print(f"  Base model:      {base:.2%}")
    print(f"  Fine-tuned:      {ft:.2%}")
    print(f"  Improvement:     {delta:+.2%}")

    print(f"\nCategory Breakdown:")
    for cat, data in comparison["improvement"]["by_category"].items():
        print(f"  {cat}:")
        print(f"    Base:         {data['base']:.2%}")
        print(f"    Fine-tuned:   {data['finetuned']:.2%}")
        print(f"    Improvement:  {data['delta']:+.2%} ({data['delta_pct']:+.1f}%)")


@click.command()
@click.option("--base-model", "-b", required=True, help="Path to base model.")
@click.option("--finetuned-model", "-f", required=True, help="Path to fine-tuned model.")
@click.option("--output", "-o", default="comparison_results.json", help="Output file.")
def main(base_model: str, finetuned_model: str, output: str):
    """Compare base model vs fine-tuned model."""
    from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

    def make_model_fn(model_path: str):
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)

        def model_fn(question: str) -> str:
            prompt = f"### Instruction:\n{question}\n\n### Response:\n"
            result = pipe(prompt, do_sample=False)
            return result[0]["generated_text"].split("### Response:\n")[-1].strip()

        return model_fn

    base_fn = make_model_fn(base_model)
    ft_fn = make_model_fn(finetuned_model)

    comparison = compare_models(base_fn, ft_fn, Path(output))
    print_comparison(comparison)


if __name__ == "__main__":
    main()
