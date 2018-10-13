class Node(object):
    
    
    def __init__(self, data, left = None, right = None):
        
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self, data):
        
        if data <= self.data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)
                
    
    def __repr__(self):
        return str(self.data)

def insert(head, node):
    
    if not head:
        return node
    
    if node.data <= head.data:
        head.left = insert(head.left, node)
    if node.data > head.data:
        head.right = insert(head.right, node)
        
    return head  
    
def lookup(head, value):
    
    if not head:
        return None # Not found
        
    if value == head.data:
        return head
        
    if value < head.data:
        return lookup(head.left, value)
    
    if value > head.data:
        return lookup(head.right, value)
        
    
        
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
    
    
class TreeHasNoNodes(Exception):
    pass
    

def min_node(node):
    
    if not node:
        raise TreeHasNoNodes
        
    if not node.left:
        return node
        
    return min_node(node.left)
    
    
def max_depth(root):
    
    if not root:
        return 0
        
    if (not root.left) and (not root.right):
        return 0
        
    left_depth = 1 + max_depth(root.left)
    right_depth = 1 + max_depth(root.right)
    
    return max(left_depth, right_depth)
    

