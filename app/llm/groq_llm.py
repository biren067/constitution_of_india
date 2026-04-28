from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY


def get_groq_model():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile"
    )


chatModel = get_groq_model()


system_prompt = (
    "You are an Constitutional assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
