# Funció per transformar un únic usuari en un diccionari
def word_schema(paraula) -> dict:
    return {"word": paraula[0],
            "theme": paraula[1],
            }

# Funció per transformar una llista d'usuaris en una llista de diccionaris
def word_schema(paraules) -> dict:
    return [word_schema(paraula) for paraula in paraules]