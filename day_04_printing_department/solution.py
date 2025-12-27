import os

def read_input():
    # Construct the path relative to this script file
    file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(file_path, 'r') as f:
        # Read each line, strip whitespace, and convert to a list of characters
        return [list(line.strip()) for line in f]

grid = read_input()


def count_adjacent_rolls(grid, x, y) -> int:
    """ 
    This function counts the number of adjacent cells to the cell at (x, y) in the grid
    that contain the "@" symbol (representing rolls).
    The adjacent cells are:
      1 2 3
      4 X 6
      7 8 9
    Where X is (x, y).
    It returns the count of "@" in any of the 8 surrounding positions.
    The function also correctly handles grid boundaries.
    Define which positions are valid (in bounds)
    """
    valid_1 = x > 0 and y > 0
    valid_2 = x > 0
    valid_3 = x > 0 and y < len(grid[0]) - 1
    valid_4 = y > 0
    valid_6 = y < len(grid[0]) - 1
    valid_7 = x < len(grid) - 1 and y > 0
    valid_8 = x < len(grid) - 1
    valid_9 = x < len(grid) - 1 and y < len(grid[0]) - 1

    # Check each valid position for "@"
    count = 0
    if valid_1 and grid[x-1][y-1] == "@":
        count += 1
    if valid_2 and grid[x-1][y] == "@":
        count += 1
    if valid_3 and grid[x-1][y+1] == "@":
        count += 1
    if valid_4 and grid[x][y-1] == "@":
        count += 1
    if valid_6 and grid[x][y+1] == "@":
        count += 1
    if valid_7 and grid[x+1][y-1] == "@":
        count += 1
    if valid_8 and grid[x+1][y] == "@":
        count += 1
    if valid_9 and grid[x+1][y+1] == "@":
        count += 1
    
    return count

def count_accessible(grid):
    """ Given a grid, count the total number of accessible rolls. """
    total_accessible = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":  # Only count rolls, not empty cells
                cur_adjacent_rolls = count_adjacent_rolls(grid, x=row, y=col)
                if cur_adjacent_rolls < 4: 
                    total_accessible += 1
    return total_accessible


def count_accessible_with_iter_remove(grid):
    """ Given a grid, count the total number of accessible rolls by itereatively removing the rolls """
    total_accessible = 0
    iter_accesible = 1
    cur_grid = grid
    while iter_accesible != 0:
        next_grid = cur_grid
        iter_accesible = 0

        for row in range(len(cur_grid)):
            for col in range(len(cur_grid[0])):
                if cur_grid[row][col] == "@":
                    cur_adjacent_rolls = count_adjacent_rolls(cur_grid, x=row, y=col)
                    if cur_adjacent_rolls < 4:
                        iter_accesible += 1
                        next_grid[row][col] = "x"
        
        total_accessible += iter_accesible
        cur_grid = next_grid
    return total_accessible


