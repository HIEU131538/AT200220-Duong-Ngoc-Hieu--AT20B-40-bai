def buid_failure(pattern):
    n=len(pattern)
    F=[-1]*n
    for j in range(1,n):
        for k in range(j-1,-1,-1):
            if pattern[:k]==pattern[j-k:j]:
                F[j]=k
                break
    return F

def KMP(text,pattern):
    n=len(text)
    m=len(pattern)
    position=[]
    if m==0:
        return position
    F=buid_failure(pattern)
    i=0 #duyet trong text
    j=0 #duyet trong pattern
    while i<=n-m:
        
        while j< m and text[i+j]==pattern[j]:
            j+=1
        if j==m:
            position.append(i)
        if j==0:
            i+=1
        else:
            i=i+j-F[j-1]
            j=max(F[j-1],0)
    return position

text=input('Nhap text: ')
pattern=input('Nhap pattern: ')
k=KMP(text,pattern)
print(k)
