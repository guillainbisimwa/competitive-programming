class Solution:
    MOD = 1_000_000_007
    def countGoodNumbers(self, n: int) -> int:
        # Calculate the number of even and odd positions in the digit string
        odd = n // 2
        even = (n + 1) // 2
        
        # Calculate the total number of good digit strings
        # multiplying 5 by even because there could only be 5 even numbers between 0-9
        # multiplying 4 by odd because there could only be 4 prime numbers between 0-9
        return (self.pow(5, even) * self.pow(4, odd)) % self.MOD
    
    def pow(self, x: int, n: int) -> int:
        # Base case for the recursion
        if n == 0:
            return 1
        
        # Recursively calculate x^(n/2)
        temp = self.pow(x, n // 2)
        
        # If n is even, return (x^(n/2))^2
        if n % 2 == 0:
            return (temp * temp) % self.MOD
        # If n is odd, return (x^(n/2))^2 * x
        else:
            return (x * temp * temp) % self.MOD