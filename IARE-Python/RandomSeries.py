import random

n = 5
# for i in range(n):
#     print(int(random.random()*10))
l = []
i = 0
k = 0
while i<n:
    k = int(random.random()*10)
    while k not in l:
        l.append(k)
    i+=1
print(l)