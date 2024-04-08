class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cars = [0] * 1001 # len(trips[0])

        # Apply sweep line technique
        for trip in trips:
            cars[trip[1]] += trip[0]
            cars[trip[2]] -= trip[0]

        prefix = 0
        for load in cars:
            prefix += load
            if prefix > capacity:  # If at any time passengers exceed the limit
                return False  # Then return False

        return True