import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings,HuggingFaceInstructEmbeddings
from langchain.vectorstores import faiss


def get_pdf_text(pdf_files):
    text = ""
    for pdf in pdf_files:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter =CharacterTextSplitter(
        separator='\n',
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function =len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorStore(text_chunks):
    # embeddings= OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(model_name = "hkunlp/instructor-xl")
    vectorStore = faiss.from_text(text = text_chunks, embeddings = embeddings)
    return vectorStore


def main():
    load_dotenv()
    st.set_page_config(page_title="Exam_saviour", page_icon="books:")
    st.header("Make your exams EASY :books:")
    st.text_input("Ask anything related to the course:")
    
    with st.sidebar:
        st.subheader("Your documents")
        pfd_files = st.file_uploader("Upload  your PDFs here", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # pdf text 
                raw_data = get_pdf_text(pfd_files)
                
                # text chunks
                text_chunks = get_text_chunks(raw_data)

                # vector store
                vectorStore = get_vectorStore(text_chunks)


if __name__ == '__main__':
    main()