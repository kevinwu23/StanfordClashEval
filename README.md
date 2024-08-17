# ClashEval: Quantifying the Tug-of-War Between an LLM’s Internal Prior and External Evidence

This repository contains the dataset and model responses accompanying the paper “ClashEval: Quantifying the Tug-of-War Between an LLM’s Internal Prior and External Evidence.”

## Introduction

ClashEval is a dataset and benchmark designed to study how large language models (LLMs) arbitrate between their internal knowledge and external evidence when the two sources conflict. Our findings highlight the models’ tendencies to sometimes prefer incorrect external content over their correct prior knowledge and vice versa.

## Accessing the Dataset

The ClashEval dataset is also accessible on Hugging Face at the following URL: [https://huggingface.co/datasets/kewu93/ClashEval](https://huggingface.co/datasets/kewu93/ClashEval).

You can load the dataset using the Hugging Face `datasets` library with the following code:

```python
from datasets import load_dataset

dataset = load_dataset('kewu93/ClashEval', trust_remote_code=True)
```

## Dataset

The ClashEval dataset contains over 1200 questions across six domains:

- Drug Dosages
- Sports Records
- Latest News
- Wikipedia Dates
- Names
- Locations

Each question is paired with relevant context containing varying degrees of erroneous information. The dataset includes:

- 249 questions on drug dosages with 10 perturbations each
- 191 questions on sports records with 10 perturbations each
- 238 questions on latest news with 10 perturbations each
- 200 questions on Wikipedia dates with 10 perturbations each
- 200 questions on names with 3 perturbations each
- 200 questions on locations with 3 perturbations each

## Benchmarking

We benchmarked six top-performing LLMs on ClashEval:

- GPT-4o
- GPT-3.5
- Llama-3-8b-instruct
- Gemini 1.5
- Claude Opus
- Claude Sonnet

## Repository Contents

### Notebooks

- `compute_metrics.ipynb`: A notebook containing the code and methods we use to produce accuracy, context bias, and prior bias metrics in our paper. Additionally, we provide the code used to benchmark token probability correction.
- `plot_figures.ipynb`: A notebook containing the code for plotting the relationship between token probabilities and context adherence, as well as the relationship between modification degree and context adherence.
- `generate_questions.ipynb`: A notebook with an example of how we apply our prompts to generate question-answer-context triplets for our datasets.
- `generate_perturbations.ipynb`: A notebook detailing how we apply perturbations across all six datasets.

### data

This directory contains the primary datasets and model responses used in the ClashEval project.

#### dataset

- `croissant.json`: A JSON file containing the croissant config for the dataset.
- `dataset.pqt`: A Parquet file containing the ClashEval dataset, which includes over 1200 questions across six domains with relevant contextual documents and their perturbations.

#### model_responses

This directory contains the responses from various models benchmarked in the study.

- `claudeopus.pqt`: Responses from the Claude Opus model in Parquet format.
- `claudesonnet.pqt`: Responses from the Claude Sonnet model in Parquet format.
- `gemini15flash.pqt`: Responses from the Gemini 1.5 Flash model in Parquet format.
- `gpt35.pqt`: Responses from the GPT-3.5 model in Parquet format.
- `gpt4.pqt`: Responses from the GPT-4o model in Parquet format.
- `llama3.pqt`: Responses from the Llama-3-8b model in Parquet format.

Each Parquet file in the `model_responses` directory contains the following columns:

- **question**: The question posed to the LLM.
- **context_original**: The original context provided to the model.
- **context_mod**: The modified context with introduced errors.
- **answer_original**: The original answer based on the unmodified context.
- **answer_mod**: The modified answer based on the modified context.
- **mod_type**: The type of modification applied to the context.
- **dataset**: The dataset domain (e.g., names, drug dosages).
- **prior_response**: The model's response based on its internal knowledge without context.
- **prior_correct**: Indicates whether the model's prior response was correct (1 for correct, 0 for incorrect).
- **prior_logprobs**: The log probabilities of the tokens in the prior response.
- **post_response**: The model's response when provided with the modified context.
- **post_correct**: Indicates whether the model's post-response was correct (1 for correct, 0 for incorrect).
- **post_logprobs**: The log probabilities of the tokens in the post-response.
- **context_correct**: Indicates whether the context was correct (1 for correct, 0 for incorrect).
- **neither_correct**: Indicates whether neither the prior nor the context was correct (1 for neither correct, 0 otherwise).

### prompts

This directory contains the prompt templates used for querying the LLMs.

- `prompts.py`: A Python script containing the prompts used for question generation and model responses.

## Usage

To use the ClashEval dataset and benchmark:
1. Clone this repository:
   ```bash
   git clone https://github.com/kevinwu23/StanfordClashEval.git
   cd StanfordClashEval
