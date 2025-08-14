definir total como real
escribir "ingrese el valor total de la compra, si esta supera un monto de 100$, se le hara un descuento del 10%"
leer total
si total>100 entonces
    total <- total*0.9
    escribir "el total con descuento es ",total
si no
    escribir "el total a pagar es ",total
fin si