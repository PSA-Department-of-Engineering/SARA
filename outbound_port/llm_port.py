"""Outbound ports for external services."""

from domain.dto.llm_request_dto import LLMRequestDTO
from domain.dto.llm_response_dto import LLMResponseDTO
from driven_adapter.ollama_client import OllamaClient


class llmPort():
    def __init__(self):
        self.client = OllamaClient()

    def generate_response(self, request: LLMRequestDTO) -> LLMResponseDTO:
        return self.client.generate_response(request)