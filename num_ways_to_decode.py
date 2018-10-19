def num_ways(data):
    #call helper
    return num_ways_(data, len(data))
    
def num_ways_(data,k):
    """
    data: Encoded String
    k: Number of characters from the end of the string to consider in each recursion
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

                
def num_ways_dp(data):
    """
    Alternative, more effecient solution
    Store intermediate results in a cache list to avoid recomputation
    """
    cache = [None] * (len(data) + 1)
    return num_ways_dp_(data, len(data), cache)    
            
def num_ways_dp_(data, k, cache):
    """
    Helper function using Dynamic Programming
    
    data: Encoded String
    k: Number of characters from the end of the string to consider in each recursion
    cache: Store intermediate results to avoid recomputation 
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

def decode(data, k):
    from itertools import zip_longest
    
    mapper = dict(zip_longest(range(1,27), list("abcdefghijklmnopqrstuvwxyz")))
    
    if k == 0:
        return ""
        
    i = len(data) - k
    
    if data[i] == '0':
        return ""   
    
    results = []  
    key_1 = data[i]
    key_2 = data[i:i+2]
    
    if key_1 in mapper:
        ans_1 = mapper[key_1] + decode(data, k -1)
    else:
        ans_1 = ""
     
    if key_2 in mapper:
        ans_2 = mapper[key_2] + decode(data, k -2)
    else:
        ans_1 = ""
        
  