# Question by Google 
# Given the root of a binary tree, 
  #implement serialise(root), which serialises the tree into a string
  #deserialise(s) which deserialises a string back into a BT


class Node: 
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right 



    
def serialise(root):
    # turn tree into a string
    print(root)

def deserialise(s):
    tree = s.split()
    
    


deserialise('root left left.left -1 right -1 -1')

#test
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialise(serialise(node)).left.left.val == 'left.left'
    