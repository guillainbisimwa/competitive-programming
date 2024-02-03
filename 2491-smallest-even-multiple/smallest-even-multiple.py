class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """    
        if n == 2:
            return 2
    
        max_value = max(n, 2)

        while True:
            if max_value % 2 == 0 and max_value % n == 0:
                return max_value
            max_value += 1
