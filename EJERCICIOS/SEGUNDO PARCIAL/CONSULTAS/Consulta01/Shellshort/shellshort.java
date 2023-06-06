public class ShellSort {
    public static void shellSort(int[] arr) {
        int n = arr.length;
        int gap = n / 2;

        while (gap > 0) {
            for (int i = gap; i < n; i++) {
                int temp = arr[i];
                int j = i;
                while (j >= gap && arr[j - gap] > temp) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }
                arr[j] = temp;
            }
            gap /= 2;
        }
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 12, 1};

        shellSort(arr);

        System.out.print("Array ordenado: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
