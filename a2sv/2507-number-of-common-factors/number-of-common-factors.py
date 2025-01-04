class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c = 0
        minimal = min(a,b)
        for i in range(1,minimal+1):
            if a % i == 0 and b % i == 0:
                c+=1
        return c