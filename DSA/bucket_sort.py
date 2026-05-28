def bucket_sort(arr):
    num_buckets = len(arr)
    if num_buckets <= 1:
        return arr

    buckets = [[] for _ in range(num_buckets)]

    for value in arr:
        bucket_index = int(value * num_buckets)
        if bucket_index >= num_buckets:
            bucket_index = num_buckets - 1
        buckets[bucket_index].append(value)

    sorted_index = 0
    for bucket in buckets:
        bucket.sort()  # Using Python's built-in Timesort
        for value in bucket:
            arr[sorted_index] = value
            sorted_index += 1

    return arr


Q = [0.42, 0.32, 0.75, 0.45, 0.12, 0.37]
print(f"Unsorted data: {Q}")

sorted_Q = bucket_sort(Q)
print(f"Sorted data: {sorted_Q}")
