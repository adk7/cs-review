def anagrams(word):
    
    if len(word) == 1:
        return [word]
    
    first = word[0]
    a = anagrams(word[1:])
    
    return [w[:i] + first + w[i:] for w in a for i in range(len(w)+1) ]