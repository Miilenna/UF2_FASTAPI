import psycopg2

def insert_data_csv_to_db(pos, data):

    # Estableix la connexió amb la base de dades PostgreSQL
    conn = psycopg2.connect(
        database = "postgres",
        user = "user_postgres",
        password = "pass_postgres",
        host = "localhost",
        port = "5432"
    )

    cur = conn.cursor() #Crea un cursor per executar les consultes
    
    sql = "INSERT INTO paraules (word, theme) VALUES (%s, %s);"
    
    values = ((data.get("WORD")[pos], data.get("THEME")[pos]))
    
    cur.execute(sql, values)
    conn.commit()
    
    cur.close()
    conn.close()
    
    return {"Message":"Data inserted"}