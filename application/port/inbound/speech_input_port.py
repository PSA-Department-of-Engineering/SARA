"""Inbound ports for input handling."""

from domain.dto.speech_dto import SpeechDTO
from application.use_cases.handle_conversation import HandleConversation
from config.logging_config import get_logger

logger = get_logger(__name__)


class SpeechInputPort:
    """Port for speech input."""

    def __init__(self):
        """Initialize the port with the use case handler."""
        self.conversation_handler = HandleConversation()

    def handle_conversation(self, user_input: str) -> SpeechDTO:
        """Transcribe speech to text."""
        logger.debug("inbound_port_called", 
                    port="SpeechInputPort", 
                    method="handle_conversation",
                    user_input_length=len(user_input))
        
        result = self.conversation_handler.handle_conversation(user_input)
        
        logger.debug("inbound_port_returning", 
                    port="SpeechInputPort",
                    has_result=result is not None)
        
        return result
