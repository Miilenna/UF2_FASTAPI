from connexio import connexio
import psycopg2

#1
def get_start():
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT texts_joc FROM informació;")
    text = cur.fetchall()

    cur.close()
    conn.close()

    return text

#2
def get_word():
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("SELECT texts_joc FROM informació;")
    text = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return text

#3
def get_intents():
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("UPDATE informació SET total_intents = total_intents + 1;")
    conn.commit()
    
    cur.execute("SELECT total_intents FROM informació;")
    
    
    intents = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return intents

def get_abecedari(idioma):
    conn = connexio()
    cur = conn.cursor()
    
    if idioma == "catala":
        cur.execute("SELECT lletres FROM alfabet WHERE idioma = 'catala' and id_alfabet=2;")
    else:
        cur.execute("SELECT lletres FROM alfabet WHERE idioma = 'castellano' and id_alfabet=1;")
        
    abecedari = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return abecedari    

def update_abecedari(idioma, noves_lletres):
    conn = connexio()
    cur = conn.cursor()
    
    if idioma == "catala":
        cur.execute(
            "UPDATE alfabet SET lletres = %s WHERE idioma = 'catala' AND id_alfabet = 2;",
            (noves_lletres,)
        )
    elif idioma == "castellano":
        cur.execute(
            "UPDATE alfabet SET lletres = %s WHERE idioma = 'castellano' AND id_alfabet = 1;",
            (noves_lletres,)
        )
    
    conn.commit()
    cur.close()
    conn.close()