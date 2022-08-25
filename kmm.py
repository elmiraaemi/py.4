a=int(input(" first namber :"))
b=int(input(" second namber :"))
b2=[]
a2=[]
for i in range(1 , (a*b)+1):
    c = a * i
    a2.append(c)
for i in range(1 , (a*b)+1):
    d = b * i
    b2.append(d)
x=list(set(a2).intersection(b2))
print(min(x))