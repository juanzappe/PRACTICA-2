descriptions = [
    "Streaming de música en vivo con covers y composiciones",
    "Charla interactiva con la audiencia sobre series y películas",
    "Jugamos a juegos retro y charlamos sobre su historia",
    "Exploramos la mejor música de los 80s y 90s",
    "Programa de entretenimiento con noticias y curiosidades del mundo gamer",
    "Sesión de charla con invitados especiales del mundo del streaming",
    "Música en directo con improvisaciones y peticiones del chat",
    "Un espacio para charlar relajada sobre tecnología y cultura digital",
    "Exploramos el impacto de la música en los videojuegos clásicos"
]

# Inicializamos contadores
menciones = {
    "entretenimiento": 0,
    "música": 0,
    "charla": 0
}

# Recorremos cada descripción
for desc in descriptions:
    texto = desc.lower()
    if "entretenimiento" in texto:
        menciones["entretenimiento"] += 1
    if "música" in texto:
        menciones["música"] += 1
    if "charla" in texto or "charlar" in texto or "charlamos" in texto:
        menciones["charla"] += 1

# Mostramos resultados
for palabra, cantidad in menciones.items():
    print(f"Menciones de '{palabra}': {cantidad}")
