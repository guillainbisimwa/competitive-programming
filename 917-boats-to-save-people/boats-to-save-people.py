class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        high = len(people) - 1
        ans = 0
        while high >= l:
            curr = people[high]
            if curr + people[l] <= limit:
                ans += 1
                high -= 1
                l += 1
            else:
                ans += 1
                high -= 1
        return ans