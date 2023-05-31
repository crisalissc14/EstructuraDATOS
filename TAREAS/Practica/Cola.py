class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.items.pop(0)


# Crear una instancia de la Cola
cola_marcas_carros = Cola()

# Encolar marcas de carros
cola_marcas_carros.encolar("Toyota")
cola_marcas_carros.encolar("Honda")
cola_marcas_carros.encolar("Ford")
cola_marcas_carros.encolar("Chevrolet")
cola_marcas_carros.encolar("BMW")

# Desencolar marcas de carros
while not cola_marcas_carros.esta_vacia():
    marca = cola_marcas_carros.desencolar()
    print("Marca desencolada:", marca)
