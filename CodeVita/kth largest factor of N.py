N,k=list(map(int, input().split(',')))
# need to find factor
# index number need to find value after finding factors of N
factor=[]
# finding factors
for i in range(1, N+1):
    if N%i == 0:factor.append(i)

# if k > number of factors return 1
if k < len(factor):print(factor[k])
else:print(1)