def cuadrados_medios(X0, D, n):
    for i in range(n):
        Y0 = X0 ** 2
        Y0_str = str(Y0).zfill(2 * D) 
        inicio = (len(Y0_str) - D) // 2
        X1_str = Y0_str[inicio:inicio + D]
        X1 = int(X1_str)  
        r = X1 / (10 ** D)  
        print(f"Iteración {i + 1}:")
        print(f"  Y0 = {Y0} (con relleno: {Y0_str})")
        print(f"  X1 = {X1_str} (dígitos centrales)")
        print(f"  r{i + 1} = {r}\n")
        X0 = X1 

D = int(input("Dígitos (D > 3): "))
X0 = int(input(f"Semilla X0 ({D} dígitos): "))
n = int(input("Números a generar: "))

print("\nGenerando números...\n")
cuadrados_medios(X0, D, n)