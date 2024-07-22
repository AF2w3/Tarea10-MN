import numpy as np

# Definimos la matriz
matriz = {
    'c': {
        'A': np.array([[2, -3, 1], [4, 3, 0], [5, 2, -4]]),
        'B': np.array([[1, 0, 1], [1, 0, -1], [2, -1, -2]])
    }
}

# Realizamos la multiplicacion
for key, value in matriz.items():
    A = value['A']
    B = value['B']
    C = np.dot(A, B)
    print(f"Multiplicación de la matriz {key}:")
    print(C)
    print("\n")