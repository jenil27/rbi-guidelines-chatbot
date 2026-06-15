# 📄 RBI Guidelines Chatbot

A RAG-based conversational chatbot to query RBI NBFC guidelines using LangChain, Groq LLM, and Gradio.

## 🚀 Demo

![Upload PDF](demo1.png)
![Ask Questions](demo2.png)
![Summary](demo3.png)

## 🛠️ Tech Stack

- **LangChain** — RAG pipeline
- **HuggingFace Embeddings** — `all-MiniLM-L6-v2` (free, no API key)
- **Groq LLM** — `llama-3.1-8b-instant` (free API)
- **FAISS** — vector store for semantic search
- **Gradio** — interactive chat UI

## ⚙️ Features

- Upload any RBI PDF and ask questions
- Multi-turn conversational memory
- Semantic search with FAISS
- Completely free to run

## 🔧 Setup

1. Clone the repo
```bash
   git clone https://github.com/jenil27/rbi-guidelines-chatbot.git
   cd rbi-guidelines-chatbot
```

2. Create virtual environment
```bash
   python -m venv .venv
   .venv\Scripts\activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Add your Groq API key
```bash
   cp .env.example .env
```
   Edit `.env` and add your key from [console.groq.com](https://console.groq.com)

5. Run the app
```bash
   python app.py
```

6. Open `http://127.0.0.1:7860` in your browser

## 📁 Project Structure

```
rbi-guidelines-chatbot/
├── app.py              # Gradio UI
├── rag_pipeline.py     # RAG pipeline
├── requirements.txt
├── .env.example
└── README.md
```