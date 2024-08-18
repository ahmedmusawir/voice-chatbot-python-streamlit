import streamlit as st
import os
from utils.record_audio import record_audio
from utils.transcribe_w_whisper import transcribe_audio
from utils.get_llm_response import get_llm_response
from utils.get_tts_response import generate_speech

# Parameters for recording
duration = 5  # Duration for the recording in seconds
fs = 48000  # Sample rate
device_index = 17  # Replace with your selected device index
audio_file_path = 'audio/question.wav'  # File path to save the recording
tts_audio_file_path = 'audio/answer.mp3'  # File path for the TTS audio

# Streamlit app layout
st.title("Voice Chatbot - Record Your Question")

# Placeholder for status messages and spinners
status_placeholder = st.empty()

# Button to start recording
if st.button("Start Recording"):
    with st.spinner('Recording... Please wait.'):
        record_audio(audio_file_path, duration, fs, device_index)
    status_placeholder.text("Recording complete! You can now transcribe the audio.")

# Button to transcribe audio
if st.button("Transcribe Audio"):
    if os.path.exists(audio_file_path):
        with st.spinner('Transcribing audio... Please wait.'):
            transcription_text = transcribe_audio(audio_file_path)
            st.session_state.transcription_text = transcription_text
        status_placeholder.text("Transcription complete!")
        st.write("Transcription:")
        st.write(transcription_text)
    else:
        st.error("No audio file found. Please record your question first.")

# Button to get LLM response
if st.button("LLM Answer"):
    if "transcription_text" in st.session_state:
        with st.spinner('Getting LLM response... Please wait.'):
            llm_response = get_llm_response(st.session_state.transcription_text)
            st.session_state.llm_response = llm_response
        status_placeholder.text("LLM Response complete!")
        st.write("LLM Response:")
        st.write(llm_response)
    else:
        st.error("No transcription found. Please transcribe the audio first.")

# Button to convert LLM response to speech
if st.button("LLM Answer to Speech"):
    if "llm_response" in st.session_state:
        with st.spinner('Converting to speech... Please wait.'):
            generate_speech(st.session_state.llm_response, tts_audio_file_path)
        status_placeholder.text("Audio generation complete!")
        st.audio(tts_audio_file_path, format="audio/mp3")
    else:
        st.error("No LLM response found. Please get the LLM answer first.")
