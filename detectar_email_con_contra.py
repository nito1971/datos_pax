import re

ruta = '/mnt/local/datos/Documentos/PASSW/diccpass_rockyou/original/weakpass_2a'

def buscar_email(filename):
    '''
    Esta expresión regular busca:

    1. Una cadena que contiene al menos un carácter alfabeto o número (`[A-Za-z0-9.]`) seguida de `@`, un punto y guion 
    (`-`), otro punto (`\.`) y finalmente dos letras (`[A-Za-z]{2,}`). Esto es la dirección de correo electrónico.
    2. El carácter `:`.
    3. Cualquier texto que se encuentre después del carácter `:` (capturado con el grupo `(.*?)`).
    '''
    email_patron = r'([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}):(.*)'
    with open(filename, 'r') as file:
        for linea in file:
            coincidencias = re.findall(email_patron, linea)
            for coincidencia in coincidencias:
                print(f"Email: {coincidencia[0]}, Rest: {coincidencia[1]}")
        
        

if __name__ == '__main__':    
    buscar_email(ruta)

