def bubble_sort(items):
    
    n= len(items)
    no_swap = True
    
    for i in range(n):
        for j in range(0,n-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                no_swap = False
                
        if no_swap:
            break 
            
    return items
    
    
    
items = [6,3,7,9,4,2,1,6,7,8,9,10]

print(bubble_sort(items))