valorCompra = float(input("Ingrese el valor de la compra: "))
if valorCompra > 100:
    valorFinal = valorCompra * 0.9
    print("La compra aplica a descuento. El valor final con el 10% de descuento es", valorFinal)
else:
    print("La compra no aplica a descuento. El valor a pagar es", valorCompra)