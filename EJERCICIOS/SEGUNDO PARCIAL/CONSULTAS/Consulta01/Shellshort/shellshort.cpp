#include <iostream>
using namespace std;

void shellSort(int arr[], int n) {
    // Definir las brechas iniciales
    for (int gap = n / 2; gap > 0; gap /= 2) {
        // Realizar la ordenación por inserción con la brecha actual
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            arr[j] = temp;
        }
    }
}

int main() {
    int arr[] = {5, 2, 8, 12, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    shellSort(arr, n);

    cout << "Array ordenado: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
