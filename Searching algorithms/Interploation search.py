n=[10, 12, 13, 16, 18, 19, 20, 21,22, 23, 24, 33, 35, 42, 47]
x=int(input("Enter the element to be searched: "))
lo=0
hi=len(n)-1
pos=0
while x>=n[lo] and x<=n[hi]:
    if lo==hi:
        if n[lo] == x:  
                pos=lo
                break
        else:
            pos=-1
            break
    
    else:
        pos  = lo + int(((float(hi - lo) / ( n[hi] - n[lo])) * ( x - n[lo])))
        if n[pos]==x:
            break
        elif n[pos]<x:
            lo=pos+1
        else:
            hi=pos-1


print(pos)
