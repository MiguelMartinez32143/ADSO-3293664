productos_disponibles = [
    ("Pan", 1500),
    ("Leche", 3800),
    ("Queso", 8500),
    ("Huevos", 600),
    ("Café", 12000)
]

def mostrar_productos():
    print("\n=== PRODUCTOS DISPONIBLES ===")
    for i, (nombre, precio) in enumerate(productos_disponibles, start=1):
        print(f"{i}. {nombre:<10} - ${precio:,.2f}")

def seleccionar_productos():
    factura = []
    while True:
        mostrar_productos()
        opcion = input("\nIngrese el número del producto (o '0' para terminar): ")
        if opcion == "0":
            break
        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(productos_disponibles):
                cantidad = int(input("Ingrese la cantidad: "))
                nombre, precio = productos_disponibles[indice]
                factura.append((nombre, precio, cantidad))
            else:
                print("❌ Producto no válido.")
        except ValueError:
            print("❌ Ingrese un número válido.")
    return factura
