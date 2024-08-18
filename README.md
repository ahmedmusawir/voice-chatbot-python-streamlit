# Voice Chatbot with Streamlit and Advanced LLMs

## Overview

This project is a voice-based chatbot application that integrates cutting-edge LLM models, including OpenAI GPT-4o, Claude Sonnet 3.5, Llama 3.1 70b, and Gemini Pro 1.5. Built with Streamlit, this chatbot captures voice input, transcribes it using OpenAI’s Whisper model, generates a response using the selected LLM, and then converts the response into speech using OpenAI’s TTS capabilities.

![Voice Chatbot with Streamlit](https://res.cloudinary.com/dyb0qa58h/image/upload/v1723942489/Voice_Chatbot_w_Steamlit_jigrsu.jpg)

## Features

- Voice Input: Users can interact with the chatbot using their voice.
- Multiple LLMs: The chatbot supports multiple advanced LLM models, which can be selected from the sidebar.
- Real-time Transcription: Audio input is transcribed in real-time using OpenAI’s Whisper model.
- Text-to-Speech Output: The LLM's text response is converted to speech and played back to the user.
- Responsive UI: The user interface is built with Streamlit, offering a clean and responsive design.

## Technologies Used

- Streamlit: For building the web-based UI.
- OpenAI Whisper: For accurate speech-to-text transcription.
- OpenAI GPT-4o: For generating intelligent responses.
- Claude Sonnet 3.5 (Anthropic): Another option for LLM-based responses.
- Llama 3.1 70b (Meta AI): Advanced LLM from Meta AI.
- Gemini Pro 1.5 (Google DeepMind): LLM developed by Google DeepMind.
- OpenAI TTS: For converting text responses into speech.

## Installation

To run this project locally, follow these steps:

1. Clone the Repository

```
git clone https://github.com/yourusername/voice-chatbot-python-streamlit.git
cd voice-chatbot-python-streamlit

```

2. Set Up the Virtual Environment:

```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

```

3. Install Dependencies:

```
pip install -r requirements.txt

```

4. Set Up API Keys:

- Create a .env file in the root directory and add your API keys for OpenAI, Anthropic, Groq, and Google.
- Example .env file:

```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key

```

5. Run the Application:

```
streamlit run app.py

```

## Usage

1. Select your preferred LLM model from the sidebar.
2. Click "Ask Question" and speak your query.
3. Wait for the transcription, LLM response, and TTS to complete.
4. Listen to the AI’s spoken response.
