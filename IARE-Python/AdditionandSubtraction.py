def Addition(a, b):
    c = []

    for i in range(len(a)):
        k = []
        for j in range(len(a)):
            k.append(a[i][j] + b[i][j])
        c.append(k)

    print(c)

def Subtraction(a, b):
    c = []

    for i in range(len(a)):
        k = []
        for j in range(len(a)):
            k.append(a[i][j] - b[i][j])
        c.append(k)

    print(c)

a = [
    [1,2,3],
    [4,5,6],
    [5,6,7]
]

b = [
    [3,2,1],
    [5,4,3],
    [9,8,7]
]

Addition(a, b)
Subtraction(a, b)