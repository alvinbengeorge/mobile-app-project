from pydantic import BaseModel

class Item(BaseModel):
    name: str
    image: str
    price: float
    non_veg: bool
    type: str

class Cart(BaseModel):
    item: Item
    quantity: int

