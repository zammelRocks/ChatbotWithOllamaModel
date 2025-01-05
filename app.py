from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful research assistant and you will help student finding books,research papers related to their interests. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('LIbrary assistant with LLAMA3 ollama')
input_text=st.text_input("Search the topic with generative AI")

# ollama LLAma3.2 LLm 
llm=Ollama(model="llama3.2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

# trying this  locally with streamlit
# streamlit run app.py