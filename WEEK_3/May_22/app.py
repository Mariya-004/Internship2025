import asyncio
import os
import streamlit as st
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
import chromadb
from chromadb.config import Settings
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()

# === Initialize ChromaDB client ===
client = chromadb.PersistentClient(
    path=".chroma_db",
)
collection = client.get_or_create_collection(name="FAQ")

#get pdf text
async def get_pdf_text(pdf_text):
    text=" "
    for pdf in pdf_text:
        reader = PdfReader(pdf) # Open the PDF file
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

async def chunk_text(text):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=10000, # Adjust chunk size as needed
        chunk_overlap=100, #chunk overlap means how many tokens to overlap between chunks    
    )
    chunks=text_splitter.split_text(text) # Split the text into chunks
    return chunks

async def add_chunks_to_chromadb(chunks):
    for chunk in chunks:
        collection.add(
            documents=[chunk],
            metadatas=[{"source": "pdf"}], # Add metadata if needed
            ids=[str(hash(chunk))] # Use a unique ID for each chunk
        )
async def retreive_data_from_chromadb(inputs: str)-> str:
    user_query = inputs # This line caused the KeyError if 'user_query' wasn't passed
    results = collection.query(
        query_texts=[user_query],
        n_results=5
    ) 
    return results

    
async def main():
    model_client = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key=os.getenv("API_KEY")
    )

    query_handler = AssistantAgent(
        name="QueryHandler",
        model_client=model_client,
        system_message="""You are a helpful assistant that answers questions from the users. If not sure, say "I don't know" and delegate to RAGRetriever."""
    )

  

    RAGRetriever = AssistantAgent(
        name="RAGRetriever",
        model_client=model_client,
        system_message="Use the retreive_data_from_chromadb tool to get the context.Use the user query to get the context.",
        tools=[retreive_data_from_chromadb],
    )

    user = UserProxyAgent(
        name="User",
        description="User submitting and asking FAQ questions."
    )

    termination = TextMentionTermination("Stop")
    group_chat = RoundRobinGroupChat(
        [user, query_handler, RAGRetriever],
        termination_condition=termination
    )

    # Process PDF
    pdf_text = await get_pdf_text(['bob.pdf.pdf'])  # Make sure file exists
    chunks = await chunk_text(pdf_text)
    await add_chunks_to_chromadb(chunks)

    await Console(group_chat.run_stream(task="Ask a question about the FAQ or add a new FAQ."))

if __name__ == "__main__":
    asyncio.run(main())