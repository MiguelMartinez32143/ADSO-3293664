primerNumero = float(input("Ingrese el primer número: "))
segundoNumero = float(input("Ingrese el segundo número: "))
if primerNumero > segundoNumero:
    print("El mayor es", primerNumero)
elif segundoNumero > primerNumero:
    print("El mayor es", segundoNumero)
else:
    print("Ambos números son iguales")