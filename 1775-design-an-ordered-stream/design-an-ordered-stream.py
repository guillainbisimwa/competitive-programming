class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.ptr = 0
        self.res = [None] * n
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        result = []
        self.res[idKey - 1] = value
        while self.ptr < len(self.res) and self.res[self.ptr] is not None:
            result.append(self.res[self.ptr])
            self.ptr += 1
        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
