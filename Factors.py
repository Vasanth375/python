for k in range(3):
    n=int(input("Enter number"))
    factors=[]
    
    # finding factors
    for i in range(1,  n+1):
        if n%i == 0:
            factors.append(i)

    # removing n value in factor list
    if n in factors:
        factors.remove(n)
    print(sorted(factors))

    # checking whether it is perfect number or not
    if sum(factors) == n:
        print("It is perfect number")
    else:
        print("Not a perfect number")