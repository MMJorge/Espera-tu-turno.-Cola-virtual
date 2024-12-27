def generador_numero_perfumeria():
    for n in range(1,10000):
        yield f"P - {n}"

def generador_numero_farmacia():
    for n in range(1,10000):
        yield f"F - {n}"

def generador_numero_cosmetica():
    for n in range(1,10000):
        yield f"C - {n}"


p = generador_numero_perfumeria()
f = generador_numero_farmacia()
c = generador_numero_cosmetica()


def decorador(eleccion):

    print("\n" + "*" * 23)
    print("Su numero es: ")
    if eleccion == "P":
        print(next(p))
    elif eleccion == "F":
        print(next(f))
    else:
        print(next(c))
    print("Espere y será atendido")
    print("*" * 23 + "\n")



