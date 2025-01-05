import requests
import streamlit as st

def get_ollama_response(input_text):
    """Fetch response from the Ollama API."""
    try:
        response = requests.post(
            "http://localhost:49986/science/invoke",
            json={'input': {'topic': input_text}}
        )
        response.raise_for_status()  # Raise an error for bad status codes
        response_data = response.json()
        return response_data.get('output', "No output found in response.")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
    except ValueError:
        return "Error: Unable to decode the JSON response."

# Streamlit framework setup
st.title('Langchain Demo With LLAMA3.2 API')

input_text = st.text_input("Search a book about")

if input_text:
    result = get_ollama_response(input_text)
    st.write(result)

# Run this by typing `streamlit run client.py`
