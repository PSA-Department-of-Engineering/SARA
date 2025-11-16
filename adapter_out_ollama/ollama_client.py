"""Driven adapters for external services."""

import ollama

from domain.dto.llm_request_dto import LLMRequestDTO
from domain.dto.llm_response_dto import LLMResponseDTO
from config.logging_config import get_logger

logger = get_logger(__name__)


class OllamaClient():
    """Ollama implementation of LLM client."""

    def generate_response(self, request: LLMRequestDTO) -> LLMResponseDTO:
        """Generate a response using Ollama."""
        logger.info("generating_llm_response", 
                   model=request.model, 
                   prompt_length=len(request.prompt))
        logger.debug("llm_request_details", 
                    model=request.model, 
                    prompt=request.prompt[:100] + "..." if len(request.prompt) > 100 else request.prompt)
        
        try:
            response = ollama.generate(model=request.model, prompt=request.prompt)
            
            response_text = response["response"]
            logger.info("llm_response_generated", 
                       model=request.model,
                       response_length=len(response_text))
            logger.debug("llm_response_details", 
                        response=response_text[:100] + "..." if len(response_text) > 100 else response_text)
            
            return LLMResponseDTO(response=response_text)
            
        except Exception as e:
            logger.error("llm_generation_failed", 
                        model=request.model, 
                        error=str(e),
                        exc_info=True)
            raise
