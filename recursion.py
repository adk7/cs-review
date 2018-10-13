def recursive_reverse(string):
    
    if len(string) == 1:
        return string
        
    return recursive_reverse(string[1:]) + string[0]
    
    
def iterative_reverse(string):
    string = list(string)
    first = 0
    last = len(string) - 1
    
    
    while first < last:
        string[first] , string[last] = string[last], string[first]
        first += 1
        last -= 1
        
    return "".join(string)
        
        
def get_subsets(given_set, subsets=[]):
    
    if len(given_set) == 0:
        return [[]]
    
    first = given_set[0]
    subsets = get_subsets(given_set[1:])
    
    return subsets + [[first] + sub for sub in subsets]
    
    
    
        
    