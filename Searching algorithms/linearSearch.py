def linearSearch(li,size,findNum):
    for i in range(size):
        if findNum==li[i]:
            return i
    return -1
        
            
        


size=int(input("Enter the size of the list:"))
li=list(map(int,input().split()))
findNum=int(input("Enter the value you wanr to search:"))
result=linearSearch(li,size,findNum)
if result==-1:
    print("Element is not presemt in the array")
else:
    print("Element is present at index ",result)
