INPUT = "aaasssaaaaaabbbbbbbbccccccccsbabbbccc"
ALPHABET = {'a', 'b', 'c'}

def find_word(word, alphabet):
    
    i = j = 0
    min_len = float("inf")
    min_string = ""
    counter = {key: 0 for key in alphabet}
    count = 0
    required_count = len(alphabet)
    
    while j < len(word):
        w = word[j]
        if w in counter:
            counter[w] += 1
            if counter[w] == 1:
                count += 1 # if we are seeing letter for the first time
                
        if count == required_count:
            # This means we have encountered all the letters in alphabet in out current window
            while counter.get(word[i], 0) > 1:
                # move left pointer until the count of the character == 1
                i += 1
                counter[word[i]] -= 1
                
            window_length = j - i + 1
            if window_length < min_len:
                min_len = window_length
                min_string = word[i:j+1]
                
            counter = {key: 0 for key in alphabet}
            count = 0
            j = i
            i += 1  
            
        j += 1
    
    print(min_string, min_len)        

find_word(INPUT, ALPHABET)   