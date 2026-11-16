a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
discriminante = b**2 - 4*a*c
if a == 0:
    print("La ecuacion no tiene solucion porque a debe ser diferente de 0")
else:
    if a != 0 and discriminante >= 0:
        print("La ecuacion tiene solucion")
        print("El discriminante es:", discriminante)
    else:
        print("La ecuacion no tiene solucion")
        print("El discriminante es:", discriminante)