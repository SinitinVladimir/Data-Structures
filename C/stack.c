#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Define the stack structure
typedef struct {
    int top;
    unsigned capacity;
    int* array;
} Stack;

// Function to create a stack of a given capacity
Stack* createStack(unsigned capacity) {
    Stack* stack = (Stack*) malloc(sizeof(Stack)); // Allocate memory for the stack structure
    stack->capacity = capacity; // Set the capacity of the stack
    stack->top = -1; // Initialize the top of the stack to -1, indicating that the stack is empty
    stack->array = (int*) malloc(stack->capacity * sizeof(int)); // Allocate memory for the array that will hold the stack's elements
    return stack; // Return the created stack
}

// Function to check if the stack is full
int isFull(Stack* stack) {
    return stack->top == stack->capacity - 1; // The stack is full when the top index equals the last index of the stack's array
}

// Function to check if the stack is empty
int isEmpty(Stack* stack) {
    return stack->top == -1; // The stack is empty when the top index is -1
}

// Function to add an item to the top of the stack
void push(Stack* stack, int item) {
    if (isFull(stack)) // If the stack is full, return without doing anything
        return;
    stack->array[++stack->top] = item; // Increment the top index and add the item to the new top of the stack
}

// Function to remove and return the item from the top of the stack
int pop(Stack* stack) {
    if (isEmpty(stack)) // If the stack is empty, return the smallest possible integer
        return INT_MIN;
    return stack->array[stack->top--]; // Return the top item of the stack and decrement the top index
}

// Function to return the item at the top of the stack without removing it
int peek(Stack* stack) {
    if (isEmpty(stack)) // If the stack is empty, return the smallest possible integer
        return INT_MIN;
    return stack->array[stack->top]; // Return the top item of the stack
}

// Function to free the memory used by the stack
void freeStack(Stack* stack) {
    free(stack->array); // Free the memory allocated for the stack's storage
    free(stack); // Free the memory allocated for the stack structure
}

// Main function to test the stack operations
int main() {
    Stack* stack = createStack(100); // Create a stack with capacity 100

    push(stack, 10); // Push 10 to the stack
    push(stack, 20); // Push 20 to the stack
    push(stack, 30); // Push 30 to the stack

    printf("%d popped from stack\n", pop(stack)); // Pop the top item from the stack and print it

    printf("Top element is %d\n", peek(stack)); // Print the top element of the stack

    printf("Stack is empty: %s\n", isEmpty(stack)?"true":"false"); // Check if the stack is empty

    printf("Stack is full: %s\n", isFull(stack)?"true":"false"); // Check if the stack is full

    freeStack(stack); // Free the memory used by the stack when done

    return 0;
}
