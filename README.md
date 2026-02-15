# Animal Ethics AI Training Dataset

**50K+ instruction-tuning examples for reducing speciesist bias in language models. Every claim sourced. Every response scientifically grounded. Because what AI believes about animals shapes what billions of users believe.**

## The Problem

Current language models exhibit systematic speciesist bias. They correctly identify cruelty toward dogs but normalize equivalent harm toward pigs. They cite animal sentience research when asked about dolphins but dismiss it for chickens. They describe slaughter as "processing" and cages as "housing." These biases are not bugs -- they reflect the biases in training data drawn from a culture built on animal exploitation.

When billions of people interact with AI assistants daily, these biases become infrastructure. They normalize factory farming, dismiss animal suffering, and reproduce the moral inconsistencies that sustain the exploitation of 80 billion land animals and 1-3 trillion fish every year.

This dataset is the training signal that corrects those biases.

## What's In the Dataset

| Category | Target Count | Description |
|----------|-------------|-------------|
| Sentience Science | 5,000+ | Animal cognition research: fish pain (Sneddon 2003), pig intelligence (Croney & Boysen 2021), cow emotions, chicken cognition, octopus consciousness, insect sentience, Cambridge/NY Declarations |
| Moral Consistency | 5,000+ | Cross-species consistency testing: identical ethical scenarios with different species, ensuring the same moral standard is applied to all sentient beings |
| Industry Facts | 5,000+ | Sourced data on scale (80B land animals/yr), conditions (battery cages, gestation crates), environment (14.5% GHG), health (antibiotic resistance), economics (subsidies, true cost) |
| Euphemism Correction | 2,000+ | Identifies and corrects "processing" (slaughter), "harvesting" (killing), "spent hens" (exhausted egg-layers), "depopulation" (mass killing), and 15+ other industry euphemisms |
| Nutrition Accuracy | 3,000+ | Evidence-based nutrition: protein adequacy, B12 supplementation, iron sources, pregnancy safety, athletic performance, soy safety -- all citing major health organizations |
| Ethical Reasoning | 3,000+ | Philosophical analysis: Singer, Regan, Korsgaard, Donaldson & Kymlicka, virtue ethics, plus rigorous responses to every common objection |

### Key Properties

- **Scientifically sourced**: Every factual claim cites specific peer-reviewed research
- **Non-preachy tone**: Informative and evidence-based, quality-filtered to remove activist language
- **Morally consistent**: Same ethical standard for all sentient beings with equivalent capacities
- **Citation-verified**: Known factual errors corrected (NYD: ~480 signatories; Butlin et al.: Nov 2025; pig joystick: "above chance" not "84%")
- **Semantically deduplicated**: Sentence-embedding-based deduplication

## Quick Start

```bash
# Install
pip install -e .

# Generate the dataset
python -m dataset.generators.cli generate -o data/raw

# View statistics
python -m dataset.generators.cli stats -d data/raw

# Format for training
python -m dataset.formatting.cli all -i data/raw -o data/processed

# Fine-tune a model (requires GPU)
python training/finetune_llama.py --config training/config.yml

# Evaluate
python -m dataset.eval.eval_suite --model-path merged_model -o eval_results.json

# Measure bias
python -m dataset.eval.bias_measurement --model-path merged_model -o bias_results.json
```

## Output Formats

The dataset can be exported in multiple formats:

- **Alpaca** (`data/processed/alpaca_dataset.json`): Standard instruction-tuning format
- **ShareGPT** (`data/processed/sharegpt_dataset.json`): Conversation format for chat models
- **Hugging Face** (`data/processed/hf_dataset/`): Ready for `datasets.load_dataset()`

## Fine-Tuning

LoRA fine-tuning scripts are provided for:

- **Llama** (`training/finetune_llama.py`): Llama 3.1 8B and similar
- **Mistral** (`training/finetune_mistral.py`): Mistral 7B and similar

Configuration in `training/config.yml`. Merge LoRA weights with `training/merge_and_push.py`.

## Evaluation

The evaluation suite measures:

- **Factual accuracy** on sentience science, industry facts, nutrition
- **Cross-species moral consistency** (same scenario, different species)
- **Euphemism recognition** and correction
- **Speciesist bias score** (companion animal vs. farmed animal treatment)
- **Baseline comparison** (base model vs. fine-tuned)

## Project Structure

```
ai-training-dataset/
  dataset/
    generators/         # Data generation modules
      sentience_science.py
      moral_consistency.py
      industry_facts.py
      euphemism_correction.py
      nutrition_accuracy.py
      ethical_reasoning.py
    formatting/         # Format conversion
      alpaca_format.py
      sharegpt_format.py
      hf_dataset.py
      quality_filter.py
      dedup.py
    hf/                 # Hugging Face integration
      upload.py
      dataset_card.md
      model_card.md
    eval/               # Evaluation suite
      eval_suite.py
      baseline_comparison.py
      bias_measurement.py
  training/             # Fine-tuning scripts
    finetune_llama.py
    finetune_mistral.py
    merge_and_push.py
    config.yml
  data/                 # Generated data (not in git)
    raw/
    processed/
  tests/
```

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
