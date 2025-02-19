import random

def sec(ci, cf, C):
 
    numeros_aleatorios = []
    for _ in range(C):
        na = random.randint(ci, cf)
        numeros_aleatorios.append(na)
    return numeros_aleatorios

def N_aleatorios():
    
    print("secuencia 1:")
    ci1 = int(input("escribe la cantidad inicial del rango: "))
    cf1 = int(input("escribe la cantidad final del rango: "))
    C1 = int(input("escribe la cantidad de números aleatorios a imprimir: "))

    if ci1 > cf1:
        print("Error: El valor inicial no puede ser mayor que el final.")
        return

    print("\nsecuencia 2:")
    ci2 = int(input("escribe la cantidad inicial del rango: "))
    cf2 = int(input("escribe la cantidad final del rango: "))
    C2 = int(input("escribe la cantidad de números aleatorios a imprimir: "))

    if ci2 > cf2:
        print("Error: El valor inicial no puede ser mayor que el final.")
        return

    print("\nSecuencia 1:")
    secuencia1 = sec(ci1, cf1, C1)
    print(f"Secuencia 1: {secuencia1}")
    suma1 = sum(secuencia1)

    print("\nSecuencia 2:")
    secuencia2 = sec(ci2, cf2, C2)
    print(f"Secuencia 2: {secuencia2}")
    suma2 = sum(secuencia2)

    print("\nResultados:")
    print(f"Total secuencia 1: {suma1}")
    print(f"Total secuencia 2: {suma2}")

if __name__ == "__main__":
    N_aleatorios()