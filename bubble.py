def bubbleSort(array):
    # Test for types
    for el in array:
        if not isinstance(el, int):
            raise TypeError('Unexpected types')

    n = len(array)

    # Sorting algorithm
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]  # Swap elements
    return array
