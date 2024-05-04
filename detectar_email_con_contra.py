import re

ruta = '/mnt/local/datos/Documentos/PASSW/diccpass_rockyou/original/weakpass_2a'

def buscar_email(filename):    
    email_patron = r'([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}):(.*)'
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

'''

Este código en Python utiliza la biblioteca re (regular expressions, expresiones regulares) 
para buscar direcciones de correo electrónico (email) dentro de un archivo de texto y imprimir
los resultados.

Aquí hay una explicación detallada del código:
-----------------------------
Importación de bibliotecas

El código importa la biblioteca re, que es responsable de las expresiones regulares en Python. 
Las expresiones regulares son una forma de describir patrones en cadenas de texto y se utilizan 
comúnmente para buscar o reemplazar texto dentro de archivos.

------------------------------
Definición de la función buscar_email

La función buscar_email toma un parámetro filename, que es el nombre del archivo que contiene
las direcciones de correo electrónico a buscar. La función utiliza una expresión 
regular para buscar direcciones de correo electrónico en cada línea del archivo y luego imprime 
los resultados.

-------------------------------
Expresión regular

La expresión regular utilizada por la función es:

([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}):(.*)

Esto puede parecer complicado, pero en realidad es una descripción de un patrón que coincide con 
direcciones de correo electrónico. Aquí hay un análisis detallado del patrón:

- [A-Za-z0-9._%+-]+ : Coincide con uno o más caracteres alfabéticos (letras), números, puntos, guiones, 
   barras o signos de porcentaje.
- @ : El símbolo "@".
- [A-Za-z0-9.-]+ : Coincide con uno o más caracteres alfanuméricos, puntos o guiones.
- \. : Un punto (.) literal.
- [A-Za-z]{2,} : Coincide con dos o más letras.
- : : El símbolo ":".
- (.*) : Coincide con cualquier texto (captura de grupo).

----------------------------------
Funcionalidad de la función

La función utiliza el método open para abrir el archivo especificado en modo de lectura ('r') 
y codificación ("latin1"). Luego, itera sobre cada línea del archivo utilizando un bucle for.

Para cada línea, la función utiliza el método findall de la biblioteca re para buscar 
coincidencias con la expresión regular. Las coincidencias se almacenan en una lista llamada coincidencias.

Luego, la función itera sobre las coincidencias y imprime los resultados utilizando un 
formato de string que muestra el email y el resto de la dirección.

Try-except para manejar errores

La función utiliza un bloque try-except para manejar posibles errores al abrir o
leer el archivo. Si se produce algún error, la función imprimirá el mensaje de 
error en lugar de dejar que el programa cruce.

-----------------------------------
Ejecución del código

Finalmente, el código ejecuta la función buscar_email con el nombre del archivo especificado como parámetro.






'''