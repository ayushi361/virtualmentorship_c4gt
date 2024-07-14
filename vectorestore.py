import os
import time
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain.docstore.document import Document
from pdf_pro import get_pdf_text
from chunks import load_config, split_with_character_text_splitter

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def create_faiss_index_in_batches(docs, batch_size, sleep_time):
    faiss_index = None
    
    for i in range(0, len(docs), batch_size):
        batch_docs = docs[i:i + batch_size]
        print(f"Processing batch {i // batch_size + 1} / {(len(docs) + batch_size - 1) // batch_size}")
        
        if faiss_index is None:
            faiss_index = FAISS.from_texts(batch_docs, embeddings)
        else:
            faiss_index.add_texts(batch_docs)
        
        time.sleep(sleep_time)
    
    return faiss_index

def create_new_faiss():
    print("Creating new FAISS index...")
    text = get_pdf_text()
    
    try:
        config = load_config()
    except Exception as e:
        print("Exception : ",e)

    chunks = split_with_character_text_splitter(text, config['chunk_size'], config['chunk_overlap'])
    faiss_index = create_faiss_index_in_batches(chunks, batch_size=config['batch_size'], sleep_time=config['sleep_time'])

    try:
        faiss_index.save_local("faiss_index_with_google")
        print("FAISS created successfully!")
    except:
        print("Error! occured while creating FAISS")

    return


