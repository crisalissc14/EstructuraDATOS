'''UNIVERSIDAD DE LAS FUERZAS ARMADAS (ESPE)
Nombres: Cristina Colimba  
Asignatura: Estructura de Datos  NRC: 9897
Tema: Colas'''
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def agregar(self, item):
        self.items.append(item)

    def quitar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            print("La cola está vacía.")

    def tamano(self):
        return len(self.items)


# Ejemplo de uso
cola = Cola()

# Agregar elementos a la cola
cola.agregar(10)
cola.agregar(20)
cola.agregar(30)

# Obtener el tamaño de la cola
print("Tamaño de la cola:", cola.tamano())

# Quitar elementos de la cola
elemento1 = cola.quitar()
elemento2 = cola.quitar()

# Imprimir los elementos quitados
print("Elemento 1:", elemento1)
print("Elemento 2:", elemento2)

# Verificar si la cola está vacía
if cola.esta_vacia():
    print("La cola está vacía.")
else:
    print("La cola no está vacía.")
