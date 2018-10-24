def longest_repeated_subsequence(word):
    import numpy as np
    
    n = len(word)
    T = np.array([[0]*(n + 1)] * (n + 1))
    
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            i = row - 1
            j = col - 1
            if i != j and word[i] == word[j]:
                T[row][col] = 1 + T[i][j]
            else:
                T[row][col] = max(T[row][j], T[i][col])
    return T