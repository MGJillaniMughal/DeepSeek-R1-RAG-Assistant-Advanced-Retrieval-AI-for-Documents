import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import time
import json

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "latest_response" not in st.session_state:
    st.session_state.latest_response = None

def get_pdf_text(pdf_docs):
    """Extract text from uploaded PDFs."""
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        except Exception as e:
            st.error(f"Error processing {pdf.name}: {str(e)}")
    return text

def get_text_chunks(text):
    """Split extracted text into chunks for better processing."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=128,
        separators=["\n\n", "\n", " ", ""],
    )
    return text_splitter.split_text(text)

def get_vector_store(text_chunks):
    """Generate a FAISS vector store from text chunks."""
    try:
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
        return vector_store
    except Exception as e:
        st.error(f"Vector store creation error: {str(e)}")
        return None

def get_conversational_chain(vector_store):
    """Set up the conversational retrieval chain with enhanced prompting."""
    prompt_template = """
    You are an advanced AI assistant developed by Jillani SoftTech.
    Your goal is to provide clear, factual, and concise answers.
    Follow a structured step-by-step reasoning process to enhance accuracy.
    
    **Guidelines:**
    - **Do not hallucinate information.** If the answer is not in the context, respond with: "I'm sorry, but the answer is not available in the provided documents."
    - **Extract relevant details** from the context and summarize concisely.
    - **Ensure logical consistency** by verifying information before answering.
    
    **Context:**
    {context}

    **Chat History:**
    {chat_history}

    **User Question:**
    {question}

    **Thought Process:**
    1. Understand the key intent of the question.
    2. Retrieve the most relevant information from the context.
    3. Validate the retrieved details against prior responses.
    4. Construct a well-reasoned, structured, and concise response.

    **Final Answer:**
    """
    
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key='answer'
    )
    
    model = ChatGroq(
        temperature=0.2,
        model_name="deepseek-r1-distill-llama-70b",
        groq_api_key=GROQ_API_KEY
    )
    
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "chat_history", "question"]
    )
    
    chain = ConversationalRetrievalChain.from_llm(
        llm=model,
        retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt},
        return_source_documents=True,
        verbose=True
    )
    
    return chain

def display_chat_history():
    """Display chat history with improved formatting."""
    for message in st.session_state.messages:
        role, content = message["role"], message["content"]
        if role == "user":
            st.markdown(
                f"<div style='text-align: right; padding: 8px; border-radius: 10px;'><b>You:</b> {content}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div style='text-align: left; padding: 8px; border-radius: 10px;'><b>AI:</b> {content}</div>",
                unsafe_allow_html=True
            )

def process_user_input(user_question, chain):
    """Process user input and update chat history immediately."""
    if user_question:
        st.session_state.messages.append({"role": "user", "content": user_question})
        
        with st.spinner("Thinking..."):
            response = chain.invoke({"question": user_question})
            st.session_state.latest_response = response['answer']
            
        st.session_state.messages.append({"role": "assistant", "content": st.session_state.latest_response})
        st.session_state.chat_history.append((user_question, st.session_state.latest_response))
        st.rerun()

def main():
    """Main Streamlit application with enhanced UI and improved retrieval."""
    st.set_page_config(page_title="DeepSeek RAG Assistant – Advanced Retrieval AI for Documents", page_icon="📚", layout="wide")
    
    st.title("📚 DeepSeek R1 RAG Assistant – Advanced Retrieval AI for Documents")
    st.markdown("---")
    
    with st.sidebar:
        st.header("Upload & Process PDFs")
        pdf_docs = st.file_uploader("Upload your PDFs", accept_multiple_files=True, type=["pdf"])
        
        if st.button("Process Documents", key="process_docs"):
            with st.spinner("Processing..."):
                st.session_state.messages.clear()
                st.session_state.chat_history.clear()
                
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                
                if vector_store:
                    st.session_state.chain = get_conversational_chain(vector_store)
                    st.success("✅ Documents processed! Start chatting.")
                    time.sleep(1)
                    st.rerun()
        
        st.markdown("---")
        if st.button("Clear Chat History"):
            st.session_state.messages.clear()
            st.session_state.chat_history.clear()
            st.rerun()
    
    if "chain" in st.session_state:
        display_chat_history()
        user_question = st.chat_input("Ask about your PDFs...")
        if user_question:
            process_user_input(user_question, st.session_state.chain)
    else:
        st.info("👈 Upload and process PDFs to start chatting!")
    
    st.markdown("---")
    st.markdown("<div style='text-align: center;'><b>Powered by Jillani SoftTech 😎</b></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
