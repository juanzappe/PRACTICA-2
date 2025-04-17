rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

# Pedimos al usuario una palabra clave
palabra_clave = input("Ingrese una palabra clave para buscar en las reglas: ").lower()

# Separamos las reglas en líneas
lista_reglas = rules.split('\n')

# Buscamos y mostramos las que contienen la palabra clave
print("\nReglas que contienen la palabra clave:")
for regla in lista_reglas:
    if palabra_clave in regla.lower():
        print("- " + regla)
