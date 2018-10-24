def merge_sort(items):
    return merge_sort_(items, 0, len(items)-1)

def merge_sort_(items, low, high):
    
    if(low < high):
        
        mid = (low+high)//2
        merge_sort_(items, low, mid)
        merge_sort_(items, mid+1, high)
        merge(items, low, mid, high)
            
def merge(items, low, mid, high):
  
    L = items[low:mid+1]
    R = items[mid+1:high+1]
    
    i = j = 0
    k = low
    
    while i < len(L) and j < len(R):
        
        if(L[i] <= R[j]):
            items[k] = L[i]
            i+=1
        else:
            items[k] = R[j]
            j+=1
     
        k+=1

    while i < len(L):
        items[k] = L[i]
        i+=1
        k+=1
        
    while j < len(R):
        items[k] = R[j]
        j+=1
        k+=1
    