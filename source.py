import streamlit as st
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="Exam_saviour", page_icon="books:")
    st.header("Make your exams EASY :books:")
    st.text_input("Ask anything related to the course:")
    
    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload  your PDFs here")
        st.button("Process")


if __name__ == '__main__':
    main()