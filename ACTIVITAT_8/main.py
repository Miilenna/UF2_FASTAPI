from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    category: str
    discount: Optional[float] = None
    
items = {"milena": "Milena vardumyan"}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/{item_id}", status_code=204)
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=204, detail="No content")
    return {"item_id": item_id}