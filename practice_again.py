def longest_consequitive_character(string):
    
    max_count = 0
    max_char = None
    prev_char = None
    
    count = 0
    #AAB
    for i in range(1, len(string)):
        current_char = string[i]
        
        if current_char == prev_char:
            count += 1
        else:
            count = 1
        
        if count > max_count:
            max_count = count
            max_char = current_char
            
        prev_char = current_char
                   
    return {max_char: max_count}
    
    
class Node(object):
    
    def __init__(self, val, left = None, right = None):
        
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return "Node('{.val}', {.left}, {})".format(self, self, self.right)
        
   
def cutting_rod(prices, length):
    
    if length == 0:
        return 0
        
    max_value = 0
    
    for i in range(0, length):
        val = prices[i] + cutting_rod(prices, length - i - 1)
        
        if val > max_value:
            max_value = val
            
    return max_value
    
        
        
def egg_breaking(num_eggs, num_floors):
    
    if num_eggs == 1 or num_floors == 1:
        return num_floors
        
    if num_eggs < 1 or num_floors < 1:
        return 0
        
    min_attempts = 1000
    
    for i in range(1, num_floors + 1):
        val = 1 + max(egg_breaking(num_eggs - 1, i - 1), egg_breaking(num_eggs, num_floors - i))
        
        if val < min_attempts:
            min_attempts = val
            
    return min_attempts
        
                    
def subset_sum(given_set, total):
    
    if total == 0:
        return True
        
    if not given_set:
        return False
        
    if len(given_set) == 1:
        return total == given_set[0]
        
    
    for i in range(len(given_set)):
        curr = given_set[i]
        left = subset_sum(given_set[:i], total - curr)
        right = subset_sum(given_set[i+1:], total - curr)
        
        if left or right:
            return True
    
    return False
         