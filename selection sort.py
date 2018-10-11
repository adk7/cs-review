def selection_sort(items):
    
    n = len(items)
    
    for i in range(n):
        for j in range(i+1,n):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
                
    return items
    
    
items = [6,3,7,9,4,2,1,6,7,8,9,10]

print(selection_sort(items))