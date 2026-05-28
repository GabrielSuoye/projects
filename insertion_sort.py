def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


B = [23, 15, 10, 44, 9, 17]
print(f"Unsorted data: {B}")

sorted_B = insertion_sort(B)
print(f"Sorted data: {sorted_B}")
