class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        listOfFriend = list(range(1,n+1))
        i=0

        while len(listOfFriend) != 1:
            # find the friend to remove?
            i = (i + k - 1) % len(listOfFriend)
            del listOfFriend[i]

            # remove that frien
        
        return listOfFriend[0]
        