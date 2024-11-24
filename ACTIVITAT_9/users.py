import psycopg2
from db_connect import connexio # importa la funció connexio que gestiona la connexió a la base de dades

def read_users():
    conn, connection = connexio() 
    try:  
        # Consulta per llegir tots els registres de la taula USERS
        sql_read = '''SELECT id, nom, cognom FROM USERS;'''

        connection.execute(sql_read) # Executa la consulta
        
        #Recull tots els registres de la consulta
        resultat = connection.fetchall()
        return resultat
    
    # Serveix per si hi ha cap error durant l'execució
    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    
    finally:
        # Tanca la connexió i el cursor
        connection.close()
        conn.close()