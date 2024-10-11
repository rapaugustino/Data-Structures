class Queue:
    """
    A class representing a queue data structure using a list.

    Methods
    -------
    is_empty():
        Checks if the queue is empty.
    enqueue(item):
        Adds an item to the end of the queue.
    dequeue():
        Removes and returns the item from the front of the queue.
    size():
        Returns the number of items in the queue.
    peek():
        Returns the item at the front of the queue without removing it.
    display():
        Returns a list representation of the queue.
    """
    def __init__(self):
        """Initializes an empty queue."""
        self.queue = []

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns
        -------
        bool
            True if the queue is empty, False otherwise.
        """
        return self.queue == []

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.

        Parameters
        ----------
        item : any
            The item to be added to the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns
        -------
        any
            The item removed from the front of the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        """
        Returns the number of items in the queue.

        Returns
        -------
        int
            The number of items in the queue.
        """
        return len(self.queue)

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns
        -------
        any
            The item at the front of the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def display(self):
        """
        Returns a list representation of the queue.

        Returns
        -------
        list
            A list containing the items in the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self.queue
        else:
            return None

# Example usage of the Queue class
q = Queue()
q.enqueue(1)  # Adds 1 to the queue
q.enqueue(2)  # Adds 2 to the queue
q.enqueue(3)  # Adds 3 to the queue

# Display the current state of the queue
print(q.display())  # Output: [1, 2, 3]

# Peek at the front item of the queue
print(q.peek())  # Output: 1

# Get the size of the queue
print(q.size())  # Output: 3

# Check if the queue is empty
print(q.is_empty())  # Output: False

# Dequeue an item from the front of the queue
print(q.dequeue())  # Output: 1
