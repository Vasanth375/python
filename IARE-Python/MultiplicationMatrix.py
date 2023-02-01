def multiply_matrices(A, B):
    # Initialize an empty matrix for the result
    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    # Loop through each element and perform the multiplication
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# Example usage:
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

# Perform multiplication of matrices
result_mul = multiply_matrices(A, B)
print("Multiplication:")
for row in result_mul:
    print(row)
