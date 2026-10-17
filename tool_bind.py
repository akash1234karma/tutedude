from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model='gpt-3.5-turbo')

@tool
def addition(a:int, b:int) ->int:
    """Adding two number"""
    return a+b

@tool
def multiply(a:int, b:int) ->int:
    """Multiply two number"""
    return a*b

llm_with_tool=llm.bind_tools([addition,multiply])
response=llm_with_tool.invoke([HumanMessage(content='Add 4 and 6')])

print(response)
