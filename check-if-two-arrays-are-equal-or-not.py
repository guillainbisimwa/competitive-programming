#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        count_A = {}
        count_B = {}
        
        # Count occurrences of elements in array A
        for num in A:
            count_A[num] = count_A.get(num, 0) + 1
        
        # Count occurrences of elements in array B
        for num in B:
            count_B[num] = count_B.get(num, 0) + 1
        
        # Check if both dictionaries are equal
        return count_A == count_B
 
# Driver Code Starts
# Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
