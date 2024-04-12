class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        temp = [[0] * m for _ in range(n)]

        for i in range(n):
            sum = 0
            for j in range(m):
                sum += mat[i][j]
                temp[i][j] = sum

        for i in range(n):
            for j in range(m):
                sum = 0
                ur, lr = max(0, i - k), min(n - 1, i + k)
                lc, rc = max(0, j - k), min(m - 1, j + k)
                for x in range(ur, lr + 1):
                    sum += temp[x][rc]
                    if lc != 0:
                        sum -= temp[x][lc - 1]
                mat[i][j] = sum

        return mat