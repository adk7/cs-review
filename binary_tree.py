class BinaryTreeNode(object):
    
    
    def __init__(self, data, left = None, right = None):
        
        self.data = data
        self.left = left
        self.right = right
    
    '''
    redundant methods
        
    def getData(self):    
        return self.data
        
    def setLeftChild(self, left_child):
        self.left = left_child
    
    def setRightChild(self, right_child):
        self.right = right_child
        
    def getLeftChild(self):
        return self.left
        
    def getRightChild(self):
        return self.right   
    '''
    
    
    def __repr__(self):
        return str(self.data)
        
from collections import deque

def breadth_first_traversal(node):
    
    to_check = deque()
    to_check.append(node)
    
    while len(to_check) != 0:
        current_node = to_check.popleft()
        print(current_node.data) #process node
        
        if(current_node.left):
            to_check.append(current_node.left)
            
        if(current_node.right):
            to_check.append(current_node.right)
    
    
    
def depth_first_traversal(node):
    
    '''
    This is in-order traversal.
    
    Pre-order: process current node before left and right subtree
    Post-order: process current node after left and right subtree
    
    '''
    
    if not node:
        return
        
    depth_first_traversal(node.left)
    print(node.data)
    depth_first_traversal(node.right)
        
    return 
    
    
def mirror_tree(root):
    
    if not root:
        return
        
    root.left, root.right = root.right, root.left
    
    mirror_tree(root.left)
    mirror_tree(root.right)
    