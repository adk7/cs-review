from functools import lru_cache
import numpy as np

#@lru_cache()
def longest_plaindromic_subsequence(seq, start, l, cache):
    
    if l == 1:
        cache[start][start+l - 1] = 1
        return 1
        
    if l == 0:
        return 0
        
    if cache[start][start+l - 1]:
        return cache[start][start+l - 1]
        
    if seq[start] == seq[start + l -1]:
        r = 2 + longest_plaindromic_subsequence(seq, start + 1, l - 2, cache) 
    else: 
        r = max(longest_plaindromic_subsequence(seq, start, l -1, cache), longest_plaindromic_subsequence(seq, start + 1, l -1, cache))
    
    cache[start][start+l - 1] = r
    return r  
        
def lps(string):
    n = len(string)
    cache = np.array([[None] * n] * n)
    palindrome_len =  longest_plaindromic_subsequence(string, 0, len(string), cache)
    
    palindrome = [None] * palindrome_len
    i = 0
    j = n - 1
    
    start = 0
    end = palindrome_len - 1
    
    while start < end:
        if string[i] == string[j]:
            palindrome[start] = palindrome[end] = string[i]
            i += 1
            j -= 1
            start += 1
            end -= 1
        else:
            print(i, j)
            if cache[i + 1][j] > cache[i][j - 1]:
                i += 1
            else:
                j -= 1
                
    if start == end:
        palindrome[start] = string[i]
        
    print(palindrome)
    return palindrome_len
    
    