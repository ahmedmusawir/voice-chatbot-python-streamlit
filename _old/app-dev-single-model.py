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
st.title("Voice Chatbot")

# Placeholder for status messages and spinners
status_placeholder = st.empty()
transcription_placeholder = st.empty()
response_placeholder = st.empty()
tts_placeholder = st.empty()

# Check if process is running
process_running = st.session_state.get("process_running", False)

# "Ask Question" Button
if st.button("Ask Question", disabled=process_running):
    st.session_state.process_running = True

    with st.spinner('Recording... Please wait.'):
        record_audio(audio_file_path, duration, fs, device_index)
    status_placeholder.text("Question generation complete...")

    if os.path.exists(audio_file_path):
        with st.spinner('Transcribing with Whisper... Please wait.'):
            transcription_text = transcribe_audio(audio_file_path)
            st.session_state.transcription_text = transcription_text
        transcription_placeholder.markdown(
            f'<div style="background-color:#e0f7fa;padding:10px;border-radius:5px;">'
            f'<strong>👤 You:</strong> {transcription_text}</div>',
            unsafe_allow_html=True
        )

    if "transcription_text" in st.session_state:
        with st.spinner('Getting LLM answer with GPT 4o... Please wait.'):
            llm_response = get_llm_response(st.session_state.transcription_text)
            st.session_state.llm_response = llm_response
        response_placeholder.markdown(
            f'<div style="background-color:#ffe0e0;padding:10px;border-radius:5px;margin:1rem 0rem;">'
            f'<strong>🤖 AI:</strong> {llm_response}</div>',
            unsafe_allow_html=True
        )

    if "llm_response" in st.session_state:
        with st.spinner('Converting LLM answer to speech with TTS-1... Please wait.'):
            generate_speech(st.session_state.llm_response, tts_audio_file_path)
        tts_placeholder.text("LLM Answer to speech by TTS-1 complete...")

        # Display the audio player (Auto-playing might not work due to browser restrictions)
        st.audio(tts_audio_file_path, format="audio/mp3")

    st.session_state.process_running = False
