"""Merge LoRA weights into base model and push to Hugging Face Hub.

After fine-tuning with LoRA, this script merges the adapter weights back
into the base model and optionally uploads the result to HF Hub.

Usage:
    python training/merge_and_push.py --base-model meta-llama/Llama-3.1-8B-Instruct \
        --adapter-path checkpoints --output merged_model

    python training/merge_and_push.py --base-model meta-llama/Llama-3.1-8B-Instruct \
        --adapter-path checkpoints --output merged_model \
        --push --hub-id openpaws/animal-ethics-llama-8b
"""

from __future__ import annotations

from pathlib import Path

import click
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def merge_and_save(
    base_model_path: str,
    adapter_path: str,
    output_path: str,
    torch_dtype: str = "bfloat16",
):
    """Merge LoRA adapter into base model and save.

    Args:
        base_model_path: HF model ID or local path for base model.
        adapter_path: Path to LoRA adapter checkpoint.
        output_path: Path to save merged model.
        torch_dtype: Torch dtype for loading (bfloat16, float16, float32).
    """
    dtype = getattr(torch, torch_dtype)

    print(f"Loading base model: {base_model_path}")
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_path,
        torch_dtype=dtype,
        device_map="auto",
    )

    print(f"Loading LoRA adapter: {adapter_path}")
    model = PeftModel.from_pretrained(base_model, adapter_path)

    print("Merging weights...")
    model = model.merge_and_unload()

    print(f"Saving merged model to: {output_path}")
    output = Path(output_path)
    output.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(output_path)

    # Save tokenizer
    print("Saving tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(base_model_path)
    tokenizer.save_pretrained(output_path)

    print("Merge complete.")
    return output_path


def push_to_hub(
    model_path: str,
    hub_id: str,
    token: str | None = None,
    private: bool = False,
):
    """Push merged model to Hugging Face Hub.

    Args:
        model_path: Path to merged model.
        hub_id: HF repo ID (e.g., 'openpaws/animal-ethics-llama-8b').
        token: HF API token.
        private: Whether to create a private repo.
    """
    from huggingface_hub import HfApi

    print(f"Pushing to Hugging Face Hub: {hub_id}")

    model = AutoModelForCausalLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    model.push_to_hub(hub_id, token=token, private=private)
    tokenizer.push_to_hub(hub_id, token=token, private=private)

    # Upload model card
    api = HfApi(token=token)
    card_path = Path(__file__).parent.parent / "dataset" / "hf" / "model_card.md"
    if card_path.exists():
        api.upload_file(
            path_or_fileobj=str(card_path),
            path_in_repo="README.md",
            repo_id=hub_id,
            repo_type="model",
            token=token,
        )

    print(f"Model pushed to https://huggingface.co/models/{hub_id}")


@click.command()
@click.option("--base-model", "-b", required=True, help="Base model path or HF ID.")
@click.option("--adapter-path", "-a", default="checkpoints", help="LoRA adapter checkpoint path.")
@click.option("--output", "-o", default="merged_model", help="Output path for merged model.")
@click.option("--push", is_flag=True, help="Push to Hugging Face Hub.")
@click.option("--hub-id", default=None, help="HF Hub model ID for pushing.")
@click.option("--token", default=None, help="HF API token.")
@click.option("--private", is_flag=True, help="Make HF repo private.")
@click.option("--dtype", default="bfloat16", help="Torch dtype.")
def main(
    base_model: str,
    adapter_path: str,
    output: str,
    push: bool,
    hub_id: str | None,
    token: str | None,
    private: bool,
    dtype: str,
):
    """Merge LoRA weights and optionally push to Hugging Face Hub."""
    merged_path = merge_and_save(base_model, adapter_path, output, torch_dtype=dtype)

    if push:
        if not hub_id:
            raise click.UsageError("--hub-id is required when using --push")
        push_to_hub(merged_path, hub_id, token=token, private=private)


if __name__ == "__main__":
    main()
