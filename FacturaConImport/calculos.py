def calcular_totales(productos, iva_porcentaje=0.19):
    subtotal_general = 0
    iva_general = 0
    detalles = []

    for producto in productos:
        subtotal = producto["precio"] * producto["cantidad"]
        iva = subtotal * iva_porcentaje
        subtotal_general += subtotal
        iva_general += iva

        detalles.append({
            "nombre": producto["nombre"],
            "cantidad": producto["cantidad"],
            "precio": producto["precio"],
            "subtotal": subtotal,
            "iva": iva
        })

    total = subtotal_general + iva_general
    return detalles, subtotal_general, iva_general, total
