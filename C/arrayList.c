#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    float value;
} Data;

typedef struct {
    Data* array;
    size_t used;
    size_t size;
} ArrayList;

void initArrayList(ArrayList* a, size_t initialSize) {
    a->array = malloc(initialSize * sizeof(Data));
    a->used = 0;
    a->size = initialSize;
}

void insertArrayList(ArrayList* a, Data element) {
    if (a->used == a->size) {
        a->size *= 2;
        a->array = realloc(a->array, a->size * sizeof(Data));
    }
    a->array[a->used++] = element;
}

void freeArrayList(ArrayList* a) {
    free(a->array);
    a->array = NULL;
    a->used = a->size = 0;
}

void printArrayList(ArrayList* a) {
    for (size_t i = 0; i < a->used; i++)
        printf("ID: %d, Value: %.2f\n", a->array[i].id, a->array[i].value);
    printf("\n");
}

ArrayList* splitArrayList(ArrayList* a, size_t pos) {
    if (pos >= a->used) {
        printf("Invalid position for splitting.\n");
        return NULL;
    }

    ArrayList* b = malloc(sizeof(ArrayList));
    initArrayList(b, a->used - pos);
    memcpy(b->array, &a->array[pos], (a->used - pos) * sizeof(Data));
    b->used = a->used - pos;
    a->used = pos;
    return b;
}

void mergeArrayList(ArrayList* a, ArrayList* b) {
    while (a->used + b->used > a->size) {
        a->size *= 2;
        a->array = realloc(a->array, a->size * sizeof(Data));
    }
    memcpy(&a->array[a->used], b->array, b->used * sizeof(Data));
    a->used += b->used;

    freeArrayList(b);
    free(b);
}

int main() {
    ArrayList arr;
    initArrayList(&arr, 1);

    Data d;
    for(int i = 0; i < 5; i++) {
        d.id = i;
        d.value = i * 1.0;
        insertArrayList(&arr, d);
    }

    printArrayList(&arr);

    ArrayList* arr2 = splitArrayList(&arr, 2);
    printArrayList(&arr);
    printArrayList(arr2);

    mergeArrayList(&arr, arr2);
    printArrayList(&arr);

    freeArrayList(&arr);

    return 0;
}
