from pydantic import BaseModel

class Tickets(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None