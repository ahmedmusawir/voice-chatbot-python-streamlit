import sounddevice as sd
import soundfile as sf

# Function to record audio
def record_audio(file_path, duration, fs, device_index):
    print("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, device=device_index)
    sd.wait()  # Wait until recording is finished
    sf.write(file_path, audio_data, fs)
    print(f"Recording saved successfully to {file_path}")
