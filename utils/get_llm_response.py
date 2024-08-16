from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def get_llm_response(transcribed_text):
    # Define the prompt template using LCEL
    _prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
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
