#include <iostream>
#include <vector>
#include <algorithm>

void radixSort(std::vector<int>& arr) {
    int maxVal = *std::max_element(arr.begin(), arr.end());

    for (int exp = 1; maxVal / exp > 0; exp *= 10) {
        countingSort(arr, exp);
    }
}

void countingSort(std::vector<int>& arr, int exp) {
    int base = 10; // Base decimal

    int n = arr.size();
    std::vector<int> count(base, 0); // Inicializar contador

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
    std::vector<int> sortedArr(n);
    for (int i = n - 1; i >= 0; i--) {
        int num = arr[i];
        int digit = (num / exp) % base;
        sortedArr[count[digit] - 1] = num;
        count[digit]--;
    }

    // Actualizar el arreglo original con el arreglo ordenado
    arr = sortedArr;
}

int main() {
    std::vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    radixSort(arr);
    for (int num : arr) {
        std::cout << num << " ";
    }
    return 0;
}
