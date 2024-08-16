class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix)
        for i in range(1,n):
            for j in range(m):
                left = matrix[i-1][j-1] if j > 0 else float('inf')
                mid = matrix[i-1][j]
                right = matrix[i-1][j+1] if j < m-1  else float('inf')
                matrix[i][j] += min(left, mid, right)

        return min(matrix[-1])




        