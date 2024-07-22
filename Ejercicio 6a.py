import numpy as np

# Función descomposicion LU
def descomposicion_LU(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
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

# Matriz
matriz = {
    'a': [
        [2, -1, 1],
        [3, 3, 9],
        [3, 3, 5]
    ]
}

# Factorización LU
for key, matrix in matriz.items():
    try:
        L, U = descomposicion_LU(matrix)
        print(f"Factorización LU de la matriz {key}:")
        print("L:")
        print(L)
        print("U:")
        print(U)
        print("\n")
    except ValueError as e:
        print(f"Error en la factorización LU de la matriz {key}: {e}\n")