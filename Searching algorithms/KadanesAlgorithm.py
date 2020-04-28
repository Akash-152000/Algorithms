def kadane(a,n):
    max_ele=max_global=a[0]
    for i in range(1,n):
        max_ele=max(a[i],max_ele+a[i])
        if max_ele>max_global:
            max_global=max_ele
    return max_global
size=int(input("Enter the size of the array:"))
arr=list(map(int,input().split()))
print(kadane(arr,size))
