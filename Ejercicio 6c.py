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
    'c': [
        [2, 0, 0, 0, 0],
        [1, 1.5, 0, 0, 0],
        [0, -3, 0.5, 0, 0],
        [2, -2, 1, 1, 0]
    ],

}

# Factorización LU
for key, matrix in matriz.items():
    try:
        # Si la matriz no es cuadrada, toma la submatriz cuadrada más grande posible
        matrix = np.array(matrix)
        if matrix.shape[0] != matrix.shape[1]:
            min_dim = min(matrix.shape)
            matrix = matrix[:min_dim, :min_dim]

        L, U = descomposicion_LU(matrix)
        print(f"Factorización LU de la matriz {key}:")
        print("L:")
        print(L)
        print("U:")
        print(U)
        print("\n")
    except ValueError as e:
        print(f"Error en la factorización LU de la matriz {key}: {e}\n")