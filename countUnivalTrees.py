
class BinaryTreeNode:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = None
        self.right = None

def buildBinaryTreeFromArray(treeArr, root = 0):
    newNode = BinaryTreeNode(treeArr[root])
    leftIndex = root * 2 + 1
    rightIndex = root * 2 + 2

    if  leftIndex < len(treeArr):
        newNode.left = BinaryTreeNode(treeArr[leftIndex])
        buildBinaryTreeFromArray(treeArr, leftIndex)
    if rightIndex < len(treeArr):
        newNode.right = BinaryTreeNode(treeArr[rightIndex])
        buildBinaryTreeFromArray(treeArr, rightIndex)

    return newNode


def countUnivalTrees(root, count = 0):
    if root.left.value != root.value or root.right.value != root.value:
        print(count)
    else:
        print('unival')
        
    
    

root = buildBinaryTreeFromArray([1,1,1,1,1,None,1])

countUnivalTrees(root)
        


