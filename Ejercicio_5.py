# Pedimos al usuario su tiempo de reacción en milisegundos
tiempo = int(input("Ingrese su tiempo de reacción en milisegundos: "))

# Clasificación según el tiempo
if tiempo < 200:
    print("Clasificación: Rápido ⚡")
elif 200 <= tiempo <= 500:
    print("Clasificación: Normal 👍")
else:
    print("Clasificación: Lento 🐢")
