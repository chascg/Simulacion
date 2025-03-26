def algoritmo_lineal(semilla, a, c, m, iteraciones):
    n = []
    r_valor = []
    x = semilla
    for _ in range(iteraciones):
        x = (a * x + c) % m
        r = x / 99
        n.append(x)
        r_valor.append(r)
    return n, r_valor

def main():
   
    semilla = int(input("Introduce la semilla (X0): "))
    a = int(input("Introduce la constante multiplicativa (a): "))
    c = int(input("Introduce la constante aditiva (c): "))
    m = int(input("Introduce el módulo (m): "))
    iteraciones = int(input("Introduce el número de iteraciones: "))

    secuencia, r_valor = algoritmo_lineal(semilla, a, c, m, iteraciones)

    print("\nSecuencia de números generados (X_i) y valores de ri:")
    for i, (num, r) in enumerate(zip(secuencia, r_valor)):
        print(f"Iteración {i+1}: Xi = {num}, ri = {r:.4f}")

if __name__ == "__main__":
    main()