"""Main entry point for SARA application."""
from adapter_in_vosk.vosk_transcriber import VoskTranscriber
from config.logging_config import configure_logging, get_logger

# Configure logging at application startup
configure_logging(log_level="INFO")
logger = get_logger(__name__)


def main():
    """Run the SARA conversation application."""
    logger.info("application_starting", 
                app_name="SARA - Speech-Assisted Response Application")

    try:
        transcriber = VoskTranscriber()
        logger.info("transcriber_initialized", component="VoskTranscriber")
    except Exception as e:
        logger.error("transcriber_initialization_failed", 
                    component="VoskTranscriber", 
                    error=str(e))
        raise
    
    logger.info("system_ready", message="Start speaking...")
    
    try:
        # Main conversation loop
        while True:
            logger.debug("waiting_for_speech_input")
            
            # Get speech input via the driver adapter
            # The adapter internally handles the use case execution
            speech_dto = transcriber.transcribe_speech()

            # Display the conversation result
            logger.info("conversation_turn_completed",
                       timestamp=speech_dto.timestamp.isoformat(),
                       user_input=speech_dto.user_input,
                       mode=speech_dto.mode.value,
                       response=speech_dto.response)

    except KeyboardInterrupt:
        logger.info("application_shutdown", reason="user_interrupt")
    except Exception as e:
        logger.error("application_error", error=str(e), exc_info=True)
        raise


if __name__ == "__main__":
    main()
