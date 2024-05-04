import csv
from pymongo import MongoClient
import hashlib
import os
ruta = "/mnt/local/datos/ALIMENTACION_PROYECTOS/250807711"
    

def get_hash(input_string):
    """
    Compute the SHA-384 hash of the input string.
    If there is an error during the computation, return None.
    :param input_string: The string to be hashed
    :return: The computed hash (as a hexadecimal string) or None if an error occurs
    """
    try:
        return hashlib.sha384(input_string.encode()).hexdigest()
    except:
        return None
# Conectarse a MongoDB
def insertar_db(datos):
    client = MongoClient('mongodb://localhost:27019/')
    db = client['datos_pax']
    collection = db['datos_pax']
    try:
        collection.insert_one(datos)
        #print("Ok")
    except Exception as e:
        #print(e)
        pass
def recorrer_ruta(ruta):
    pax = {}
    for dir, dirs, archivos in os.walk(ruta):
        for archivo in archivos:
            #if archivo.endswith(".csv"):
                archvo_a_insertar = (os.path.join(dir, archivo))
                print("*" * 40)
                print(archvo_a_insertar)
                print("*" * 40)
                # Leer archivo CSV
                try:
                    with open(archvo_a_insertar, 'r') as csvfile:
                        reader = csv.reader(csvfile)    
                        # Recopilar nombres de campos de la primera fila
                        fieldnames = next(reader)[1:]  # [1:] para eliminar el título
                        #print(fieldnames)                   
                        for row in reader:
                            _id = get_hash(str(row))
                            pax.update({"_id":_id})       
                            for i in range (0, len(fieldnames)):
                                #a = fieldnames[i] = row[i]
                                pax.update({fieldnames[i]:row[i]})  
                            #print(pax) 
                            #print ("*" * 22)
                            _id = get_hash(str(pax))
                            insertar_db(pax)  
                            pax = {}
                    os.remove(archvo_a_insertar)
                    print("Archivo eliminado")
                except:
                    pass    
if __name__ == '__main__':
    os.system("clear")
    recorrer_ruta(ruta)
    
           
 
        