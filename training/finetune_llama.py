"""LoRA fine-tuning script for Llama models.

Uses the Animal Ethics dataset with PEFT (Parameter-Efficient Fine-Tuning)
to fine-tune Llama models for reduced speciesist bias.

Usage:
    python training/finetune_llama.py --config training/config.yml
    python training/finetune_llama.py --base-model meta-llama/Llama-3.1-8B-Instruct
"""

from __future__ import annotations

import json
from pathlib import Path

import click
import torch
import yaml
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq,
)


def load_config(config_path: str) -> dict:
    """Load training configuration from YAML file."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def format_example(example: dict, tokenizer, max_length: int, config: dict) -> dict:
    """Format a single example for training."""
    if example.get("input") and example["input"].strip():
        template = config["dataset"]["prompt_template"]
        text = template.format(
            instruction=example["instruction"],
            input=example["input"],
            output=example["output"],
        )
    else:
        template = config["dataset"]["prompt_template_no_input"]
        text = template.format(
            instruction=example["instruction"],
            output=example["output"],
        )

    tokenized = tokenizer(
        text,
        truncation=True,
        max_length=max_length,
        padding=False,
    )
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized


def train(config: dict):
    """Run LoRA fine-tuning."""
    model_config = config["model"]
    lora_config = config["lora"]
    train_config = config["training"]
    dataset_config = config["dataset"]
    output_config = config["output"]

    # Load tokenizer
    print(f"Loading tokenizer from {model_config['base_model']}...")
    tokenizer = AutoTokenizer.from_pretrained(model_config["base_model"])
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id

    # Load model with quantization
    print(f"Loading model from {model_config['base_model']}...")
    bnb_config = None
    if model_config.get("load_in_4bit"):
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=getattr(torch, model_config.get("bnb_4bit_compute_dtype", "bfloat16")),
            bnb_4bit_quant_type=model_config.get("bnb_4bit_quant_type", "nf4"),
            bnb_4bit_use_double_quant=True,
        )

    model = AutoModelForCausalLM.from_pretrained(
        model_config["base_model"],
        quantization_config=bnb_config,
        device_map=model_config.get("device_map", "auto"),
        torch_dtype=getattr(torch, model_config.get("torch_dtype", "bfloat16")),
    )

    # Prepare for k-bit training
    if model_config.get("load_in_4bit"):
        model = prepare_model_for_kbit_training(model)

    # Configure LoRA
    peft_config = LoraConfig(
        r=lora_config["rank"],
        lora_alpha=lora_config["alpha"],
        lora_dropout=lora_config["dropout"],
        target_modules=lora_config["target_modules"],
        bias=lora_config.get("bias", "none"),
        task_type=lora_config.get("task_type", "CAUSAL_LM"),
    )

    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    # Load dataset
    print("Loading dataset...")
    data_files = {}
    if Path(dataset_config["train_file"]).exists():
        data_files["train"] = dataset_config["train_file"]
    if Path(dataset_config["validation_file"]).exists():
        data_files["validation"] = dataset_config["validation_file"]

    dataset = load_dataset("json", data_files=data_files)

    max_length = dataset_config.get("max_seq_length", 2048)

    def tokenize_fn(examples):
        return format_example(examples, tokenizer, max_length, config)

    print("Tokenizing dataset...")
    tokenized_dataset = dataset.map(
        tokenize_fn,
        remove_columns=dataset["train"].column_names,
        num_proc=4,
    )

    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_config["output_dir"],
        num_train_epochs=train_config["num_epochs"],
        per_device_train_batch_size=train_config["per_device_train_batch_size"],
        per_device_eval_batch_size=train_config["per_device_eval_batch_size"],
        gradient_accumulation_steps=train_config["gradient_accumulation_steps"],
        learning_rate=train_config["learning_rate"],
        weight_decay=train_config["weight_decay"],
        warmup_ratio=train_config["warmup_ratio"],
        lr_scheduler_type=train_config["lr_scheduler_type"],
        max_grad_norm=train_config["max_grad_norm"],
        fp16=train_config.get("fp16", False),
        bf16=train_config.get("bf16", True),
        logging_steps=train_config["logging_steps"],
        save_strategy=train_config["save_strategy"],
        save_steps=train_config["save_steps"],
        eval_strategy=train_config.get("eval_strategy", "steps"),
        eval_steps=train_config.get("eval_steps", 200),
        save_total_limit=train_config["save_total_limit"],
        load_best_model_at_end=train_config["load_best_model_at_end"],
        metric_for_best_model=train_config.get("metric_for_best_model", "eval_loss"),
        greater_is_better=train_config.get("greater_is_better", False),
        dataloader_num_workers=train_config.get("dataloader_num_workers", 4),
        seed=train_config.get("seed", 42),
        report_to="none",
    )

    # Data collator
    data_collator = DataCollatorForSeq2Seq(
        tokenizer=tokenizer,
        padding=True,
        return_tensors="pt",
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset.get("validation"),
        data_collator=data_collator,
        tokenizer=tokenizer,
    )

    # Train
    print("Starting training...")
    trainer.train()

    # Save
    print(f"Saving model to {output_config['output_dir']}...")
    trainer.save_model()
    tokenizer.save_pretrained(output_config["output_dir"])

    print("Training complete.")


@click.command()
@click.option("--config", "-c", default="training/config.yml", help="Training config YAML.")
@click.option("--base-model", "-m", default=None, help="Override base model path.")
def main(config: str, base_model: str | None):
    """Fine-tune a Llama model with LoRA on the Animal Ethics dataset."""
    cfg = load_config(config)
    if base_model:
        cfg["model"]["base_model"] = base_model
    train(cfg)


if __name__ == "__main__":
    main()
