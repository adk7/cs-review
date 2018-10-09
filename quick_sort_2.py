def quick_sort(items):
    
    n = len(items)
    return quick_sort_(items, 0, n-1)
    
    
    
def quick_sort_(items, low, high):
    
    if low < high:
        
        p = get_partition(items, low, high)
        quick_sort_(items, low, p-1)
        quick_sort_(items, p+1, high)


def get_partition(items, low, high):
    
    pivot_index = get_pivot_index(items, low, high)
    boundary = low
    
    items[low], items[pivot_index] = items[pivot_index], items[low]
    #print("Swapping pivot and first element: {}".format(items))
    for i in range(low, high+1):
        
        if items[i] < items[low]:
            boundary += 1            
            items[i], items[boundary] = items[boundary], items[i]
            #print("Swapping el {} and boundary {} element: {}".format(i, boundary, items))
            
    items[boundary], items[low] = items[low], items[boundary]
    #print("Swapping pivot and boundary element: {}".format(items))
        
    return boundary  
        
def get_pivot_index(items, low, high):
    
    mid = (high + low)//2
    
    s = sorted([items[low], items[mid], items[high]])
    
    if s[1] == items[low]:
        return low
    elif s[1] == items[mid]:
        return mid
    else:
        return high
              