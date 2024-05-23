# User function Template for python3

class Solution:
    def toh(self, N, fromm, to, aux ):
        # Your code here
        if N == 0:
            return 0
        a = self.toh(N - 1, fromm, aux, to)
        print("move disk",N, "from rod",fromm, "to rod",to)
        # N -= 1
        b = self.toh(N - 1, aux, to, fromm)
        
        return a + b + 1
        

        


#{ 
 # Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends