from pdf_pro import get_pdf_text
from chunks import load_config, split_with_character_text_splitter
from vectorestore import create_faiss_index_in_batches, save_faiss_index


def main():
    text = get_pdf_text()
    
    config = load_config()
    if config is None:
        print("Failed to load configuration.")
        return
    
    chunk_size = config['chunk_size']
    chunk_overlap = config['chunk_overlap']
    
    chunks = split_with_character_text_splitter(text, chunk_size, chunk_overlap)
    
    batch_size = config.get('batch_size', 50) 
    sleep_time = config.get('sleep_time', 5)  
    faiss_index = create_faiss_index_in_batches(chunks, batch_size, sleep_time)
    
    save_faiss_index(faiss_index, "faiss_index_with_google")
    
    print("FAISS index created and saved successfully.")

if __name__ == "__main__":
    main()
