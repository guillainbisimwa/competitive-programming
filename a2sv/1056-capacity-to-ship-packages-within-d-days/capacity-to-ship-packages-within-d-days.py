class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if self.canShip(mid, days, weights):
                right = mid
            else:
                left = mid + 1

        return left
    def canShip(self, capacity: int, days: int, weights: List[int]) -> bool:
        day = 1
        current_weight = 0

        for weight in weights:
            current_weight += weight
            if current_weight > capacity:
                current_weight = weight
                day += 1
                if day > days:
                    return False
        return True