import numpy as np

def gauss_jordan_inverse(A):
    n = A.shape[0]

    I = np.eye(n)
    AI = np.hstack((A, I))

    for i in range(n):

        if AI[i, i] == 0:
            for j in range(i + 1, n):
                if AI[j, i] != 0:
                    AI[[i, j]] = AI[[j, i]]
                    break
        if AI[i, i] == 0:
            raise ValueError("La matriz es singular y no puede invertirse.")

        # Diagonal contiene todos los 1's
        AI[i] = AI[i] / AI[i, i]

        for j in range(n):
            if i != j:
                AI[j] = AI[j] - AI[j, i] * AI[i]

    # Extraccion de la matriz inversa
    A_inv = AI[:, n:]
    return A_inv

def is_singular(A):
    try:
        _ = gauss_jordan_inverse(A)
        return False
    except ValueError:
        return True

matriz = {
    "d": np.array([[4, 0, 0, 0], [6, 7, 0, 0], [9, 11, 0, 0], [5, 4, 1, 1]])
}

for key, matrix in matriz.items():
    if is_singular(matrix):
        print(f"La matriz {key} es singular y no tiene inversa.\n")
    else:
        print(f"La matriz {key} es no singular.")
        inverse = gauss_jordan_inverse(matrix)
        print(f"Inversa de la matriz {key}:\n{inverse}\n")