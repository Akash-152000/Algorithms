def sum_seq(arr,n):
    if n==0:
        return 0
    else:
        return sum_seq(arr,n-1)+arr[n-1]
        
arr=[1,2,3,4,5]
n=len(arr)
print(sum_seq(arr,n))
