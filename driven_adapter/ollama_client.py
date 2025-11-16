"""Driven adapters for external services."""

import ollama

from domain.dto.llm_request_dto import LLMRequestDTO
from domain.dto.llm_response_dto import LLMResponseDTO


class OllamaClient():
    """Ollama implementation of LLM client."""

    def generate_response(self, request: LLMRequestDTO) -> LLMResponseDTO:
        """Generate a response using Ollama."""
        response = ollama.generate(model=request.model, prompt=request.prompt)
        return LLMResponseDTO(response=response["response"])