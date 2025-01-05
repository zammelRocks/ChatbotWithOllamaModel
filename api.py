from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()


os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)


##ollama llama2
llm=Ollama(model="llama3.2")

prompt=ChatPromptTemplate.from_template("Look for scientific books and research papers about {topic} ")


add_routes(
    app,
    prompt|llm,
    path="/science"


)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8001)

#Change the prompt template and apply changes
#change path
#write host
