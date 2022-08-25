a=int(input("rows : "))
b=int(input("columns : " ))
def c(a, b):
    for i in range(1, a+1):
        for j in range(1, b+1):
            print(i * j, end='\t')
        print()
c(a, b)