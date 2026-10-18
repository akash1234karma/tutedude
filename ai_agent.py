from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain_classic.agents import create_react_agent ,AgentExecutor
from langchain_classic import hub
from langsmith import Client
load_dotenv()

client=Client()
prompt=client.pull_prompt("hwchase17/react",dangerously_pull_public_prompt=True)

model=ChatOpenAI(model='gpt-3.5-turbo')
search_tool = DuckDuckGoSearchRun()
agent=create_react_agent(llm=model,tools=[search_tool],prompt=prompt)

agent_exc=AgentExecutor(agent=agent, tools=[search_tool], verbose=True, handle_parsing_errors=True)

response=agent_exc({'input':'How to prepare for ML, GenAI job'})

print(response['output'])

