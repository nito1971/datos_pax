import re
import re
def extract_email_line(filename):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    with open(filename, 'r') as file:            
        for line in file:                  
            if re.search(email_pattern, line):
              return re.search(email_pattern, line).group()

    return None


if __name__ == '__main__':
    filename = '/mnt/local/datos/ALIMENTACION_PROYECTOS/250807711/1244.csv'
    print(extract_email_line(filename))