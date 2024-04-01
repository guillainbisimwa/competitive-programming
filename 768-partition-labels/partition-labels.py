class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        freq = [0] * 26
        mp = defaultdict(int)
        ans = []
        sz = 0
        
        for e in s:
            freq[ord(e) - ord('a')] += 1
        
        for e in s:
            if e not in mp:
                if freq[ord(e) - ord('a')] - 1:
                    mp[e] = freq[ord(e) - ord('a')] - 1
                sz += freq[ord(e) - ord('a')]
            elif mp[e] == 1:
                del mp[e]
            else:
                mp[e] -= 1
            
            if len(mp) == 0:
                ans.append(sz)
                sz = 0
        
        return ans


