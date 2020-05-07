def partition(a,low,high):
    pivot=a[low]
    border=low
    for i in range(low,high+1):
        if a[i]<pivot:
            border+=1
            a[i],a[border]=a[border],a[i]
    a[border],a[low]=a[low],a[border]
    return border

def quicksort(a,low,high):
    if low<high:
        p=partition(a,low,high)
        quicksort(a,low,p-1)
        quicksort(a,p+1,high)
    return a
array=[6,3,2,8,22,55,333,11,8,2,10,98,1,44,109,33]
print(quicksort(array,0,len(array)-1))
