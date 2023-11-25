'''Program to find maximum number of connnected 1's in the grid - even diagonal 1s are counted'''
def cellCounter(grid,row,col):
    if any([col<0,row<0,row>=len(grid),col>=len(grid[0])]):
        return 0
    if grid[row][col]==0:
        return 0
    cell_count=1
    grid[row][col]=0
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            if any([c!=col,r!=row]):
                cell_count+=cellCounter(grid,r,c)
    return cell_count

def maxCellCount(grid):
    max_cell_counter = 0
    for row in range(0,len(grid)):
        for col in range(0,len(grid[0])):
            if grid[row][col]==1:
                cell_count_region = cellCounter(grid,row,col)
                max_cell_counter=max(max_cell_counter,cell_count_region)
    
    return max_cell_counter



if __name__=="__main__":
    g = [[0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1]]
    print (maxCellCount(g))