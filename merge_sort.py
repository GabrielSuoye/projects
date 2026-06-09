def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Divide; split array into two from the midpoint
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer; Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare and merge into sorted array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append any leftover elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


unsorted_data = [12, 34, 3, 17, 2, 100, 89, 5]
print(f"Original Array: {unsorted_data}")

sorted_data = merge_sort(unsorted_data)
print(f"Sorted Array: {sorted_data}")
