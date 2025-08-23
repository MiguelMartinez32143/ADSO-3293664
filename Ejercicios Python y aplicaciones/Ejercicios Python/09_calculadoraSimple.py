numeroUno = float(input("Ingrese el primer número: "))
numeroDos = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == "+":
    print("El resultado de la suma es", numeroUno + numeroDos)
elif operacion == "-":
    print("El resultado de la resta es", numeroUno - numeroDos)
elif operacion == "*":
    print("El resultado de la multiplicación es", numeroUno * numeroDos)
elif operacion == "/":
    if numeroDos != 0:
        print("El resultado de la división es", numeroUno / numeroDos)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("Operación no válida")