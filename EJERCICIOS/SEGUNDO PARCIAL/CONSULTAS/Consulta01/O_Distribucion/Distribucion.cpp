#include <iostream>
#include <vector>
using namespace std;

void countingSort(vector<int>& arr, int exp) {
    const int base = 10; // Base decimal

    int n = arr.size();
    vector<int> count(base, 0); // Inicializar contador

    // Contar la frecuencia de los dígitos
    for (int i = 0; i < n; i++) {
        int digit = (arr[i] / exp) % base;
        count[digit]++;
    }

    // Calcular las posiciones finales de los dígitos
    for (int i = 1; i < base; i++) {
        count[i] += count[i - 1];
    }

    // Construir el arreglo ordenado
    vector<int> sorted(n);
    for (int i = n - 1; i >= 0; i--) {
        int digit = (arr[i] / exp) % base;
        sorted[count[digit] - 1] = arr[i];
        count[digit]--;
    }

    // Copiar el arreglo ordenado al arreglo original
    for (int i = 0; i < n; i++) {
        arr[i] = sorted[i];
    }
}

void radixSort(vector<int>& arr) {
    int maxVal = *max_element(arr.begin(), arr.end());

    for (int exp = 1; maxVal / exp > 0; exp *= 10) {
        countingSort(arr, exp);
    }
}

int main() {
    vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    radixSort(arr);

    cout << "Array ordenado: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}

