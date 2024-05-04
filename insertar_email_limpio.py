import csv
from pymongo import MongoClient
import hashlib
import os
import time
ruta = "/mnt/local/datos/ALIMENTACION_PROYECTOS/EMAIL/original/data"
    

def get_hash(input_string):
    """
    Se obtiene el SHA-384 hash de la cadena que se le pasa cmo arguemnto.
    Si se produce un error, la función devuelve None.
    :param input_string: La cadena a procesar.
    :return: El SHA-384 hash o None si se produce un error.

    """
    try:
        return hashlib.sha384(input_string.encode()).hexdigest()
    except:
        return None
# Conectarse a MongoDB
def insertar_db(_id):
    client = MongoClient('mongodb://localhost:27019/')
    db = client['email']
    collection = db['email']
    dato = {"_id": _id }
    try:
        collection.insert_one(dato)
        #print("Ok")
    except Exception as e:
        #print(e)
        pass
def recorrer_ruta(ruta):
    pax = {}
    for dir, dirs, archivos in os.walk(ruta):
        for archivo in archivos:            
            inicio = time.time()
            archvo_a_insertar = (os.path.join(dir, archivo))
            print("*" * 40)
            print(archvo_a_insertar)
            print("*" * 40)     
                
            with open(archvo_a_insertar, 'r', encoding="latin1") as file:
                try:
                    for line in file:                                 
                        _id = line 
                        _id = _id.strip("\n")                              
                        insertar_db(_id) 
                except Exception as e:
                     pass                                
                        
            os.remove(archvo_a_insertar)
            fin = time.time()
            print("Archivo eliminado")
            print("+" *200)
            tiempo_total = (fin - inicio) / 60
            print(f"Tiempo total: {tiempo_total:.2f} minutos")
            print("+" *200)
 
            
if __name__ == '__main__':
    os.system("clear")
    recorrer_ruta(ruta)