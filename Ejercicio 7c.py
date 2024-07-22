import numpy as np

# Función de descomposicion LU
def descomposicion_LU(A):
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

def separar_m_aumentada(Ab):
    Ab = np.array(Ab, dtype=float)
    return Ab[:, :-1], Ab[:, -1].reshape(-1, 1)

def resolver_LU(L, U, b):
    n = L.shape[0]
    y = np.zeros((n, 1), dtype=float)
    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        suma = 0
        for j in range(i):
            suma += L[i, j] * y[j]
        y[i] = (b[i] - suma) / L[i, i]

    x = np.zeros((n, 1), dtype=float)
    x[-1] = y[-1] / U[-1, -1]
    for i in range(n - 2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += U[i, j] * x[j]
        x[i] = (y[i] - suma) / U[i, i]

    return x

# Sistema de ecuacion
sistema = {
    'c': [
        [2, 0, 0, 3],
        [1, 1.5, 0, 4.5],
        [0, -3, 0.5, -6.6],
        [2, -2, 1, 0.8]
    ]
}

# Resolucion del  sistema de ecuacion
for key, sistema in sistema.items():
    try:
        Ab = np.array(sistema)
        A, b = separar_m_aumentada(Ab)
        L, U = descomposicion_LU(A)
        x = resolver_LU(L, U, b)
        print(f"Solución del sistema {key}: {x.flatten()}\n")
    except Exception as e:
        print(f"Error al resolver el sistema {key}: {e}\n")