# - primero -
#Objetivo: Crear un programa que permita registrar alumnos y sus calificaciones, calculando el promedio de cada uno.
alumnos = []

while True:
    nombre = input("Ingresa el nombre del alumno (o 'salir' para ver las calificaciones): ")
    if nombre.lower() == 'salir':
        break

    materias = ["Geografía", "Historia", "Matemáticas", "Química", "Física"]
    calificaciones = []

    print(f"Ingrese las calificaciones para {nombre}:")
    
    for materia in materias:
        calificacion = input(f"{materia}: ")

        while not calificacion.isdigit() or int(calificacion) > 100:
            print("Por favor, introduce un número válido menor o igual a 100.")
            calificacion = input(f"{materia}: ")

        calificaciones.append(int(calificacion))

    promedio = round(sum(calificaciones) / len(calificaciones), 2)
    
    alumnos.append((nombre, promedio))

print("\nLista de alumnos y sus promedios:")
for alumno in alumnos:
    print(f"Alumno: {alumno[0]}, Promedio: {alumno[1]:.2f}")


valor = float(input("\nIngrese un valor de promedio para filtrar: "))

print(f"\nAlumnos con promedio mayor o igual a {valor}:")
for alumno in alumnos:
    if alumno[1] >= valor:
        print(f"Alumno: {alumno[0]}, Promedio: {alumno[1]:.2f}")

print(f"\nAlumnos con promedio menor a {valor}:")
for alumno in alumnos:
    if alumno[1] < valor:
        print(f"Alumno: {alumno[0]}, Promedio: {alumno[1]:.2f}")

# - segundo -

""""
import random

numero = random.randint(45, 90)
intentos = 0

def pistas(numero, intentos):
    while(True):
            try:
                print(intentos)
                decremento = max(1, (45 - (intentos * 15)))
                pista1 = max(0, numero - random.randint(1, decremento))
                pista2 = numero + random.randint(1, decremento)
                
                print(f"{numero} Tu número se encuentra entre {pista1} y {pista2}")
                
                respuesta = int(input("¿Cuál crees que es el número? "))

                if respuesta == numero:
                    print("¡Buen trabajo! ¡Adivinaste el número!")
                    break
                elif intentos == 4:
                    print("Perdiste")
                    break
                else:
                    print(f"Tu respuesta es incorrecta, te quedan {4-intentos} intentos")
                    intentos += 1
            except ValueError:
                 intentos +=1
                 print(f"Solo puedes introducir numeros, te restaremos un intento por esto, te quedan {4-intentos}")
                 if intentos == 4:
                    print("Perdiste")
                    break
            except EOFError:
                 intentos += 1
                 print("Cesar, cesar, no andes mamando, tienes un intento menos")
                 if intentos == 4:
                    print("Perdiste")
                    break
            except:
                 intentos += 1
                 print("Como jodes mamahuevo, menos 1 intento if if")
                 if intentos == 4:
                    print("Perdiste")
                    break
                 
pistas(numero, intentos)
"""""
#Tercero

class Item:
    def __init__(self, nombre, cantidad, unidades, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidades = unidades
        self.precio = precio
    
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad} {self.unidades}, Precio: {self.precio} por unidad"

def agregar_item():
    nombre = str(input("Proporciona el nombre del item a agregar: "))
    cantidad = int(input("Proporciona la cantidad de producto disponible: "))
    unidades = str(input("Proporciona las unidades: "))
    precio = float(input("Finalmente proporciona el precio por unidad: "))
    return Item(nombre, cantidad, unidades, precio)  # Devuelve un objeto de la clase Item

def mostrar_inventario(inventario):
    if inventario:
        print("\nInventario actual:")
        for item in inventario:
            print(item.mostrar_informacion())
    else:
        print("\nEl inventario está vacío.")

def actualizar_cantidad(inventario):
    nombre = input("Ingresa el nombre del item cuya cantidad deseas actualizar: ")
    for item in inventario:
        if item.nombre.lower() == nombre.lower():
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {item.nombre}: "))
            item.cantidad = nueva_cantidad
            print(f"La cantidad de {item.nombre} ha sido actualizada a {item.cantidad} {item.unidades}.")
            return
    print(f"No se encontró un item con el nombre '{nombre}' en el inventario.")

def eliminar_item(inventario):
    nombre = input("Ingresa el nombre del item que deseas eliminar: ")
    for item in inventario:
        if item.nombre.lower() == nombre.lower():
            inventario.remove(item)
            print(f"El item '{item.nombre}' ha sido eliminado del inventario.")
            return
    print(f"No se encontró un item con el nombre '{nombre}' en el inventario.")

def mostrar_menu():
    print("\n--- Menu de Inventario ---")
    print("1. Agregar item")
    print("2. Mostrar inventario")
    print("3. Actualizar cantidad de un item")
    print("4. Eliminar item")
    print("5. Salir")

inventario = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")
    
    try:
        if opcion == '1':
            item = agregar_item()
            inventario.append(item)
            print(f"El item '{item.nombre}' ha sido agregado al inventario.")
        elif opcion == '2':
            mostrar_inventario(inventario)
        elif opcion == '3':
            actualizar_cantidad(inventario)
        elif opcion == '4':
            eliminar_item(inventario)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")
    except:
        print("Porfavor, seleccione un numero valido en el menu")
