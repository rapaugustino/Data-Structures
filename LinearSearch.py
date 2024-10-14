def linear_search(arr, x):
    """
    Performs a linear search to find an element in a list.

    Parameters:
    arr (list): The list in which to search for the element.
    x: The element to be searched for in the list.

    Returns:
    bool: True if the element is found, False otherwise.
    """
    # Iterate over each index in the array
    for i in range(len(arr)):
        # Check if the current element is equal to the target element
        if arr[i] == x:
            # Return True if the element is found
            return True
    # Return False if the element is not found after checking all elements
    return False


# Define a list of elements to be searched
test_list = [1, 4, 5, 6, 1, 8, 9]

# Perform a linear search for the element '8' in the test_list and print the result
print(linear_search(test_list, 8))  # Output: True
