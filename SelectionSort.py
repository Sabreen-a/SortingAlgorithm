def FindSmallest(arr):
    if(arr.len<1):
        return arr
    else:
        smaller=arr[0]
        smaller_indx=0
        for i in range(1,len(arr)):
            if arr[i]<smaller:
                smaller=arr[i]
                smaller_indx=i
                return smaller_indx
            

def SelectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smaller=FindSmallest(arr)
        newArr.append(arr.pop(smaller))
        return newArr
    
    arr=[10, 2, 3, 4, 5]
    print(SelectionSort(arr))