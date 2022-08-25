import math
Eq="ax2 + bx + c = 0 "
print(Eq)
a=int(input("a = ? : "))
b=int(input("b = ? : "))
c=int(input("c = ? : "))
d1=(b*b)-4*a*c
if d1 > 0:
    d2=math.sqrt(d1)
    x1=((-1*b)+d2)/(2*a)
    x2=((-1*b)-d2)/(2*a)
    print(x1 , x2)
elif d1 == 0 :
    d2=math.sqrt(d1)
    x1=((-1*b)+d2)/(2*a)
    print(x1)
elif d1 < 0:
    print("There is no answer")