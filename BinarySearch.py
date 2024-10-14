def binary_search(arr, search_value):
    """
    Perform a binary search to find the search_value in a sorted array.

    Args:
        arr (list): A list of sorted elements to search through.
        search_value (int/float/str): The value to search for in the array.

    Returns:
        bool: True if search_value is found in the array, False otherwise.
    """

    # Initialize the starting index of the search range
    first = 0
    # Initialize the ending index of the search range
    last = len(arr) - 1

    # Continue search while there is still a range to search
    while first <= last:
        # Calculate the middle index of the current range
        middle = (first + last) // 2

        # Check if the middle element is the search value
        if arr[middle] == search_value:
            return True
        # If search value is less than the middle element, adjust the range to the left half
        elif search_value < arr[middle]:
            last = middle - 1
        # If search value is greater than the middle element, adjust the range to the right half
        else:
            first = middle + 1

    # If the value was not found, return False
    return False


# Test the binary_search function with a sample sorted list
test_list = [1, 2, 4, 5, 6, 7, 8, 9]
# Print the result of searching for the value 8
print(binary_search(test_list, 8))