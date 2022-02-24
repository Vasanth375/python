a=[i for i in range(10) if i%2==0]
b=[i for i in range(10) if i%3==0]
c=[(x,y) for x in a for y in b]
print(a,b)
print(c)