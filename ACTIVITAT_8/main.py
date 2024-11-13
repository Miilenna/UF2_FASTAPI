from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    category: str
    discount: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/{item_id}", status_code=204)
async def read_item(item_id: int):
    return {"item_id": item_id}