def encode(string):
    
    if not string:
        return ""
        
    check_char = string[0]
    count = 1
    for char in string[1:]:
        if check_char == char:
            count+=1
            
    return str(count)+check_char + encode(string[count:])
    
    
def decode(string):
    
    
    original_string = ""
    
    count = ""
    
    for char in string:
        if char.isdigit():
            count+=char
        else:
            for i in range(int(count)):
                original_string += char
            count = ""
            
    return original_string