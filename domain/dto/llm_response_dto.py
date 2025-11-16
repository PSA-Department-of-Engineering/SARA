"""DTOs for LLM data transfer."""

from pydantic import BaseModel


class LLMResponseDTO(BaseModel):
    """DTO for LLM response data."""
    response: str