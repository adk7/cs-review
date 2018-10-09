def check_for_sum(items, total):
    
    l = 0
    r = len(items) - 1
    
    
    while(l<r):
        
        sum_l_r = items[l] + items[r]
    
        if(sum_l_r == total):
            return True
            
        elif(sum_l_r < total):
            l+=1
        else:
            r-=1
            
    return False
    
    
def first_recurring(given_string):
    
    already_seen = set()
    for i in range(len(given_string)):
        
        if(given_string[i] in already_seen):
            return given_string[i]
            
        else:
            already_seen.add(given_string[i])
        
    return "Not Found"
    
    

def most_common(numbers):
    
    '''
    diff **
    return the most commonly occuring number from a list
    '''
    
    max_num = None
    max_count = -1
    counter = dict()
    
    for num in numbers:
        if(num in counter):
            counter[num] += 1
            if(counter[num] > max_count):
                max_count = counter[num]
                max_num = num
        else:
            counter[num] = 1
            
    return (max_num, max_count)
    
    
    
    
    
def is_rotation(A,B):
    '''
    diff **
    Check if one list is the rotation of the other
    assumptions: No duplicates    
    '''
    
    if len(A) != len(B):
        return False
        
    key = A[0]
    
    try:
        key_i = B.index(key)
    except ValueError:
        return False
    
    for i in range(len(A)):
        j = ((key_i) + i) % len(A)
        
        if A[i] != B[j]:
            return False
            
    return True
    
    
def common_elements(list1, list2):
    '''
    diff *
    return list of common elements in list1 and list2 
    assumptions: list1 and list2 are sorted, no dups
    '''    
    
    results = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        
        if list1[i] == list2[j]:
            results.append(list1[i])
            i+=1
            j+=1
        elif list1[i] > list2[j]:
            j+=1
        else:
            i+=1
            
    return results
    
    
def non_repeating(given_string):
    
    '''
    diff **
    return the first non repeating character from a string
    '''
    
    counter = {}
    
    for char in given_string:
        
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
            
    for char in given_string:
        
        if counter[char] == 1:
            return char
            
    return None
    
    
    
    
def is_one_away(s1, s2):
    '''
    takes two strings and returns True if they are one edit away frome each other
    '''
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    
    len_diff = len_s2 - len_s1
    
    if(len_diff > 1 or len_diff < -1):
        return False
        
    if(len_diff == 0):
        return one_away_equal_len(s1,s2)
        
    if(len_diff == -1):
        return one_away_diff_len(s1,s2)
    else:
        return one_away_diff_len(s2,s1)
        
def one_away_equal_len(s1,s2):
    
    count_edits = 0
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count_edits += 1
            if count_edits > 1:
                return False
   
    return True 
    
    
def one_away_diff_len(s1, s2):
    '''
    assumptions: s2 is shorter and s1
    '''
    
    i = 0
    count_diff = 0
    
    while(i < len(s2)):
        if s2[i] == s1[i + count_diff]:
            i+=1
        else:
            count_diff += 1
            if count_diff > 1:
                return False
                
    return True
                    
                    
    
    
def subsets(s):
    sets = []
    for i in range(1 << len(s)):
        subset = [s[bit] for bit in range(len(s)) if is_bit_set(i, bit)]
        sets.append(subset)
    return sets

def is_bit_set(num, bit):
    return num & (1 << bit) > 0
    
    
def palindrome(input_string):
    import string
    punctuations = string.punctuation + " "
    table = str.maketrans({key: None for key in punctuations})
    string = input_string.translate(table)
    return input_string == string[::-1]

    
            