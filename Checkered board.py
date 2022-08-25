a=int(input("rows : "))
b=int(input("columns : "))
c='#'
d='*'
for i in range(a):
    for j in range(b):
        if j%2==0:
            print(d,end="")
        else :
            print(c,end="")
    print()