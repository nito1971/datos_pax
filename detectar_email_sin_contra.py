import re

ruta = '/mnt/local/datos/Documentos/PASSW/diccpass_rockyou/original/weakpass_2a'

def buscar_email(filename):    
    email_patron = r'([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})'
    with open(filename, 'r', encoding="latin1") as file:
        try:
            for linea in file:
                coincidencias = re.findall(email_patron, linea)
                for coincidencia in coincidencias:
                    print(f"Email: {coincidencia[0]}, Rest: {coincidencia[1]}")
        except Exception as e:
            print(f"Error: {e}")           
        

if __name__ == '__main__':    
    buscar_email(ruta)
