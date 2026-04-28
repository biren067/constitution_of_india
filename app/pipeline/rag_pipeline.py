
from app.ingestion.loader import load_pdf
from app.ingestion.embedder import get_embeddings_vector
from app.ingestion.upsert import fetch_vectorstore

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from app.ingestion.chunker import text_splitter
from app.llm.groq_llm import get_groq_model, prompt
from app.constants import INDEX_NAME


def build_rag_chain():

    print("📄 Loading documents...")
    docs = load_pdf("app/data/the_constitution_of_india.pdf")

    # No ingestion here!
    embeddings = get_embeddings_vector()
    text_chunks = text_splitter(docs)
    print("📤 Loading vectorstore from Pinecone...")
    vectorstore = fetch_vectorstore(INDEX_NAME, embeddings, text_chunks)

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    print("🤖 Initializing LLM...")
    chat_model = get_groq_model()

    question_answer_chain = create_stuff_documents_chain(chat_model, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain
