import time

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]  # better pivot
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] <= pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Sorted data (worst-case for Quick Sort)
data = list(range(10000))

arr1 = data.copy()
start = time.time()
quick_sort(arr1, 0, len(arr1)-1)
end = time.time()
print("Quick Sort Time on sorted data:", end - start)

arr2 = data.copy()
start = time.time()
merge_sort(arr2)
end = time.time()
print("Merge Sort Time on sorted data:", end - start)
