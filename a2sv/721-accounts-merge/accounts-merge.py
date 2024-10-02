class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        # Path compression to find the root of x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of x and y
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union the two sets by making one root point to the other
            self.parent[rootY] = rootX

    def add(self, x):
        # Add a new element to the UnionFind structure if it's not already present
        if x not in self.parent:
            self.parent[x] = x


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        for account in accounts:
            name = account[0] 
            first_email = account[1] 

            uf.add(first_email)
            email_to_name[first_email] = name

            for email in account[1:]:
                uf.add(email)
                uf.union(first_email, email)
                email_to_name[email] = name

        email_groups = defaultdict(list)
        for email in email_to_name:
            root_email = uf.find(email)
            email_groups[root_email].append(email)

        result = []
        for emails in email_groups.values():
            account_name = email_to_name[emails[0]]
            result.append([account_name] + sorted(emails))

        return result