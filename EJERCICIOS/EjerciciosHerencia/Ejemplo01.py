class Estudiante:
    def __init__(self, nombre, edad, carrera, habilidad_personal):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.habilidad_personal = habilidad_personal

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)
        print("Habilidad Personal:", self.habilidad_personal)


# Crear un objeto Estudiante
estudiante1 = Estudiante("Cristina", 20, "ITIN", "natación")

# Mostrar la información del estudiante
'''estudiante1.mostrar_informacion()'''

print(estudiante1.nombre)
print(estudiante1.edad)
help(estudiante1)
estudiante1.habilidad_personal