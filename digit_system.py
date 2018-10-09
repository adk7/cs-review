
def increment_by_one(given_number):
    
    system_of_digits = ['A', 'B', 'C', 'D']
    
    given_number = given_number[::-1]
    result = [given_number[i] for i in range(len(given_number))]
    
    for i in range(len(given_number)):
        digit = given_number[i]
        index = (system_of_digits.index(digit) + 1)
        if index < len(given_number): 
            next_digit = system_of_digits[index]
            result[i] = next_digit
            return result[::-1]
        else:
            index = index%len(system_of_digits)
            next_digit = system_of_digits[index]
            result[i] = next_digit
            
    result.append(system_of_digits[0])
    
    return result[::-1]
    