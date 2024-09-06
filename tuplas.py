# Creación de una tupla
def crear_tupla(num1, num2, num3):
    return (num1, num2, num3)

# Acceso a elementos de una tupla
numeros = (10, 20, 30, 40, 50)
print(numeros[2])

# Tuplas anidadas
tupla_anidada = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tupla_anidada[1][1])

# Concatenación de tuplas
pares = (2, 4, 6, 8, 10)
impares = (1, 3, 5, 7, 9)
resultado = pares + impares
print(resultado)

# Conteo de elementos en una tupla
colores = ('rojo', 'azul', 'verde', 'rojo', 'amarillo', 'rojo')
print(colores.count('rojo'))

# Conversión de lista a tupla
nombres = ['Ana', 'Juan', 'Pedro', 'Luis']
nombres_tupla = tuple(nombres)
print(nombres_tupla)

# Slicing en tuplas
tupla_larga = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
nueva_tupla = tupla_larga[:5]
print(nueva_tupla)

# Intercambio de valores utilizando tuplas
a = 5
b = 10
a, b = b, a
print(a, b)
