a=[]
b=int(input("The number of numbers in the list ? : "))
for i in range(b):
    c=int(input("Your list numbers : "))
    if c not in a:
        a.append(c)
print(a)
