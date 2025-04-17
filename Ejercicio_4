import re

usuario = input("Ingrese un nombre de usuario: ")

def validar_usuario(usuario):
    if len(usuario) < 5:
        return "❌ El nombre debe tener al menos 5 caracteres."
    if not any(c.isdigit() for c in usuario):
        return "❌ Debe contener al menos un número."
    if not any(c.isupper() for c in usuario):
        return "❌ Debe contener al menos una letra mayúscula."
    if not usuario.isalnum():
        return "❌ Solo se permiten letras y números (sin símbolos ni espacios)."
    return "✅ Nombre de usuario válido."

print(validar_usuario(usuario))
