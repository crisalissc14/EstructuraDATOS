'''class Deportes:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return(f"yo soy el deporte{self.nombre}")
    
class Baloncesto (Deportes):

    def __init__(self, nombre):
        super().__init__(nombre)'''
        
class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("El vehículo está acelerando.")

    def frenar(self):
        print("El vehículo está frenando.")


class Auto(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def encender(self):
        print("El auto está encendido.")


class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, carga_maxima):
        super().__init__(marca, modelo)
        self.carga_maxima = carga_maxima

    def cargar(self):
        print("La camioneta está cargada.")


# Crear objetos de las clases Auto y Camioneta
auto1 = Auto("Toyota", "Corolla", "Rojo")
camioneta1 = Camioneta("Ford", "Ranger", 1000)

# Acceder a los métodos y atributos de cada objeto
auto1.acelerar()
camioneta1.frenar()
auto1.encender()
camioneta1.cargar()
