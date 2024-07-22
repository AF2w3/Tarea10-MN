import numpy as np

# Definimos la matriz
matriz = {
   'd': {
        'A': np.array([[2, 1, 2], [-2, 3, 0], [2, -1, 3]]),
        'B': np.array([[1, -2], [3, -4], [0, 2]])
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