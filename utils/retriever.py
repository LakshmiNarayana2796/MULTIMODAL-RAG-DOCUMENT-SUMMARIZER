import uuid
from langchain_openai import OpenAIEmbeddings
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.schema.document import Document
from langchain.storage import InMemoryStore
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def setup_retriever(text_elements, table_elements, image_summaries):
    vectorstore = Chroma(collection_name="summaries", embedding_function=GoogleGenerativeAIEmbeddings())
    store = InMemoryStore()
    id_key = "doc_id"
    retriever = MultiVectorRetriever(vectorstore=vectorstore, docstore=store, id_key=id_key)

    # Add documents to retriever
    def add_documents(summaries, originals):
        doc_ids = [str(uuid.uuid4()) for _ in summaries]
        docs = [Document(page_content=s, metadata={id_key: doc_ids[i]}) for i, s in enumerate(summaries)]
        retriever.vectorstore.add_documents(docs)
        retriever.docstore.mset(zip(doc_ids, originals))

    add_documents(text_elements, text_elements)
    add_documents(table_elements, table_elements)
    add_documents(image_summaries, image_summaries)
    return retriever

def query_retriever(retriever, query):
    return retriever.invoke(query)
