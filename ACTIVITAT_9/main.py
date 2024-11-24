from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from users import read_users
from schemas import users_schema

app = FastAPI()

@app.get("/users", response_model=List[dict])
async def get_users():
    users = read_users()
    return users_schema(users)