from typing import List
from langchain.schema import Document


def filter_document(docs: List[Document]) -> List[Document]:
    filtered_docs = []
    for doc in docs:
        document = Document(
            page_content=doc.page_content,
            metadata={"source": doc.metadata.get("source", "Unknown")}
        )
        filtered_docs.append(document)
    return filtered_docs
