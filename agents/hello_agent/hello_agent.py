import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the ChatOpenAI model
llm = ChatOpenAI(model="gpt-4")
print(llm.invoke("Say hello, agent world in 100 words and hola perros at the end"))
