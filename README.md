# Python Learning

A hands-on Python and LLM learning repository covering foundational Python projects, model comparisons, fine-tuning, chatbot development, and a capstone-style application pipeline.

## Repository overview

This repo is organized as a collection of mini-projects and experiments that build progressively from basic Python + LLM usage to more advanced workflows like fine-tuning adapters and building application pipelines.

## Projects

### 1-API-vs-Local-Models
A beginner-friendly project focused on comparing different model access patterns:
- OpenAI API
- Gemini API
- Hugging Face models
- Local model usage

This folder contains sample scripts for calling models and comparing availability, capabilities, and basic usage patterns.

### 1.2-FineTuningProject
A practical fine-tuning project exploring parameter-efficient fine-tuning using LoRA/QLoRA.
- Training data and evaluation question files
- Baseline and finetuned model scripts
- Adapter storage and model artifacts
- Chat interface for interacting with the adapted model

This project demonstrates how to adapt a base model for a specific task or domain using lightweight fine-tuning techniques.

### 2-First-Chatbot
A simple chatbot project that introduces the basics of working with an LLM provider through a configurable application structure.
- Provider abstraction
- Configuration setup
- Chat app entry point

This is a good starting point for learning how to build interactive AI apps.

### 3-Capstone-Project1
A more complete application project that expands on the chatbot idea with structured provider logic and config-driven behavior.
- Multiple LLM providers
- Capstone-style app architecture
- Reusable application flow

This project represents a larger, more polished Python app built around LLM integration.

### python-handson
A comprehensive hands-on project that includes:
- LangChain-inspired pipeline architecture
- Data loading and configuration utilities
- Model inference flow
- Experiment notebooks
- Docker setup
- Example transcript and output data files

This folder is the most complete and feature-rich section of the repository and is ideal for learning end-to-end application design.

## Tech stack

- Python
- OpenAI / Gemini / Hugging Face APIs
- LangChain-style application patterns
- LoRA / QLoRA fine-tuning
- Jupyter notebooks
- Docker

## Learning path

This repo is structured to help a learner move from:
1. Basic model access and local API comparisons
2. Fine-tuning for custom tasks
3. Building a simple chatbot
4. Designing a more complete AI application
5. Working with data, pipelines, and deployment-related patterns

## Notes

Each project folder contains its own scripts, dependencies, and configuration files. For specific instructions, open the individual project folder and refer to its own README or setup files.

## License

This repository is intended for learning and experimentation.
