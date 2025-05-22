def extend_gcd(a,b):
    if b==0:
        return 1,a
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
    return a,x2

def im(a,b):
    d,t=extend_gcd(a,b)
    if d!=1:
        return None
    else:
        return t%b

def lam():
    p=int(input('nhap p: '))
    a=int(input('nhap a: '))
    x1=int(input('nhap x1: '))
    y1=int(input('nhap y1: '))
    x2=int(input('nhap x2: '))
    y2=int(input('nhap y2: '))
    
    if x2==x1 and y2==-y1:
        return (0,0)
    else:
        if x2==x1 and y2==y1:
            imu=im(2*y1,p)
            y=((3*x1*x1+a)%p)*imu %p
        else:
            kaka=im(x2-x1,p)
            y=((y2-y1)%p)*kaka %p
        x3=(y*y-x1-x2)%p
        y3=(y*(x1-x3)-y1)%p

        return (x3,y3)
    
if __name__=='__main__':
    x3,y3=lam()
    print(x3,y3)
