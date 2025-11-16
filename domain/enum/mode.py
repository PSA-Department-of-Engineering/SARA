"""Domain entities for SARA."""

from enum import Enum


class ProcessingMode(Enum):
    """Enumeration for LLM processing modes."""
    DEFAULT = "gemma3:1b"
    DEEP_THINK = "dolphin-phi"