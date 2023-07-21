# Define a class named 'Stack'
class Stack:
    # 'init' method is the constructor of the class and is called when a new object is created
    def __init__(self):
        # Define an empty list to use as the underlying data structure for the stack
        self.stack = []

    # Method to add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # Method to remove and return the item from the top of the stack
    def pop(self):
        # Check if the stack is not empty before attempting to remove an item
        if not self.is_empty():
            return self.stack.pop()
        # If the stack is empty, return None
        return None

    # Method to view the item at the top of the stack without removing it
    def peek(self):
        # Check if the stack is not empty before attempting to view an item
        if not self.is_empty():
            return self.stack[-1]
        # If the stack is empty, return None
        return None

    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Method to get the number of items in the stack
    def size(self):
        return len(self.stack)

    # Method to remove all items from the stack
    def clear(self):
        self.stack = []

    # Method to check if a specific item is in the stack
    def contains(self, item):
        return item in self.stack

    # Method to create a copy of the stack
    def clone(self):
        new_stack = Stack()
        new_stack.stack = self.stack.copy()
        return new_stack

    # Method to convert the stack to a list
    def to_array(self):
        return self.stack.copy()

    # Method to convert the stack to a string
    def __str__(self):
        return str(self.stack)

    # Method to combine two stacks into a single stack
    def merge(self, stack2):
        self.stack += stack2.to_array()

    # Method to reverse the order of items in the stack
    def reverse(self):
        self.stack.reverse()

    # Method to swap the positions of the top two items in the stack
    def swap(self):
        if len(self.stack) >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    # Method to find the minimum item in the stack
    def min(self):
        if not self.is_empty():
            return min(self.stack)
        return None

    # Method to find the maximum item in the stack
    def max(self):
        if not self.is_empty():
            return max(self.stack)
        return None

    # Method to create an iterator for the stack
    def iterator(self):
        return iter(self.stack)

    # Method to find the position of a specific item in the stack
    def index_of(self, item):
        if item in self.stack:
            return self.stack.index(item)
        return -1

    # Method to change the size of the stack
    def resize(self, new_size):
        if new_size < self.size():
            self.stack = self.stack[:new_size]
        else:
            self.stack += [None] * (new_size - self.size())

    # Method to reduce the size of the stack to fit the number of items it contains
    def trim_to_size(self):
        self.stack = self.stack[:self.size()]

    # Method to modify an item at a specific position in the stack
    def set_at(self, index, item):
        if 0 <= index < self.size():
            self.stack[index] = item


# Sample usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(f"Stack: {s}") # Stack: [10, 20, 30]
print(f"Pop: {s.pop()}") # Pop: 30
print(f"Stack: {s}") # Stack: [10, 20]
print(f"Peek: {s.peek()}") # Peek: 20
print(f"IsEmpty: {s.is_empty()}") # IsEmpty: False
print(f"Size: {s.size()}") # Size: 2
s2 = s.clone()
print(f"Cloned Stack: {s2}") # Cloned Stack: [10, 20]
s2.push(40)
print(f"Stack: {s}") # Stack: [10, 20]
print(f"Cloned Stack: {s2}") # Cloned Stack: [10, 20, 40]
s.merge(s2)
print(f"Merged Stack: {s}") # Merged Stack: [10, 20, 10, 20, 40]
s.reverse()
print(f"Reversed Stack: {s}") # Reversed Stack: [40, 20, 10, 20, 10]
s.swap()
print(f"Swapped Stack: {s}") # Swapped Stack: [20, 40, 10, 20, 10]
print(f"Min: {s.min()}") # Min: 10
print(f"Max: {s.max()}") # Max: 40
print(f"Contains 30: {s.contains(30)}") # Contains 30: False
print(f"Contains 40: {s.contains(40)}") # Contains 40: True
print(f"IndexOf 40: {s.index_of(40)}") # IndexOf 40: 1
s.resize(3)
print(f"Resized Stack: {s}") # Resized Stack: [20, 40, 10]
s.trim_to_size()
print(f"Trimmed Stack: {s}") # Trimmed Stack: [20, 40, 10]
s.set_at(1, 50)
print(f"SetAt Stack: {s}") # SetAt Stack: [20, 50, 10]
s.clear()
print(f"Cleared Stack: {s}") # Cleared Stack: []
