def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
        


def mergeSort(arr):
    mid=len(arr)//2
    if len(arr)==1:
        return arr
    else:
        left=mergeSort(arr[:mid])
        right=mergeSort(arr[mid:])
        return merge(left,right)


arr = [1,2,3,-1,3,-9]
print(mergeSort(arr))
