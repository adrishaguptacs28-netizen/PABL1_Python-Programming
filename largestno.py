arr = [1, 8, 7, 56, 90]

largest = arr[0]   # assume first element is largest

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)
