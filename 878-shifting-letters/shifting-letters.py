class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        prefix = [0] * n
        prefix[0] = shifts[0]
        
        for i in range(1, n):
            prefix[i] = shifts[i] + prefix[i - 1]
        
        total_sum = prefix[-1]
        
        for i in range(n):
            increment = 0
            
            if i == 0:
                increment = total_sum
            else:
                increment = total_sum - prefix[i - 1]
            
            increment = (ord(s[i]) - ord('a') + increment) % 26
            
            s = s[:i] + chr(ord('a') + increment) + s[i + 1:]
        return s