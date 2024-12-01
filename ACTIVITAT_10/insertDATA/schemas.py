# Función que devuelve una lista de diccionarios con una clave 'option' y el valor correspondiente a 'paraula'
def word_schema(paraula) -> list:
    return [{"option":paraula}]
# Función que devuelve una lista de diccionarios a partir de una lista de temáticas
def theme_schema(tematiques) -> dict:
    return [{"option": tematica[0]} for tematica in tematiques]