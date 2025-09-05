def imprimir_encabezado():
    print("*" * 60)
    print("TIENDA EL BUEN SABOR")
    print("NIT. 90213456")
    print("============ FACTURA ============")

def imprimir_factura(detalles, totales):
    print("\n=========== FACTURA ===========")
    print(f"{'Producto':<15}{'Cantidad':<10}{'P.Unitario':<12}{'Subtotal':<12}{'IVA':<12}")
    for d in detalles:
        print(f"{d['nombre']:<15}{d['cantidad']:<10}{d['precio']:>12,.2f}{d['subtotal']:>12,.2f}{d['iva']:>12,.2f}")
    print("=" * 60)
    print(f"{'Subtotal General:':<20} ${totales['subtotal_general']:,.2f}")
    print(f"{'IVA Total (19%):':<20} ${totales['iva_general']:,.2f}")
    print(f"{'TOTAL A PAGAR:':<20} ${totales['total']:,.2f}")
    print("=" * 60)
