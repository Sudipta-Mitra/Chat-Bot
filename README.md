
# 🧠 Kooie-Bot

Kooie-Bot is an intelligent AI chatbot built using **LangChain** and **Groq’s LLaMA 3.3 70B model**.  
It provides low-latency, high-performance conversational AI with conversational memory and a clean **Streamlit**-based UI.

---

## 🚀 Features
- ✅ Conversational memory (maintains chat history using `session_state`)
- ✅ Clean and interactive **Streamlit** web UI
- ✅ Low temperature (0.3) for focused and accurate responses
- ✅ Easily extendable to other front-ends or integrations
- ✅ Secrets managed via `.env` file
- ✅ Powered by **Groq LLMs** for high-speed inference

---

## 🛠️ Tech Stack
- **LangChain Groq** (`langchain_groq`) – Seamless integration with Groq’s LLMs  
- **Model:** `llama-3.3-70b-versatile`  
- **Streamlit** – Real-time chat UI  
- **Python-dotenv** – For environment variable management  

---

## 📂 Project Structure
```

Chat-Bot/
│── langchain\_model.py   # Main chatbot script
│── .env                 # Store your API keys 
│── requirements.txt     # Python dependencies

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sudipta-Mitra/Chat-Bot.git
cd Chat-Bot
````

### 2️⃣ Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
.\myenv\Scripts\activate

# Activate (Linux/Mac)
source myenv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create a **`.env`** file in the project root and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run the Chatbot

```bash
streamlit run langchain_model.py
```

Now open the Streamlit UI in your browser and start chatting with **Kooie-Bot** 🎉

---

## 📦 requirements.txt

Here’s a sample `requirements.txt` you can add:

```
langchain
langchain_groq
python-dotenv
streamlit
```

---

## 🔗 Connect

* Author: **Sudipta Mitra**
* GitHub: [Sudipta-Mitra](https://github.com/Sudipta-Mitra)

