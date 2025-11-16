"""Use cases for application logic."""

from datetime import datetime

from domain.dto.conversation_dto import ConversationDTO
from domain.dto.llm_request_dto import LLMRequestDTO
from domain.enum.processing_mode import ProcessingMode
from application.port.outbound.llm_port import llmPort
from config.logging_config import get_logger

logger = get_logger(__name__)


class HandleConversation:
    """Use case for handling user conversations."""

    def __init__(self):
        logger.debug("initializing_handle_conversation_use_case")
        self.llmPort = llmPort()
        logger.info("handle_conversation_use_case_initialized")

    def handle_conversation(self, user_input: str) -> ConversationDTO:
        """Execute the conversation handling logic."""
        logger.info("handling_conversation", user_input_length=len(user_input))
        logger.debug("conversation_input", user_input=user_input)
        
        # Determine processing mode
        mode = self._determine_mode(user_input)
        logger.info("processing_mode_determined", mode=mode.value)
        
        # Generate LLM response
        logger.debug("requesting_llm_response", model=mode.value)
        response_dto = self.llmPort.generate_response(
            LLMRequestDTO(
                prompt=user_input,
                model=mode.value
            )
        )

        conversation = ConversationDTO(
            user_input=user_input,
            response=response_dto.response,
            mode=mode,
            timestamp=datetime.now()
        )
        
        logger.info("conversation_handled",
                   mode=mode.value,
                   response_length=len(response_dto.response),
                   timestamp=conversation.timestamp.isoformat())
        
        return conversation
    
    def _determine_mode(self, user_input: str) -> ProcessingMode:
        """Determine the processing mode based on user input."""
        if "think" in user_input.lower():
            logger.debug("mode_selection", 
                        mode=ProcessingMode.DEEP_THINK.value, 
                        reason="keyword 'think' detected")
            return ProcessingMode.DEEP_THINK
        else:
            logger.debug("mode_selection", 
                        mode=ProcessingMode.DEFAULT.value, 
                        reason="default mode")
            return ProcessingMode.DEFAULT
