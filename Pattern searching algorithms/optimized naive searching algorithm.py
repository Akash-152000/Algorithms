def naive(text,pat):
    n=len(text)
    m=len(pat)
    i=0
    while i<=n-m:
        for j in range(m):
            if text[i+j]!=pat[j]:
                break
            j+=1
        if j==m:
            print("Pattern is at index",i)
            i=i+m
        elif j==0:
            i=i+1
        else:
            i=i+j

text=input()
pat=input()
naive(text,pat)
