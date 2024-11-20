from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
import db_connect
from schemas import user_schema, users_schema


@app.get("/users", response_model=List[dict])
async def read_users():
    return users_sch.users_schema(users.read())