min1 = int(input("Ingrese el minimo del intervalo 1: "))
max1 = int(input("Ingrese el maximo del intervalo 1: "))
min2 = int(input("Ingrese el minimo del intervalo 2: "))
max2 = int(input("Ingrese el maximo del intervalo 2: "))
min3 = int(input("Ingrese el minimo del intervalo 3: "))
max3 = int(input("Ingrese el maximo del intervalo 3: "))
num = int(input("Ingrese el numero a evaluar: "))

if (min1 < num < max1) or (min2 < num < max2) or (min3 < num < max3):
    print("El numero esta dentro de un intervalo")
else:
    print("El numero esta fuera de los intervalos")