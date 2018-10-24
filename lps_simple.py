from functools import lru_cache
import numpy as np

@lru_cache()
def lps(seq, start, l):
    
    if l == 1:
        return 1
        
    if l == 0:
        return 0
        
    if seq[start] == seq[start + l -1]:
        return 2 + lps(seq, start + 1, l - 2) 
    else: 
        return max(lps(seq, start, l -1), lps(seq, start + 1, l -1))
     
        
def longest_palindrome(string):
    n = len(string)
    return lps(string, 0, n)
    

    