# models/input_model.py
from pydantic import BaseModel


class InputModel(BaseModel):
    query: str
