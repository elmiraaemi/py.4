a=int(input("your number:"))
b=1
while b <= a:
    fact = 1
    for i in range(1, b+1):
        fact *= i
    if fact == a:
        print("Yes")
        break
    b += 1
else:
    print("No")