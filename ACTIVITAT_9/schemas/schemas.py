# Funció per transformar un únic usuari en un diccionari
def user_schema(user) -> dict:
    return {"Id": user[0],
            "nom": user[1],
            "cognom": user[2],
            }

# Funció per transformar una llista d'usuaris en una llista de diccionaris
def users_schema(users) -> dict:
    return [user_schema(user) for user in users]