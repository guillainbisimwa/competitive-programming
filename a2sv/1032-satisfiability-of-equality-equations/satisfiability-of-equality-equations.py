class Solution:
    def __init__(self):
        self.uf = list(range(26))
    def find(self, x):
        #  find the root/representative of the component and apply path compression
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]
    def equationsPossible(self, equations: List[str]) -> bool:
        for e in equations:
            if e[1] == '=':
                self.uf[self.find(ord(e[0]) - ord('a'))] = self.find(ord(e[3]) - ord('a'))

        for e in equations:
            if e[1] == '!' and self.find(ord(e[0]) - ord('a')) == self.find(ord(e[3]) - ord('a')):
                return False
        
        return True