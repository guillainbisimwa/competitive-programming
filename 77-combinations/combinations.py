class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        conbinaison = []

        def backtrack(num, curr):
            if len(curr) == k:
                conbinaison.append(curr[:])
                return
            for idx in range(num, n+1):
                curr.append(idx)
                backtrack(idx +  1, curr)
                curr.pop()
        backtrack(1, [])
        return conbinaison