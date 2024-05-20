class solution:
    def maxF(self, nums, k):
        nums.sort(reverse = True)
        freq = 0
        l,r = 0,0
        ans = nums[0]

        for r in range(len(nums)):
            k -= nums[l] - nums[r]
            while k < 0:
                k+= (r-l) * (nums[l]-nums[l+1])
                l +=1

            if freq <= r-l+1:
                freq = r-l+1
                ans = nums[l]
        return [freq, ans]
    def listInput(self):
        return list(map(int, input().split()))
n,k = solution().listInput()
nums = solution().listInput()

print(*solution().maxF(nums, k))