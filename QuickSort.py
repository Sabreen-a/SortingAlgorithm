def QuickSort(arr):
    if len(arr) == 0:  
        return []
    
    pivot = arr[0]
    smaller = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]  
    print(f'Pivot: {pivot}, Smaller: {smaller}, Greater: {greater}') 
    return QuickSort(smaller) + [pivot] + QuickSort(greater)

print(QuickSort([10, 2, 3, 4, 5]))
