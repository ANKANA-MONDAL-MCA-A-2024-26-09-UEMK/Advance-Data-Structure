def display_level_order_array(arr):
    for val in arr:
        if val is not None:
            print(val, end=" ")

arr = [1, 2, 3, None, 5, 6, 7]
display_level_order_array(arr)
