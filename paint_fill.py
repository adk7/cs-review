def paint_fill(matrix, row_clicked, col_clicked, old_color, new_color):
    
    total_rows, total_cols = matrix.shape
    
    if row_clicked < 0 or row_clicked >= total_rows or col_clicked < 0 or col_clicked >= total_cols:
        return
        
    if matrix[row_clicked][col_clicked] != old_color:
        return
    
    matrix[row_clicked][col_clicked] = new_color
    
    for row in range(row_clicked - 1, row_clicked + 2):
        for col in range(col_clicked - 1, col_clicked + 2):
            paint_fill(matrix, row, col, old_color, new_color)
            
            
            
def paint_fill_better(matrix, row_clicked, col_clicked, old_color, new_color):
    
    total_rows, total_cols = matrix.shape
    
    if matrix[row_clicked][col_clicked] != old_color:
        return
    
    matrix[row_clicked][col_clicked] = new_color
    
    for row in range(row_clicked - 1, row_clicked + 2):
        for col in range(col_clicked - 1, col_clicked + 2):
            if row < 0 or row >= total_rows or col < 0 or col >= total_cols:
                continue
            else:
                paint_fill(matrix, row, col, old_color, new_color)
                
                
def paint_fill_bfs(matrix, row_clicked, col_clicked, old_color, new_color):
    '''
    Using Breadth First Search
    Consider this as a tree traversal problem where each node is connected to 9 neighbouring nodes
    '''
    import queue
    to_check = queue.Queue()
    
    total_rows, total_cols = matrix.shape
    
    if matrix[row_clicked][col_clicked] != old_color:
        return
    
    matrix[row_clicked][col_clicked] = new_color
    
    to_check.put((row_clicked, col_clicked))
    
    while not to_check.empty():
        current_row, current_col = to_check.get()
        for row in range(current_row - 1, current_row + 2):
            for col in range(current_col - 1, current_col + 2):
                if row >= 0 and row < total_rows and col >= 0 and col < total_cols:
                    if matrix[row][col] == old_color:
                        matrix[row][col] = new_color
                        to_check.put((row,col))