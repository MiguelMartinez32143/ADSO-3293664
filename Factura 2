print("*" * 143)
print("TIENDA EL BUEN SABOR")
print("NIT. 90213456")
print("============ FACTURA ============")

productos = []

num_productos = int(input("¿Cuántos productos desea ingresar? "))

for i in range(num_productos):
    print(f"\n--- Producto {i+1} ---")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))

    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

Iva_porcentaje = 0.19
Subtotal_general = 0
iva_general = 0

print("\n=========== FACTURA ===========")
print(f"{'Producto':<15}{'Cant.':<8}{'P.Unitario':<12}{'Subtotal':<12}{'IVA':<12}")

for producto in productos:
    subtotal = producto["precio"] * producto["cantidad"]
    iva = subtotal * Iva_porcentaje
    Subtotal_general += subtotal
    iva_general += iva

    print(f"{producto['nombre']:<15}{producto['cantidad']:<8}{producto['precio']:>12,.2f}{subtotal:>12,.2f}{iva:>12,.2f}")

total = Subtotal_general + iva_general

print("=" * 143)
print(f"{'Subtotal General:':<20} ${Subtotal_general:,.2f}")
print(f"{'IVA Total (19%):':<20} ${iva_general:,.2f}")
print(f"{'TOTAL A PAGAR:':<20} ${total:,.2f}")
print("=" * 143)
