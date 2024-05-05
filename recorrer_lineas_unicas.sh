#!/bin/bash

directory=/mnt/local/datos/Contras/archivos_partidos
output_file=/mnt/local/datos/Contras/email_listo.txt

echo "Leyendo archivos..."

declare -A unique_lines_array

for file in "$directory"/*; do
    echo "$file"
    if [ -f "$file" ]; then
        while IFS= read -r line; do
            echo "$line"
            if ! ${unique_lines_array[$line]}; then
                unique_lines_array[$line]=1
                echo "$line" >> "${output_file}"
            fi
        done < "$file"
    fi
done

unset unique_lines_array