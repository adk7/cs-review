class Cell(object):
    
    def __init__(self, cell_id, is_final, neighbors):
        
        self.cell_id = cell_id
        self.is_final = is_final
        self.neighbours = neighbors
        
    def __repr__(self):
        return str(self.cell_id)
        

def find_path(current_cell, current_path):
    
    if current_cell.is_final:
        return True
        
    neighbours = current_cell.neighbours
    current_path_copy = current_path.copy()
    current_path_copy.append(current_cell)
    
    for n in neighbours:
        if n not in current_path and find_path(n, current_path_copy):
            for cell in current_path_copy:
                print(cell)
                
            return True
            
  