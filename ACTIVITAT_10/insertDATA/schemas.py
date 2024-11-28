# Funció per transformar un únic usuari en un diccionari
def word_schema(paraula) -> list:
    return [{"option":paraula}]

# Funció per transformar una llista d'usuaris en una llista de diccionaris
def theme_schema(tematiques) -> dict:
    return [{"option": tematica[0]} for tematica in tematiques]