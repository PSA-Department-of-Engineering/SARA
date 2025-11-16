"""Check audio device sample rate support on Raspberry Pi."""
import pyaudio

audio = pyaudio.PyAudio()

# Get default input device info
default_device = audio.get_default_input_device_info()
print(f"\nDefault Input Device: {default_device['name']}")
print(f"Default Sample Rate: {default_device['defaultSampleRate']}")
print(f"Max Input Channels: {default_device['maxInputChannels']}")

# Test common sample rates
rates = [8000, 16000, 22050, 44100, 48000]
print("\nSupported Sample Rates:")

for rate in rates:
    try:
        if audio.is_format_supported(
            rate,
            input_device=default_device['index'],
            input_channels=1,
            input_format=pyaudio.paInt16
        ):
            print(f"  ✓ {rate} Hz - SUPPORTED")
    except ValueError:
        print(f"  ✗ {rate} Hz - NOT SUPPORTED")

audio.terminate()
