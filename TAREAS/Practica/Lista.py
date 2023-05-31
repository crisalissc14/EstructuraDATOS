# Crear una lista vacía para almacenar los nombres
nombres = []

# Solicitar al usuario ingresar nombres hasta que ingrese "fin"
while True:
    nombre = input("Ingrese un nombre ('fin' para terminar): ")
    if nombre == "fin":
        break
    nombres.append(nombre)

# Ordenar la lista de nombres alfabéticamente
nombres.sort()

# Mostrar los nombres en orden alfabético
print("Nombres en orden alfabético:")
for nombre in nombres:
    print(nombre)
