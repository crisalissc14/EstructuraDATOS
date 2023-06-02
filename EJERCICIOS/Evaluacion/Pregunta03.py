class ColaRopa:
    # Creamos una lista vacía para almacenar los elementos de la cola
    def __init__(self):
        self.items = []
 # Verificamos si la cola está vacía
    def esta_vacia(self):
        return len(self.items) == 0
# Añadimos el elemento al final de la cola
    def encolar(self, elemento):
        self.items.append(elemento)
# Eliminamos y retornamos el primer elemento de la cola
    def desencolar(self):
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

# Creamos una instancia de la clase ColaRopa
cola_ropa = ColaRopa()
# Añadimos elementos a la cola
cola_ropa.encolar("Skeachers")
cola_ropa.encolar("NorthStar")
cola_ropa.encolar("Nike")
 # Desencolamos y mostramos los elementos de la cola
try:
    print(cola_ropa.desencolar())  # Output: Skeachers
    print(cola_ropa.desencolar())  # Output: NorthStar
    print(cola_ropa.desencolar())  # Output: Nike
    print(cola_ropa.desencolar())  # Output: ValueError: La cola está vacía
except ValueError as e:
    print(e)
 # Mostramos el mensaje de error correspondiente
