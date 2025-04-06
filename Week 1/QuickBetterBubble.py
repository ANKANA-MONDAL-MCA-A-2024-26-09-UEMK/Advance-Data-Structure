import time

from random import randint

data = [randint(1, 1000) for _ in range(1000)]

# Bubble Sort Timing
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] <= pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# Timing Bubble Sort
arr1 = data.copy()
start = time.time()
bubble_sort(arr1)
end = time.time()
print("Bubble Sort Time:", end - start)

# Timing Quick Sort
arr2 = data.copy()
start = time.time()
quick_sort(arr2, 0, len(arr2)-1)
end = time.time()
print("Quick Sort Time:", end - start)
