def binary_search(sorted_list, item):
    return binary_search_(sorted_list, item, 0, len(sorted_list) - 1)
    
def binary_search_(sorted_list, item, first, last):
    
    if first < last: 
        mid = (first + last)//2
        
        if sorted_list[mid] > item:
            return binary_search_(sorted_list, item, first, mid - 1)
        elif sorted_list[mid] < item:
            return binary_search_(sorted_list, item, mid + 1, last)
        else:
            return mid
            
    if sorted_list[first] == item:
        return first
    else:
        return -1