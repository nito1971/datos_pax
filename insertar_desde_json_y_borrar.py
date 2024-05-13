import os
import json
import shutil
import pymongo
from pymongo import MongoClient
import re

# Ruta de la carpeta donde buscar archivos JSON
root_dir = '/mnt/10.0.0.12/desarrollo/datos_pax/BBDD_email'
contador = 0

def insertar_db(_id):
    client = MongoClient('mongodb://10.0.0.12:27017/')
    #client = MongoClient('mongodb://localhost:27019/')
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

# Recorrer la carpeta y sus subcarpetas
for root, dirs, files in os.walk(root_dir):
    for file in files:
        # Verificar si el archivo es un archivo JSON
        if file.endswith('.json'):
            # Leer el archivo JSON
            with open(os.path.join(root, file), 'r') as f:
                data = json.load(f)
                # Recorrer el diccionario JSON
                for elemento in data:
                    for key, value in elemento.items():
                        if key == "indice_txt":
                            #print(value)
                            insertar_db(value)
                            contador += 1
                            print(f"Contador: {contador}")
                            

        # Eliminar el archivo JSON
        os.remove(os.path.join(root, file))