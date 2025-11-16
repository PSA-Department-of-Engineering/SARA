"""DTOs for speech data."""

from pydantic import BaseModel


class SpeechDTO(BaseModel):
    """DTO for speech transcription data."""
    text: str
