import streamlit as st
from mlx_lm import load, generate

# Load the MLX model and tokenizer
model, tokenizer = load("mlx-community/Llama-3.2-1B-Instruct-MLXTuned")

# Streamlit UI
st.title("MLX Model: Llama-3.2-1B-Instruct")

# Get user input through Streamlit widget
prompt = st.text_input("Give prompt:", "")

# If the user has provided a prompt, generate and display the response
if prompt:
    if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
        messages = [{"role": "user", "content": prompt}]
        prompt = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )

    # Generate the response
    response = generate(model, tokenizer, prompt=prompt, verbose=True)

    # Display the generated response
    st.write("Response:")
    st.write(response)
