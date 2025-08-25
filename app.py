from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from src.prompt import * 
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
import os


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["COHERE_API_KEY"] = "EtUixP0iz2eaxbCFiHhXJXHH69fWbOJao2poH7hk"

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
cohere_api_key = os.environ["COHERE_API_KEY"]
os.environ["CO_API_KEY"] = cohere_api_key

embeddings = download_hugging_face_embeddings()

index_name = "medicalchatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name = index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k" :5})

llm = ChatCohere(model="command-r-plus", temperature=0.4, cohere_api_key=cohere_api_key)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)


# Create the full RAG chain by combining the retriever and the QA chain.
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template("chatbot.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    responce = rag_chain.invoke({"input" : msg})
    print("Responce : ", responce["answer"])
    return str(responce["answer"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)