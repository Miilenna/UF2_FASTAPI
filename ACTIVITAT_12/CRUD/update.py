from connexio import connexio
import psycopg2

def update_començar():
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("UPDATE texts_joc FROM informació;")
    
    text = cur.fetchall()
    cur.close()
    conn.close()

    return text

def update_començar_paraula():
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("UPDATE texts_joc FROM informació;")
    
    text = cur.fetchall()
    cur.close()
    conn.close()

    return text

def update_abecedari(idioma):
    conn = connexio()
    cur = conn.cursor()
    
    # valida si el idioma es catalán y su id se corresponde
    if idioma == "catala":
        cur.execute("SELECT lletres FROM alfabet WHERE idioma = 'catala' and id_alfabet=2;")
    else:
        # valida si el idioma es catalán y su id se corresponde
        cur.execute("SELECT lletres FROM alfabet WHERE idioma = 'castellano' and id_alfabet=1;") 
    
    abecedari = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return abecedari    