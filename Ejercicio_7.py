import random
import string
from datetime import datetime

# Función para generar el código de descuento
def generar_codigo(nombre):
    nombre = nombre.upper()
    fecha = datetime.now().strftime('%d%m%Y')  # formato: día, mes, año (sin separadores)
    base = nombre + fecha  # nombre + fecha

    # Rellenar el resto con letras y números aleatorios
    restante = 30 - len(base)
    aleatorios = ''.join(random.choices(string.ascii_uppercase + string.digits, k=restante))

    return base + aleatorios

# Ingreso del usuario con validación
while True:
    usuario = input("Ingrese su nombre (máximo 15 caracteres): ")
    if len(usuario) <= 15:
        break
    else:
        print("❌ El nombre excede los 15 caracteres. Intente nuevamente.")

# Generar y mostrar el código
codigo_descuento = generar_codigo(usuario)
print("\n🎉 Su código de descuento es:")
print(codigo_descuento)
