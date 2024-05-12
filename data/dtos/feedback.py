from pydantic import BaseModel

class Feedback(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None