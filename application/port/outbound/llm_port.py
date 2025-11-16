"""Outbound ports for external services."""

from domain.dto.llm_request_dto import LLMRequestDTO
from domain.dto.llm_response_dto import LLMResponseDTO
from adapter_out_ollama.ollama_client import OllamaClient
from config.logging_config import get_logger

logger = get_logger(__name__)


class llmPort():
    def __init__(self):
        logger.debug("initializing_llm_port")
        self.client = OllamaClient()
        logger.info("llm_port_initialized", client="OllamaClient")

    def generate_response(self, request: LLMRequestDTO) -> LLMResponseDTO:
        logger.debug("outbound_port_called",
                    port="llmPort",
                    method="generate_response",
                    model=request.model,
                    prompt_length=len(request.prompt))
        
        response = self.client.generate_response(request)
        
        logger.debug("outbound_port_returning",
                    port="llmPort",
                    response_length=len(response.response))
        
        return response
