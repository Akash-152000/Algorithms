

def prime_factors(x):
    li=[i for i in range(x+1)]
    li[0]=li[1]=0
    for i in range(2,x+1):
        if li[i]!=0:
            print("i",i)
            j=2
            while i*j<=x:
                print(i*j)
                li[i*j]=0
                print(li)
                j+=1
    return li
from math import sqrt
li=prime_factors(int(input()))
for ele in li:
    if ele==0:
        continue
    else:
        print(ele,end=" ")
