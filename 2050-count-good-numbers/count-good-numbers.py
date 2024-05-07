class Solution:
    MOD = 1_000_000_007
    def countGoodNumbers(self, n: int) -> int:
        odd = n // 2
        even = (n + 1) // 2
        
      
        return (self.pow(5, even) * self.pow(4, odd)) % self.MOD
    
    def pow(self, x: int, n: int) -> int:
        if n == 0:
            return 1
        temp = self.pow(x, n // 2)
        
        if n % 2 == 0:
            return (temp * temp) % self.MOD
        else:
            return (x * temp * temp) % self.MOD