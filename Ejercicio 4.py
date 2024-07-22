import numpy as np

def descomposicion_LU(A):
    """ Descomposición LU de una matriz cuadrada A."""
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

def calc_determinante(A):
    """Calculo del determinante usando descomposición LU."""
    _, U = descomposicion_LU(A)
    detA = np.prod(np.diag(U))
    return detA

def matriz_A(alpha):
    return [
        [1, -1, alpha],
        [2, 2, 1],
        [0, alpha, -3/2]
    ]

# Valores de alfa que hacen que el determinante sea cero
alphas = np.linspace(-100, 100, 1000)
valores_singulares = []

for alpha in alphas:
    A = matriz_A(alpha)
    try:
        detA = calc_determinante(A)
        if np.isclose(detA, 0, atol=1e-8):  # Determinante cercano a cero
            valores_singulares.append(alpha)
    except ValueError:
        continue

print("Valores de alpha que hacen que la matriz sea singular:", valores_singulares)