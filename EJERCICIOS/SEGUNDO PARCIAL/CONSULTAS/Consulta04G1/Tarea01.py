def busqueda_exhaustiva():
    # Definir variables
    lanzamientos = ['roja', 'azul', 'verde', 'amarilla']
    puntuaciones = [10, 6, 4, 2]
    limite_lanzamientos = 3
    limite_puntuacion = 15
    mejor_puntuacion = 0
    mejor_combinacion = []
    
    # Generar todas las combinaciones posibles de lanzamientos
    for lanzamiento1 in lanzamientos:
        for lanzamiento2 in lanzamientos:
            for lanzamiento3 in lanzamientos:
                combinacion = [lanzamiento1, lanzamiento2, lanzamiento3]
                puntuacion_total = sum([puntuaciones[lanzamientos.index(lanzamiento)] for lanzamiento in combinacion])
                
                # Verificar si la combinación cumple con los criterios
                if puntuacion_total <= limite_puntuacion and len(set(combinacion)) <= limite_lanzamientos:
                    # Actualizar la mejor puntuación y combinación
                    if puntuacion_total > mejor_puntuacion:
                        mejor_puntuacion = puntuacion_total
                        mejor_combinacion = combinacion
                        
    # Imprimir la mejor combinación encontrada
    print("Mejor combinación de lanzamientos:")
    for i, lanzamiento in enumerate(mejor_combinacion):
        print(f"Lanzamiento {i+1}: Región {lanzamiento} ({puntuaciones[lanzamientos.index(lanzamiento)]} puntos)")

# Ejecutar la función de búsqueda exhaustiva
busqueda_exhaustiva()

