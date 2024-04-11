import sys
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

def main(data_from_test=None):
    try:
        if data_from_test is None:
            input_data = sys.stdin.readline() # повертає рядок
            data_list = data_manip(input_data) # перетворює рядок у список чисел
        else:
            data_list = data_from_test

        # Перевірка на наявність рядкових значень
        if any(isinstance(x, str) for x in data_list):
            sys.stderr.write(f"Values contain strings\n")
            return 1

        # Видалення рядкових значень
        data_list = [x for x in data_list if isinstance(x, (int, float))]


        # Сортування списку
        sorted_numbers = bubbleSort(data_list)

        # Показ відсортованого списку
        sys.stdout.write(' '.join(map(str, sorted_numbers)))

        return 0, sorted_numbers
    except Exception:
        sys.stderr.write(f"Values are invalid\n")
        return 1

def fail(data_test=None):
    try:
        if data_test is None:
           input_data = sys.stdin.readline() # повертає рядок
           data_l = data_manip(input_data) # перетворює рядок у список чисел
        else:
           data_l = data_test

        data_l = [x for x in data_l if isinstance(x, (int, float))]

        if not data_l:
            sys.stderr.write(f"Values are invalid\n")
            return 2
    except Exception:
        sys.stderr.write(f"Values are invalid\n")
        return 2
