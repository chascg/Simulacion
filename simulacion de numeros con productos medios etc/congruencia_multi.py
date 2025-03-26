def algoritmo_lineal(semilla, a, m, iteraciones):
    n = []
    r_valor = []
    x = semilla
    for _ in range(iteraciones):
        x = (a * x) % m
        r = x / m  # Se corrigió la división para normalizar correctamente
        n.append(x)
        r_valor.append(r)
    return n, r_valor

def main():
    while True:
        try:
            semilla = int(input("Introduce la semilla (X0): "))
            if semilla > 0 and semilla % 2 != 0:
                break
            else:
                print("La semilla debe ser un número impar y mayor que 0.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    while True:
        try:
            a = int(input("Introduce la constante multiplicativa (a): "))
            m = int(input("Introduce el módulo (m): "))
            iteraciones = int(input("Introduce el número de iteraciones: "))
            if a > 0 and m > 0 and iteraciones > 0:
                break
            else:
                print("Los valores de 'a', 'm' e 'iteraciones' deben ser mayores que 0.")
        except ValueError:
            print("Por favor, introduce números enteros válidos.")

    secuencia, r_valor = algoritmo_lineal(semilla, a, m, iteraciones)
    
    print("\nSecuencia de números generados (X_i) y valores de ri:")
    for i, (num, r) in enumerate(zip(secuencia, r_valor), start=1):
        print(f"Iteración {i}: Xi = {num}, ri = {r:.4f}")

if __name__ == "__main__":
    main()
