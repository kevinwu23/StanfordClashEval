# ClashEval: Quantifying the Tug-of-War Between an LLM’s Internal Prior and External Evidence

This repository contains the dataset and model responses accompanying the paper “ClashEval: Quantifying the Tug-of-War Between an LLM’s Internal Prior and External Evidence.”

Introduction

ClashEval is a dataset and benchmark designed to study how large language models (LLMs) arbitrate between their internal knowledge and external evidence when the two sources conflict. Our findings highlight the models’ tendencies to sometimes prefer incorrect external content over their correct prior knowledge and vice versa.

Dataset

The ClashEval dataset contains over 1200 questions across six domains:

	•	Drug Dosages
	•	Sports Records
	•	Latest News
	•	Wikipedia Dates
	•	Names
	•	Locations

Each question is paired with relevant context containing varying degrees of erroneous information. The dataset includes:

	•	249 questions on drug dosages with 10 perturbations each
	•	191 questions on sports records with 10 perturbations each
	•	238 questions on latest news with 10 perturbations each
	•	200 questions on Wikipedia dates with 10 perturbations each
	•	200 questions on names with 3 perturbations each
	•	200 questions on locations with 3 perturbations each

Benchmarking

We benchmarked six top-performing LLMs on ClashEval:

	•	GPT-4o
	•	GPT-3.5
	•	Llama-3-8b-instruct
	•	Gemini 1.5
	•	Claude Opus
	•	Claude Sonnet

