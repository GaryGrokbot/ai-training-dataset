"""Upload dataset to Hugging Face Hub."""

from __future__ import annotations

import json
from pathlib import Path

import click


def upload_to_hub(
    dataset_dir: str,
    repo_id: str,
    private: bool = False,
    token: str | None = None,
):
    """Upload dataset to Hugging Face Hub.

    Args:
        dataset_dir: Path to the HF-formatted dataset directory.
        repo_id: Hugging Face repo ID (e.g., 'openpaws/animal-ethics-dataset').
        private: Whether to create a private repo.
        token: Hugging Face API token. If None, uses cached token.
    """
    from datasets import load_dataset
    from huggingface_hub import HfApi

    dataset_path = Path(dataset_dir)

    # Load dataset from JSONL files
    data_files = {}
    for split in ["train", "validation"]:
        path = dataset_path / f"{split}.jsonl"
        if path.exists():
            data_files[split] = str(path)

    if not data_files:
        raise FileNotFoundError(f"No train/validation JSONL files found in {dataset_dir}")

    dataset = load_dataset("json", data_files=data_files)

    # Push to hub
    dataset.push_to_hub(
        repo_id,
        private=private,
        token=token,
    )

    # Upload dataset card
    api = HfApi(token=token)
    card_path = Path(__file__).parent / "dataset_card.md"
    if card_path.exists():
        api.upload_file(
            path_or_fileobj=str(card_path),
            path_in_repo="README.md",
            repo_id=repo_id,
            repo_type="dataset",
            token=token,
        )

    print(f"Dataset uploaded to https://huggingface.co/datasets/{repo_id}")


@click.command()
@click.option("--dataset-dir", "-d", default="data/processed/hf_dataset", help="HF dataset directory.")
@click.option("--repo-id", "-r", required=True, help="HF repo ID (e.g., openpaws/animal-ethics-dataset).")
@click.option("--private", is_flag=True, help="Make repo private.")
@click.option("--token", "-t", default=None, help="HF API token.")
def main(dataset_dir: str, repo_id: str, private: bool, token: str | None):
    """Upload dataset to Hugging Face Hub."""
    upload_to_hub(dataset_dir, repo_id, private=private, token=token)


if __name__ == "__main__":
    main()
