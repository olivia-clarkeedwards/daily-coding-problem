class BinaryTreeNode:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = None
        self.right = None 


# Input: Integer array
# Output: BinaryTreeNode (root)

def buildBinaryTreeFromArray(treeArr, rootIndex = 0):
    
    if rootIndex > len(treeArr) - 1:
        return None
    
    root = BinaryTreeNode(treeArr[rootIndex])
    root.left = buildBinaryTreeFromArray(treeArr, rootIndex * 2 + 1)
    root.right = buildBinaryTreeFromArray(treeArr, rootIndex * 2 + 2)

    return root


def preOrderTraversal(root):
    
    if root is None:
        return 
    
    preOrderTraversal(root.left)
    print(root.value)
    preOrderTraversal(root.right)


def isUnivalTree(root):
    #write my code here
    
    



root = buildBinaryTreeFromArray([1, None])
preOrderTraversal(root)
print(isUnivalTree(root))
