import csv
from pymongo import MongoClient
import hashlib
import os
import time
import random
import os
import pathlib
import threading
import re

ruta = "/mnt/10.0.0.12/desarrollo/datos_pax/"

'''
def numero_archivos():
    initial_count = 0
    for path in pathlib.Path(ruta).iterdir():
        if path.is_file():
            initial_count += 1
            print(initial_count)

    return(initial_count)

'''

    
def calcular_tiempo_ejecucion(tiempo):
    if tiempo < 60:
       print(f"Tiempo total: {tiempo:.2f} segundos")
    else:
        tiempo_minutos = tiempo / 60
        print(f"Tiempo total: {tiempo_minutos:.2f} minutos")


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
def recorrer_ruta(ruta):   
    for dir, dirs, archivos in os.walk(ruta):
        for archivo in archivos: 
            if archivo.endswith(".txt"):         
                inicio = time.time()
                archvo_a_insertar = (os.path.join(dir, archivo))
                print("*" * 40)
                print(archvo_a_insertar)
                print("*" * 40)     
                    
                with open(archvo_a_insertar, 'r', encoding="latin1") as file:
                    try:
                        for line in file:
                            if line != ""+"\n":                                 
                                _id = line 
                                _id = _id.strip("\n")                              
                                insertar_db(_id) 
                            else:
                                pass

                    except Exception as e:
                        print(f"Error: {e}")
                        pass                                
                            
                os.remove(archvo_a_insertar)
                fin = time.time()
                print("Archivo eliminado")
                print("+" *100)
                calcular_tiempo_ejecucion(fin - inicio)
                #print(f"Tiempo total: {tiempo_total:.2f} minutos")
                print("+" *100)
 
def inicio(hilo):
    print(f"Hilo {hilo} iniciado.")
    inicio = time.time()
    try:        
        indice_random = random.randint(0, len(lista_archivos))
        archivo = lista_archivos[indice_random]
        if archivo.endswith(".txt"):
            ruta_archivo = os.path.join(ruta, archivo)
            with open(ruta_archivo, "r") as f:
                for linea in f:
                    if linea != ""+"\n":
                        linea_a_hashear = linea.rstrip("\n")                    
                        _id = linea_a_hashear            
                                    
                        insertar_db(_id)
                        #print(f"Usuario: {usuario} - Passwd: {passwd}")
                    else:
                        pass
                                
                os.remove(ruta_archivo)                
                print(f"{archivo} ha sido eliminado.")
                final = time.time()
                tiempo_total = (final - inicio)
                print(f"Tiempo total de ejecución: {tiempo_total} segundos para el hilo {hilo}")
                lista_archivos.pop(indice_random)
               
    except Exception as e:
        print(e)
        return False  




###################################################################
###################################################################
lista_archivos = os.listdir(ruta)
n_archivos = len(os.listdir(ruta))
while(n_archivos > 0):
   # Creamos una lista de 5 hilos.
    #os.system("clear")

    hilos = []    
    for i in range(10):
        hilo = threading.Thread(target=inicio, args=(i,))
        hilos.append(hilo)

    # Iniciamos todos los hilos.
    for hilo in hilos:
        hilo.start()
    
        # Esperamos a que todos los hilos terminen.
    for hilo in hilos:
        hilo.join()

    
   
print("Terminado")