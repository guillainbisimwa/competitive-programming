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
        

    def printPreorderNonRecursion(self):
        """
        Approch:
        use a stack [LIFO]
        start with the node in stack
        
        """
        stack = []
        ans = []
        if not self.root:
            return
        else: 
            stack.append(self.root)
            while stack:
                node = stack.pop()
                ans.append(str(node.data)+" -")
                # put L and then R in the stack
               
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return ans
        

    def printInorder(self, node, foundValues):

        if node:
            if node.left:
                foundValues = self.printInorder(node.left, foundValues)
            
            foundValues += (str(node.data)+" - ")

            if node.right:
                foundValues = self.printInorder(node.right, foundValues)
            return foundValues
        
    def printInorderNonRecursion(self):
        if not self.root:
            return
        
        stack = []
        ans = []
        node = self.root
        
        while node or stack:
            if node:
                stack.append(node)
                # if node.left:
                node = node.left
            else:
                node = stack.pop()
                ans.append(str(node.data)+" -")
                # if node.right:
                node = node.right

        return ans
    
    def printPostorder(self, node, foundValues):

        if node:
            if node.left:
                foundValues = self.printPreorder(node.left, foundValues)
            if node.right:
                foundValues = self.printPreorder(node.right, foundValues)

            foundValues += (str(node.data)+" - ")
            
            return foundValues


    def deleteNode(self, root: Node, key: int) -> Node:
        if not root:
            return root

        if root.data == key:
            if root.left and root.right:
                # Find the minimum node in the right subtree
                [psucc, succ] = self.findMin(root.right, root)
                
                # Splice out the successor
                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right
                
                # Reset the left and right children of the successor
                succ.left = root.left
                succ.right = root.right
                return succ
            else:
                # Easier cases when the node to be deleted has only one child or no children
                if root.left:
                    return root.left
                else:
                    return root.right
        else:
            if root.data > key:
                if root.left:
                    root.left = self.deleteNode(root.left, key)
            else:
                if root.right:
                    root.right = self.deleteNode(root.right, key)
        
        return root

    def findMin(self, root, parent):
        """ Return the minimum node in the current tree and its parent """
        # We use an ugly trick: the parent node is passed in as an argument
        # so that eventually when the leftmost child is reached, the
        # call can return both the parent to the successor and the successor
        if root.left:
            return self.findMin(root.left, root)
        else:
            return [parent, root]

        
        

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

print(tree.search(tree.root, 2))
print(tree.printPreorder(tree.root, ""))
print(*tree.printPreorderNonRecursion())

print(tree.printInorder(tree.root, ""))
print(*tree.printInorderNonRecursion())

print(tree.printPostorder(tree.root, ""))

tree.deleteNode(tree.root, 2)


print(tree.search(tree.root, 2))
print(tree.printPreorder(tree.root, ""))
print(*tree.printPreorderNonRecursion())

print(tree.printInorder(tree.root, ""))
print(*tree.printInorderNonRecursion())




# print(tree.root.left.data) # 2
# print(tree.root.left.left.data) # 4
# print(tree.root.left.right.data) # 5
# print(tree.root.right.data) # 3
# print(tree.root.right.left.data) # 6
# print(tree.root.right.right.data) # 7


