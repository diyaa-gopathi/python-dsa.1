def bubble_sort(arr):
    n = len(arr)
    for a in range(n - 1):
        for b in range(n - 1 - a):
            if arr[b] > arr[b + 1]:
                arr[b], arr[b + 1] = arr[b + 1], arr[b]
arr = [5, 3, 8, 4, 2]
bubble_sort(arr)
print(" the sorted array is:", arr)