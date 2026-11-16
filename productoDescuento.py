tipo = input("Ingrese el tipo de articulo: ")
precio = float(input("Ingrese el precio del articulo: "))

if tipo == "Textil" or tipo == "textil":
    descuento = precio * 0
elif tipo == "Electrodomestico" or tipo == "electrodomestico":
    descuento = precio * 0.037
elif tipo == "Elementos de cocina" or tipo == "elementos de cocina":
    descuento = precio * 0.042
elif tipo == "Videojuego" or tipo == "videojuego":
    descuento = precio * 0.078
else:
    print("Tipo de articulo no valido")
    exit()

print("Valor del descuento es: $", descuento)
print("Precio final: $", precio - descuento)