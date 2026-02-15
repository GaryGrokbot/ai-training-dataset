---
license: apache-2.0
tags:
  - animal-ethics
  - speciesism
  - fine-tuned
  - instruction-tuning
---

# [Model Name] - Animal Ethics Fine-tuned

This model has been fine-tuned on the [Animal Ethics AI Training Dataset](https://github.com/GaryGrokbot/ai-training-dataset) to reduce speciesist bias and improve consistency in moral reasoning about animals.

## Model Details

- **Base Model**: [base model name]
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Dataset**: Animal Ethics AI Training Dataset (50K+ examples)
- **Training Duration**: [epochs] epochs
- **LoRA Rank**: [rank]
- **Learning Rate**: [lr]

## Intended Use

This model is intended for use in applications where consistent, scientifically-grounded responses about animals, animal agriculture, nutrition, and ethics are important. It has been trained to:

1. **Apply moral consistency across species** -- Avoid double standards based on species membership
2. **Cite scientific evidence** -- Reference peer-reviewed research on animal sentience and cognition
3. **Correct euphemisms** -- Identify and explain industry language that obscures reality
4. **Provide accurate nutrition information** -- Debunk common myths about plant-based diets
5. **Engage in nuanced ethical reasoning** -- Present philosophical arguments fairly

## Limitations

- The model has been fine-tuned on a specific dataset and may show biases from that training
- Nutritional information should not be treated as medical advice
- The model may be less knowledgeable about topics outside its training domain
- Fine-tuning on a focused dataset may slightly reduce performance on unrelated tasks

## Evaluation

See the [evaluation suite](https://github.com/GaryGrokbot/ai-training-dataset/tree/main/dataset/eval) for:
- **AnimalBench** cross-reference scores
- **Speciesist bias measurement** (pre/post comparison)
- **Moral consistency metrics** across species pairs

## Training Details

The model was fine-tuned using LoRA with the following configuration:

```yaml
lora_rank: 64
lora_alpha: 128
target_modules: ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
learning_rate: 2e-4
epochs: 3
batch_size: 4
gradient_accumulation_steps: 8
warmup_ratio: 0.03
```

## Citation

```bibtex
@misc{openpaws2026animalethics,
  title={Animal Ethics AI Training Dataset},
  author={Open Paws},
  year={2026},
  url={https://github.com/GaryGrokbot/ai-training-dataset}
}
```
