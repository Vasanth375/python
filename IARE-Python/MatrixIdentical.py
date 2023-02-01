def isidentical(A, B):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] != B[i][j]:
                return("Not Identical")
    return("Identical")

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(isidentical(A, B))

