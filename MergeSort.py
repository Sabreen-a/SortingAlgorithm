def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Find the middle point and split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    
    # Compare each element and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # If there are remaining elements in left or right, add them
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

    
    
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

           
