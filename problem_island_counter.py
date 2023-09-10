m1 = [[1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 1]]

def findIslandCount(input_matrix):
    island_counter=0
    row_count   = len(m1)
    column_count = len(m1[0])
    visited = set()
    for row in range(row_count):
        for col in range(column_count):
            if (row,col) not in visited and input_matrix[row][col]==1:
                if (row,col+1) in visited:
                    pass
                else:
                    print (row,col,input_matrix[row][col])
                    island_counter+=1
            # elif row==0 and input_matrix[row][col]==1:
                # island_counter=1
            if input_matrix[row][col]==1:
                visited.add((row,col))
                if col<column_count-1 and input_matrix[row][col+1]==1:
                    visited.add((row,col+1))
                if row<row_count-1 and input_matrix[row+1][col]==1:
                    visited.add((row+1,col))
    
    print (visited)
    return island_counter


print (findIslandCount(m1))
