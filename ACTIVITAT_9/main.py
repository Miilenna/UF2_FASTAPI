# Importa las clases necesarias desde FastAPI y otros módulos
from typing import List
from fastapi import FastAPI
from crud.users import read_users
from schemas.schemas import users_schema

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Define una ruta GET para obtener todos los usuarios
@app.get("/users/", response_model=List[dict])
async def get_users():
    # Llama a la función read_users para obtener la lista de usuarios
    users = read_users()
    
    # Devuelve los usuarios serializados con la función 'users_schema'
    return users_schema(users)