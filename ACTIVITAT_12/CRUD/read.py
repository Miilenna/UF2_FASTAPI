from connexio import connexio
import psycopg2

#1 --> función que selecciona el texto 'començar partida'
def get_start():
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT texts_joc FROM informació;")
    text = cur.fetchall()

    cur.close()
    conn.close()

    return text

#2 --> función que selecciona el texto 'començar partida'
def get_word():
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("SELECT texts_joc FROM informació;")
    text = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return text

#3 --> función que actualiza el número de intentos cada vez que se hace click en el botón (en este caso seria al hacer click en alguna letra)
def get_intents():
    conn = connexio()
    cur = conn.cursor()
    
    # aquí es donde actualiza los intentos
    cur.execute("UPDATE informació SET total_intents = total_intents + 1;")
    conn.commit() # aquí guarda los cambios
    
    # aquí lo muestra
    cur.execute("SELECT total_intents FROM informació;")
    
    
    intents = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return intents

# 4 --> función que valida si el idioma puesto es el que está registrado en la bbdd, en este caso, si es catala o castellano devuelve el abecedario correspondiente
def get_abecedari(idioma):
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
