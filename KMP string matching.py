def KMP(string, pattern):
    
    kmp_indices = [0] * len(pattern)
    i = 0
    j = 1
    
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            kmp_indices[j] = i + 1
            i += 1 
            j += 1
            
        else:
            if i - 1 > 0:
                i = kmp_indices[i - 1]
            else:
                i = 0
            j += 1    
            
    
    i = 0
    j = 0
    
    while i < len(string):
        if string[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            i += 1
            j += 1
        else:
            j = kmp_indices[j - 1]
            i += 1
            
    return False
            