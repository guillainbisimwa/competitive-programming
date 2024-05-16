class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self, root) -> None:
        self.root = Node(root)

    def insertElement(self, node, element) -> None:
        if node:

            if node.data > element:
                # left
                if node.left != None:
                    self.insertElement(node.left, element)
                else:
                    node.left = Node(element)
            else:
                if node.right != None:
                    self.insertElement(node.right, element)
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


tree = BST(5)

# print(tree.root.data) # 5

tree.insertElement(tree.root, 9)
tree.insertElement(tree.root, 4)


print(tree.root.right.data) # 9
print(tree.root.left.data) # 4

print(tree.search(tree.root, 4))
