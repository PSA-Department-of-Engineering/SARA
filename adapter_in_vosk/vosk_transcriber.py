"""Driver adapters for input handling."""

import vosk  # type: ignore
import pyaudio
import json
import os

from domain.dto.speech_dto import SpeechDTO
from application.port.inbound.speech_input_port import SpeechInputPort
from config.logging_config import get_logger

logger = get_logger(__name__)


class VoskTranscriber():
    """Vosk-based speech transcriber."""

    def __init__(self):
        """Initialize Vosk model and recognizer."""
        logger.info("initializing_vosk_transcriber")
        
        # Get the absolute path to the model directory
        model_path = os.path.join(os.path.dirname(__file__), 'vosk-model')
        
        try:
            self.model = vosk.Model(model_path)
            logger.debug("vosk_model_loaded", model_path=model_path)
        except Exception as e:
            logger.error("vosk_model_load_failed", model_path=model_path, error=str(e))
            raise
        
        self.recognizer = vosk.KaldiRecognizer(self.model, 16000)
        self.audio = pyaudio.PyAudio()
        self.speech_port = SpeechInputPort()
        logger.info("vosk_transcriber_initialized", sample_rate=16000)

    def transcribe_speech(self) -> SpeechDTO:
        """Record and transcribe speech."""
        logger.debug("opening_audio_stream")
        
        try:
            stream = self.audio.open(
                format=pyaudio.paInt16, 
                channels=1, 
                rate=16000, 
                input=True, 
                frames_per_buffer=8192
            )
            stream.start_stream()
            logger.info("listening_for_speech", status="active")
        except Exception as e:
            logger.error("audio_stream_open_failed", error=str(e))
            raise

        while True:
            try:
                data = stream.read(4096, exception_on_overflow=False)
                
                if self.recognizer.AcceptWaveform(data):  # type: ignore
                    result = json.loads(self.recognizer.Result())  # type: ignore
                    logger.debug("speech_recognized", result=result)
                    
                    user_input = result.get('text', '')
                    
                    if user_input:
                        logger.info("speech_transcribed", 
                                   text=user_input, 
                                   length=len(user_input))
                        
                        stream.stop_stream()
                        stream.close()
                        logger.debug("audio_stream_closed")
                        
                        # Call the use case through the port
                        logger.debug("invoking_conversation_handler", user_input=user_input)
                        return self.speech_port.handle_conversation(user_input)
                        
            except Exception as e:
                logger.error("speech_transcription_error", error=str(e))
                stream.stop_stream()
                stream.close()
                raise
