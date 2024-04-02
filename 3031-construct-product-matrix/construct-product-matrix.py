import math

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        MOD = 12345  # Module for BigInt operations

        # Calculate productRight matrix
        productRight = [[0] * n for _ in range(m)]
        product = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                productRight[i][j] = product
                product = (product * int(grid[i][j])) % MOD  # Use int for smaller numbers

        # Calculate result matrix
        result = [[0] * n for _ in range(m)]
        productLeft = 1
        for i in range(m):
            for j in range(n):
                result[i][j] = (productLeft * productRight[i][j]) % MOD
                productLeft = (productLeft * int(grid[i][j])) % MOD

        return result
