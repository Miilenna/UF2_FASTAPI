import psycopg2

def connexio():
    # Estableix la connexió amb la base de dades PostgreSQL
    conn = psycopg2.connect(
        database = "postgres",
        user = "user_postgres",
        password = "pass_postgres",
        host = "localhost",
        port = "5432"
    )

    connection = conn.cursor() #Crea un cursor per executar les consultes
    return conn, connection # Retorna la connexió i el cursor