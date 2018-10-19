def k_most_freq(arr, k):
    
    counter = {}
    bucket = [None] * (len(arr) + 1)
    
    for el in arr:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1  
            
    for key, value in counter.items():
        if bucket[value]:
            bucket[value].append(key)
        else:
            bucket[value] = [key]  
            
    for i in range(len(bucket) - 1, -1, -1):
        while k > 0 and bucket[i]:
            print(bucket[i].pop())
            k -= 1
    
        