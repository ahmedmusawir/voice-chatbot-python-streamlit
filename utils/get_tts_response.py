from pathlib import Path
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

def generate_speech(text_input, output_path):
    # Create the speech using OpenAI's TTS model
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text_input
    )

    # Open the file to write the response content
    with open(output_path, "wb") as file:
        for chunk in response.iter_bytes():
            file.write(chunk)
