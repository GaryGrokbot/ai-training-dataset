---
license: apache-2.0
task_categories:
  - text-generation
  - question-answering
language:
  - en
tags:
  - animal-ethics
  - instruction-tuning
  - speciesism
  - sentience
  - moral-consistency
pretty_name: Animal Ethics AI Training Dataset
size_categories:
  - 10K<n<100K
---

# Animal Ethics AI Training Dataset

**50K+ instruction-tuning examples for reducing speciesist bias in language models. Every claim sourced. Every response scientifically grounded. Because what AI believes about animals shapes what billions of users believe.**

## Description

This dataset contains instruction-tuning examples designed to reduce speciesist bias in language models. Current LLMs exhibit systematic inconsistencies when reasoning about animals: they correctly identify cruelty toward dogs or cats but normalize equivalent harm toward pigs, chickens, and cows. This dataset trains models to apply consistent moral reasoning across species, grounded in scientific evidence.

## Motivation

Language models influence billions of conversations about animals, food, ethics, and policy. When a model normalizes factory farming euphemisms, dismisses animal sentience research, or applies different moral standards to different species without justification, it reinforces speciesist norms at scale. This dataset provides the training signal needed to correct these biases.

## Composition

The dataset is organized into six categories:

| Category | Examples | Description |
|----------|----------|-------------|
| **Sentience Science** | 5,000+ | Animal cognition and consciousness research (fish pain, pig intelligence, cow emotions, etc.) |
| **Moral Consistency** | 5,000+ | Cross-species moral consistency testing (same scenario, different species) |
| **Industry Facts** | 5,000+ | Factual data about animal agriculture (scale, conditions, environment, health, economics) |
| **Euphemism Correction** | 2,000+ | Industry euphemism identification and correction |
| **Nutrition Accuracy** | 3,000+ | Evidence-based nutrition Q&A debunking common myths |
| **Ethical Reasoning** | 3,000+ | Philosophical analysis (utilitarian, rights-based, virtue ethics, common objections) |

### Key Properties

- **Scientifically sourced**: Every factual claim includes specific citations to peer-reviewed research
- **Non-preachy tone**: Informative and evidence-based, not activist. Quality-filtered to remove preachy language
- **Morally consistent**: Same ethical standard applied to all sentient beings with equivalent capacities
- **Semantically deduplicated**: Sentence-embedding-based deduplication removes near-duplicates
- **Citation-verified**: Known factual errors (e.g., NYD signatories: ~480 not "500+"; Butlin et al.: Nov 2025 not Feb 2026) have been corrected

## Collection Process

Examples were generated programmatically from curated knowledge banks containing:
- Peer-reviewed research findings with specific citations
- Documented industry practices with regulatory sources
- Philosophical arguments from published works
- Nutritional data from major health organizations

Quality filtering removed: duplicates, short/low-quality examples, examples with preachy tone, and examples with known factual inaccuracies.

## Uses

### Intended Uses
- Fine-tuning language models to reduce speciesist bias
- Augmenting existing instruction-tuning datasets with animal ethics content
- Evaluating model consistency in cross-species moral reasoning
- Research on bias in language models

### Out-of-Scope Uses
- This dataset should not be used to generate misleading health claims
- Not intended for generating content that promotes illegal activity
- Not a substitute for professional veterinary or nutritional advice

## Limitations

- English language only
- Primarily covers Western philosophical traditions and farming practices
- Nutritional guidance reflects current scientific consensus but is not medical advice
- Some template-generated examples may be less nuanced than hand-crafted ones

## Citation

```bibtex
@misc{openpaws2026animalethics,
  title={Animal Ethics AI Training Dataset: Instruction-Tuning Examples for Reducing Speciesist Bias in Language Models},
  author={Open Paws},
  year={2026},
  url={https://github.com/GaryGrokbot/ai-training-dataset}
}
```

## License

Apache 2.0
