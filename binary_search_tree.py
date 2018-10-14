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
        print(current_node.data, sep=", ") #process node
        
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
    print(node.data, end=", ")
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
    

def print_range(root, low, high):
    
    
    if not root:
        return
        
    if low <= root.data:
        print_range(root.left, low, high)
    
    if low <= root.data <= high:
        print(root.data)
        
    if low > root.data:
        print_range(root.right, low, high) 


def is_bst(root):
    
    if not root:
        return True
        
    if (not root.left) and (not root.right):
        return True
    
    left = right = True
        
    if root.left:
        if root.left.data <= root.data:
            left = is_bst(root.left)
        else:
            return False
            
    if root.right:
        if root.right.data > root.data:
            right = is_bst(root.right)
        else:
            return False
            
    return left and right    
        


def check_path_sum(node, total, current_total = 0):
    '''
    this checks for running total! different from sum of path from root to leaf!!!! 
    This function returns true if the path from root to any node yields a sum of total! 
    Different fromthe function below which checks for sum of path from root to leaf
    '''
    
    if not node:
        return current_total == total
     
    current_total += node.data
    if current_total == total:
            return True

    check_left = check_path_sum(node.left, total, current_total)
    check_right = check_path_sum(node.right, total, current_total)
    
    if check_left or check_right:
        return True
    else:
        return False
        
        

def check_path_sum_root_to_leaf(node, total):
    '''
    Checks if a path from root to leaf has sum of total
    '''
    
    if not node:
        return False
     
    if (not node.left) and (not node.right):
        return node.data == total
        
    if total < node.data:
        return False
    
    if node.left:
        check_left = check_path_sum(node.left, total - node.data)
    
    if node.right:
        check_right = check_path_sum(node.right, total - node.data)
    
    if check_left or check_right:
        return True
    else:
        return False
        
        
        
def print_all_paths(node, current_path = []):
    '''
    Print all paths from root node to the leaf node
    '''
    
    if not node:
        return
        
    current_path.append(node)
        
    if not node.left and not node.right:    
        print(*current_path, sep = " -> ", end="\n")
    
    print_all_paths(node.left, current_path)
    print_all_paths(node.right, current_path)
    
    current_path.remove(node)
    


def least_common_ancestor(root, node_a, node_b):
    
    if not root:
        return None
        
    
    if root == node_a or root == node_b:
        return root
        
    left_lca = least_common_ancestor(root.left, node_a, node_b)
    right_lca = least_common_ancestor(root.right, node_a, node_b)
    
    if left_lca and right_lca:
         return root
         
    if left_lca:
        return left_lca
        
    return right_lca
                    
    
        