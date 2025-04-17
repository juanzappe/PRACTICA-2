titles = [ "Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
 "Jugando al nuevo FPS del momento con amigos",
 "Música en vivo: improvisaciones al piano"
 ]

titulo_mas_largo = ""
max_palabras = 0

for titulo in titles:
    cantidad_palabras = len(titulo.split())
    if cantidad_palabras > max_palabras:
        max_palabras = cantidad_palabras
        titulo_mas_largo = titulo

print("El título con más palabras es:")
print(f"'{titulo_mas_largo}' ({max_palabras} palabras)")