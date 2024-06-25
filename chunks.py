from langchain_text_splitters import CharacterTextSplitter
from langchain.docstore.document import Document

#creating chunks 
def split_with_character_text_splitter(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(text)