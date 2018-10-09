def chunkify(string, chunk_size=5, delim=":"):
    
    paragraphs = string.split(":")
    
    chunk_list = []
    current_chunk = ""
    
    for p in paragraphs:
        
        if len(current_chunk) + len(p) > chunk_size:
            if len(current_chunk) > 0:
                chunk_list.append(current_chunk)
                current_chunk = ""
                
        if len(p) > chunk_size:
            if len(current_chunk) > 0:
                chunk_list.append(current_chunk)
                current_chunk = ""
            chunk_list.append(p + delim)
            continue
        
        current_chunk += p + delim      
        
                
    if len(current_chunk) > 0:
        chunk_list.append(current_chunk)
        
    yield from chunk_list