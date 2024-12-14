# Función que devuelve una lista de diccionarios con una clave 'option' y el valor correspondiente a 'paraula'
def paraula_schema(paraula) -> list:
    return [{"text":paraula}]
# Función que devuelve una lista de diccionarios a partir de una lista de temáticas
def word_schema(words) -> dict:
    return [{"text": word[0]} for word in words]