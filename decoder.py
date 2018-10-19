import string

a2i = dict(zip(string.ascii_lowercase,
               (str(x) for x in range(1, len(string.ascii_lowercase)+1))))
i2a = dict(zip(a2i.values(), a2i.keys()))


def all_strings(data, k, results=set([""])):
    
    if k == 0:
        return results
        
    i = len(data) - k
    
    found_1 = set()
    key_1 = data[i]
    if key_1 != "0":
        found_1 = all_strings(data, k - 1, {s + i2a[key_1] for s in results})
    else:
        return set([""])
        
    found_2 = set()
    
    if k > 1:
        key_2 = data[i:i + 2]
        if key_2 in i2a:
            found_2 = all_strings(data, k - 2, {s + i2a[key_2] for s in results})
            
    return found_1.union(found_2)
    
def decode(data):
    return all_strings(data, len(data))