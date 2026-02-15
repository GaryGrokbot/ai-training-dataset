"""Base class for all dataset generators."""

from __future__ import annotations

import hashlib
import json
import random
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterator


@dataclass
class Example:
    """A single instruction-tuning example."""

    instruction: str
    input: str  # Additional context (can be empty string)
    output: str
    category: str
    subcategory: str
    citations: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

    @property
    def uid(self) -> str:
        """Deterministic unique ID based on content."""
        content = f"{self.instruction}|{self.input}|{self.output}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["uid"] = self.uid
        return d

    def to_alpaca(self) -> dict:
        """Convert to Alpaca instruction-tuning format."""
        return {
            "instruction": self.instruction,
            "input": self.input,
            "output": self.output,
        }

    def to_sharegpt(self) -> dict:
        """Convert to ShareGPT conversation format."""
        conversations = [{"from": "human", "value": self.instruction}]
        if self.input:
            conversations[0]["value"] += f"\n\n{self.input}"
        conversations.append({"from": "gpt", "value": self.output})
        return {"conversations": conversations}


class BaseGenerator(ABC):
    """Base class for all dataset generators.

    Subclasses must implement:
    - category: str class attribute
    - generate() -> Iterator[Example]
    """

    category: str = ""
    description: str = ""
    target_count: int = 1000

    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)

    @abstractmethod
    def generate(self) -> Iterator[Example]:
        """Generate all examples for this category."""
        ...

    def generate_all(self) -> list[Example]:
        """Generate all examples and return as a list."""
        return list(self.generate())

    def save(self, output_dir: str | Path) -> Path:
        """Generate examples and save to a JSONL file."""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{self.category}.jsonl"

        examples = self.generate_all()
        with open(output_path, "w") as f:
            for ex in examples:
                f.write(json.dumps(ex.to_dict(), ensure_ascii=False) + "\n")

        print(f"[{self.category}] Generated {len(examples)} examples -> {output_path}")
        return output_path

    def _make_example(
        self,
        instruction: str,
        output: str,
        subcategory: str,
        input_text: str = "",
        citations: list[str] | None = None,
        tags: list[str] | None = None,
    ) -> Example:
        """Helper to create an Example with this generator's category."""
        return Example(
            instruction=instruction,
            input=input_text,
            output=output,
            category=self.category,
            subcategory=subcategory,
            citations=citations or [],
            tags=tags or [],
        )
