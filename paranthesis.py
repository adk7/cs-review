def paranthesis_match(expression):
    
    expression = list(expression)
    mapper = {'(':')', '{': '}', '[':']' }
    all_brackets = list(mapper.keys()) + list(mapper.values())
    
    expression = list(filter(lambda x: x in all_brackets, expression))
            
    if len(expression)%2 != 0:
        return False
        
    parenthesis_stack = []
        
    for ch in expression:
        if ch in mapper:
            parenthesis_stack.append(ch)
        else:
            p = parenthesis_stack.pop()
            if ch != mapper[p]:
                return False
        
    return True
            
    