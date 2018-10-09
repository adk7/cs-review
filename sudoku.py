def is_valid_sudoku(board):
    
    if not is_valid_rows_and_cols(board):
        return False
        
    if not is_valid_blocks(board):
        return False
        
    return True
    
    
def is_valid_rows_and_cols(board):
    n = 9
    row_list = [set() for _ in range(n)] 
    col_list = [set() for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            num = board[row][col]
            if num == -1:
                continue
            if num in row_list[row] or num in col_list[col]:
                return False
                
            row_list[row].add(num)
            col_list[col].add(num)
            
    return True
    
    
def is_valid_blocks(board):
    
    n = 9
    block_list = [set() for _ in range(9)]
    
    for row in range(n):
        for col in range(n):
            num = board[row][col]
            
            if num == -1:
                continue
                
            block_index = get_block_index(row, col)
            if num in block_list[block_index]:
                return False
                
            block_list[block_index].add(num)
            
    return True
    
    
def get_block_index(row, col):
    return (3 * (row//3)) + (col//3)
    
    
def rotate_list(items, n):
    result = []
    for i in range(len(items)):
        result.append(items[(i+n)%len(items)])
        
    return result
    
def get_rotation_n(row_n):
    
    return ((row_n//3) + (3*(row_n%3)))
        