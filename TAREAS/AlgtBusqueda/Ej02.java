import java.util.Arrays;
import java.util.Scanner;

public class BusquedaBinaria {
    public static void main(String[] args) {
        // Paso 1: Solicitar al usuario el número objetivo
        System.out.println("Bienvenido al programa de búsqueda binaria.");
        System.out.println("Por favor, ingrese el número que desea buscar.");
        int numObjetivo = obtenerNumeroValido();

        // Paso 2: Crear una lista de números enteros ordenada de forma ascendente
        int[] numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        // Paso 3: Implementar la función de búsqueda binaria
        int posicion = busquedaBinaria(numeros, numObjetivo);

        // Paso 4: Realizar la búsqueda binaria en la lista
        System.out.println("Realizando búsqueda...");

        // Paso 5: Mostrar los resultados de la búsqueda
        if (posicion != -1) {
            System.out.println("¡Encontrado! El número " + numObjetivo + " se encuentra en la posición " + posicion + " de la lista.");
        } else {
            System.out.println("No se encontró el número " + numObjetivo + " en la lista.");
        }

        System.out.println("Gracias por utilizar el programa de búsqueda binaria. ¡Hasta luego!");
    }

    public static int busquedaBinaria(int[] lista, int objetivo) {
        int izquierda = 0;
        int derecha = lista.length - 1;

        while (izquierda <= derecha) {
            int medio = izquierda + (derecha - izquierda) / 2;

            if (lista[medio] == objetivo) {
                return medio;
            }

            if (lista[medio] < objetivo) {
                izquierda = medio + 1;
            } else {
                derecha = medio - 1;
            }
        }

        return -1;
    }

    public static int obtenerNumeroValido() {
        Scanner scanner = new Scanner(System.in);
        int numero;

        do {
            System.out.print("Número objetivo: ");
            while (!scanner.hasNextInt()) {
                System.out.println("Entrada inválida. Por favor, ingrese un número entero.");
                scanner.next();
            }
            numero = scanner.nextInt();

            if (numero < 1 || numero > 10) {
                System.out.println("El número ingresado está fuera del rango válido (1-10). Inténtelo nuevamente.");
            }
        } while (numero < 1 || numero > 10);

        return numero;
    }
}


