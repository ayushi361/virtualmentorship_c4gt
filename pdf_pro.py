import os
from PyPDF2 import PdfReader
import docx

def get_pdf_text():
    text = ""
    folder_path = "pdfs"
    docx_files = [f for f in os.listdir(folder_path) if f.endswith('.docx')]
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    for docx_file in docx_files:
        docx_path = os.path.join(folder_path, docx_file)
        try:
            doc = docx.Document(docx_path)
            for paragraph in doc.paragraphs:
                if paragraph.style.name == 'List Bullet':
                    text += '• ' + paragraph.text + '\n'  
                else:
                    text += paragraph.text + '\n'
        except Exception as e:
            error_message = f"Error reading DOCX file '{docx_file}': {e}"
            print(error_message)

    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        try:
            pdf_reader = PdfReader(open(pdf_path, "rb"))
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                text += page_text
        except Exception as e:
            error_message = f"Error reading PDF file '{pdf_file}': {e}"
            print(error_message)
    
    return text
