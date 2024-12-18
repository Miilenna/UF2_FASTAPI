from connexio import connexio
import psycopg2

#-----------------------------COMENÇAR PARTIDA------------------------------------
def update_començar(paraula):
    conn = connexio()
    cur = conn.cursor()
    try:
        cur.execute("UPDATE informació SET texts_joc = %s;", (paraula,))
        conn.commit()
        return {
            "message":"Actualizado correctamente"
        }
        
    except Exception as e:
        print(f"Error in update_començar: {e}")
        return None
    finally:
        cur.close()
        conn.close()
#-----------------------------PARAULA SECRETA------------------------------------
def update_començar_paraula(paraula):
    conn = connexio()
    cur = conn.cursor()
    try:
        cur.execute("UPDATE informació SET texts_joc = %s;", (paraula,))
        conn.commit()
        return {
            "message":"Actualizado correctamente"
        }
        
    except Exception as e:
        print(f"Error in update_començar: {e}")
        return None
    finally:
        cur.close()
        conn.close()
#-----------------------------ABECEDARI------------------------------------
def update_abecedari(lletres):
    conn = connexio()
    cur = conn.cursor()
    
    try:
        cur.execute("UPDATE alfabet SET lletres = %s;", (lletres,))    
        conn.commit()
        return {
            "message":"Actualizado correctamente"
        }
    except Exception as e:
        print(f"Error in update_començar: {e}")
        return None
    finally:
        cur.close()
        conn.close() 