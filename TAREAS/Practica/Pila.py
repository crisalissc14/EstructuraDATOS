class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        return self.items.pop()


# Crear una instancia de la Pila
pila_maquillaje = Pila()

# Apilar elementos en la pila
pila_maquillaje.apilar("Base de maquillaje")
pila_maquillaje.apilar("Corrector")
pila_maquillaje.apilar("Rubor")
pila_maquillaje.apilar("Sombras de ojos")
pila_maquillaje.apilar("Labial")

# Desapilar elementos de la pila
while not pila_maquillaje.esta_vacia():
    producto = pila_maquillaje.desapilar()
    print("Producto desapilado:", producto)
