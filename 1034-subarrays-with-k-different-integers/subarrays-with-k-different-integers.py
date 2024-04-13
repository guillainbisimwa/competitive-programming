class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)

        ans = 0
        temp = 0
        l = 0
        s = False

        i = 0
        for j in range(n):
            if mp[nums[j]] == 0:
                l += 1
            mp[nums[j]] += 1

            while l > k:
                mp[nums[i]] -= 1
                if mp[nums[i]] <= 0:
                    mp[nums[i]] = 0
                    l -= 1
                i += 1
                temp = i
                s = True

            if l == k:
                while mp[nums[i]] > 1:
                    mp[nums[i]] -= 1
                    i += 1
                if s:
                    ans += i - temp + 1
                else:
                    ans += i + 1

        return ans