"""DTOs for domain data transfer."""

from datetime import datetime

from pydantic import BaseModel

from domain.enum.processing_mode import ProcessingMode


class ConversationDTO(BaseModel):
    """DTO for conversation data."""
    user_input: str
    response: str
    mode: ProcessingMode
    timestamp: datetime
