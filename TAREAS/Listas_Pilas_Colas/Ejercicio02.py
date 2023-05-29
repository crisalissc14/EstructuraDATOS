'''UNIVERSIDAD DE LAS FUERZAS ARMADAS (ESPE)
Nombres: Cristina Colimba  
Asignatura: Estructura de Datos  NRC: 9897
Tema: Pilas'''

class PilaArticulosBelleza:
    def __init__(self):
        self.pila = []

    def esta_vacia(self):
        return len(self.pila) == 0

    def apilar(self, articulo):
        self.pila.append(articulo)

    def desapilar(self):
        if self.esta_vacia():
            print("La pila está vacía. No se puede desapilar.")
        else:
            articulo = self.pila.pop()
            return articulo

# Crear una instancia de la pila
pila_articulos = PilaArticulosBelleza()

# Apilar algunos artículos
pila_articulos.apilar("Labial")
pila_articulos.apilar("Máscara de pestañas")
pila_articulos.apilar("Crema facial")

# Desapilar un artículo
articulo_desapilado = pila_articulos.desapilar()
print("Artículo desapilado:", articulo_desapilado)

# Verificar si la pila está vacía
if pila_articulos.esta_vacia():
    print("La pila está vacía")
else:
    print("La pila no está vacía")
