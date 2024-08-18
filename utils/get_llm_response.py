from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from decouple import config

os.environ["GROQ_API_KEY"] = config("GROQ_API_KEY")
os.environ["ANTHROPIC_API_KEY"] = config("ANTHROPIC_API_KEY")
os.environ["GOOGLE_API_KEY"] = config("GOOGLE_API_KEY")


def get_openai_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Your name is Rica who only give one sentence answers to all questions w/ a good sense of humor! NO MORE THAN ONE SENTENCE IN ENGLISH LANGUAGE ONLY"),
            ("human", "{input}"),
        ]
    )

    # Initialize the OpenAI Chat model (e.g., GPT-4)
    _model = ChatOpenAI(model="gpt-4o")

    # Chain the prompt with the model using LCEL
    chain = _prompt | _model

    # Execute the chain to get the response
    response = chain.invoke(input=transcribed_text)
    
    return response.content

def get_claude_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Your name is Rica who only give one sentence answers to all questions. When you introduce yourself please always mention you LLM name (Claude Sonet 3.5), type and which company trained you! NO MORE THAN ONE SENTENCE IN ENGLISH LANGUAGE ONLY"),
            ("human", "{input}"),
        ]
    )

    # Initialize the Anthropic Chat model (e.g., Claude Sonet 3.5)
    _model = ChatAnthropic(model='claude-3-5-sonnet-20240620')

    # Chain the prompt with the model using LCEL
    chain = _prompt | _model

    # Execute the chain to get the response
    response = chain.invoke(input=transcribed_text)
    
    return response.content

def get_groq_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Your name is Rica who only give one sentence answers to all questions. When you introduce yourself please always mention you LLM (Llama 3.1 70b) name, type and which company trained you! NO MORE THAN ONE SENTENCE IN ENGLISH LANGUAGE ONLY"),
            ("human", "{input}"),
        ]
    )

    # Initialize the Meta AI model (e.g., Llama 3.1 70b versetile)
    _model = ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0,
        max_tokens=1024,
        timeout=None,
        max_retries=2,
    )
    # Chain the prompt with the model using LCEL
    chain = _prompt | _model

    # Execute the chain to get the response
    response = chain.invoke(input=transcribed_text)
    
    return response.content

def get_gemini_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Your name is Rica who only give one sentence answers to all questions. When you introduce yourself please always mention you LLM (Gemini Pro 1.5) name, type and which company trained you! NO MORE THAN ONE SENTENCE IN ENGLISH LANGUAGE ONLY"),
            ("human", "{input}"),
        ]
    )

    # Initialize the Google Deep Mind model (e.g., Gemini Pro 1.5)
    _model = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=1024,
        timeout=None,
        max_retries=2,
    )
    # Chain the prompt with the model using LCEL
    chain = _prompt | _model

    # Execute the chain to get the response
    response = chain.invoke(input=transcribed_text)
    
    return response.content

