from fastapi import FastAPI
app = FastAPI()

intents = 0

@app.get("/començar")
def començar():
    return { 
            "text":"Començar partida"
            }
    
@app.get("/començar/paraula")
def comença_paraula():
    return { 
            "text":"Començar partida"
            }

@app.post("/intents")
def intents():
    intents += 1
    return {
        intents
    }