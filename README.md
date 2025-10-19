# SARA

Version: 1.0
Author: Project Owner  
Last Updated: 2025-10-19

## 1. Introduction

SARA is an AI-powered assistant designed to run on a Raspberry Pi 4 (8GB). It uses open-source models for wake word detection, language processing, and text-to-speech to provide personalized alarms and interactions.

## 2. Tech Stack
- **LLM**: Gemma 2 (2B parameters, default for speed) and Phi-3 Mini (3.8B parameters, for deeper thinking)
- **Wake Word Detection**: OpenWakeWord (open-source wake word detection)
- **Speech-to-Text**: Vosk (Toolkit with small, efficient models)
- **Text-to-Speech**: Piper (Fast, high-quality, natural-sounding)
- **Runtime**: Ollama for LLM, Python SDKs for other components
- **Hardware**: Raspberry Pi 4 (8GB RAM)

## 3. Features

### A. Modes
- **Default Mode**: Uses Gemma 2 (2B parameters) for fast, instant responses.
- **Deep Think Mode**: Switches to Phi-3 Mini when prompted (e.g., "think about it") for more detailed, thoughtful replies.

