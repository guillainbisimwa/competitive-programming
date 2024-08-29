class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xBit = 0
        yBit = 0
        count = 0
        
        while x != 0 or y != 0:
            xBit = x & 1
            yBit = y & 1
            
            if xBit != yBit:
                count += 1
            
            x = x >> 1
            y = y >> 1
        
        return count