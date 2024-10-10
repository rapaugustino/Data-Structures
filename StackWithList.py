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
        Exception
            If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        Raises
        ------
        Exception
            If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]


# Testing the Stack class
stack = Stack()

# Test pushing elements
stack.push(1)
stack.push(2)
stack.push(3)

# Test stack content after pushes
print(stack.items)  # Expected: [1, 2, 3]

# Test peeking the top element
print(stack.peek())  # Expected: 3

# Test popping the top element
print(stack.pop())  # Expected: 3

# Test stack content after pop
print(stack.items)  # Expected: [1, 2]

# Test if stack is empty
print(stack.is_empty())  # Expected: False

# Test the size of the stack
print(stack.size())  # Expected: 2

# Test popping all elements to empty the stack
print(stack.pop())  # Expected: 2
print(stack.pop())  # Expected: 1

# Test if stack is empty after popping all elements
print(stack.is_empty())  # Expected: True

# Test the size of the stack after popping all elements
print(stack.size())  # Expected: 0

# Test popping from an empty stack (should raise an exception)
try:
    stack.pop()
except Exception as e:
    print(e)  # Expected: Exception("Stack is empty")

# Test peeking from an empty stack (should raise an exception)
try:
    stack.peek()
except Exception as e:
    print(e)  # Expected: Exception("Stack is empty")