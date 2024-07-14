import os
from retrieval import get_retriever
from vectorestore import create_new_faiss
from llm import get_llm_instance


prompt_template = """You're an  civic tech and environment specialist, you need to give answer to solve local public issues related to environment and local civic issues only. 
Try to answer within the given context. Dont give answer if the question is not related to the environment issues or local civic issues, simply say I dont know. 


User Question : ```{question}```

Context : ```{context}```

#Answer"""


def get_response(question):
    try:
        retriever = get_retriever()
        relevant_docs = retriever.invoke(question)
        final_prompt = prompt_template.format(question=question, context=relevant_docs)
        llm = get_llm_instance()
        gemini_res = llm.invoke(final_prompt)

        return gemini_res.content
    
    except Exception as e:
        print(f"Exception : {e}")
    


faiss_index_path = "faiss_index_with_google"

if os.path.exists(faiss_index_path):
    print("Using Existing FAISS!")
else:
    create_new_faiss()

while True:
    question = input("Enter Question : ")
    gemini_res = get_response(question)
    print(gemini_res+"\n-------------------------------------------------------------------------------------------------------")

