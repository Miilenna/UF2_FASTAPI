from typing import List
from fastapi import FastAPI, HTTPException
from connexio import connexio
import CRUD.read as read
import CRUD.update as update
from schemas import word_schema, paraula_schema
app = FastAPI()

# 1 --> endpoint que devuelve el 'començar partida' del botón
@app.get("/començar", response_model=List[dict])
async def get_start():
    text = read.get_start()
    if not text:
        raise HTTPException(status_code=404, detail="No s'han trobat")
    return word_schema(text)

# 2 --> endpoint que devuelve el 'començar partida' donde iria la palabra secreta
@app.get("/començar/paraula", response_model=List[dict])
def get_word():
    text = read.get_word()
    if not text: 
        raise HTTPException(status_code=404, detail="No s'han trobat la paraula")
    return word_schema(text)
    
# 3 --> endpoint que devuelve el número de intentos y aumenta el número por cada intento
@app.post("/intents", response_model=List[dict])
def intents():
    intents = read.get_intents()
    if not intents: 
        raise HTTPException(status_code=404, detail="No s'han trobat la paraula")
    return word_schema(intents)

# 4 --> endpoint que devuelve un abecedario dependiendo del idioma que le pases, si no está registrado en la bbdd te devuelve una exception
@app.get("/abecedari", response_model=List[dict])
def lletres(option: str):
    lletres = read.get_abecedari(option)
    if option not in ["catala", "castellano"]:
        raise HTTPException(status_code=404, detail=f"No s'han trobat l'abecedari de l'idioma {option}")
    if not lletres: 
        raise HTTPException(status_code=404, detail="No s'han trobat l'abecedari")
    return word_schema(lletres)

#----------------------------------PUT-------------------------------------------
@app.put("/començar_update", response_model=List[dict])
async def update_start(option: str):
    text = update.update_començar(option)
    if not text:
        raise HTTPException(status_code=404, detail="No s'ha pogut fer el update")
    return word_schema(text)

@app.put("/començar_update_paraula", response_model=List[dict])
async def update_start_paraula():
    text = update.update_començar_paraula()
    if not text:
        raise HTTPException(status_code=404, detail="No s'ha pogut fer el update")
    return word_schema(text)

@app.put("/abecedari_update", response_model=List[dict])
def lletres_update(option: str):
    lletres = update.update_abecedari(option)
    if not lletres: 
        raise HTTPException(status_code=404, detail="No s'han trobat l'abecedari per fer update")
    return word_schema(lletres)