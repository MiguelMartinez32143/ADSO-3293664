def ingresar_productos():
    productos = []
    num_productos = int(input("¿Cuántos productos desea ingresar? "))

    for i in range(num_productos):
        print(f"\n--- Producto {i+1} ---")
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio unitario: "))
        cantidad = int(input("Cantidad: "))

        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })

    return productos
