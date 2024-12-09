from fastapi import FastAPI
app = FastAPI()

intents = 0

# 1
@app.get("/començar")
def començar():
    return { 
            "text":"Començar partida"
            }
# 2
@app.get("/començar/paraula")
def comença_paraula():
    return { 
            "text":"Començar partida"
            }
# 3
@app.post("/intents")
def intents():
    return {
        intents
    }