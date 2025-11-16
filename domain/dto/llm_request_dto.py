"""DTOs for LLM data transfer."""

from pydantic import BaseModel


class LLMRequestDTO(BaseModel):
    """DTO for LLM request data."""
    prompt: str
    model: str
