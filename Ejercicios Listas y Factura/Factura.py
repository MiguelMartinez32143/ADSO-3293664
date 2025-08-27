print("*" * 143)
print("TIENDA EL BUEN SABOR")
print("NIT. 90213456")
print("============FACTURA No 001====================")

productos=[
{"nombre":"Frijoles","precio":3200,"cantidad":4},
{"nombre":"Lentejas","precio":2800,"cantidad":3},
{"nombre":"Yuca","precio":2500,"cantidad":5},
{"nombre":"Plátano","precio":2000,"cantidad":7}
]

Iva_porcentaje=0.19
Subtotal_general=0
iva_general=0

print("\n===========FACTURA No 001==========")
print(f"{'producto':<10}{'Cant.':<6}{'P.Unitario':<10} {'Subtotal':<10}{'Iva':<10}")

for producto in productos:
subtotal = producto["precio"]*producto["cantidad"]
iva = subtotal*Iva_porcentaje
Subtotal_general += subtotal
iva_general += iva

print(f"{producto['nombre']:<10} {producto['cantidad']:<6}{producto['precio']:<10,.2f}{subtotal:<10,.2f}{iva:<10,.2f}")

total = Subtotal_general+iva_general

print("=" * 143)
print(f"{'Subtotal General:':<20} ${Subtotal_general:,.2f}")
print(f"{'IVA Total(19):':<20} ${iva_general:,.2f}")
print(f"{'TOTAL A PAGAR:':<20} ${total:,.2f}")
print("=" * 143)