# class Node():
#     def __init__(self, val=None, right=None, left = None) -> None:
#         self.val : val
#         self.right = right
#         self.left = left
# class BST:
#     def __init__(self, val) -> None:
#         self.root = Node(val)

#     def eatingCandies(self):
#         return self.root

#     def insert(self, node, position, value):
#         if position=="R":
#             node.right =Node(value)
#         else:
#             node.left =Node(value)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     weight = list(map(int, input().split()))
#     lenW = len(weight)
#     # print(lenW//2)
#     tree = None
#     if len(weight) % 2 == 0:
#        tree = BST(0)
#        node = tree.root
#        for i in range(int(lenW/2)):
#            tree.insert(node, "L", weight[i-1])
#            node = node.left
#     else:
#         tree = BST(weight[lenW//2])
#         node = tree.root
#         for j in range(lenW//2):
#            tree.insert(node, "R", weight[j+(lenW//2)])
#            node = node.right
 

def eatingCandies():
    num_candies = int(input())

    weights = list(map(int, input().split()))
    left = 0

    right = num_candies - 1

    alice_weight = weights[0]

    bob_weight = weights [num_candies - 1]

    max_candies = 0

    while left < right:

        if alice_weight == bob_weight:

            max_candies = max(max_candies, left + 1 + num_candies - right)

        if alice_weight <= bob_weight: #, 
            left += 1

            alice_weight += weights [left]

        elif bob_weight < alice_weight:

            right -= 1 
            bob_weight += weights [right]

    print(max_candies)

num_test_cases = int(input())

for _ in range(num_test_cases):

    eatingCandies()