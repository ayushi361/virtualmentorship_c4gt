import os
import time
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain.docstore.document import Document  

load_dotenv()

def create_faiss_index_in_batches(docs, batch_size, sleep_time):
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=google_api_key)
    faiss_index = None
    
    documents = [Document(page_content=doc) for doc in docs]
    
    for i in range(0, len(documents), batch_size):
        batch_docs = documents[i:i + batch_size]
        print(f"Processing batch {i // batch_size + 1} / {(len(documents) + batch_size - 1) // batch_size}")
        
        if faiss_index is None:
            faiss_index = FAISS.from_documents(batch_docs, embeddings)
        else:
            faiss_index.add_documents(batch_docs)
        
        time.sleep(sleep_time)
    
    return faiss_index

def save_faiss_index(faiss_index, path):
    faiss_index.save_local(path)
