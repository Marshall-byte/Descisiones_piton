a = float(input("Digite el primer numero: "))
b = float(input("Digite el segundo numero: "))
if a >= b:
    if a == b:
        print(a, "es igual a", b)
    else:
        print(a, "es mayor que", b)
else:
    print(b, "es mayor que", a)