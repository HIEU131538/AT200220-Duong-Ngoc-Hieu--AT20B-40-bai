def binhphuongcolap(a,k,n):
    b=1
    if k==0:
        return b
    A=a
    k_bin=bin(k)[2:]
    t=len(k_bin)
    if k_bin[-1]=='1':
        b=a 
    
    for i in range(1,t):
        A=(A*A)%n
        if k_bin[-1-i]=='1':
            b=(A*b)%n
        
    return b

if __name__=='__main__':
    p=int(input('NHAP VAO p: '))
    g=int(input('NHAP VAO g: '))
    x=int(input('NHAP VAO x: '))
    y=binhphuongcolap(g,x,p)
    print('KHOA CONG KHAI Y LA: ',y)
