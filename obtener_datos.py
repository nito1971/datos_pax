import csv
from pymongo import MongoClient
pax = {}

# Conectarse a MongoDB
def insertar_db(datos):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['datos_pax']
    collection = db['datos_pax']
    try:
        collection.insert_one(datos)
        print("Ok")
    except Exception as e:
        print(e)
    

# Leer archivo CSV
with open('/mnt/local/datos/ALIMENTACION_PROYECTOS/250807711/0.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)    
    # Recopilar nombres de campos de la primera fila
    fieldnames = next(reader)[1:]  # [1:] para eliminar el título
    print(fieldnames)    
    
    for row in reader:       
        for i in range (0, len(fieldnames)):
            a = fieldnames[i] = row[i]
            pax
            print(a)
                     
            #print(pax)
            insertar_db(pax)
 
        