def binh_phuong_co_lap(a,k,n):
    b=1
    if k==0:
        return b
    A=a
    k_bin=bin(k)[2:]# chuyen k sang chuoi nhi phan
    t=len(k_bin)

    if k_bin[-1]== '1':
        b=a 

    for i in range(1,t):
        A=(A*A)%n
        if k_bin[-1-i]=='1':
            b=(b*A)%n

    return b

if __name__=='__main__':
    p=int(input('NHAP SO P:'))
    q=int(input('NHAP VAO q:'))
    a=int(input('NHAP VAO a:'))
    b=int(input('Nhap vao b: '))
    # khoa chung
    c=binh_phuong_co_lap(q,a*b,p)
    print('khoc chung c: ',c)
