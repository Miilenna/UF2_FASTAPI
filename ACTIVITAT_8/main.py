# Importaciones necesarias
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Instancia para la aplicación de FastAPI
app = FastAPI()

# Definimos un modelo de datos con Pydantic para la estructura de un Item
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    category: str
    discount: float | None = None

# Diccionario que almacena items de ejemplo
items = {
    1: {"name": "Item One", "price": 10.0},
    2: {"name": "Item Two", "price": 20.0},
}

# Enpoint principal
@app.get("/")
async def main():
    return "Main"

# Endpoint para "crear" un item nuevo
@app.post("/items/")
async def create_item(item: Item):
    return item

# Endpoint para leer la información de un item por su Id
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        # Si el id no se encuentra se lanza un error 400
        raise HTTPException(status_code=400, detail="Error de cliente")
    return {"item": items[item_id]} # Devuelve el item si existe