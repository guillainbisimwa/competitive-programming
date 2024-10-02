class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = []
        a = -1
        b = -1

        for i in range(len(edges)):
            a = -1
            b = -1

            for j in range(len(nodes)):
                if edges[i][0] in nodes[j]:
                    a = j
                if edges[i][1] in nodes[j]:
                    b = j
                if a != -1 and b != -1:
                    break

            if a == -1 and b == -1:
                nodes.append(set(edges[i]))
            elif a == b:
                return edges[i]
            elif a == -1:
                nodes[b].add(edges[i][0])
            elif b == -1:
                nodes[a].add(edges[i][1])
            else:
                nodes[a].update(nodes[b])
                del nodes[b]

        return []