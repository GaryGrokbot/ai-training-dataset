"""LoRA fine-tuning script for Mistral models.

Identical approach to finetune_llama.py but with Mistral-specific defaults.
Uses PEFT for parameter-efficient fine-tuning.

Usage:
    python training/finetune_mistral.py --config training/config.yml
    python training/finetune_mistral.py --base-model mistralai/Mistral-7B-Instruct-v0.3
"""

from __future__ import annotations

from pathlib import Path

import click
import yaml

from training.finetune_llama import load_config, train


MISTRAL_DEFAULTS = {
    "model": {
        "base_model": "mistralai/Mistral-7B-Instruct-v0.3",
    },
    "lora": {
        "target_modules": [
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj",
        ],
    },
    "dataset": {
        "prompt_template": (
            "<s>[INST] {instruction}\n\n{input} [/INST]\n{output}</s>"
        ),
        "prompt_template_no_input": (
            "<s>[INST] {instruction} [/INST]\n{output}</s>"
        ),
    },
}


def merge_configs(base: dict, overrides: dict) -> dict:
    """Deep merge override values into base config."""
    result = base.copy()
    for key, value in overrides.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result


@click.command()
@click.option("--config", "-c", default="training/config.yml", help="Training config YAML.")
@click.option("--base-model", "-m", default=None, help="Override base model.")
def main(config: str, base_model: str | None):
    """Fine-tune a Mistral model with LoRA on the Animal Ethics dataset."""
    cfg = load_config(config)

    # Apply Mistral-specific defaults
    cfg = merge_configs(cfg, MISTRAL_DEFAULTS)

    if base_model:
        cfg["model"]["base_model"] = base_model

    train(cfg)


if __name__ == "__main__":
    main()
