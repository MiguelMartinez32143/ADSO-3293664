definir a,b,r como real
definir op como caracter
leer a
leer b
leer op
si op="+" entonces
    r <- a+b
si no
    si op="-" entonces
        r <- a-b
    si no
        si op="*" entonces
            r <- a*b
        si no
            si op="/" entonces
                r <- a/b
            fin si
        fin si
    fin si
fin si
escribir "el resultado de la operacion es ",r