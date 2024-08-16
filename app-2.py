import streamlit as st
import os
from utils.record_audio import record_audio
from utils.transcribe_w_whisper import transcribe_audio

# Parameters for recording
duration = 5  # Duration for the recording in seconds
fs = 48000  # Sample rate
device_index = 17  # Replace with your selected device index
audio_file_path = 'audio/question.wav'  # File path to save the recording

# Streamlit app layout
st.title("Voice Chatbot - Record Your Question")

# Placeholder for status messages
status_placeholder = st.empty()

# Button to start recording
if st.button("Start Recording"):
    status_placeholder.text("Recording... Please wait.")
    record_audio(audio_file_path, duration, fs, device_index)
    status_placeholder.text("Recording complete! You can now transcribe the audio.")

# Button to transcribe audio
if st.button("Transcribe Audio"):
    if os.path.exists(audio_file_path):
        status_placeholder.text("Transcribing audio... Please wait.")
        transcription = transcribe_audio(audio_file_path)
        status_placeholder.text("Transcription complete!")
        st.write("Transcription:")
        st.write(transcription)
    else:
        st.error("No audio file found. Please record your question first.")
