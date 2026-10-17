from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model='gpt-3.5-turbo')

@tool
def addition(a:int, b:int) -> int:
    """Add"""
    return a+b
@tool
def Multiply(a:int, b:int) -> int:
    """Multiple"""
    return a*b

#tool binding

llm_with_tools=llm.bind_tools([addition,Multiply])
messages=[]
query=HumanMessage("can you please perform product of these two numbers 4 and 6. also please add those number")
messages.append(query)

#tool calling

AI=llm_with_tools.invoke(messages)
messages.append(AI)
tool_call=AI.tool_calls[0]

tool_message=ToolMessage(content=str(tool_call),name=tool_call['name'],tool_call_id=tool_call['id'])
messages.append(tool_message)

#tool exec
response=llm_with_tools.invoke(messages)
print(response.content)