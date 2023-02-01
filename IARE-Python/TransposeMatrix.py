a = [
    [1,2],
    [4,5],
    [1,2]
]

transposeA = []

for i in range(len(a[1])):
    k = []
    for j in range(len(a)):
        k.append(a[j][i])

    transposeA.append(k)

print(transposeA)
