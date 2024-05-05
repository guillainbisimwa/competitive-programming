from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.ordered = OrderedDict()
    
    def get(self, key: int) -> int:
        if key in self.ordered:

            self.ordered.move_to_end(key)
            return self.ordered[key]

        return -1

    def put(self, key: int, value: int) -> None:
        self.ordered[key] = value

        self.ordered.move_to_end(key)

        if len(self.ordered) > self.capacity:
            self.ordered.popitem(last=False) 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)