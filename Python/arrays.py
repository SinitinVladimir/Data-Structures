# 'class' is a reserved keyword in Python that is used to define a class
# 'Data' is the name of the class
class Data:
    # 'def' is a reserved keyword used to define functions or methods
    # '__init__' is a special method in Python classes, known as a constructor. It is automatically called when a new object of the class is created.
    def __init__(self, id, value):
        # 'self' is a reference to the instance of the class and is used to access variables and methods associated with that instance
        # 'self.id' and 'self.value' are instance variables
        self.id = id
        self.value = value

    # '__str__' is a special method that returns a string representation of the object
    def __str__(self):
        # 'return' is a keyword that is used to end the execution of a function and returns the result
        return f'ID: {self.id}, Value: {self.value:.2f}'

# 'def' is used again to define a new function 'print_array'
def print_array(arr):
    # 'for' is a keyword for looping over a sequence such as a list
    # 'in' is a keyword used to check if a value exists in a sequence or to iterate through a sequence
    for a in arr:
        print(a)
    print()

# Function to insert an element at a specific position in the array
def insert_element(arr, pos, val):
    # 'if' is a keyword for making a condition, 'or' is a logical operator that combines conditional statements
    if pos < 0 or pos > len(arr):
        print("Invalid position for insertion.")
        return -1
    arr.insert(pos, val)
    return 0

# Function to delete an element from a specific position in the array
def delete_element(arr, pos):
    if pos < 0 or pos >= len(arr):
        print("Invalid position for deletion.")
        return -1
    del arr[pos]
    return 0

# Function to concatenate (join together) two arrays
def concatenate_arrays(arr1, arr2):
    # '+' is an operator that can be used to concatenate lists
    return arr1 + arr2

def main():
    arr = []
    size = int(input("Enter the size of the array: "))
    if size < 1 or size > 100:
        print("Invalid array size. Enter a size between 1 and 100.")
        return

    print("Enter the elements of the array (id and value): ")
    for i in range(size):
        id, value = map(float, input().split())
        arr.append(Data(int(id), value))

    print("Original array: ")
    print_array(arr)

    pos, id, value = map(float, input("Enter the position and value to insert (id and value): ").split())
    if insert_element(arr, int(pos), Data(int(id), value)) == -1:
        return
    print(f"Array after inserting ID: {int(id)}, Value: {value:.2f} at position {int(pos)}: ")
    print_array(arr)

    pos = int(input("Enter the position to delete: "))
    if delete_element(arr, pos) == -1:
        return
    print(f"Array after deleting element at position {pos}: ")
    print_array(arr) 

    size2 = int(input("Enter the size of the second array for concatenation: "))
    if size2 < 1 or size2 > 50:
        print("Invalid array size. Enter a size between 1 and 50.")
        return

    arr2 = []
    print("Enter the elements of the second array for concatenation (id and value): ")
    for i in range(size2):
        id, value = map(float, input().split())
        arr2.append(Data(int(id), value))

    result = concatenate_arrays(arr, arr2)
    print("Array after concatenation: ")
    print_array(result)

    split_index = int(input("Enter the position to split the array: "))
    if split_index < 0 or split_index > len(result):
        print("Invalid position for splitting the array.")
        return

    arr1 = result[:split_index]
    arr2 = result[split_index:]
    print("Array after splitting: ")
    print_array(arr1)
    print_array(arr2)

if __name__ == '__main__':
    # 'main' is the name of the function to be executed
    main()
