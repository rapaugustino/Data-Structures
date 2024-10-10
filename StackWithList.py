class StackEmptyException(Exception):
    """Custom exception to be raised when stack-related operations fail due to the stack being empty."""
    pass


class Stack:
    """
    A class used to represent a Stack.

    Attributes
    ----------
    items : list
        a list to store stack elements

    Methods
    -------
    size():
        Returns the number of elements in the stack.
    is_empty():
        Checks if the stack is empty.
    push(item):
        Adds an element to the top of the stack.
    pop():
        Removes and returns the top element of the stack.
    peek():
        Returns the top element of the stack without removing it.
    """

    def __init__(self):
        """Initializes an empty stack."""
        self.items = []

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.items)

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Adds an element to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the top element of the stack.

        Raises
        ------
        StackEmptyException
            If the stack is empty.
        """
        if self.is_empty():
            raise StackEmptyException("Stack is empty")
        return self.items.pop()

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        Raises
        ------
        StackEmptyException
            If the stack is empty.
        """
        if self.is_empty():
            raise StackEmptyException("Stack is empty")
        return self.items[-1]