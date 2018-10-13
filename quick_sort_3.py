def quick_sort(items):
    quick_sort_(items, 0, len(items)-1)
    
    
def quick_sort_(items, first, last):
    
    if first < last:
        p = get_partition(items, first, last)
        quick_sort_(items, first, p - 1)
        quick_sort_(items, p + 1, last)
        
def get_partition(items, first, last):
    pivot = items[first]
    boundary = first
    
    for i in range(first, last + 1):
        
        if pivot > items[i]:
            boundary += 1
            items[boundary], items[i] = items[i], items[boundary]
            
    items[first], items[boundary] = items[boundary], items[first]
    
    return boundary