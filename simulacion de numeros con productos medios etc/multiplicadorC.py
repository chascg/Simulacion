def multiplicador_constante(X0, a, D, n):
    for i in range(n):
        Y0 = a * X0
        Y0_str = str(Y0)

        if len(Y0_str) < 2 * D:
            Y0_str = Y0_str.zfill(2 * D)
            print(f"  Y0 (con relleno) = {Y0_str}")
        else:
            print(f"  Y0 = {Y0}")
        
        inicio = (len(Y0_str) - D) // 2
        X1_str = Y0_str[inicio:inicio + D]
        X1 = int(X1_str)  
        r = X1 / (10 ** D)  
        print(f"  X1 = {X1_str} (dígitos centrales)")
        print(f"  r{i + 1} = {r}\n")
        X0 = X1  
        
D = int(input("Dígitos (D > 3): "))
X0 = int(input(f"Semilla X0 ({D} dígitos): "))
a = int(input(f"Constante a ({D} dígitos): "))
n = int(input("Números a generar: "))

print("\nGenerando números...\n")
multiplicador_constante(X0, a, D, n)