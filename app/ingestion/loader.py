from langchain_community.document_loaders import PyPDFLoader


def load_pdf(data):
    loader = PyPDFLoader(data)
    documents = loader.load()
    return documents
