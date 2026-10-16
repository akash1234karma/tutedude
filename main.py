from langserve import add_routes
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

app=FastAPI()

class TranslationRequest(BaseModel):
    lang:str
    text:str

@app.get('/Hello')
def hello():
    return{'message':"How are you"}

@app.post('/llm')
def translate(request:TranslationRequest):
    llm=ChatOpenAI(model='gpt-3.5-turbo')
    prompt=PromptTemplate(template='Translate the text {text} from english to {lang}', input_variables=['text','lang'])
    parser=StrOutputParser()

    chain=prompt|llm|parser

    result=chain.invoke({'text':request.text, 'lang':request.lang})
    return{'translation':result}
