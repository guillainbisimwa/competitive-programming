class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        words = [word for word in words if len(word) > 0]
        words = words[::-1]

        return ' '.join(words)
        