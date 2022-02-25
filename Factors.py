n=33
factors=[]
for i in range(1,n+1):
    for j in range(1, n+1):
        if i*j == n:
            factors.append(j)

print(sorted(factors))