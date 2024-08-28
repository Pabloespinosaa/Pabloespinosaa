#Ejercicio 1
palabras = ["Python", "Java", "C++", "Python", "JavaScript", "Python", "C#"]
contador = 0
for palabra in palabras:
    if palabra == "Python":
        contador += 1
print(f"La palabra 'Python' aparece {contador} veces en la lista.")

#Ejercicio 2
frases = ["hola", "mundo", "python", "es", "genial"]
frases_mayusculas = []
for frase in frases:
    mayuscula = ""
    for caracter in frase:
        if caracter.isalpha():
            mayuscula += chr(ord(caracter) - 32)
        else:
            mayuscula += caracter
    frases_mayusculas.append(mayuscula)
print(frases_mayusculas)
#Ejercicio 3
palabras = ["sol", "luna", "cielo", "mar", "estrella", "pez"]
palabraaja= []
for palabra in palabras:
    if len(palabra) >= 4:
        palabraaja.append(palabra)
print(palabraaja)


#Ejercicio 4
numeros = [15, 22, 8, 34, 9, 6, 17]
maximo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
print(f"El número máximo es: {maximo}")


#Ejercicio 5

numeros = [-3, 5, -7, 2, -8, 10, -4, 6]
contador_positivos = 0
for numero in numeros:
    if numero > 0:
        contador_positivos += 1
print(f"Hay {contador_positivos} números positivos en la lista.")

#Ejercicio 6

numeros = [1, 2, 3, 4, 5]
numeros_invertidos = []
for i in range(len(numeros) - 1, -1, -1):
    numeros_invertidos.append(numeros[i])
print(numeros_invertidos)

#Ejercicio 7

numeros = [4, 7, 2, 9, 3, 8, 5]
suma = 0
for numero in numeros:
    suma += numero
media = suma / len(numeros)
print(f"La media es: {media}")
