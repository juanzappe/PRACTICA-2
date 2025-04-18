clients = [
    "  Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
    " Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
    "luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
    "  ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
    "carlos mendes", "RICARDO FERNÁNDEZ  ", " Laura ramos", "CARLOS MENDES",
    "alejandro gonzález", " ALEJANDRO GONZÁLEZ  ", "Patricia Vega",
    "patricia VEGA", "Andrés Ocampo", "  andrés ocampo", "Monica Herrera",
    "MONICA HERRERA  ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
    "SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
    "Damián Castillo  ", None, "", "  "
]

# Limpiar la lista
clientes_limpios = set()  # Usamos un set para eliminar duplicados

for cliente in clients:
    if cliente and cliente.strip():  # Verificamos que no sea None ni cadena vacía
        cliente_limpio = cliente.strip().title()
        clientes_limpios.add(cliente_limpio)

# Convertimos el set a lista y la ordenamos
clientes_limpios = sorted(clientes_limpios)

# Mostramos el resultado
print("✅ Lista limpia de clientes:")
for cliente in clientes_limpios:
    print("-", cliente)
