"""
    Ejemplo básicos de una listas anidadas en Python
"""

# Declaración de una matriz en Python (Lista Anidada Vacía)
# En este caso, se crean dos listas vacías dentro de otra lista.
mi_matriz = [[], []]
print(mi_matriz)  # Salida: [[], []] (Matriz con dos filas vacías)

# Declaración de una matriz en Python con valores predefinidos
# Aquí cada sublista representa una fila en la matriz
mi_matriz_2 = [
    [1, 2],    # Fila 0
    [3, 10],   # Fila 1
    [8, 9]     # Fila 2
]
print(mi_matriz_2)  
# Salida: [[1, 2], [3, 10], [8, 9]] (Matriz de 3 filas x 2 columnas)

# Declaración de una matriz con valores por defecto (0), según un tamaño conocido
# Se crea una matriz con 2 filas, cada una con 10 elementos inicializados en 0
mi_matriz_3 = [[0] * 10, [0] * 10]  
print(mi_matriz_3)  
# Salida: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
