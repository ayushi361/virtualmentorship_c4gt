from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyB1UlbIjPDN9Gv-IQWdzywdEKzhgA6lf4g"

def get_llm_instance(model="gemini-1.5-flash", temperature=0.3, top_p=0.3):
    llm = ChatGoogleGenerativeAI(model=model,temperature=temperature, top_p=top_p)

    return llm