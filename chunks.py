import json
from langchain_text_splitters import CharacterTextSplitter
from langchain.docstore.document import Document

# Load the config values from the JSON files
def load_config(config_path='config.json'):
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print(f"Config file '{config_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{config_path}': {e}")
        return None

# Creating chunks 
def split_with_character_text_splitter(text, chunk_size, chunk_overlap):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # Save all chunks to a single files
    with open('chunks.txt', 'w', encoding='utf-8') as chunks_file:
        for chunk in chunks:
            chunks_file.write(chunk + '\n\n')  # Add newline between chunks
    
    return chunks
