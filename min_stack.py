'''
On Hindsight it is not a good idea to inherit from list. 
Becuase other list operations like adding two lists will cause the min value to be incorrect

Instead I should store both original stack and min stack as class variables which are basically lists

But this was good practice for OOP in Python
'''


class Stack(list):
    
    
    def __init__(self):
        super().__init__()
        
    def push(self, item):
        self.append(item)
            
    def pop(self):
        return super().pop()
   
    def peek(self):
        return self.__getitem__(self.__len__() - 1)


class MinStack(Stack):
    
    def __init__(self):
        self.min_stack = Stack()
        super().__init__()
        
    def push(self, item):
        if self.__len__() > 0:
            min_value = self.min_stack.peek()
            if(item < min_value):
                self.min_stack.push(item)
                super().push(item)
            else:
                self.min_stack.push(min_value)
                super().push(item)
        else:
           self.min_stack.push(item)
           super().push(item)
                
    def pop(self):
        self.min_stack.pop()
        return super().pop()
                
    def get_min(self):
        return self.min_stack.peek()