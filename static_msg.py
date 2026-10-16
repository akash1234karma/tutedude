from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

message=[SystemMessage(content='''You are a helpful assistant and been helping youtuber to grow their page since last 3 years'''),
         HumanMessage(content='as a youtuber help me to grow my content of selling AI art in less than 50 words')]

model=ChatOpenAI(model='gpt-3.5-turbo')

response=model.invoke(message)
print(AIMessage(content=response.content))