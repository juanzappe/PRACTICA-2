# Ingreso de las dos palabras
palabra1 = input("Ingrese la primera palabra: ").lower()
palabra2 = input("Ingrese la segunda palabra: ").lower()

# Verificación de anagramas
if sorted(palabra1) == sorted(palabra2):
    print("✅ Las palabras son anagramas.")
else:
    print("❌ Las palabras NO son anagramas.")
