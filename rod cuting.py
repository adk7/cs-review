from functools import lru_cache

prices = [2,5,7,8]

@lru_cache()
def max_value(length):
    
    if length <= 0:
        return 0
        
    max_v = 0
    
    for i in range(length):
        print(i)
        value = prices[i] + max_value(length - i - 1)
        
        if value > max_v:
            max_v = value
            
    return max_v
    
    