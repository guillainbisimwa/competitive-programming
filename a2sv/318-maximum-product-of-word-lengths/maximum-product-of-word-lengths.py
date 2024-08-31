class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        bits = []
        # MASK CALCULATION
        for w in words:
            bit = 0
            for char in w:
                index = ord(char) - 97 # ord(a)
                bit |= 1 << index
            bits.append(bit)
                


        # COMPARING MASK??
        for i in range(len(words)):
            for j in range(i):
                if not (bits[i] & bits[j]):
                    ans = max(ans, len(words[i] * len(words[j])))
        return ans


        # RETURN (length(word[i]) * length(word[j])) WITH NO LETTERS IN COMMON
        return ans
