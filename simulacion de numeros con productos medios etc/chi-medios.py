def cuadrados_medios(X0, D, n):
    numeros = []
    for i in range(n):
        Y0 = X0 ** 2
        Y0_str = str(Y0).zfill(2 * D)
        inicio = (len(Y0_str) - D) // 2
        X1_str = Y0_str[inicio:inicio + D]
        X1 = int(X1_str)
        r = X1 / (10 ** D)
        numeros.append(r)
        print(f"Iteración {i + 1}: r{i + 1} = {r}")
        X0 = X1
    
    prueba_chi_cuadrada(numeros, n)

def prueba_chi_cuadrada(numeros, n, k=10):
    """ Realiza la prueba de Chi-cuadrada sin usar scipy """
    
    # Definir los intervalos
    intervalos = [i / k for i in range(k + 1)]
    frecuencias_observadas = [0] * k

    # Contar frecuencias observadas
    for num in numeros:
        for j in range(k):
            if intervalos[j] <= num < intervalos[j + 1]:
                frecuencias_observadas[j] += 1
                break

    # Frecuencia esperada (número total de muestras dividido en los intervalos)
    frecuencia_esperada = n / k
    chi_cuadrado = sum((fo - frecuencia_esperada) ** 2 / frecuencia_esperada for fo in frecuencias_observadas)

    # Valor crítico aproximado para alfa=0.05 y k-1 grados de libertad
    tabla_critica = {9: 16.92, 10: 18.31, 11: 19.68, 12: 21.03}  # Valores tabulados
    chi_critico = tabla_critica.get(k - 1, 16.92)  # Valor por defecto para 9 gl

    print("\nPrueba de Chi-Cuadrada:")
    print(f"Valor calculado: {chi_cuadrado:.4f}")
    print(f"Valor crítico (α=0.05, gl={k - 1}): {chi_critico:.4f}")
    
    if chi_cuadrado < chi_critico:
        print("Los números parecen seguir una distribución uniforme.")
    else:
        print("Los números NO siguen una distribución uniforme.")

D = int(input("Dígitos (D > 3): "))
X0 = int(input(f"Semilla X0 ({D} dígitos): "))
n = int(input("Números a generar: "))

print("\nGenerando números...")
cuadrados_medios(X0, D, n)
	