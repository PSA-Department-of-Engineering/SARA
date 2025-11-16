"""Use cases for application logic."""

from datetime import datetime

from domain.dto.conversation_dto import ConversationDTO
from domain.dto.llm_request_dto import LLMRequestDTO
from domain.enum.processing_mode import ProcessingMode
from outbound_port.llm_port import llmPort


class HandleConversation:
    """Use case for handling user conversations."""

    def execute(self, user_input: str) -> ConversationDTO:
        """Execute the conversation handling logic."""
        # Determine mode
        if "think" in user_input.lower():
            mode = ProcessingMode.DEEP_THINK
        else:
            mode = ProcessingMode.DEFAULT

        # Create LLM request
        request = LLMRequestDTO(prompt=user_input, model=mode.value)

        # Get LLM response via port
        port = llmPort()
        response_dto = port.generate_response(request)

        # Create and return conversation DTO
        return ConversationDTO(
            user_input=user_input,
            response=response_dto.response,
            mode=mode,
            timestamp=datetime.now()
        )