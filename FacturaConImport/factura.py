def imprimir_encabezado():
    print("*" * 143)
    print("TIENDA EL BUEN SABOR")
    print("NIT. 90213456")
    print("============ FACTURA ============")

def imprimir_factura(detalles, subtotal_general, iva_general, total):
    print("\n=========== FACTURA ===========")
    print(f"{'Producto':<15}{'Cantidad.':<8}{'P.Unitario':<12}{'Subtotal':<12}{'IVA':<12}")

    for d in detalles:
        print(f"{d['nombre']:<15}{d['cantidad']:<8}{d['precio']:>12,.2f}{d['subtotal']:>12,.2f}{d['iva']:>12,.2f}")

    print("=" * 143)
    print(f"{'Subtotal General:':<20} ${subtotal_general:,.2f}")
    print(f"{'IVA Total (19%):':<20} ${iva_general:,.2f}")
    print(f"{'TOTAL A PAGAR:':<20} ${total:,.2f}")
    print("=" * 143)
