from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


def get_retriever():
    faiss_db = FAISS.load_local("faiss_index_with_google", embeddings, allow_dangerous_deserialization= True)

    retriever=faiss_db.as_retriever(search_kwargs={"k": 4})

    return retriever
