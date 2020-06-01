##With recursion

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

'''
##Without recursion
def mergeSort(array):
    if len(array)>1:
        mid=len(array)//2
        left=array[:mid]
        right=array[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i<len(left) and j <len(right):
            if left[i]<right[j]:
                array[k]=left[i]
                i+=1
                k+=1
            else:
                array[k]=right[j]
                j+=1
                k+=1
        while i<len(left):                     
            array[k]=left[i]
            i+=1
            k+=1
        while j<len(right):                     
            array[k]=right[j]
            j+=1
            k+=1

arr = [1,2,3,-1,3,-9]
mergeSort(arr)
print(arr)
'''
