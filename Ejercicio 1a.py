import numpy as np

# Definimos la matriz
matriz = {
    'a': {
        'A': np.array([[2, -3], [3, -1]]),
        'B': np.array([[1, 5], [2, 0]])
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