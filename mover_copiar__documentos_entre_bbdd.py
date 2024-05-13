import pymongo
''' Este script mueve documentos de una base de datos mongo a otra.'''

# Conexiones a las bases de datos y colecciones en servidor 1 (192.168.1.10)
client_a = pymongo.MongoClient('mongodb://10.0.0.12:27017/email')
db_a = client_a['email']
collection_a = db_a['email']

# Conexiones a las bases de datos y colecciones en servidor 2 (192.168.1.11)
client_b = pymongo.MongoClient('mongodb://10.0.0.100:27017/email')
db_b = client_b['email']
collection_b = db_b['email']


# Lee documentos desde la base de datos A
cursor = collection_a.find()
while True:
    try:
        for doc in cursor:
                print(f"Documento leido: {doc['_id']}")

                # Inserta el documento en la base de datos B
                collection_b.insert_one(doc)
                print(f"Documento insertado: {doc['_id']}")

                # Borra el documento de la base de datos A
                #collection_a.delete_one({'_id': doc['_id']})
                #print(f"Documento borrado: {doc['_id']}")
    except Exception as e:
            print(f"error")
            #collection_a.delete_one({'_id': doc['_id']})
            #print(f"Documento borrado: {doc['_id']}")
            pass

    

print("Finalizado!")

