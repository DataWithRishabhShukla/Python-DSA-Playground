def count_non_repeated_elements(arr):
    if not arr:
        return 0

    # Sort the array
    arr.sort()

    non_repeated_count = 0
    n = len(arr)

    # Check for non-repeated elements
    for i in range(n):
        if (i == 0 and arr[i] != arr[i + 1]) or \
           (i == n - 1 and arr[i] != arr[i - 1]) or \
           (0 < i < n - 1 and arr[i] != arr[i - 1] and arr[i] != arr[i + 1]):
            non_repeated_count += 1

    return non_repeated_count

# Test the function with an example array
arr = [1, 2, 3, 2, 3, 4, 5, 4, 6, 7]
result = count_non_repeated_elements(arr)
print("Count of non-repeated elements:", result)
