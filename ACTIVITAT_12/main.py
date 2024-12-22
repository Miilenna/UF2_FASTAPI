from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from connexio import connexio
from schemas import word_schema
import CRUD.read as read
import CRUD.update as update
import CRUD.create as create
import CRUD.delete as delete

app = FastAPI()

#-----------------------------ESQUEMA INFORMACIÓ------------------------------------
class Informacio(BaseModel):
    total_intents: int  # Nombre total d'intents disponibles al joc
    texts_joc: str  # Text relacionat amb el joc (p. ex., una pista o paraula clau)

#-----------------------------ESQUEMA INFORMACIÓ AMB ID------------------------------------
class InformacioAmbId(BaseModel):
    id: Optional[int]  # ID opcional per identificar l'entrada a la base de dades
    total_intents: int
    texts_joc: str

#-----------------------------ESQUEMA ABECEDARI------------------------------------
class Alfabet(BaseModel):
    lletres: str  # Lletres disponibles a l'abecedari (p. ex., "ABCDE")
    idioma: str  # Idioma associat a l'abecedari (p. ex., "Català")

#-----------------------------ESQUEMA ABECEDARI AMB ID------------------------------------
class AlfabetAmbId(BaseModel):
    id_alfabet: Optional[int]  # ID opcional per identificar l'abecedari a la base de dades
    lletres: str
    idioma: str

#----------------------------------GET-------------------------------------------
# Endpoint que retorna el text del botó "començar partida"
@app.get("/comencar", response_model=List[dict])
async def get_start():
    text = read.get_start()  # Recupera el text inicial de la base de dades
    if not text:
        raise HTTPException(status_code=404, detail="No s'han trobat")
    return word_schema(text)  # Retorna els resultats en format JSON

# Endpoint que retorna la paraula secreta per a "començar partida"
@app.get("/comencar/paraula", response_model=List[dict])
async def get_word():
    text = read.get_word()  # Recupera la paraula secreta
    if not text: 
        raise HTTPException(status_code=404, detail="No s'ha trobat la paraula")
    return word_schema(text)  # Retorna els resultats en format JSON

# Endpoint que retorna l'abecedari segons l'idioma especificat
@app.get("/abecedari", response_model=List[dict])
async def lletres(idioma: str):
    # Valida que l'idioma sigui suportat
    if idioma not in ["catala", "castellano"]:
        raise HTTPException(status_code=404, detail=f"No s'ha trobat l'abecedari de l'idioma {idioma}")
    lletres = read.get_abecedari(idioma)  # Recupera l'abecedari de la base de dades
    if not lletres: 
        raise HTTPException(status_code=404, detail="No s'ha trobat l'abecedari")
    return word_schema(lletres)  # Retorna els resultats en format JSON

#----------------------------------POST-------------------------------------------
# Endpoint que retorna el nombre d'intents i l'incrementa
@app.post("/intents", response_model=List[dict])
async def intents():
    intents = read.get_intents()  # Recupera el nombre d'intents
    if not intents: 
        raise HTTPException(status_code=404, detail="No s'han trobat els intents")
    return word_schema(intents)  # Retorna els resultats en format JSON

# Endpoint per inserir informació de la partida
@app.post("/comencar_insert")
async def insert_start(info: Informacio):
    result = create.create_informacio(info.total_intents, info.texts_joc)  # Insereix la informació
    if result.get("status") != 1:
        raise HTTPException(status_code=400, detail="No s'ha pogut fer el insert")
    return {"message": "Afegit correctament"}

# Endpoint per inserir un abecedari
@app.post("/abecedari_insert")
async def insert_alfabet(alf: Alfabet):
    result = create.create_alfabet(alf.lletres, alf.idioma)  # Insereix l'abecedari
    if result.get("status") != 1:
        raise HTTPException(status_code=400, detail="No s'ha pogut fer el insert")
    return {"message": "Afegit correctament"}

#----------------------------------PUT-------------------------------------------
# Endpoint per actualitzar el text de partida
@app.put("/comencar_update/{id}")
async def update_start(id: int, paraula: str):
    result = update.update_començar(id, paraula)  # Actualitza el text
    if not result:
        raise HTTPException(status_code=400, detail="No s'ha pogut fer l'actualització")
    return {"message": "Actualitzat correctament"}

# Endpoint per actualitzar la paraula secreta
@app.put("/comencar_update_paraula/{id}")
async def update_start_paraula(id: int, paraula: str):
    result = update.update_començar_paraula(id, paraula)  # Actualitza la paraula secreta
    if not result:
        raise HTTPException(status_code=400, detail="No s'ha pogut fer l'actualització")
    return {"message": "Actualitzat correctament"}

# Endpoint per actualitzar l'abecedari
@app.put("/abecedari_update/{id_alfabet}")
async def update_lletres(id_alfabet: int, lletres: str):
    result = update.update_abecedari(id_alfabet, lletres)  # Actualitza l'abecedari
    if not result:
        raise HTTPException(status_code=400, detail="No s'ha pogut fer l'actualització")
    return {"message": "Actualitzat correctament"}

#----------------------------------DELETE-------------------------------------------
# Endpoint per eliminar informació de la partida
@app.delete("/comencar_delete/{id}")
async def delete_paraula(id: int):
    result = delete.delete_paraula(id)  # Elimina la informació de la partida
    if result.get("status") != 1:
        raise HTTPException(status_code=400, detail="No s'ha pogut eliminar la informació")
    return {"message": "Eliminat correctament"}

# Endpoint per eliminar un abecedari
@app.delete("/abecedari_delete/{id_alfabet}")
async def delete_alfabet(id_alfabet: int):
    result = delete.delete_alfabet(id_alfabet)  # Elimina l'abecedari
    if result.get("status") != 1:
        raise HTTPException(status_code=400, detail="No s'ha pogut eliminar l'abecedari")
    return {"message": "Eliminat correctament"}
