def shortestDistance(self, matrix):

    
    V = len(matrix)
    
    inf = float('inf')
    for i in range(V):
        for j in range(V):
            if matrix[i][j] == -1 and i != j:  
                matrix[i][j] = inf

    for K in range(V):
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):

                if matrix[i][j] > matrix[i][K] + matrix[K][j] :
                    matrix[i][j] = matrix[i][K] + matrix[K][j]


    for i in range(V):
        for j in range(V):
            if matrix[i][j] == inf:
                matrix[i][j] = -1   
    return matrix