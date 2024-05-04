import re

def find_email_line(filename):
    '''
    Esta expresión regular busca:

    1. Una cadena que contiene al menos un carácter alfabeto o número (`[A-Za-z0-9.]`) seguida de `@`, un punto y guion 
    (`-`), otro punto (`\.`) y finalmente dos letras (`[A-Za-z]{2,}`). Esto es la dirección de correo electrónico.
    2. El carácter `:`.
    3. Cualquier texto que se encuentre después del carácter `:` (capturado con el grupo `(.*?)`).
    '''


    email_pattern = r'([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}):(.*)'
    with open(filename, 'r') as file:
        content = file.read()
    
    matches = re.findall(email_pattern, content)
    for match in matches:
        email, rest = match
        print(f"Email: {email}, Rest: {rest}")

find_email_line('example.txt')


