import requests
import streamlit as st


def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8001/science/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With LLAMA3.2 API')

input_text=st.text_input("Search a book about ")



if input_text:
    st.write(get_ollama_response(input_text))

# Run this by taping streamlit run client.py