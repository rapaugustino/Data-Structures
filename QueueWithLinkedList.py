class Node:
    def __init__(self, data):
        """
        Initialize a new node with the given data and no next node.

        :param data: The data to be held by the node.
        """
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        """
        Initialize an empty queue with front and rear set to None.
        """
        self.front = None
        self.rear = None

    def is_empty(self):
        """
        Check if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return self.front is None

    def enqueue(self, data):
        """
        Add a new node with the given data to the end of the queue.

        :param data: The data to be added to the queue.
        """
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Remove and return the data from the front of the queue.

        :return: The data from the front of the queue.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

    def peek(self):
        """
        Return the data from the front of the queue without removing it.

        :return: The data from the front of the queue.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data

    def size(self):
        """
        Return the number of elements in the queue.

        :return: The number of elements in the queue.
        """
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def clear(self):
        """
        Remove all elements from the queue.
        """
        self.front = self.rear = None


# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.dequeue()  # Output: 10
queue.peek()  # Output: 20
queue.size()  # Output: 1
queue.clear()
queue.is_empty()  # Output: True