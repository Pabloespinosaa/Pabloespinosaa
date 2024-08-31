#Ejercicio 1
def sumarmatrices(matrix1, matrix2):
    filas = len(matrix1)
    columnas = len(matrix1[0])
    matrixresultado = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matrixresultado[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrixresultado
matrix1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
matrix2 = [[10, 11, 12],[13, 14, 15],[16, 17, 18]]
matrixsuma = sumarmatrices(matrix1, matrix2)
print("\nMatriz Resultante (Suma):")
for fila in matrixsuma:
    print(fila)

#Ejercicio 2
def multiplicarmatrices(matrix1, matrix2):
    filas1 = len(matrix1)
    columnas1 = len(matrix1[0])
    filas2 = len(matrix2)
    columnas2 = len(matrix2[0])
    
    if columnas1 != filas2:
        raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
    
    matrixresultado = [[0 for _ in range(columnas2)] for _ in range(filas1)]
    
 
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(columnas1):
                matrixresultado[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return matrixresultado

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

matrixproducto = multiplicarmatrices(matrix1, matrix2)
print("\nMatriz Resultante (Multiplicación):")
for fila in matrixproducto:
    print(fila)
#Ejercicio 3
def transponer_matriz(matrix):
    filas = len(matrix)
    columnas = len(matrix[0])
    
    matrixtranspuesta = [[matrix[j][i] for j in range(filas)] for i in range(columnas)]
    return matrixtranspuesta
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrixt = transponer_matriz(matrix)
print("\nMatriz Transpuesta:")
for fila in matrixt:
    print(fila)
#Ejercicio 4
def es_cuadrado_magico(matrix):
    n = len(matrix)
    suma_magica = sum(matrix[0])
    for fila in matrix:
        if sum(fila) != suma_magica:
            return False
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != suma_magica:
            return False
    if sum(matrix[i][i] for i in range(n)) != suma_magica:
        return False
    
    if sum(matrix[i][n-i-1] for i in range(n)) != suma_magica:
        return False
    return True
matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
es_magico = es_cuadrado_magico(matrix)
print("\n¿Es un cuadrado mágico?")
print(es_magico)