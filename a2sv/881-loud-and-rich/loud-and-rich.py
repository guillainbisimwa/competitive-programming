class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        dgree = [0] * n
        adj_list = defaultdict(list)
        for rich, poor in richer:
            adj_list[rich].append(poor)
            dgree[poor] += 1
        
        queue = []
        for i in range(n):
            if not dgree[i]:
                queue.append(i)
        
        ans = [i for i in range(n)]

        i = 0
        while i < n:
            rich = queue[i]
            for poor in adj_list[rich]:
                if quiet[ans[poor]] > quiet[ans[rich]]:
                    ans[poor] = ans[rich]

                dgree[poor] -= 1
                if not dgree[poor]: queue.append(poor)
            i += 1

        return ans