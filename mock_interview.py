"""
Given an array of integers representing heights in a bar graph / skyline, determine the volume of water that it can hold.

Input: An array of positive integers that represent the heights of bars in a bar chart.

Output: The number of "units" of water that the bar chart can hold.

Note that water "spills over" the sides if there's nothing to contain it. 
Formally, a cell can contain water if, and only if, it has a wall to its right and a wall to its left.
  
Input: [5, 3, 2, 1, 5]
Output: 9

#...#
#...#
##..#
###.#
#####

Input: [2, 4, 1, 5, 3]
Output: 3

   #
 #.#
 #.##
##.##
#####

Input: [2, 1, 5, 1, 3]
Output: 3

  #
  #
  #.#
#.#.#
#####

"""


def vol_water(bar_graph):
    n = len(bar_graph)
    left = [None] * n
    right = [None] * n

    max_left = 0
    max_right = 0
    volume = 0

    for i in range(1,n):
        if bar_graph[i-1] > max_left:
            max_left = bar_graph[i-1]
        left[i] = max_left

    for i in range(n-1, -1, -1):
        if bar_graph[i + 1] > max_right:
            max_right = bar_graph[i + 1]
        right[i] = max_right

    #Input: [2, 1, 5, 1, 3]
    for i in range(1,n-1):
        v = min( (left[i] - bar_graph[i]) , (right[i] - bar_graph[i] ))
        if v > 0:
            volume += v

    return volume




"""
Write a function that takes an input string and a character set and returns the minimum-length substring which contains every 
letter of the character set at least once, in any order
If you don't find a match, return an empty string

Example:
Input: "aabbcb"
Alphabet: {'a', 'b', 'c'}
Output: "abbc"

Input: "aaaaaaaaaabbbbbbbbccccccccsbabbbccc"
Alphabet: {'a', 'b', 'c'}
Output: "csba"

Input: "aaaaaaaaaabbbbbbbbccccccccsbabbbccc"
Alphabet: {'a', 'b', 'c', 'f'}
Output: ""
"""



def smallest_substring(input_string, alphabet):
    
    left = right = 0
    count = 0
    required_count = len(alphabet)
    window_count = {}
    min_len = len(input_string)
    
    while right < len(input_string):
        char = input_string[right]
        if char in window_count:
            window_count[char] += 1
        else:
            window_count[char] = 1
            if char in alphabet:
                count += 1
                
        if count == required_count:
            while(left < right):
                if input_string[left] == input_string[left + 1]:
                    window_count[input_string[left]] -= 1
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    