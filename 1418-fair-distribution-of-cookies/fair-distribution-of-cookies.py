class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtracking(i, arr, minim):
            # If valid solution
            if i == len(cookies):
                return min(minim, max(arr))

            # loop through all choises
            for j in range(len(arr)):
                if arr[j] + cookies[i] >= minim:
                    continue
                arr[j] += cookies[i]
                minim = backtracking(i+1, arr, minim )
                arr[j] -= cookies[i]
            return minim


            # if valide choise
        arr = [0] * k

        minimum = backtracking(0, arr, float('inf'))
        return minimum
        
            
