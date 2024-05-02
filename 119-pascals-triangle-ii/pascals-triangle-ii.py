class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        a = [[0] * 34 for _ in range(34)]
        
        a[0][0] = 1
        a[1][0] = a[1][1] = 1
        
        for i in range(2, rowIndex + 1):
            a[i][0] = a[i - 1][0]
            a[i][rowIndex] = a[i - 1][rowIndex - 1]
            for j in range(1, rowIndex):
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
        
        for i in range(rowIndex + 1):
            res.append(a[rowIndex][i])
        
        return res