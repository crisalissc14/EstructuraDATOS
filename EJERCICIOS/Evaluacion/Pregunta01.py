#¿Cuál es la complejidad temporal de la operación de búsqueda en una Lista?
class util_Escolar:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Crear una lista de util_s escolares
util_s_escolares = [
    util_Escolar("Libro", 10),
    util_Escolar("Cuaderno", 5),
    util_Escolar("Lápiz", 2),
    util_Escolar("Borrador", 1),
]

# Buscar un util_ escolar por nombre
def buscar_util__escolar(lista, nombre):
    for util_ in lista:
        if util_.nombre == nombre:
            return util_
    return None

nombre_buscar = "Lápiz"
util_existencia = buscar_util__escolar(util_s_escolares, nombre_buscar)

if util_existencia:
    print(f"El util_ escolar '{nombre_buscar}' fueexistenciautil_existencia. Precio: {util_existencia.precio}")
else:
    print(f"No se encontró el util_ escolar '{nombre_buscar}'.")

#La complejidad temporal de la búsqueda en este caso es O(n),
#ya que la función recorre secuencialmente cada elemento de la lista en el peor de los casos
