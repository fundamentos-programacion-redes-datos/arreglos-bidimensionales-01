# Inicio

# Declaración de la matriz para almacenar notas (3 filas - estudiantes, 4 columnas - notas)
notas = [[0] * 4, 
         [0] * 4, 
         [0] * 4]  # Matriz 3x4 correctamente inicializada en 0

# Declaración del arreglo unidimensional para almacenar los promedios de los estudiantes
promedios = [0] * 3  # Lista de 3 elementos inicializados en 0 (un promedio por estudiante)

# Ingreso de notas por teclado
for estudiante in range(3):  # Recorre las filas (estudiantes)
    for nota in range(4):  # Recorre las columnas (notas)
        # Se usa (nota + 1) y (estudiante + 1) porque los índices inician en 0
        nota_ingresada = input(f"Ingrese la nota {nota + 1} del estudiante {estudiante + 1}: ")
        notas[estudiante][nota] = float(nota_ingresada)  # Conversión a float para manejar decimales

# Cálculo del promedio por estudiante y almacenamiento en el arreglo promedios
for estudiante in range(3):  # Recorre las filas (estudiantes)
    suma = 0  # Reinicia el acumulador de suma por cada estudiante
    for nota in range(4):  # Recorre las notas del estudiante
        suma = suma + notas[estudiante][nota]  # Acumulación correcta de notas
    promedios[estudiante] = suma / 4  # Cálculo correcto del promedio

# Mostrar los promedios almacenados en el arreglo promedios
print("\nPromedios de los estudiantes:")
contador = 1
for promedio in promedios:
    print(f"El promedio del estudiante {contador} es: {promedio:.2f}")  #  Se imprime con dos decimales
    contador = contador + 1

# Fin
