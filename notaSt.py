n1 = float(input("Ingrese la nota 1: "))
n2 = float(input("Ingrese la nota 2: "))
n3 = float(input("Ingrese la nota 3: "))
n4 = float(input("Ingrese la nota 4: "))
n5 = float(input("Ingrese la nota 5: "))

definitiva = (n1 + n2 + n3 + n4 + n5) / 5

if definitiva > 5:
    print("Error: notas invalidas, formato entre 0.0 y 5.0")
else:
    if definitiva > 3.5:
        print("Gano el curso")
        print("Su nota es:", definitiva)
    else:
        print("Perdio el curso")
        print("Su nota es:", definitiva)