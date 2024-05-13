import os
import shutil

# Ruta de la carpeta origen
src_dir = '//mnt/local/datos/ALIMENTACION_PROYECTOS/EMAIL/partido'

# Ruta de la carpeta destino
dst_dir = '/mnt/10.0.0.12/desarrollo/datos_pax/archivos_partidos'

# Recorrer la carpeta origen
for filename in os.listdir(src_dir):
    # Verificar si el archivo es un archivo .txt
    if filename.endswith('.txt'):
        # Obtener el path completo del archivo
        try:
            filepath = os.path.join(src_dir, filename)

            # Verificar si el archivo ya existe en la carpeta destino
            dst_filepath = os.path.join(dst_dir, filename)
            if os.path.exists(dst_filepath):
                print(f"Archivo {filename} ya existe en {dst_dir}. Lo elimino.")
                os.remove(dst_filepath)  # Eliminar el archivo existente

            # Mover el archivo a la carpeta destino
            shutil.move(filepath, dst_dir)
            print(f"Archivo {filename} movido a {dst_dir}.")
        except Exception as e:
            print(f"Error al mover el archivo {filename}: {e}")