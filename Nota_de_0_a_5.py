nota = float(input("Digite la nota del estudiante: "))
if nota >= 0 and nota < 3.0:
    print("insuficiente")
else:
    if nota > 3.5 and nota < 4.0:
        print("Sobresaliente")
    else:
        if nota >= 4.0 and nota < 5.0:
            print("Excelente")
        else:
            if nota >= 3.0 and nota <= 3.5:
                print("Aceptable")
            else:
                print("Valor no valido")