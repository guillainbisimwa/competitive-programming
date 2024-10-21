class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        prime = [True] * n
        count = 0
        
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False
        
        for i in range(2, n):
            if prime[i]:
                count += 1
        
        return count