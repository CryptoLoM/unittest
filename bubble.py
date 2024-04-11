def bubbleSort(array):
    filtered_data = [x for x in array if isinstance(x, (int, float))]  # Filter out strings

    for item in filtered_data:
        if not isinstance(item, (int, float)):
            raise TypeError("List contains non-integer and non-float elements.")

    if not filtered_data:
        print('Nothing to sort. The list returns with the initial view:', array)
        return array

    is_sorted = all(filtered_data[i] <= filtered_data[i + 1] for i in range(len(filtered_data) - 1))

    if is_sorted:
        print("The list is already sorted:", filtered_data)
        return filtered_data

    # Bubble sort algorithm
    for i in range(len(filtered_data) - 1):
        for j in range(0, len(filtered_data) - i - 1):
            if filtered_data[j] > filtered_data[j + 1]:
                filtered_data[j], filtered_data[j + 1] = filtered_data[j + 1], filtered_data[j]  # Swap elements
    return filtered_data

