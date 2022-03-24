for k in range(3):
    n=int(input("Enter number"))
    factors=[]
    for i in range(1,n+1):
        for j in range(1, n+1):
            if i*j == n:
                factors.append(j)
    if n in factors:
        factors.remove(n)
    print(sorted(factors))
    if sum(factors) == n:
        print("It is perfect number")
    else:
        print("Not a perfect number")