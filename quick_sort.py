def quick_sort(items):
    return quick_sort_(items, 0, len(items) - 1)
    

def quick_sort_(items, low, high):
    
    if(low < high):
               
        p = partition(items, low, high)
        quick_sort_(items, low, p - 1)
        quick_sort_(items, p + 1, high)

def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi
        
def partition(items, low, high):
    
    pivot_index = get_pivot(items,low,high)
    pivot_value = items[pivot_index]
    
    items[pivot_index], items[low] = items[low], items[pivot_index]
    border = low
    
    for i in range(low, high+1):
        if items[i] < pivot_value:
            border += 1
            items[i], items[border] = items[border], items[i]
            print(items)
    
    items[low], items[border] = items[border], items[low]       
    return(border)        
    