class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        while n != 0:
            shifting1 = n & 1  
            # before shifting...

            n >>= 1
            shifting2 = n & 1  
            # after shifting...

            if shifting1 == shifting2:
                return False
        return True
