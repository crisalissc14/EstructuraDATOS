import java.util.Arrays;

public class RadixSort {
    public static void countingSort(int[] arr, int exp) {
        final int base = 10; // Base decimal

        int n = arr.length;
        int[] count = new int[base]; // Inicializar contador

        // Contar la frecuencia de los dígitos
        for (int num : arr) {
            int digit = (num / exp) % base;
            count[digit]++;
        }

        // Calcular las posiciones finales de los dígitos
        for (int i = 1; i < base; i++) {
            count[i] += count[i - 1];
        }

        // Construir el arreglo ordenado
        int[] sorted = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int digit = (arr[i] / exp) % base;
            sorted[count[digit] - 1] = arr[i];
            count[digit]--;
        }

        // Copiar el arreglo ordenado al arreglo original
        System.arraycopy(sorted, 0, arr, 0, n);
    }

    public static void radixSort(int[] arr) {
        int maxVal = Arrays.stream(arr).max().getAsInt();

        for (int exp = 1; maxVal / exp > 0; exp *= 10) {
            countingSort(arr, exp);
        }
    }

    public static void main(String[] args) {
        int[] arr = {170, 45, 75, 90, 802, 24, 2, 66};
        radixSort(arr);

        System.out.print("Array ordenado: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
