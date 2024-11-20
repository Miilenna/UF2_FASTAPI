def user_schema(user) -> dict:
    return {"Id": user[0],
            "nom": user[1],
            "cognom": user[2]
            }

def users_schema(users) -> dict:
    return [user_schema(user) for user in users]