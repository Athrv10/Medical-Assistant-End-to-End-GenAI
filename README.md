# GenAI Medical Chatbot 🩺

This project is a Retrieval-Augmented Generation (RAG) based medical chatbot. It uses a sophisticated AI pipeline to answer user questions based on a custom knowledge base of medical PDF documents. The application is built with Flask, LangChain, Cohere, and Pinecone.

## ✨ Features

*Interactive Web Interface: A simple and clean chat interface for users to ask medical-related questions.

*Custom Knowledge Base: Answers questions by retrieving information directly from PDF documents you provide.

*RAG Pipeline: Utilizes a state-of-the-art RAG architecture to ensure answers are contextually relevant and grounded in the source material.


*Powerful LLM: Powered by Cohere's command-r-plus model for generating coherent and accurate responses.

*Scalable Vector Storage: Uses Pinecone as a serverless vector database to efficiently store and search document embeddings.

## 🛠️ Tech Stack

*Backend: Flask

*LLM & Orchestration: LangChain, Cohere (langchain-cohere)

*Vector Database: Pinecone (langchain-pinecone)

*Embeddings: Hugging Face Sentence Transformers (sentence-transformers)

*Frontend: HTML, CSS, jQuery

*Data Loading: PyPDF

## 📂 Project Structure

.
├── Data/
│   └── Medical_book.pdf
├── research/
│   └── trails.ipynb
├── src/
│   ├── __init__.py
│   ├── helper.py
│   └── prompt.py
├── static/
│   └── style.css
├── templates/
│   └── chatbot.html
├── .env
├── .gitignore
├── app.py
├── LICENSE
├── README.md
├── requirement.txt
├── setup.py
├── store_index.py
└── template.py

## 💬 Usage
*Navigate to the web interface in your browser.

*Type your medical question into the message box at the bottom.

*Press "Send" or hit the Enter key.

*The bot will retrieve relevant information from your documents and generate a response.
