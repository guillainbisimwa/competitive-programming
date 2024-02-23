class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposeMatrix = []

        for col in range(len(matrix[0])):
            new_row = []
            
            for row in range(len(matrix)):
                new_row.append(0)
            
            transposeMatrix.append(new_row)

        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposeMatrix[j][i] = matrix[i][j]
        
        return transposeMatrix
