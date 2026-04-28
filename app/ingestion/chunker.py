from typing import List
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def text_splitter(documents: List[Document]) -> List[Document]:
    """ Given a list of documents objects, return a list of documents with only the page content and source metadata. """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=20)
    text_chunk = text_splitter.split_documents(documents)
    return text_chunk
