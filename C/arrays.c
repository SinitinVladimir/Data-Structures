#include <stdio.h>

typedef struct {
    int id;
    float value;
} Data;

// Function to print array
void printArray(Data arr[], int size) {
    for (int i=0; i < size; i++)
        printf("ID: %d, Value: %.2f\n", arr[i].id, arr[i].value);
    printf("\n");
}

// Function to insert element at a position
int insertElement(Data arr[], int *size, int pos, Data val) {
    if (pos < 1 || pos > *size + 1) {
        printf("Invalid position for insertion.\n");
        return -1;
    }

    for (int i=*size; i>=pos; i--)
        arr[i] = arr[i-1];
    arr[pos-1] = val;
    (*size)++;
    return 0;
}

// Function to delete element from a position
int deleteElement(Data arr[], int *size, int pos) {
    if (pos < 1 || pos > *size) {
        printf("Invalid position for deletion.\n");
        return -1;
    }

    for (int i=pos-1; i<*size; i++)
        arr[i] = arr[i+1];
    (*size)--;
    return 0;
}

// Function to concatenate two arrays
void concatenateArrays(Data arr1[], int size1, Data arr2[], int size2, Data result[]) {
    for (int i=0; i<size1; i++)
        result[i] = arr1[i];
    for (int i=0; i<size2; i++)
        result[i+size1] = arr2[i];
}

// Main function
int main() {
    Data arr[100], arr1[50], arr2[50], result[100];
    int size, size1, size2;
    int pos, splitIndex;
    Data val;

    printf("Enter the size of the array: ");
    scanf("%d", &size);
    if (size < 1 || size > 100) {
        printf("Invalid array size. Enter a size between 1 and 100.\n");
        return -1;
    }

    printf("Enter the elements of the array (id and value): ");
    for(int i=0; i<size; i++)
        scanf("%d %f", &arr[i].id, &arr[i].value);

    printf("Original array: \n");
    printArray(arr, size);

    // Inserting an element
    printf("Enter the position and value to insert (id and value): ");
    scanf("%d %d %f", &pos, &val.id, &val.value);
    if (insertElement(arr, &size, pos, val) == -1)
        return -1;
    printf("Array after inserting ID: %d, Value: %.2f at position %d: \n", val.id, val.value, pos);
    printArray(arr, size);

    // Deleting an element
    printf("Enter the position to delete: ");
    scanf("%d", &pos);
    if (deleteElement(arr, &size, pos) == -1)
        return -1;
    printf("Array after deleting element at position %d: \n", pos);
    printArray(arr, size);

    printf("Enter the size of the second array for concatenation: ");
    scanf("%d", &size2);
    if (size2 < 1 || size2 > 50) {
        printf("Invalid array size. Enter a size between 1 and 50.\n");
        return -1;
    }

    printf("Enter the elements of the second array for concatenation (id and value): ");
    for(int i=0; i<size2; i++)
        scanf("%d %f", &arr2[i].id, &arr2[i].value);

    // Concatenating the arrays
    concatenateArrays(arr, size, arr2, size2, result);
    printf("Array after concatenation: \n");
    printArray(result, size+size2);

    // Splitting the array
    printf("Enter the position to split the array: ");
    scanf("%d", &splitIndex);
    if (splitIndex < 1 || splitIndex > size + size2) {
        printf("Invalid position for splitting the array.\n");
        return -1;
    }

    for (int i=0; i<splitIndex; i++)
        arr1[i] = result[i];
    for (int i=splitIndex; i<size+size2; i++)
        arr2[i-splitIndex] = result[i];
    printf("Array after splitting: \n");
    printArray(arr1, splitIndex);
    printArray(arr2, size+size2-splitIndex);

    return 0;
}
