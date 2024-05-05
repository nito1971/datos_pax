#!/bin/bash

# Directorio a recorrer
DIR_A_RECORRER=/mnt/local/datos/Contras/archivos_partidos

# Archivo de salida para las líneas no repetidas
ARCHIVO_SALIDA=/mnt/local/datos/Contras/email_listo.txt

# Comprobar si se proporcionaron los argumentos necesarios
if [[ -z "$DIR_A_RECORRER" ]] || [[ -z "$ARCHIVO_SALIDA" ]]; then
    echo "Uso: $0 [directorio] [archivo_de_salida]"
    exit 1
fi

# Función para leer archivos línea por línea
leer_archivo() {
    local archivo=$1
    while IFS= read -r linea || [[ -n "$linea" ]]; do
        echo "$linea"
    done < "$archivo"
}

# Exportar la función para que esté disponible para find
export -f leer_archivo

# Inicializar el archivo de salida
> "$ARCHIVO_SALIDA"

# Recorrer el directorio de forma recursiva y procesar los archivos
find "$DIR_A_RECORRER" -type f -exec bash -c 'leer_archivo "$0"' {} \; | sort | uniq > "$ARCHIVO_SALIDA"

echo "Las líneas no repetidas se han escrito en '$ARCHIVO_SALIDA'"