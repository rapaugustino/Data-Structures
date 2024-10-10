class Node:
    """
    A class used to represent a Node in a linked list.

    Attributes
    ----------
    data : any
        The data stored in the node.
    next : Node
        The next node in the linked list.
    """

    def __init__(self, data):
        """Initializes a node with data and sets the next node to None."""
        self.data = data
        self.next = None


class Stack:
    """
    A class used to represent a Stack using a linked list.

    Attributes
    ----------
    top : Node
        The top node of the stack.

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
        self.top = None
        self._size = 0

    def size(self):
        """Returns the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Checks if the stack is empty."""
        return self.top is None

    def push(self, item):
        """Adds an element to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

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
        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        return popped_node.data

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
        return self.top.data


# Testing the Stack class
stack = Stack()

# Test pushing elements
stack.push(1)
stack.push(2)
stack.push(3)

# Test stack content after pushes
current = stack.top
stack_content = []
while current:
    stack_content.append(current.data)
    current = current.next
print(stack_content)  # Expected: [3, 2, 1]

# Test peeking the top element
print(stack.peek())  # Expected: 3

# Test popping the top element
print(stack.pop())  # Expected: 3

# Test stack content after pop
current = stack.top
stack_content = []
while current:
    stack_content.append(current.data)
    current = current.next
print(stack_content)  # Expected: [2, 1]

# Test if stack is empty
print(stack.is_empty())  # Expected: False

# Test the size of the stack
print(stack.size()) # Expected: 2

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