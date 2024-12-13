import streamlit as st
from utils.data_processing import extract_pdf_elements, encode_images
from utils.summarizer import summarize_text, summarize_table, summarize_image
from utils.retriever import setup_retriever, query_retriever
from utils.config import INPUT_PATH, OUTPUT_PATH

st.set_page_config(page_title="PDF Analysis", layout="wide")

# Upload PDF
st.title("PDF Analysis Tool")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with open(f"{INPUT_PATH}/uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    # Extract elements
    st.info("Extracting elements from the PDF...")
    text_elements, table_elements, image_elements = extract_pdf_elements("uploaded.pdf")
    
    st.success("Extraction complete!")
    st.write(f"Number of Text Elements: {len(text_elements)}")
    st.write(f"Number of Table Elements: {len(table_elements)}")
    st.write(f"Number of Image Elements: {len(image_elements)}")
    
    # Summarize and display results
    if st.button("Summarize Text"):
        st.write("**Text Summaries:**")
        for i, text in enumerate(text_elements[:2]):
            st.write(f"Text {i+1}: {summarize_text(text)}")

    if st.button("Summarize Tables"):
        st.write("**Table Summaries:**")
        for i, table in enumerate(table_elements[:1]):
            st.write(f"Table {i+1}: {summarize_table(table)}")

    if st.button("Summarize Images"):
        st.write("**Image Summaries:**")
        for i, image in enumerate(image_elements[:2]):
            st.write(f"Image {i+1}: {summarize_image(image)}")
    
    # Retriever functionality
    retriever = setup_retriever(text_elements, table_elements, image_elements)
    query = st.text_input("Ask a question about the PDF content:")
    if query:
        response = query_retriever(retriever, query)
        st.write("**Response:**", response)
