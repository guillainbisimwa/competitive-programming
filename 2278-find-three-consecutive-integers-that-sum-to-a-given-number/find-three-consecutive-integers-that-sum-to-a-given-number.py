class Solution(object):
    def sumOfThree(self, num):
        return [] if num % 3 else [num//3-1, num//3, num//3+1]

