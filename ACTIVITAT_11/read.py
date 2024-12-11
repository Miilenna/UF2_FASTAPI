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
        cur.execute("SELECT lletres FROM alfabet WHERE idioma = 'catalan' and id_alfabet=2;")
    else:
        cur.execute("SELECT lletres FROM alfabet WHERE idioma = 'castellano' and id_alfabet=1;")
        
    abecedari = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return abecedari    
    