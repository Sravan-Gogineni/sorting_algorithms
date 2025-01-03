def selection_sort(array):
    current_small = array[0]
    i = 1
    j = 0
    index = 0
    while j < len(array):
        current_small = array[j]
        while i < len(array):
            if array[i] < current_small:
                current_small = array[i]
                index = i
            i = i + 1
        temp = array[j]
        array[j] = current_small
        array[index] = temp
        j = j + 1
        i = j + 1
    return array

array = [2, 6, 3, 8, 4, 1, 9, 5, 7]
sorted_array = selection_sort(array)
print(sorted_array)