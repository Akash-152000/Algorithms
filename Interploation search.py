def interpolation(n,x,lo,hi):
    pos=lo-int((x-n[lo])*(lo-hi)/(n[hi]-n[lo]))
    if pos==x:
        return n.index(pos)
    elif x<pos:
        hi=pos
        interpolation(n,x,lo,hi)
    else:
        lo=pos
        interpolation(n,x,lo,hi)


n=list(map(int,input().split()))
x=int(input("Enter the element to be searched: "))
lo=0
hi=len(n)-1
print("Elment is at the index:",interpolation(n,x,lo,hi))
