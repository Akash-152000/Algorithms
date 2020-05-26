def reverse(arr,start,stop):
    if start<stop-1:
        arr[start],arr[stop-1]=arr[stop-1],arr[start]
        reverse(arr,start+1,stop-1)
    return arr
arr=[1,2,3,4,5,6,7]
start=0
stop=len(arr)
print(reverse(arr,start,stop))
