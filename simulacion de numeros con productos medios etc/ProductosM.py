def productos_medios(X0, X1, D, n):
    for i in range(n):
        Y0 = X0 * X1
        Y0_str = str(Y0).zfill(2 * D)
        X2 = int(Y0_str[(len(Y0_str) - D) // 2 :][:D])
        r = X2 / (10 ** D)
        print(f"Iteración {i + 1}:")
        print(f"  Y0 = {Y0}")
        print(f"  X2 = {X2} (dígitos centrales)")
        print(f"  r{i + 1} = {r}\n")
        X0, X1 = X1, X2

D = int(input("Dígitos (D > 3): "))
X0 = int(input(f"Semilla X0 ({D} dígitos): "))
X1 = int(input(f"Semilla X1 ({D} dígitos): "))
n = int(input("Números a generar: "))

print("\nGenerando números...\n")
productos_medios(X0, X1, D, n)