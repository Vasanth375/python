# 10 to 40
a = [12,56,34,23,78,18,35,30]
a = [301, 392, 7, 201, 40001, 320, 1, 315, 365]
a = [381, 392,7, 11, 201, 40001, 320, 1, 315, 364]

# debug this to see the problem
# Actual wrong solution that leaves a value in the iterations
# for i in a:
#     if i not in range(200, 400+1):
#         a.remove(i)
# print(a)

# solution for the above problem
for i in range(len(a)-1,0, -1):
    if a[i] not in range(200, 400+1):
        a.remove(a[i])
print(a)

