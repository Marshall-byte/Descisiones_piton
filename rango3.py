x = float(input("Ingrese un número real (x): "))
if x > 3.5 and x <= 7.8:
    print("El número", x, "se encuentra en el rango (3.5, 7.8]")
else:
    if x >= 4.5 and x < 9.3:
        print("El número", x, "se encuentra en el rango [9.3, 4.5)")
    else:
        if x >= 23.4 and x <= 45.3:
            print("El número", x, "se encuentra en el rango [23.4, 45.3]")
        else:
            print("El número", x, "NO se encuentra en ninguno de los rangos.")