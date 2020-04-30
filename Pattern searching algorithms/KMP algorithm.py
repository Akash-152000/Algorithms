def kmp(text,pat):
    n=len(text)
    m=len(pat)
    lps=[0]*m
    i=0
    j=0
    
    def LPS(pat,m,lps):
        i=1
        j=0
        lps[0]
        while i<m:
            if pat[i]==pat[j]:
                j+=1
                lps[i]=j
                i+=1
            else:
                if j==0:
                    lps[i]=0
                    i+=1
                else:
                    j=lps[j-1]
    
    LPS(pat,m,lps)
    while i<n:
        if text[i]==pat[j]:
            i+=1
            j+=1
        if j==m:
            print("Pattern found at index: ",i-j)
            j=lps[j-1]
        elif i<n and text[i]!=pat[j]:
            if j==0:
                i+=1
            else:
                j=lps[j-1]
    

text=input()
pat=input()
kmp(text,pat)
