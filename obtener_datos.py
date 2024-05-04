import csv
from pymongo import MongoClient
import hashlib
import os
import time
ruta = "/mnt/local/datos/ALIMENTACION_PROYECTOS/250807711"
    

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
                inicio = time.time()
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
                    fin = time.time()
                    print("Archivo eliminado")
                    print("+" *100)
                    print(f"Tiempo de ejecucion: {fin - inicio}")
                    print("+" *100)
                except:
                    pass    
if __name__ == '__main__':
    os.system("clear")
    recorrer_ruta(ruta)
    
           
 ###################################################################################
'''

---------------------------------
Importaciones

- csv: biblioteca para leer y escribir archivos CSV.
- MongoClient y MongoDB: bibliotecas para conectarse a un servidor MongoDB.
- hashlib: biblioteca para generar hash de cadenas de texto.
- os: biblioteca para interactuar con el sistema operativo (Ejemplo, obtener 
  la ruta actual del archivo).
- time: biblioteca para trabajar con fechas y tiempos.

----------------------------------
Definiciones de funciones

- get_hash(input_string): función que calcula el hash SHA-384 de una cadena de texto. 
  Si hay un error durante el cálculo, devuelve None.
- insertar_db(datos): función que inserta un documento en la base de datos MongoDB. 
  Recibe un diccionario datos como parámetro y lo almacena en la colección datos_pax.
- recorrer_ruta(ruta): función principal que recorre una ruta específica, lee archivos
  CSV, los procesa y los almacena en la base de datos MongoDB.

- Main

1- Se ejecuta el script con la instrucción os.system("clear"), lo que limpia la pantalla.
2- Llama a la función recorrer_ruta(ruta) para recorrer la ruta especificada.

-------------------------------------
Estructura del código

1- La variable ruta se define como la ruta actual del archivo.
2- La función get_hash(input_string) se define para calcular el hash SHA-384 de una cadena de texto.
3- La función insertar_db(datos) se define para insertar un documento en la base de datos MongoDB.
4- La función recorrer_ruta(ruta) se define para recorrer una ruta específica, leer archivos CSV y procesarlos.
5- Se ejecutan las instrucciones principales con la instrucción os.system("clear").

--------------------------------------
Funcionalidad

El script tiene como objetivo recorrer una ruta específica, leer archivos CSV, procesarlos y
almacenarlos en una base 
de datos MongoDB. Cada archivo CSV se lee línea por línea, y cada fila se procesa generando 
un hash único para cada fila.
Luego, el diccionario resultante se almacena en la base de datos MongoDB.
        

'''
