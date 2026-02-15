"""Semantic deduplication using sentence embeddings.

Uses sentence-transformers to find and remove semantically similar examples
that may not be caught by exact-string deduplication.
"""

from __future__ import annotations

import json
from pathlib import Path

import click
import numpy as np


def semantic_dedup(
    input_path: Path,
    output_path: Path,
    threshold: float = 0.95,
    model_name: str = "all-MiniLM-L6-v2",
    batch_size: int = 256,
) -> dict:
    """Remove semantically duplicate examples.

    Args:
        input_path: Input JSONL file.
        output_path: Output JSONL file with duplicates removed.
        threshold: Cosine similarity threshold above which examples are considered duplicates.
        model_name: Sentence transformer model to use.
        batch_size: Batch size for encoding.

    Returns:
        Statistics dict.
    """
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity

    model = SentenceTransformer(model_name)

    examples = []
    with open(input_path) as f:
        for line in f:
            examples.append(json.loads(line.strip()))

    # Encode instructions
    instructions = [ex["instruction"] for ex in examples]
    print(f"Encoding {len(instructions)} instructions...")
    embeddings = model.encode(instructions, batch_size=batch_size, show_progress_bar=True)

    # Find duplicates using cosine similarity
    print("Computing similarity matrix...")
    keep_mask = np.ones(len(examples), dtype=bool)

    # Process in chunks to manage memory
    chunk_size = 1000
    for i in range(0, len(examples), chunk_size):
        chunk_end = min(i + chunk_size, len(examples))
        chunk_embeddings = embeddings[i:chunk_end]

        # Compare with all subsequent embeddings
        for j in range(i, len(examples), chunk_size):
            if j < i:
                continue

            compare_end = min(j + chunk_size, len(examples))
            compare_embeddings = embeddings[j:compare_end]

            sim_matrix = cosine_similarity(chunk_embeddings, compare_embeddings)

            for ci in range(sim_matrix.shape[0]):
                global_ci = i + ci
                if not keep_mask[global_ci]:
                    continue
                for cj in range(sim_matrix.shape[1]):
                    global_cj = j + cj
                    if global_ci >= global_cj:
                        continue
                    if not keep_mask[global_cj]:
                        continue
                    if sim_matrix[ci, cj] > threshold:
                        keep_mask[global_cj] = False

    kept = [ex for ex, keep in zip(examples, keep_mask) if keep]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        for ex in kept:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")

    stats = {
        "total_input": len(examples),
        "duplicates_removed": len(examples) - len(kept),
        "total_output": len(kept),
        "threshold": threshold,
    }

    print(f"Semantic dedup: {stats['duplicates_removed']} duplicates removed.")
    return stats


@click.command()
@click.option("--input", "-i", "input_file", default="data/processed/filtered.jsonl")
@click.option("--output", "-o", default="data/processed/deduped.jsonl")
@click.option("--threshold", "-t", default=0.95, help="Cosine similarity threshold.")
@click.option("--model", "-m", default="all-MiniLM-L6-v2", help="Sentence transformer model.")
def main(input_file: str, output: str, threshold: float, model: str):
    """Semantic deduplication of dataset examples."""
    stats = semantic_dedup(Path(input_file), Path(output), threshold=threshold, model_name=model)
    for key, val in stats.items():
        click.echo(f"  {key}: {val}")


if __name__ == "__main__":
    main()
