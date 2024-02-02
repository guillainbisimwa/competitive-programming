class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reverse = 0
        original = x
        while x != 0:
            var = x % 10
            reverse = reverse * 10 + var
            x //= 10

        return original == reverse
        