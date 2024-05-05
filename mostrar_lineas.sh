#!/bin/bash

# Directorio a recorrer
directory=/mnt/local/datos/Contras/archivos_partidos

# Recorremos el directorio y mostramos las líneas de cada archivo
for file in "$directory"/*; do
    if [ -f "$file" ]; then
        echo "Archivo: $file"
        cat "$file"
        echo ""
    fi
done
