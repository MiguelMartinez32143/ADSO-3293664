# Ejercicio de lista en Python con platos típicos

miLista = ["Arepas", "Tacos", "Paella", "Sushi", "Ceviche"]

print("Lista original:", miLista)

# Agregar un elemento
miLista.append("Pizza")
print("Lista después de agregar un elemento:", miLista)

# Eliminar un elemento
miLista.remove("Paella")
print("Lista después de eliminar un elemento:", miLista)

# Modificar un elemento
miLista[0] = "Bandeja Paisa"
print("Lista después de modificar un elemento:", miLista)

# Recorrer la lista
print("Platos típicos en la lista:")
for plato in miLista:
    print(plato)
