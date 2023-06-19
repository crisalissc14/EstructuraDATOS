# Paso 1: Solicitar al usuario el número objetivo
print("¡Hola! Soy el Buscador de Números.")
print("Estoy aquí para ayudarte a encontrar el número que estás buscando.")
NumObjetivo = int(input("Por favor, ingresa el número que deseas encontrar: "))

# Paso 2: Crear una lista de números enteros
numeros = []
numeros_str = input("Ingresa una lista de números separados por comas: ")
numeros = [int(num) for num in numeros_str.split(",")]

# Paso 3: Implementar la función de búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Paso 4: Realizar la búsqueda lineal en la lista
posicion = busqueda_lineal(numeros, NumObjetivo)

# Paso 5: Mostrar los resultados de la búsqueda
print("Realizando búsqueda...")
print("")

if posicion != -1:
    print(f"¡Encontrado! El número {NumObjetivo} se encuentra en la posición {posicion} de la lista.")
else:
    print(f"No se encontró el número {NumObjetivo} en la lista.")

print("")
print("¡Gracias por utilizar el Buscador de Números! ¡Hasta luego!")

