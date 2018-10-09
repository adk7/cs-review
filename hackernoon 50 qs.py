def sum_of_consequitive_series(series):
    '''
    This function assumes you are passing in a consequitive series of natural numbers starting from 1
    '''
    n = len(series)
    return (n*(n+1))/2

def missing_number(given_list):
    
    '''
    given a list from 1 to 100 with one missing number, return the missing number
    '''
    check_sum = sum_of_consequitive_series(range(100))
    actual_sum = sum(given_list)
    
    return check_sum - actual_sum


        
def get_duplicates(given_list):
    '''
    return all duplicates from given_list of integers
    I chose to return a set of dups, you can also return a dictionary of dups with the count of occurences
    '''
    
    dups = set()
    already_seen = set()
    
    for el in given_list:
        if el in already_seen:
            dups.add(el)
        else:
            already_seen.add(el)
    return dups
    
def check_sum(given_list, given_sum):
    '''
    given a list of integers return all pairs of integers that add to given_sum
    '''
    
    result = []
    already_seen = set()
    
    for num in given_list:
        diff = given_sum - num
        if diff in already_seen:
            result.append((num, diff))
        already_seen.add(num)
        
    return result
        
def remove_dups(given_list):
    '''
    easiest sol is list(set(given_list))
    but for the sake of it, let's use a counter
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    
    counter = {} 
    result = []
    
    for num in given_list:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
            
    for num in given_list:
        if counter[num] == 1:
            result.append(num)
            
    return result
    
def quick_sort(items):
    '''
    sort items using quick sort recursive algo
    '''
    return quick_sort_(items, 0, len(items) - 1)
    

def quick_sort_(items, low, high):
    
    if(low < high):
               
        p = partition(items, low, high) # get partition p such that everything on the left side of p is less than items[p] and everything on the right is > p
        quick_sort_(items, low, p - 1)  # recursive call on the items left side of p
        quick_sort_(items, p + 1, high) # recurive call on the right side of p

def get_pivot(A, low, hi):
    '''
    return the median value of A[low], A[mid], A[hi]
    '''
    mid = (hi + low) // 2
    s = sorted([A[low], A[mid], A[hi]])
    if s[1] == A[low]:
        return low
    elif s[1] == A[mid]:
        return mid
    return hi
        
def partition(items, low, high):
    
    pivot_index = get_pivot(items,low,high) # get the median and set as pivot
    pivot_value = items[pivot_index] 
    
    items[pivot_index], items[low] = items[low], items[pivot_index] # swap pivot with left most element
    border = low # intitialize border to low, border indicates the partition p such that everything less that p is on the left and > than p is on right
    
    for i in range(low, high+1):
        if items[i] < pivot_value:
            border += 1
            items[i], items[border] = items[border], items[i]
            print(items)
    
    items[low], items[border] = items[border], items[low] # swap pivot with border after loop is complete
    return(border)        
        
        

def string_duplicates(string):
    '''
    This is no different from getting dups from an integer array
    but it would make sense to return a string output rather than a list. 
    '''        
    
    return get_duplicates(string)
                    
def is_anagram(string1, string2):
    
    if len(string1) != len(string2):
        return False
        
    counter_1 = {}
    counter_2 = {}
    
    for char in string1:
        if char in counter_1:
            counter_1[char] += 1
        else:
            counter_1[char] = 1
            
    for char in string2:
        if char in counter_2:
            counter_2[char] += 1
        else:
            counter_2[char] = 1
            
        
    return counter_1 == counter_2
    
                    
                                    
def first_non_repeating(string):
    
    counter = dict()
    
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
            
    for char in string:
        if counter[char] > 1:
            return char                
                    
def recursive_reverse(string, start=0):
    '''
    reverse a string recursively
    '''
    if len(string[start:]) <= 1:
        return string[start:]
        
    else:
        return recursive_reverse(string, start+1) + string[start]
        
        
def check_only_digits(string):
    '''
    If I am not allowed to use isdigit, 
    ord() returns ascii of the char
    check if ascii value is int he range of 48 to 57
    '''
    
    for char in string:
        if not char.isdigit():
            return False
        return True
        
def check_only_digits_primitive(string):
    '''
    using ASCII
    '''
    
    for char in string:
        ascii = ord(char)
        if not ord("0") <= ascii <= ord("9"):
            return False
    return True
        
        
def count_vowels_and_consonants(string):
    
    vowels = list("aeiou")
    consonants= list("bcdfghjklmnpqrstvwxyz")
    
    counter_v = 0
    counter_c = 0
    
    for char in string:
        if char in vowels:
            counter_v += 1
        if char in consonants:
            counter_c += 1
            
    print("In string '{}', there are {} vowels and {} consonants".format(string, counter_v, counter_c))
    
    
def character_counter(string):
    '''
    Pythonic soultion is to use counter from collections module
    ''' 
    from collections import defaultdict # to avoid key error when passing a char that hasnt occured in string
    counter = defaultdict(int)
    
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
            
    return counter
    
def one_character_counter(string,char):
    counter = character_counter(string)
    
    return counter[char]

def permutations(string):
    '''
    use itertools and get it over with! 
    Dont remember the recursicve solution
    '''
    string_list = list(string)
    n = len(string)
    

def reverse_words(sentence):
    
    sentence = sentence.split(" ")
    
    return " ".join([recursive_reverse(word) for word in sentence])
    
    
def check_rotation(string1, string2):
    
    
    if len(string1) != len(string2):
        return False
        
    n = len(string1)
    
    key = string1[0]
    key_index = string2.index(key)
    
    i = j = 0
    
    for i in range(n):
        if string1[i] != string2[(key_index + i) % n]:
            return False
    return True