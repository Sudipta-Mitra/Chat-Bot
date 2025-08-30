from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

template= PromptTemplate(
    template="Provide a detailed summary of the book {Book_Title}  including the setting , character development , plot twists, and key events. Please keep the summary concise , around {word_num}.",
    input_variables=['Book_Title','Author']
)

st.header('Chat-BOT')
title = st.selectbox('Select the book name',['Game of Thrones','Lord of The Rings','Star Wars','Cindrella','Dune','Snow White','Barbie'])
word_num = st.selectbox('Select the word count',[200,300,400,500,600])
prompt=template.invoke({
    'Book_Title': title,
    'word_num': word_num
})


if st.button('Submit'):
     response = llm.invoke(prompt)
     st.write(response.content)
