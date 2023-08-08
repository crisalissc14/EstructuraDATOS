class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def _init_(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def recorrido_preorden(self, nodo):
        if nodo:
            print(nodo.valor)
            self.recorrido_preorden(nodo.izquierda)
            self.recorrido_preorden(nodo.derecha)

    def recorrido_inorden(self, nodo):
        if nodo:
            self.recorrido_inorden(nodo.izquierda)
            print(nodo.valor)
            self.recorrido_inorden(nodo.derecha)

    def recorrido_postorden(self, nodo):
        if nodo:
            self.recorrido_postorden(nodo.izquierda)
            self.recorrido_postorden(nodo.derecha)
            print(nodo.valor)

    def recorrido_nivel(self):
        if self.raiz is None:
            return

        cola = []
        cola.append(self.raiz)

        while len(cola) > 0:
            nodo = cola.pop(0)
            print(nodo.valor)

            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)

# Ejemplo de uso
arbol = Arbol()
n = int(input("Ingrese la cantidad de nodos: "))

for _ in range(n):
    valor = int(input("Ingrese el valor del nodo: "))
    arbol.insertar(valor)

print("\nRecorrido Preorden:")
arbol.recorrido_preorden(arbol.raiz)

print("\nRecorrido Inorden:")
arbol.recorrido_inorden(arbol.raiz)

print("\nRecorrido Postorden:")
arbol.recorrido_postorden(arbol.raiz)

print("\nRecorrido por Niveles:")
arbol.recorrido_nivel()