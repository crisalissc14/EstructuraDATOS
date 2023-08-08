class NodoArbol:
    def _init_(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def crear_arbol_binario(niveles):
    raiz = NodoArbol(input("Ingrese el valor de la raíz: "))
    cola = [raiz]
    for nivel in range(niveles - 1):
        nueva_cola = []
        for nodo in cola:
            num_hijos = int(input(f"Ingrese la cantidad de hijos para el nodo {nodo.valor}: "))
            for i in range(num_hijos):
                valor_hijo = input(f"Ingrese el valor del hijo {i + 1} para el nodo {nodo.valor}: ")
                nuevo_hijo = NodoArbol(valor_hijo)
                if nodo.izquierda is None:
                    nodo.izquierda = nuevo_hijo
                else:
                    nodo.derecha = nuevo_hijo
                nueva_cola.append(nuevo_hijo)
        cola = nueva_cola
    return raiz

def imprimir_arbol(arbol, nivel=0):
    if arbol is not None:
        print("  " * nivel + arbol.valor)
        imprimir_arbol(arbol.izquierda, nivel + 1)
        imprimir_arbol(arbol.derecha, nivel + 1)

def convertir_a_arbol_binario(arbol):
    if arbol is None:
        return None
    nodo_binario = NodoArbol(arbol.valor)
    nodo_binario.izquierda = convertir_a_arbol_binario(arbol.izquierda)
    nodo_binario.derecha = convertir_a_arbol_binario(arbol.derecha)
    return nodo_binario

niveles = int(input("Ingrese el número de niveles del árbol inicial: "))
arbol_inicial = crear_arbol_binario(niveles)

print("\nÁrbol Matriz:")
imprimir_arbol(arbol_inicial)

arbol_binario = convertir_a_arbol_binario(arbol_inicial)

print("\nÁrbol Binario:")
imprimir_arbol(arbol_binario)