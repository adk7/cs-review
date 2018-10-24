def longest_increasing_subsequence(arr):
    
    T = [1] * len(arr)      # intermediate results
    final = list(range(len(arr))) # final solution for backtracking 
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                if T[j] + 1 > T[i]:
                    T[i] = T[j] + 1
                    final[i] = j 
                    
    max_len = max(T)
    index = T.index(max_len)
    seq = []
    
    while(len(seq) < max_len):
        seq.append(arr[index])
        index = final[index]
        
    return seq[::-1]
    
    

def longest_common_subsequence(str1, str2):
    import numpy as np
    
    T = np.array([[0] * (len(str2) + 1)] * (len(str1) + 1))
    
    for i in range(1 , len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                T[i][j] = 1 + T[i-1][j - 1]
            else: 
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
                
    return T
    
    
def min_jumps(arr):
    
    T = [0 if idx == 0 else float("inf") for idx in range(len(arr))]
    
    for i in range(1, len(arr)):
        for j in range(i):
            if i <= j + arr[j]:
                T[i] = min(T[i], T[j] + 1)
                
    return T