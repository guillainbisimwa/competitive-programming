class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count_s = [0] * 26

        for char in s:
            count_s[ord(char) - ord('a')] += 1

        for char in t:
            count_s[ord(char) - ord('a')] -= 1

        for i in range(26):
            if count_s[i] < 0:
                return chr(ord('a') + i)
