from entrada_v2 import mostrar_productos, seleccionar_productos
from calculos_v2 import calcular_totales
from factura_v2 import imprimir_encabezado, imprimir_factura

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Crear factura")
        print("2. Ver productos disponibles")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            productos = seleccionar_productos()
            if productos:
                imprimir_encabezado()
                detalles, totales = calcular_totales(productos)
                imprimir_factura(detalles, totales)
            else:
                print("⚠️ No seleccionó ningún producto.")
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            print("👋 ¡Gracias por usar el sistema!")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
