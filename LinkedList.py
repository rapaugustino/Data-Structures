class Node:
    """
    A class used to represent a Node in a linked list.

    Attributes
    ----------
    data : any
        The data stored in the node.
    next : Node or None
        The reference to the next node in the linked list.

    Methods
    -------
    __init__(self, data):
        Initializes a new node with the given data and sets the next pointer to None.
    """

    def __init__(self, data):
        """
        Initialize a new node with given data and set the next pointer to None.

        :param data: The data to be stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A class used to represent a singly linked list.

    Attributes
    ----------
    head : Node or None
        The first node in the linked list.
    tail : Node or None
        The last node in the linked list.

    Methods
    -------
    __init__(self):
        Initializes an empty linked list with head and tail set to None.

    is_empty(self):
        Checks if the linked list is empty.

    add_at_end(self, data):
        Adds a new node with the given data at the end of the linked list.

    add_at_start(self, data):
        Adds a new node with the given data at the start of the linked list.

    insert_after(self, prev_data, data):
        Inserts a new node with the given data after the node with prev_data.

    delete_node(self, key):
        Deletes the first node with the given key from the linked list.

    delete_at_position(self, position):
        Deletes the node at the given position in the linked list.

    search(self, key):
        Searches for the first node with the given key in the linked list.

    search_by_data(self, data):
        Searches for any node with the given data in the linked list.

    display(self):
        Displays the contents of the linked list.
    """

    def __init__(self):
        """Initialize an empty linked list with head and tail set to None."""
        self.head = None
        self.tail = None

    def is_empty(self):
        """
        Check if the linked list is empty.

        :return: True if the linked list is empty, False otherwise.
        """
        return self.head is None

    def add_at_end(self, data):
        """
        Add a new node with the given data at the end of the linked list.

        :param data: The data to be added to the new node.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_at_start(self, data):
        """
        Add a new node with the given data at the start of the linked list.

        :param data: The data to be added to the new node.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, prev_data, data):
        """
        Insert a new node with the given data after the node with prev_data.

        :param prev_data: The data of the node after which the new node should be inserted.
        :param data: The data to be added to the new node.
        """
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            print(f"Node with data {prev_data} not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        if current == self.tail:
            self.tail = new_node

    def delete_node(self, key):
        """
        Delete the first node with the given key from the linked list.

        :param key: The data of the node to be deleted.
        """
        current = self.head
        if current and current.data == key:
            self.head = current.next
            if self.head is None:
                self.tail = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print(f"Node with key {key} not found.")
            return
        prev.next = current.next
        if current == self.tail:
            self.tail = prev

    def delete_at_position(self, position):
        """
        Delete the node at the given position in the linked list.

        :param position: The position of the node to be deleted (0-based index).
        """
        if self.is_empty():
            print("Linked list is empty.")
            return
        current = self.head
        if position == 0:
            self.head = current.next
            if self.head is None:
                self.tail = None
            return
        prev = None
        for _ in range(position):
            prev = current
            current = current.next
            if current is None:
                print("Position is out of range.")
                return
        prev.next = current.next
        if current == self.tail:
            self.tail = prev

    def search(self, key):
        """
        Search for the first node with the given key in the linked list.

        :param key: The data to search for.
        :return: The position of the node with the given key, or -1 if not found.
        """
        if self.is_empty():
            print("Linked list is empty.")
            return -1
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1  # if the key is not found

    def search_by_data(self, data):
        """
        Search for any node with the given data in the linked list.

        :param data: The data to search for.
        :return: True if the data is found, False otherwise.
        """
        if self.is_empty():
            print("Linked list is empty.")
            return False
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """
        Display the contents of the linked list.
        """
        current = self.head
        if self.is_empty():
            print("Linked list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage and additional testing
linked_list = LinkedList()
linked_list.add_at_end(3)
linked_list.add_at_end(5)
linked_list.add_at_start(2)
linked_list.insert_after(3, 4)
linked_list.display()  # Output: 2 -> 3 -> 4 -> 5 -> None

# Test search
position_5 = linked_list.search(5)
print(position_5)  # Output: 3
position_10 = linked_list.search(10)
print(position_10)  # Output: -1

# Test search_by_data
found_3 = linked_list.search_by_data(3)
print(found_3)  # Output: True
found_5 = linked_list.search_by_data(5)
print(found_5)  # Output: True
found_10 = linked_list.search_by_data(10)
print(found_10)  # Output: False

# Test delete_node
linked_list.delete_node(3)
linked_list.display()  # Output: 2 -> 4 -> 5 -> None

# Test delete_at_position
linked_list.delete_at_position(1)
linked_list.display()  # Output: 2 -> 5 -> None

# Additional tests
linked_list.add_at_end(6)
linked_list.add_at_end(7)
linked_list.display()  # Output: 2 -> 5 -> 6 -> 7 -> None
linked_list.delete_at_position(0)
linked_list.display()  # Output: 5 -> 6 -> 7 -> None
linked_list.delete_at_position(2)
linked_list.display()  # Output: 5 -> 6 -> None
linked_list.delete_node(6)
linked_list.display()  # Output: 5 -> None
linked_list.delete_node(5)
linked_list.display()  # Output: Linked list is empty.