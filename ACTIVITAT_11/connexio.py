# Imports
import random
import psycopg2

# Función para establecer una conexión con la base de datos PostgreSQL
def connexio():
    return psycopg2.connect(
        database = "postgres",
        user = "user_postgres",
        password = "pass_postgres",
        host = "localhost",
        port = "5432"
    )