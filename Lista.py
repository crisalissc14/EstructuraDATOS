#Crear una lista de numeros
numeros = [1,2,3,4,5]
#Acceder a elementos de las lista
print(numeros[0])
print(numeros[2])
#Modificar elementos de la lista
numeros[1]=10
print(numeros)
#agregar elementos a la lista
numeros.append(6)
print(numeros)
#eliminar elementos de la lista
numeros.remove(3)
print(numeros)
#longitud de la lista
print(len(numeros))
#recorrer la lista en un bucle
for numero in numeros:
 print(numero)