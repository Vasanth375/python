n=11    # number we have to find whether it is prime or not

factors=[]

# find factors of n
for i in range(1,n+1):
    for j in range(1, n+1):
        if i*j == n:
            factors.append(j)

# if factors of n is greater than 2 it is not prime number
if len(factors) > 2:
    print(n,"is not a prime number.")
else:
    print(n,"is a prime number.")