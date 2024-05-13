import os
import shutil

# Ruta de la carpeta origen
src_dir = '/mnt/10.0.0.12/desarrollo/datos_pax'

# Ruta de la carpeta destino
dst_dir = '/mnt/10.0.0.12/desarrollo/datos_pax/archivos_partidos'

# Recorrer la carpeta origen
for filename in os.listdir(src_dir):
    # Verificar si el archivo es un archivo .txt
    if filename.endswith('.txt'):
        # Obtener el path completo del archivo
        filepath = os.path.join(src_dir, filename)
        
        # Mover el archivo a la carpeta destino
        shutil.move(filepath, dst_dir)
        print(f"Archivo {filename} movido a la carpeta {dst_dir}")