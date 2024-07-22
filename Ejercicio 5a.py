import numpy as np

# Función eliminacion_gaussiana
def eliminacion_gaussiana(A: np.ndarray) -> np.ndarray:
    if not isinstance(A, np.ndarray):
        A = np.array(A)
    assert A.shape[0] == A.shape[1] - 1, "La matriz A debe ser de tamaño n-by-(n+1)."
    n = A.shape[0]

    for i in range(0, n - 1):
        p = None
        for pi in range(i, n):
            if A[pi, i] == 0:
                continue

            if p is None:
                p = pi
                continue

            if abs(A[pi, i]) < abs(A[p, i]):
                p = pi

        if p is None:
            raise ValueError("No existe solución única.")

        if p != i:
            _aux = A[i, :].copy()
            A[i, :] = A[p, :].copy()
            A[p, :] = _aux

        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]
            A[j, i:] = A[j, i:] - m * A[i, i:]

    if A[n - 1, n - 1] == 0:
        raise ValueError("No existe solución única.")

    solucion = np.zeros(n)
    solucion[n - 1] = A[n - 1, n] / A[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += A[i, j] * solucion[j]
        solucion[i] = (A[i, n] - suma) / A[i, i]

    return solucion

# Datos del sistema a
A_a = np.array([
    [1, 0, 0],
    [2, 1, 0],
    [-1, 0, 1]
], dtype=float)
B_a = np.array([2, -1, 1], dtype=float)


# Resolucion del sistema a
Ab_a = np.hstack((A_a, B_a.reshape(-1, 1)))
solucion_a = eliminacion_gaussiana(Ab_a)
print(f"Solución del sistema a: {solucion_a}")