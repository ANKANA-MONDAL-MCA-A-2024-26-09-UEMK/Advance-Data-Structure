def merge_sort(arr, depth=0):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, depth+1)
        merge_sort(R, depth+1)

        i = j = k = 0

        # Merging the arrays
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking for remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        print(f"{'  '*depth}After merge: {arr}")

data = [64, 25, 12, 22, 11]
merge_sort(data.copy())
