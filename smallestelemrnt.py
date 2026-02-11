arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

n = len(arr)

# Bubble Sort (manual sorting)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# kth smallest element
print(arr[k-1])
