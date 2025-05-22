def extend_gcd(a,b):
    if b==0:
        d=a
        x,y=1,0
        return x
    x2,x1=1,0
    y2,y1=0,1
    while b>0:
        q=a//b
        r=a%b
        x=x2-q*x1
        y=y2-q*y1
        a=b
        b=r
        x2=x1
        x1=x
        y2=y1
        y1=y
    return x2%p

if __name__=='__main__':
    p=int(input('Nhap vao p: '))
    g=int(input('nhap vao g: '))
    x=int(input('nhap vao x: '))
    a=int(input('Nhap vao a: '))
    b=int(input('nhap vao b: '))
    tmp=extend_gcd(pow(a,x),p)
    h=(b*tmp)%p
    print(h)
