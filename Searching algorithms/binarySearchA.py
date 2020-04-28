def binarySearch(a,l,h,x):
    if h>=1:
        mid=(l+h)//2
        if a[mid]==x:
            return mid
        elif a[mid]>x:
            return binarySearch(a,l,mid+1,x)
        else:
            return binarySearch(a,mid,h,x)
    else:
        return -1



arr=list(map(int,input().split()))
arr.sort()
x=int(input("Search:"))
result=binarySearch(arr,0,len(arr)-1,x)
if result==-1:
    print("List is empty")
else:
    print("Answer:",result)
