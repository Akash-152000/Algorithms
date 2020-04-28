import math
def jump(a,n,x):
    step=int(math.sqrt(n))
    for i in range(0,n,step):
        if a[i]==x:
            return i
        elif a[i]<x:
            prev=i
            continue
        else:
            for j in range(prev,i):
                if a[j]==x:
                    return j


arr=list(map(int,input().split()))
arr.sort()
x=int(input())
if len(arr)%2==0:
    result=jump(arr,len(arr),x)
else:
    result=jump(arr,len(arr)-1,x)

if result==None:
    if arr[len(arr)-1]==x:
        print(len(arr))
    else:
        print("Not present")
else:
    print(result)
