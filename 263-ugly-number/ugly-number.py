class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        primes = [2, 3, 5]
        for prime in primes:
            while n % prime == 0:
                n = n // prime
        return n == 1