import numpy as np

def descomposicion_LU(A):
    """Descomposición LU de una matriz cuadrada A."""
    A = np.array(A, dtype=float)
    assert A.shape[0] == A.shape[1], "La matriz A debe ser cuadrada."
    n = A.shape[0]
    L = np.zeros((n, n), dtype=float)
    for i in range(n):
        if A[i, i] == 0:
            raise ValueError("No existe solución única.")
        L[i, i] = 1
        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]
            A[j, i:] -= m * A[i, i:]
            L[j, i] = m
    return L, A

def resolver_LU(L, U, b):
    """Resolucion de un sistema de ecuaciones lineales mediante la descomposición LU."""
    n = L.shape[0]
    y = np.zeros(n, dtype=float)
    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        suma = sum(L[i, j] * y[j] for j in range(i))
        y[i] = (b[i] - suma) / L[i, i]
    x = np.zeros(n, dtype=float)
    x[-1] = y[-1] / U[-1, -1]
    for i in range(n - 2, -1, -1):
        suma = sum(U[i, j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) / U[i, i]
    return x

# Sistema de ecuacion
A = np.array([
    [1, -1, 2, -1],
    [1, 0, -1, 1],
    [2, 1, 3, -4],
    [-1, 2, 1, -4]
])

b1 = np.array([6, 4, -2, 5])


# Descomposición LU
L, U = descomposicion_LU(A)

# Resolucion del primer sistema
x1 = resolver_LU(L, U, b1)
print(f"Solución del primer sistema:\n{x1}\n")

