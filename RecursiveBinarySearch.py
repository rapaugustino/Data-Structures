def recursive_binary_search(array, target):
    """
    Perform a binary search using recursion.

    :param array: List of elements to search through.
    :param target: The element to be searched for.
    :return: True if the target is found in the array, otherwise False.
    """
    if len(array) == 0:
        # Base case: if the array is empty, the target is not found
        return False
    else:
        # Calculate the middle index of the array
        middle = len(array) // 2

        # If the middle element is the target, return True
        if array[middle] == target:
            return True

        # If the target is less than the middle element, search the left subarray
        elif target < array[middle]:
            return recursive_binary_search(array[:middle], target)

        # If the target is greater than the middle element, search the right subarray
        else:
            return recursive_binary_search(array[middle + 1:], target)


# Example usage of the recursive_binary_search function
print(recursive_binary_search([1, 5, 8, 9, 15, 20, 70, 72], 5))
