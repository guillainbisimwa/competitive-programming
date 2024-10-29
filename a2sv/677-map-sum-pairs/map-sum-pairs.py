class TrieNode:
    def __init__(self):
        self.value = 0
        self.children = [None] * 26

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.mp = {}

    def insert(self, key: str, val: int):
        node = self.root
        prev = self.mp.get(key, 0)

        for c in key:
            index = ord(c) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node.value += val - prev
            node = node.children[index]

        node.value += val - prev
        self.mp[key] = val  # Update the dic

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not node.children[index]:
                return 0
            node = node.children[index]
        return node.value
