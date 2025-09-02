from entrada import ingresar_productos
from calculos import calcular_totales
from factura import imprimir_encabezado, imprimir_factura

def main():
    imprimir_encabezado()
    productos = ingresar_productos()
    detalles, subtotal_general, iva_general, total = calcular_totales(productos)
    imprimir_factura(detalles, subtotal_general, iva_general, total)

if __name__ == "__main__":
    main()
