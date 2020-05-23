def binarySearch(arr,l,h,x):
    if h>=l:
        mid=int(l+(h-l)/2)
        if arr[mid]==x:
            return mid
        if arr[mid]>x:
            return binarySearch(arr,l,mid-1,x)
        
        return binarySearch(arr,mid+1,h,x)
    return -1

def search(arr,n,x):
    if arr[0]==x:
        return 0
    i=1
    while i<n and arr[i]<=x:
        i=i*2
    return binarySearch(arr,i/2,min(i,n),x)


arr=[2, 3, 4, 10, 40]
n=len(arr)
x=10

print(x,"is at index",search(arr,n,x))
