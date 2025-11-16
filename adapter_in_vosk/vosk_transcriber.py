"""Driver adapters for input handling."""

import vosk  # type: ignore
import pyaudio
import json
import os

from domain.dto.conversation_dto import ConversationDTO
from application.port.inbound.speech_input_port import SpeechInputPort
from config.logging_config import get_logger

logger = get_logger(__name__)


class VoskTranscriber():
    """Vosk-based speech transcriber."""

    def __init__(self):
        """Initialize Vosk model and recognizer."""
        # Get the absolute path to the model directory
        model_path = os.path.join(os.path.dirname(__file__), 'vosk-model')
        
        try:
            self.model = vosk.Model(model_path)
            self.recognizer = vosk.KaldiRecognizer(self.model, 48000)
            self.audio = pyaudio.PyAudio()
            self.speech_port = SpeechInputPort()
        except Exception as e:
            logger.error("❌ Vosk initialization failed", error=str(e))
            raise

    def transcribe_speech(self) -> ConversationDTO:
        """Record and transcribe speech."""
        try:
            stream = self.audio.open(
                format=pyaudio.paInt16, 
                channels=1, 
                rate=48000, 
                input=True, 
                frames_per_buffer=8192
            )
            stream.start_stream()
            logger.info("🎤 Listening...")
        except Exception as e:
            logger.error("❌ Audio stream failed", error=str(e))
            raise
            raise

        while True:
            try:
                data = stream.read(4096, exception_on_overflow=False)
                
                if self.recognizer.AcceptWaveform(data):  # type: ignore
                    result = json.loads(self.recognizer.Result())  # type: ignore
                    user_input = result.get('text', '')
                    
                    if user_input:
                        logger.info("📝 Transcribed", text=user_input)
                        
                        stream.stop_stream()
                        stream.close()
                        
                        # Call the use case through the port
                        return self.speech_port.handle_conversation(user_input)
                        
            except Exception as e:
                logger.error("❌ Transcription error", error=str(e))
                stream.stop_stream()
                stream.close()
                raise
