import pandas as pd
from typing import List
from fastapi import FastAPI
import connection
from schemas import word_schema

def csv_to_json():
    df = pd.read_csv("paraules_temàtica_penjat.csv")
    d = df.to_dict(orient='list')

    return d
data = csv_to_json()

for i in range(500):
    connection.insert_data_csv_to_db(i, data)
    
app = FastAPI()

@app.get("/penjat/tematica/opcions", model_response=List[dict])
async def get_word():
    word_schema()