from pinecone import ServerlessSpec
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from app.config import PINECONE_API_KEY

pinecone_api_key = PINECONE_API_KEY
pinecone = Pinecone(api_key=pinecone_api_key)


index_name = "constitution-bot"
serverless_spec = ServerlessSpec(cloud="aws", region="us-east-1")
if not pinecone.has_index(index_name):
    pinecone.create_index(index_name,
                          dimension=384,
                          metric="cosine",
                          spec=serverless_spec)
index = pinecone.Index(index_name)


def create_vectorstore(index_name, model, text_chunks):
    vectorstore = PineconeVectorStore.from_documents(
        documents=text_chunks,
        embedding=model,
        index_name=index_name
    )
    return vectorstore

# vectorstore = create_vectorstore(index_name, embeddings_model, text_chunks)


# Load Existing index

# Embed each chunk and upsert the embeddings into your Pinecone index.
def fetch_vectorstore(index_name, embedding):
    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embedding
    )
    return docsearch
