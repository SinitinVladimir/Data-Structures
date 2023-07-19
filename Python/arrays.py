# Define a class 'Data' to store id and value together
class Data:
    # Initialization function to set id and value when a new object is created
    def __init__(self, id, value):
        self.id = id
        self.value = value

    # Function to convert the Data object to a string for printing
    def __str__(self):
        return f'ID: {self.id}, Value: {self.value:.2f}'


# Function to print the entire array
def print_array(arr):
    # Loop through each element in the array
    for a in arr:
        # Print the element
        print(a)
    # Print a newline
    print()


# Function to insert an element at a specific position in the array
def insert_element(arr, pos, val):
    # Check if the position is valid
    if pos < 1 or pos > len(arr) + 1:
        # If not, print an error message
        print("Invalid position for insertion.")
        return -1
    # Insert the element at the given position
    arr.insert(pos - 1, val)
    return 0


# Function to delete an element from a specific position in the array
def delete_element(arr, pos):
    # Check if the position is valid
    if pos < 1 or pos > len(arr):
        # If not, print an error message
        print("Invalid position for deletion.")
        return -1
    # Delete the element at the given position
    del arr[pos - 1]
    return 0


# Function to concatenate (join together) two arrays
def concatenate_arrays(arr1, arr2):
    return arr1 + arr2


# The main function where the program starts
def main():
    # Create an empty array
    arr = []
    # Ask the user for the size of the array
    size = int(input("Enter the size of the array: "))
    # Check if the size is within the allowed range
    if size < 1 or size > 100:
        # If not, print an error message
        print("Invalid array size. Enter a size between 1 and 100.")
        return

    # Ask the user to input the elements of the array
    print("Enter the elements of the array (id and value): ")
    for i in range(size):
        id, value = map(float, input().split())
        # Add each element to the array
        arr.append(Data(int(id), value))

    # Print the original array
    print("Original array: ")
    print_array(arr)

    # Ask the user to input the position and value to insert
    pos, id, value = map(float, input("Enter the position and value to insert (id and value): ").split())
    # Attempt to insert the element
    if insert_element(arr, int(pos), Data(int(id), value)) == -1:
        # If the insertion failed, end the program
        return
    # Print the array after the insertion
    print(f"Array after inserting ID: {int(id)}, Value: {value:.2f} at position {int(pos)}: ")
    print_array(arr)

    # Ask the user to input the position to delete
    pos = int(input("Enter the position to delete: "))
    # Attempt to delete the element
    if delete_element(arr, pos) == -1:
        # If the deletion failed, end the program
        return
    # Print the array after the deletion
    print(f"Array after deleting element at position {pos}: ")
    print_array(arr)

    # Ask the user for the size of the second array for concatenation
    size2 = int(input("Enter the size of the second array for concatenation: "))
    # Check if the size is within the allowed range
    if size2 < 1 or size2 > 50:
        # If not, print an error message
        print("Invalid array size. Enter a size between 1 and 50.")
        return

    # Create the second array
    arr2 = []
    # Ask the user to input the elements of the second array
    print("Enter the elements of the second array for concatenation (id and value): ")
    for i in range(size2):
        id, value = map(float, input().split())
        # Add each element to the second array
        arr2.append(Data(int(id), value))

    # Concatenate the two arrays
    result = concatenate_arrays(arr, arr2)
    # Print the array after concatenation
    print("Array after concatenation: ")
    print_array(result)

    # Ask the user to input the position to split the array
    split_index = int(input("Enter the position to split the array: "))
    # Check if the position is within the allowed range
    if split_index < 1 or split_index > len(result):
        # If not, print an error message
        print("Invalid position for splitting the array.")
        return

    # Split the array at the given position
    arr1 = result[:split_index]
    arr2 = result[split_index:]
    # Print the arrays after splitting
    print("Array after splitting: ")
    print_array(arr1)
    print_array(arr2)


# Run the main function when the script is executed
if __name__ == '__main__':
    main()
