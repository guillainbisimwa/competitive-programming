class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        boxes = tuple((k, len(list(g))) for k,g in groupby(boxes))

        @lru_cache(None)
        def dfs(grps: tuple) -> int:
            
            if not grps: return 0
            (colorL, lenL), grps = grps[0], grps[1:]

            res = lenL*lenL + dfs(grps)

            for i, (colorR, lenR) in enumerate(grps):
                if colorL == colorR:
                    res = max(res, dfs(grps[:i]) + 
                              dfs(((colorL, lenL+lenR),) + grps[i+1:]))

            return res

        return dfs(boxes)