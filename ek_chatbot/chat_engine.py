from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)



# Initialize the LLM
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize the ChatChain
chat_chain = ChatChain(llm=llm)

async def generate_response(user_input):
    response = await chat_chain(user_input)
    return response
