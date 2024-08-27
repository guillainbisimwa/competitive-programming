class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        offset = 1
        
        for index in range(1, n + 1):
            if offset * 2 == index:
                offset *= 2
            result[index] = result[index - offset] + 1
        
        return result