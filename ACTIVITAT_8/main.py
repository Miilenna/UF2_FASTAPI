from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    category: str
    discount: float | None = None
    
items = {
    1: {"name": "Item One", "price": 10.0},
    2: {"name": "Item Two", "price": 20.0},
}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/")
async def main():
    return "Main"


@app.get("/items/{item_id}", status_code=400)
async def read_item(item_id: int):
    return {"item": item_id}

    # if item_id not in items:
    #     raise HTTPException(status_code=400, detail="Error de cliente")