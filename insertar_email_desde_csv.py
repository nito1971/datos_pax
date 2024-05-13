import csv
import pymongo
from pymongo import MongoClient
import re


ruta = "/mnt/10.0.0.12/desarrollo/datos_pax/BBDD_email/email.email.csv"
contador = 0

'''
with open(ruta, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == 'indice_txt_text':
            print(row[1])
'''
# Conectarse a MongoDB
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


with open(ruta, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Salta la primera fila (encabezados)
    
    for row in reader:
        #print(row[3])
        insertar_db(row[3])
        contador += 1
        print(contador)
            