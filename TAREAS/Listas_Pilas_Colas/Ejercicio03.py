'''UNIVERSIDAD DE LAS FUERZAS ARMADAS (ESPE)
Nombres: Cristina Colimba  
Asignatura: Estructura de Datos  NRC: 9897
Tema: Pilas'''
class Pila:
    def __init__(self):
        self.pila = []

    def esta_vacia(self):
        return len(self.pila) == 0

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            print("La pila está vacía. No se puede desapilar.")
        else:
            return self.pila.pop()

def es_palindromo(palabra):
    pila = Pila()

    for letra in palabra:
        pila.apilar(letra)

    palabra_invertida = ""
    while not pila.esta_vacia():
        letra = pila.desapilar()
        palabra_invertida += letra

    return palabra == palabra_invertida

# Ejemplo de prueba
palabra1 = "arenera"
palabra2 = "python"

if es_palindromo(palabra1):
    print(f"{palabra1} es un palíndromo")
else:
    print(f"{palabra1} no es un palíndromo")

if es_palindromo(palabra2):
    print(f"{palabra2} es un palíndromo")
else:
    print(f"{palabra2} no es un palíndromo")
