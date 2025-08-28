from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

# Streamlit UI config
st.set_page_config(page_title="ChatBot", layout="centered")
st.title("🧠 Kooie-Bot")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Say something...")

if prompt:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get LLM response
    with st.chat_message("assistant"):
        response = llm.invoke(prompt)
        st.markdown(response.content)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response.content})
