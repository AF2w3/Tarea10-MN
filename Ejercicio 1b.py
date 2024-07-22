import numpy as np

# Definimos la matriz
matriz = {
    'b': {
        'A': np.array([[2, -3, 1], [3, -1, -3]]),
        'B': np.array([[1, 5, -4], [-3, 2, 0], [2, 1, 3]])
    },

}

# Realizamos la multiplicacion
for key, value in matriz.items():
    A = value['A']
    B = value['B']
    C = np.dot(A, B)
    print(f"Multiplicación de la matriz {key}:")
    print(C)
    print("\n")