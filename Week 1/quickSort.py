def quick_sort(arr, low, high, depth=0):
    if low < high:
        pi = partition(arr, low, high)
        print(f"{'  '*depth}After partition at index {pi}: {arr}")
        quick_sort(arr, low, pi-1, depth+1)
        quick_sort(arr, pi+1, high, depth+1)

def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] <= pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

data = [64, 25, 12, 22, 11]
quick_sort(data.copy(), 0, len(data)-1)
