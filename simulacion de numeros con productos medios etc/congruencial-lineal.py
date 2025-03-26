def congruencial_aditivo(x, m, iteraciones):
    secuencia = []
    r_valor = []
    
    for _ in range(iteraciones):
        nuevo_x = (x[-1] + x[-2]) % m 
        secuencia.append(nuevo_x)
        r_valor.append(nuevo_x / (m - 1))  
        x.append(nuevo_x) 
    
    return secuencia, r_valor

def main():
    while True:
        try:
            cantidad_inicial = int(input("Introduce la cantidad de valores iniciales (mínimo 2): "))
            if cantidad_inicial >= 2:
                break
            else:
                print("Debes ingresar al menos 2 valores iniciales.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    x = []
    for i in range(cantidad_inicial):
        while True:
            try:
                valor = int(input(f"Introduce el valor inicial X{i+1}: "))
                x.append(valor)
                break
            except ValueError:
                print("Por favor, introduce un número entero válido.")

    while True:
        try:
            m = int(input("Introduce el módulo (m): "))
            if m > 0:
                break
            else:
                print("El módulo debe ser mayor que 0.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    while True:
        try:
            iteraciones = int(input("Introduce el número de iteraciones: "))
            if iteraciones > 0:
                break
            else:
                print("El número de iteraciones debe ser mayor que 0.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    secuencia, r_valor = congruencial_aditivo(x, m, iteraciones)

    print("\nSecuencia de números generados (X_i) y valores de r_i:")
    for i, (num, r) in enumerate(zip(secuencia, r_valor), start=cantidad_inicial):
        print(f"X_{i} = {num}, r_{i - cantidad_inicial + 1} = {r:.4f}")

if __name__ == "__main__":
    main()
