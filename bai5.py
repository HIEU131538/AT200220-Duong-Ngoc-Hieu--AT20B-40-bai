def extend_gcd(a,b):
    # tra ve (gcd ,x,y) sao cho a*x+b*y=gcd
    if b==0:
        return(a,1,0)
    else:
        g,x1,y1=extend_gcd(b,a%b)
        x=y1
        y=x1-(a//b)*y1
        return (g,x,y)
    
def mod_in(a,p):
    g,x,y=extend_gcd(a,p)
    if g !=1:
        return "NOT FOUND"
    else:
        return x%p # nho am thi minh tim ra duong ne
    
p=int(input("NHAP p: "))
a=int(input('Nhap a: '))

print(mod_in(a,p))
