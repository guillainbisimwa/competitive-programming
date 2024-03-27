class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)
        m = len(word2)

        i = 0
        j = 0
        ans = ""
        while i < n and j < m:
            if word1[i:] >= word2[j:]:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1

        while i < n:
            ans += word1[i]
            i += 1

        while j < m:
            ans += word2[j]
            j += 1

        return ans
        