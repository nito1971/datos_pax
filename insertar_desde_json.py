import json
import pymongo
from pymongo import MongoClient
import re

ruta = "/mnt/local/datos/Documentos/PASSW/BBDD_email/email.email.json"
valores_coincidentes = [] 
contador = 0

def insertar_db(_id):
    #client = MongoClient('mongodb://10.0.0.12:27017/')
    client = MongoClient('mongodb://localhost:27019/')
    db = client['email']
    collection = db['email']
    dato = {"_id": _id }
    try:
        collection.insert_one(dato)
        #print("Ok")
    except Exception as e:
        razon = str(e)
        if re.search("E11000 duplicate key", razon):
            print("Clave duplicada")
        else:
            print(e)
        pass


# Leer el archivo JSON
with open(ruta) as f:
    datos_json = json.load(f)

# Recorrer el diccionario JSON
for elemento in datos_json:
       for key, value in elemento.items():
           if key == "indice_txt":
               #print(value)
               insertar_db(value)
               contador += 1
               print(f"Contador: {contador}")   
        