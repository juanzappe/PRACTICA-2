zen = "Beautiful is better than ugly. " \
"Explicit is better than implicit. " \
"Simple is better than complex." \
"Complex is better than complicated." \
"Flat is better than nested." \
"Sparse is better than dense. " \
"Readability counts."

# Separar el Zen de Python en líneas
lineas = zen.split('.')

# Filtrar las líneas donde la segunda palabra empieza con una vocal
for linea in lineas:
    palabras = linea.split()
    if len(palabras) > 1 and palabras[1][0].lower() in 'aeiou':
        print(linea)
