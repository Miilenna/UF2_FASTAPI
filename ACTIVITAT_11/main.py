from typing import List
from fastapi import FastAPI, HTTPException
import connexio
import read
from schemas import word_schema, paraula_schema
app = FastAPI()

# 1
@app.get("/començar", response_model=List[dict])
async def get_start():
    text = read.get_start()
    if not text:
        raise HTTPException(status_code=404, detail="No s'han trobat la paraula")
    return word_schema(text)
# 2
@app.get("/començar/paraula", response_model=List[dict])
def get_word():
    text = read.get_word()
    if not text: 
        raise HTTPException(status_code=404, detail="No s'han trobat la paraula")
    return word_schema(text)
    
# 3
@app.post("/intents", response_model=List[dict])
def intents():
    intents = read.get_intents()
    if not intents: 
        raise HTTPException(status_code=404, detail="No s'han trobat la paraula")
    return word_schema(intents)

@app.get("/alfabet", response_model=List[dict])
def lletres(option: str):
    lletres = read.get_abecedari(option)
    if not lletres: 
        raise HTTPException(status_code=404, detail="No s'han trobat l'abecedari")
    return word_schema(lletres)
