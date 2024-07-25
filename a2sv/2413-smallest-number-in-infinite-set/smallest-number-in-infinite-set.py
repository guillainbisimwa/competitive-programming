class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.added_back = set()

    def popSmallest(self) -> int:
        if self.added_back:
            smallest = min(self.added_back)
            self.added_back.remove(smallest)
        else:
            smallest = self.current
            self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_back:
            self.added_back.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)