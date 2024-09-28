def QuickSort(arr):
    if len(arr) == 0:  
        return []
    
    pivot = arr[0]
    smaller = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]  
    #print(f'Pivot: {pivot}, Smaller: {smaller}, Greater: {greater}') 
    print(QuickSort(smaller) + [pivot] + QuickSort(greater)) 
    return QuickSort(smaller) + [pivot] + QuickSort(greater)

print(QuickSort([10, 2, 3, 4, 5]))

#https://jamesg.blog/2024/06/16/python-memory-usage/ for visualize time complexity >mprof run QuickSort.py mprof plot

