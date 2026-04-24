from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.cache import InMemoryCache 
from langchain.globals import set_llm_cache


load_dotenv()

# Initialize chat model
chat = ChatOpenAI(model="gpt-3.5-turbo")
set_llm_cache(InMemoryCache())