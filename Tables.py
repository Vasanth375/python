n = int(input("Enter how many tables you want to print: "))

for i in range(1,n+1):
    for j in range(1,10+1):
        print(i,'x',j,'=',i*j)
    print()