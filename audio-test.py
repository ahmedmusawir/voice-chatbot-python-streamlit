import sounddevice as sd
import soundfile as sf

# Parameters for recording
duration = 5  # seconds
fs = 48000  # Sample rate
device_index = 17  # Thronmax MDrill Zero Microphone (WASAPI)

# Record audio
def record_voice(filename, duration, fs, device_index):
    print("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, device=device_index)
    sd.wait()  # Wait until recording is finished
    sf.write(filename, audio_data, fs)
    print(f"Recording saved to {filename}")

# Example usage
record_voice('audio/question.wav', duration, fs, device_index)
