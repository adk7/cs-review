class NodeNotFound(Exception):
    pass
    

class Node(object):
    
    def __init__(self, data):
        
        self.left = None
        self.right = None
        self.data = data
        
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        
        if self.right:
            self.right.PrintTree()
            
            
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
                        
    def __repr__(self):
        return "Tree with Root {}".format(self.data)        
        
        

def is_same_tree(root1, root2):
    
    if root1 == None and root2 == None:
        return True
    
    if root1 == None or root2 == None:
        return False
        
    if root1.data == root2.data and is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right):
        return True
    else:
        return False