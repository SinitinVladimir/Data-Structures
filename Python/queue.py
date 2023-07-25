# Import the necessary modules
from collections import deque  # deque is a built-in Python module for a double-ended queue
from copy import deepcopy      # deepcopy is a function that creates a new copy of a complex object (like a list)

class Queue: 
    # The '__init__' method initializes the Queue object with an empty queue and a maximum size
    def __init__(self, max_size=None):
        self.queue = deque()    # Create an empty deque for the queue
        self.max_size = max_size # Set the maximum size of the queue

    # The 'enqueue' method adds an item to the end of the queue
    def enqueue(self, item):
        # Before adding the item, check if the queue is full
        if self.is_full():
            print("Queue is full. Can't enqueue.")
            return
        # If the queue is not full, add the item
        self.queue.append(item)

    # The 'dequeue' method removes an item from the front of the queue
    def dequeue(self):
        # Before removing the item, check if the queue is empty
        if self.is_empty():
            print("Queue is empty. Can't dequeue.")
            return
        # If the queue is not empty, remove the item from the front
        return self.queue.popleft()

    # The 'is_empty' method checks if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # The 'is_full' method checks if the queue is full
    def is_full(self):
        # If no maximum size is set, the queue can never be full
        if self.max_size is None:
            return False
        # If a maximum size is set, the queue is full if it reaches this size
        return len(self.queue) == self.max_size

    # The 'peek' method returns the item at the front of the queue without removing it
    def peek(self):
        # Check if the queue is empty before attempting to peek
        if self.is_empty():
            print("Queue is empty.")
            return
        # If the queue is not empty, return the front item
        return self.queue[0]

    # The 'size' method returns the number of items in the queue
    def size(self):
        return len(self.queue)

    # The 'clear' method removes all items from the queue
    def clear(self):
        self.queue.clear()

    # The 'contains' method checks if a certain item is in the queue
    def contains(self, item):
        return item in self.queue

    # The 'to_array' method converts the queue to a list
    def to_array(self):
        return list(self.queue)

    # The '__str__' method converts the queue to a string
    def __str__(self):
        return ', '.join(map(str, self.queue))

    # The 'resize' method changes the size of the queue
    def resize(self, new_size):
        if new_size < self.size():
            self.queue = deque(list(self.queue)[:new_size])
        self.max_size = new_size

    # The 'iterator' method returns an iterator for the queue
    def iterator(self):
        return iter(self.queue)

    # The 'clone' method creates a new copy of the queue
    def clone(self):
        new_queue = Queue(self.max_size)
        new_queue.queue = deepcopy(self.queue)
        return new_queue

# Now, let's test the queue
q = Queue(5)  # Create a new queue with maximum size 5
q.enqueue(10) # Add 10 to the queue
q.enqueue(20) # Add 20 to the queue
q.enqueue(30) # Add 30 to the queue
print(f"Queue: {q}") # Print the queue, should output: Queue: 10, 20, 30
print(f"Dequeued: {q.dequeue()}") # Remove the front item from the queue and print it, should output: Dequeued: 10
print(f"Queue after dequeue: {q}") # Print the queue after dequeue, should output: Queue after dequeue: 20, 30
print(f"Is queue empty?: {q.is_empty()}") # Check if the queue is empty, should output: Is queue empty?: False
print(f"Size of queue: {q.size()}") # Get the size of the queue, should output: Size of queue: 2
print(f"Peek: {q.peek()}") # Get the front item of the queue without removing it, should output: Peek: 20
print(f"Is queue full?: {q.is_full()}") # Check if the queue is full, should output: Is queue full?: False
q.enqueue(40) # Add 40 to the queue
q.enqueue(50) # Add 50 to the queue
print(f"Queue after enqueuing 40 and 50: {q}") # Print the queue, should output: Queue after enqueuing 40 and 50: 20, 30, 40, 50
print(f"Is queue full?: {q.is_full()}") # Check if the queue is full, should output: Is queue full?: True
print(f"Queue contains 20?: {q.contains(20)}") # Check if the queue contains 20, should output: Queue contains 20?: True
print(f"Queue contains 100?: {q.contains(100)}") # Check if the queue contains 100, should output: Queue contains 100?: False
q2 = q.clone() # Clone the queue
print(f"Cloned Queue: {q2}") # Print the cloned queue, should output: Cloned Queue: 20, 30, 40, 50
q.resize(3) # Resize the queue to 3
print(f"Resized Queue: {q}") # Print the resized queue, should output: Resized Queue: 20, 30, 40
q.clear() # Clear the queue
print(f"Queue after clear: {q}") # Print the queue after clear, should output: Queue after clear: 
print(f"Is queue empty?: {q.is_empty()}") # Check if the queue is empty, should output: Is queue empty?: True
print(f"Original queue (should be empty): {q}") # Print the original queue, should output: Original queue (should be empty): 
print(f"Cloned queue (should have 10, 20, 30, 40, 50): {q2}") # Print the cloned queue, should output: Cloned queue (should have 20, 30, 40, 50): 20, 30, 40, 50
for i in q2.iterator(): # Iterate over the cloned queue
    print(f"Iterating over cloned queue: {i}") # Print each item, should output: Iterating over cloned queue: 20, Iterating over cloned queue: 30, etc.
