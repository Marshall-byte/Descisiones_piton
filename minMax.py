minimo = int(input("Ingrese el valor minimo: "))
maximo = int(input("Ingrese el valor maximo: "))
num = int(input("Ingrese el numero a evaluar: "))
if num >= minimo and num <= maximo:
    print("El numero esta dentro del intervalo")
else:
    print("El numero esta fuera del intervalo")