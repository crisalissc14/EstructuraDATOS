import java.util.Arrays;

public class RadixSort {

    public static void radixSort(int[] arr) {
        int maxVal = Arrays.stream(arr).max().getAsInt();

        for (int exp = 1; maxVal / exp > 0; exp *= 10) {
            countingSort(arr, exp);
        }
    }

    private static void countingSort(int[] arr, int exp) {
        int base = 10; // Base decimal

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
        int[] sortedArr = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int num = arr[i];
            int digit = (num / exp) % base;
            sortedArr[count[digit] - 1] = num;
            count[digit]--;
        }

        // Actualizar el arreglo original con el arreglo ordenado
        System.arraycopy(sortedArr, 0, arr, 0, n);
    }

    public static void main(String[] args) {
        int[] arr = {170, 45, 75, 90, 802, 24, 2, 66};
        radixSort(arr);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
