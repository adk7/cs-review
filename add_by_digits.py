def add_by_digits(list1, list2):
    
    list1 = list1[::-1]
    list2 = list2[::-1]
    sum_list = []
    
    i = j = 0 
    carry = 0
    
    while i < len(list1):
        if j < len(list2):
            sum_int = list1[i] + list2[j] + carry
        else:
            sum_int = list1[i] + carry
            
        sum_str = str(sum_int)
        
        if(len(sum_str) > 1):
            carry = int(sum_str[0])
            sum_list.append(int(sum_str[1]))
        else:
            sum_list.append(sum_int)
            carry = 0
        
        i += 1 
        j += 1
        
    return sum_list[::-1]
        
        
list1 = [1, 2,5,4]
list2 = [6,9]

print(add_by_digits(list1,list2))