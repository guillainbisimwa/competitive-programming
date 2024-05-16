class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self, root) -> None:
        self.root = Node(root)

    def insertElementBinary(self, node, element) -> None:
        if node:

            if node.data > element:
                # left
                if node.left != None:
                    self.insertElementBinary(node.left, element)
                else:
                    node.left = Node(element)
            else:
                if node.right != None:
                    self.insertElementBinary(node.right, element)
                else:
                    node.right = Node(element)

    def insertElement(self, node, element, ind) -> None:
        if node:

            if ind == "L":
                # left
                if node.left != None:
                    self.insertElement(node.left, element, "L")
                else:
                    node.left = Node(element)
            else:
                if node.right != None:
                    self.insertElement(node.right, element, "R")
                else:
                    node.right = Node(element)
    
    def search(self,node, value):
        """ 
        loop through the tree from the root
        """
        if node:
            if node.data == value:
                return True
            else:
                return self.search(node.left, value) or  self.search(node.right, value) 
                
        else:
            return False

    def printPreorder(self, node, foundValues):

        if node:
            foundValues += (str(node.data)+" - ")
            if node.left:
                foundValues = self.printPreorder(node.left, foundValues)
            if node.right:
                foundValues = self.printPreorder(node.right, foundValues)
            return foundValues

tree = BST(1)

# print(tree.root.data) # 5
print(tree.printPreorder(tree.root, ""))

tree.insertElement(tree.root, 2,"L")
tree.insertElement(tree.root, 3, "R")
tree.insertElement(tree.root, 4,"L")
tree.insertElement(tree.root.left, 5,"R")
tree.insertElement(tree.root.right, 6,"L")
tree.insertElement(tree.root, 7, "R")


# print(tree.root.right.data) # 9
# print(tree.root.left.data) # 4

print(tree.search(tree.root, 4))
print(tree.printPreorder(tree.root, ""))

# print(tree.root.left.data) # 2
# print(tree.root.left.left.data) # 4
# print(tree.root.left.right.data) # 5
# print(tree.root.right.data) # 3
# print(tree.root.right.left.data) # 6
# print(tree.root.right.right.data) # 7


