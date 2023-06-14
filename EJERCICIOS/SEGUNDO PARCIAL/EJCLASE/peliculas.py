# Definir la lista de películas
peliculas = []

# Función para mostrar todas las películas
def mostrar_peliculas():
    if len(peliculas) == 0:
        print("No hay películas registradas.")
    else:
        print("Lista de películas:")
        for pelicula in peliculas:
            print(f"Título: {pelicula['titulo']}")
            print(f"Año: {pelicula['anio']}")
            print(f"Género: {pelicula['genero']}")
            print("------")

# Función para agregar una película
def agregar_pelicula():
    titulo = input("Ingrese el título de la película: ")
    anio = input("Ingrese el año de la película: ")
    genero = input("Ingrese el género de la película: ")
    pelicula = {
        "titulo": titulo,
        "anio": anio,
        "genero": genero
    }
    peliculas.append(pelicula)
    print("Película agregada correctamente.")

# Función para actualizar una película
def actualizar_pelicula():
    titulo = input("Ingrese el título de la película que desea actualizar: ")
    for pelicula in peliculas:
        if pelicula['titulo'] == titulo:
            anio = input("Ingrese el nuevo año de la película: ")
            genero = input("Ingrese el nuevo género de la película: ")
            pelicula['anio'] = anio
            pelicula['genero'] = genero
            print("Película actualizada correctamente.")
            return
    print("No se encontró la película.")

# Función para eliminar una película
def eliminar_pelicula():
    titulo = input("Ingrese el título de la película que desea eliminar: ")
    for pelicula in peliculas:
        if pelicula['titulo'] == titulo:
            peliculas.remove(pelicula)
            print("Película eliminada correctamente.")
            return
    print("No se encontró la película.")

# Menú principal
while True:
    print("\n--- CRUD de Películas ---")
    print("1. Mostrar todas las películas")
    print("2. Agregar una película")
    print("3. Actualizar una película")
    print("4. Eliminar una película")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_peliculas()
    elif opcion == "2":
        agregar_pelicula()
    elif opcion == "3":
        actualizar_pelicula()
    elif opcion == "4":
        eliminar_pelicula()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
