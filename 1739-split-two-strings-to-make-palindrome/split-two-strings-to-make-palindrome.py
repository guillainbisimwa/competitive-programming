class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        n = len(a)
        sum1, sum2 = 0, 0
        
        for i in range(n // 2):
            if a[i] == a[n - i - 1]:
                sum1 += 2
            if b[i] == b[n - i - 1]:
                sum2 += 2
        
        sum1 += n & 1
        sum2 += n & 1
        sum12, sum22 = sum1, sum2
        
        if sum1 == n or sum2 == n:
            return True
        
        for i in range(n // 2):
            if a[i] == a[n - i - 1]:
                sum1 -= 2
                sum12 -= 2
            if b[i] == b[n - i - 1]:
                sum2 -= 2
                sum22 -= 2
            if a[i] == b[n - i - 1]:
                sum1 += 2
                sum22 += 2
            if a[n - i - 1] == b[i]:
                sum2 += 2
                sum12 += 2
            if sum1 == n or sum2 == n or sum12 == n or sum22 == n:
                return True
        
        return False