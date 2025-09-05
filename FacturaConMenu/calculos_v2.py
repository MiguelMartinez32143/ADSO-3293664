def calcular_totales(productos, iva_porcentaje=0.19):
    subtotal_general = 0
    iva_general = 0
    detalles = []
    
    for producto in productos:
        nombre, precio, cantidad = producto
        subtotal = precio * cantidad
        iva = subtotal * iva_porcentaje
        subtotal_general += subtotal
        iva_general += iva
        detalles.append({
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal,
            "iva": iva
        })
    totales = {
        "subtotal_general": subtotal_general,
        "iva_general": iva_general,
        "total": subtotal_general + iva_general
    }
    return detalles, totales
