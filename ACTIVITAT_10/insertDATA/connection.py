import random
import psycopg2

def connect_db():
    return psycopg2.connect(
        database = "postgres",
        user = "user_postgres",
        password = "pass_postgres",
        host = "localhost",
        port = "5432"
    )

def insert_data_csv_to_db(pos, data):

    # Estableix la connexió amb la base de dades PostgreSQL
    conn = connect_db()
    cur = conn.cursor() #Crea un cursor per executar les consultes
    
    sql = "INSERT INTO paraules (word, theme) VALUES (%s, %s);"
    values = ((data.get("WORD")[pos], data.get("THEME")[pos]))
    
    cur.execute(sql, values)
    conn.commit()
    cur.close()
    conn.close()
    
    return {"Message":"Data inserted"}

def get_theme():
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("SELECT DISTINCT theme FROM paraules;")
    themes = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return themes

def get_random_paraula(tematica: str):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("SELECT word FROM paraules WHERE theme = %s;",(tematica,))
    words = cur.fetchall()
    
    cur.close()
    conn.close()
    
    if words:
        return random.choice(words)[0]
    return None