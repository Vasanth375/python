from math import sqrt
n=20

# finding factors
factors=[]
for i in range(1,n+1):
    if n%i == 0:
        factors.append(i)

# removing 1 and n from factors
if n in factors and 1 in factors:
    factors.remove(n)
    factors.remove(1)

# defination for squarefree function
def isSquareFree(n):
     
    if n % 2 == 0:
        n = n / 2

    # dividing n by 2 again if it's true return false
    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n) + 1)):
        if n % i == 0:
            n = n / i
 
        if n % i == 0:
            return False
    return True

k=0
for i in factors:
    if isSquareFree(i):
        k+=1

print(k)