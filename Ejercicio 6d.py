import numpy as np

# Función descomposicion LUo
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
    'd': [
        [2.1756, 4.0231, -2.1732, 5.1967],
        [-4.0231, 6.0000, 0, 1.1973],
        [-1.0000, -5.2107, 1.1111, 0],
        [6.0235, 7.0000, 0, -4.1561]
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