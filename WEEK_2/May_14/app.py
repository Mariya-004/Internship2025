import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
# Set the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#we read the pdf going through the pages and extracting the text

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text
#splitting the text into chunks 
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=1000
    )
    chunks = text_splitter.split_text(text)
    return chunks

#creating the embeddings
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = Chroma.from_texts(text_chunks, embeddings,persist_directory="chroma_store")
    vector_store.persist() #saving the vector store locally
    

def get_conversation_chain():
    prompt_template="""Answer the question as detailed as possible from the provided context, make sure to provide the source of the answer.If the answer is not in the context, say "I don't know".
    Context: {context}
    Question: {question}
    Answer: """

    model=ChatGoogleGenerativeAI(model="models/gemini-2.0-flash",temperature=0.3)
    prompt=PromptTemplate(template=prompt_template, input_variables=["context","question"])
    chain=load_qa_chain(model,chain_type="stuff",prompt=prompt) #stuff does internal text summarization
    return chain

#getting user input
def user_input_handler(user_input):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = Chroma(persist_directory="chroma_store",embedding_function= embeddings)
    docs= new_db.similarity_search(user_input)
    chain = get_conversation_chain()

    response=chain(
        {
            "input_documents": docs,
            "question": user_input
        },return_only_outputs=True)
    print(response)
    st.write("Answer: ", response["output_text"])
    
#creating the streamlit app
def main():
    st.title("PDF Question Answering")
    st.write("Upload your PDF files here:")
    pdf_docs = st.file_uploader("Upload PDF", type="pdf", accept_multiple_files=True)
    
    if st.button("Process PDFs"):
        if pdf_docs:
            text = get_pdf_text(pdf_docs)
            text_chunks = get_text_chunks(text)
            get_vector_store(text_chunks)
            st.success("PDFs processed successfully!")
        else:
            st.error("Please upload at least one PDF file.")
    
    user_input_text = st.text_input("Ask a question about the PDF content:")
    if st.button("Get Answer"):
        if user_input_text:
            user_input_handler(user_input_text)
        else:
            st.error("Please enter a question.")
if __name__ == "__main__":
    main()