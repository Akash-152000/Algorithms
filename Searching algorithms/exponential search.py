def search(arr,n,x):
    if arr[0]==x:
        return 0
    i=1
    while i<n and arr[i]<=x:
        i=i*2
    


arr=[2, 3, 4, 10, 40]
n=len(arr)
x=10

print(x,"is at index",search(arr,n,x))
