def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"After iteration {i+1}: {arr}")

data = [64, 25, 12, 22, 11]
bubble_sort(data.copy())
