from fastapi import FastAPI
from app.models.input_model import InputModel
from app.pipeline.rag_pipeline import build_rag_chain
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# ✅ Add CORS middleware here

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],  # allow all (good for development)
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)
# Load once at startup
rag_chain = build_rag_chain()


@app.post("/fetch-data")
def fetch_data(input: InputModel):
    response = rag_chain.invoke({"input": input.query})
    return {"message": response["answer"]}
