from connexio import connexio
import psycopg2

#-----------------------------COMENÇAR PARTIDA------------------------------------
def create_informacio(total_intents, texts_joc):
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        # Inserta una nova fila a la taula "informació" amb el nombre total d'intents i el text del joc
        query = "INSERT INTO informació (total_intents, texts_joc) VALUES (%s, %s);"
        values = (total_intents, texts_joc)
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Insert successful"}
    except Exception as e:
        # Retorna un error si la inserció falla
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

#-------------------------------ABECEDARI------------------------------------
def create_alfabet(lletres, idioma):
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        # Inserta una nova fila a la taula "alfabet" amb les lletres i l'idioma
        query = "INSERT INTO alfabet (lletres, idioma) VALUES (%s, %s);"
        values = (lletres, idioma)
        cur.execute(query, values)
        conn.commit()
        return {"status": 1, "message": "Insert successful"}
    except Exception as e:
        # Retorna un error si la inserció falla
        print(f"Error during insertion: {e}")  # Mostra l'error per depuració
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió
