def square_matrix_simple(matrix=[]):
    # Create a new matrix of the same size as the input matrix
    result_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    # Iterate over each element in the matrix and compute its square
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2
    
    return result_matrix

