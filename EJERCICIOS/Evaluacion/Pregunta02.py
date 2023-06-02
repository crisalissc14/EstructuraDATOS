#b) ¿Cuál es la estructura de datos adecuada para implementar una Pila? ¿Por qué?
#Simplidad, eficiencia y flexibilidad el momento de aplizar nuestro código
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0
# len : longitud o numeros de la lista
    def apilar(self, num):
        self.items.append(num)
#append: agregar los numeros o elementos        

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()
#lista.pop(): eliminará y devolverá el último elemento de la lista.

# Crear una instancia de la clase Pila
pila = Pila()

# Apilar nums en la pila
pila.apilar(3.14)
pila.apilar(1.23)
pila.apilar(2.718)

# Desapilar nums de la pila
print(pila.desapilar())  # Output: 2.718
print(pila.desapilar())  # Output: 1.23
print(pila.desapilar())  # Output: 3.14
print(pila.desapilar())  # Output: None (pila vacía)
