from langchain_groq import ChatGroq
from  dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
    
)
response =llm.invoke('hi how are you')
print(response.content)

