import pandas as pd
from typing import List
from fastapi import FastAPI, HTTPException
import connection
from schemas import theme_schema, word_schema

def csv_to_json():
    df = pd.read_csv("paraules_temàtica_penjat.csv")
    d = df.to_dict(orient='list')

    return d
data = csv_to_json()

for i in range(500):
    connection.insert_data_csv_to_db(i, data)
    
app = FastAPI()

@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def get_theme():
    themes = connection.get_theme()
    if not themes:
        raise HTTPException(status_code=404, detail="No s'han trobat la temàtiques")
    return theme_schema(themes)

@app.get("/penjat/tematica/{option}", response_model=List[dict])
async def get_random_paraula(option: str):
    word = connection.get_random_paraula(option)
    if not word:
        raise HTTPException(status_code=404, detail=f"No s'ha trobat cap paraula per la temàtica: {option}")
    return word_schema(word)
