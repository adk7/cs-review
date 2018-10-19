class Node(object):
    
    def __init__(self, value, left=None, right=None):
        
        self.value = value
        self.left = left
        self.right = right
        
    def __repr__(self):
        return "Tree Node with value {}".format(self.value)
        
    def __eq__(self, other):
        return self.value == other.value
        

def is_unival(root):
    
    if not root:
        return True
        
    if root.left and root.value != root.left.value:
        return False
        
    if root.right and root.value != root.right.value:
        return False
        
    if is_unival(root.left) and is_unival(root.right):
        return True
        
    return False
        
def count_unival(root):
    
    if not root:
        return 0
        
    count = 0
    
    if is_unival(root):
        count += 1
        
    return count + count_unival(root.left) + count_unival(root.right)
    
    
def largest_square_matrix(matrix):
    """
    Given a matrix with only 1's and 0's, return the largest square matrix that has only 1's within the original matrix
    """
    
    n_rows, n_cols = matrix.shape
    cache = matrix.copy()
    max_square = 1
    
    for i in range(n_rows):
        for j in range(n_cols):
            
            if i - 1 >= 0 and j - 1 >= 0 and matrix[i][j] > 0:
                cache[i][j] += min(cache[i-1][j-1], cache[i-1][j], cache[i][j-1])
                
            if cache[i][j] > max_square:
                max_square = cache[i][j]
                
    print(cache)
    return max_square
   
        
   
def max_area_in_histogram(heights) :
    """
    Given heights array which stores the heights of a histogram, find the max are of a rectangle
    """
    
    max_area = 0
    index_stack = range(len(heights))
    
    
        
    

def fib(n): 
    """
    This is innefctive and slow. 
    """
    if n == 1 or n == 2: 
        return 1
    
    return fib(n-1) + fib(n-2)
        
        

def fib_(n, memo):
    
    if memo[n]:
        return memo[n]
    
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_(n-1, memo) + fib_(n-2, memo)
        
    memo[n] = result
    
    return result
    
def fib_better(n):
    memo = [None]* (n+1)
    return fib_(n, memo)
    
    
def fib_bottom_up(n):
    
    if n == 1 or n == 2:
        return 1
        
    bottom_up = [None] * (n+1)
    bottom_up[1] = bottom_up[2] = 1
    
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        
    return bottom_up[n]
    
    
def fib_gen():
   
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
    
    
def k_most_freq(items, k):
    
    counter = dict()
    for el in items:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
    
    bucket = [None] * (len(items) + 1)                
    for key, value in counter.items():
        if bucket[value]:
            bucket[value].append(key)
        else:
            bucket[value] = [key]
    
    results = []
    for i in range(len(items), 0, -1):
        if(bucket[i]):
            for el in bucket[i]:
                if len(results) < k:
                    results.append(el)
                else:
                    return results
                    
    return results
        
        
def paranthesis_match(expression):
    import itertools
    
    open_brackets = list("{[(")
    close_brackets = list("}])")
    mapper = dict(itertools.zip_longest(open_brackets, close_brackets))
    
    stack = []
    
    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if len(stack) == 0 or char != mapper[stack.pop()]:
                return False
    
    if len(stack) == 0:            
        return True
    else:
        return False
            
    
def move_0s_in_place(array):
    
    last_index = len(array) - 1
    first_index = 0
    
    while(first_index < last_index):
        if array[first_index] == 0:
            while(first_index < last_index and array[last_index] == 0):
                last_index -= 1
            array[first_index], array[last_index] = array[last_index], array[first_index]
            
        first_index += 1
        
    return array
    
    
def recursive_deque(stack):
    """
    Implement Queue dequeue operation with a stack
    """
    if len(stack) == 1:
        return stack.pop()
        
    top = stack.pop()
    first = recursive_deque(stack)
    stack.append(top)
    
    return first
    
    
def odd_occuring_integer(array):
    """
    Given an array with integers that repeat even number of times except one integer, 
    output the integer that repeats odd number of times
    """
    
    counter = dict()
    
    for num in array:
        if num in counter:
            del counter[num]
        else:
            counter[num] = 1
            
    return counter.popitem()
    
    
class Node(object):
    
    def __init__(self, value, left = None, right = None):
        
        self.value = value
        self.left = left
        self.right = right
        
    def __repr__(self):
        
        return "Tree Node with value {}".format(self.value)
        

def BFS(root):
    """
    Print Tree Level by level
    """
    
    from collections import deque
    
    if not root:
        return
    
    level = 1
    to_process = deque()
    to_process.append((root,level))
    
    while(len(to_process) != 0):
        
        current_node, current_level = to_process.popleft()
        
        if current_level > level:
            print("\n")
            level += 1
        
        print(current_node.value, end=" ")
                
        if current_node.left:
            to_process.append((current_node.left, current_level+1))
                
        if current_node.right:
            to_process.append((current_node.right, current_level+1))
                     
        
def num_ways_to_decode(string):
    
    if not string:
        return 1
        
    if len(string) == 1:
        return 1
    
    num_ways = 0
        
    key_1 = int(string[0])
    key_2 = int(string[0:2]) 
    
    if key_1 in range(1,27):
        num_ways += num_ways_to_decode(string[1:])
    if key_2 in range(1,27):
        num_ways += num_ways_to_decode(string[2:])
        
    return num_ways
    

    
def num_ways_(data,k):
    """
    Look only at last k characters of string
    """
    if k == 0:
        return 1
        
    i = len(data) - k
    if data[i] == '0':
        return 0 
    
    result = num_ways_(data, k - 1)    
            
    if k >= 2 and int(data[i:i+2]) <= 26:
        result += num_ways_(data, k - 2)
    
    return result
    
            
def num_ways(data):
    return num_ways_(data, len(data))
    
    
def num_ways_dp_(data, k, cache):
    """
    Using Dynamic Programming
    """
    if k == 0:
        return 1
        
    i = len(data) - k
    if data[i] == '0':
        return 0 
    
    if cache[k]:
        return cache[k]
        
    result = num_ways_dp_(data, k - 1, cache)    
            
    if k >= 2 and int(data[i:i+2]) <= 26:
        result += num_ways_dp_(data, k - 2, cache)
    
    cache[k] = result
    return result
    
            
def num_ways_dp(data):
    cache = [None] * (len(data) + 1)
    return num_ways_dp_(data, len(data), cache)
    
    
def product_of_array(array, index):
    
    left = [1] * len(array)
    right = [1] * len(array)
    
    prod_left = 1
    prod_right = 1
    
    for i in range(1, len(array)):
        prod_left *= array[i - 1]
        left[i] = prod_left
        
    for i in range(len(array) - 2, -1, -1):
        prod_right *= array[i + 1]
        right[i] = prod_right
        
    return left[index] * right[index]