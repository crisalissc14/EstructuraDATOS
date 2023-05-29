'''UNIVERSIDAD DE LAS FUERZAS ARMADAS (ESPE)
Nombres: Cristina Colimba  
Asignatura: Estructura de Datos  NRC: 9897
Tema: Pilas'''
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía.")


def verificar_simetria(lista):
    pila = Pila()
    longitud = len(lista)

    # Apilar la primera mitad de la lista en la pila
    for i in range(longitud // 2):
        pila.apilar(lista[i])

    # Comparar los elementos de la segunda mitad con los elementos desapilados
    for i in range(longitud // 2, longitud):
        if lista[i] != pila.desapilar():
            return False

    return True


# Ejemplo de uso
juguetes1 = ["muñeca", "carro", "pelota", "carro", "muñeca"]
juguetes2 = ["oso", "tren", "barco", "avión"]

print("Lista de juguetes 1:", juguetes1)
if verificar_simetria(juguetes1):
    print("La lista de juguetes 1 es simétrica.")
else:
    print("La lista de juguetes 1 no es simétrica.")

print("Lista de juguetes 2:", juguetes2)
if verificar_simetria(juguetes2):
    print("La lista de juguetes 2 es simétrica.")
else:
    print("La lista de juguetes 2 no es simétrica.")
