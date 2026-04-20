# You enter a large cavern full of rare bioluminescent dumbo octopuses! They seem to not like the Christmas lights on your submarine, so you turn them off for now.

# There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy over time and flashes brightly for a moment when its energy is full. Although your lights are off, maybe you could navigate through the cave without disturbing the octopuses if you could predict when the flashes of light will happen.

# Each octopus has an energy level - your submarine can remotely measure the energy level of each octopus (your puzzle input). For example:

# 5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526
# The energy level of each octopus is a value between 0 and 9. Here, the top-left octopus has an energy level of 5, the bottom-right one has an energy level of 6, and so on.

# You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

# First, the energy level of each octopus increases by 1.
# Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
# Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
# Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy. Consider the middle octopus with 1 energy in this situation:

# Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are there after 100 steps?

from day_11_input import energy_levels

def text_to_grid(text_input:str) -> list[list[int]] : # Build the grid
    return [[int(char) for char in line] for line in text_input.splitlines()]

def get_neighbors(grid:list[list[int]], row:int, col: int) -> list[tuple]: # Get all neighbors coordinates of a cell at (row, col) position
    rows, cols = len(grid), len(grid[0])
    
    neighbors = []
    for row_offset in [-1, 0, 1] : # y offset : up, same row, down
        for col_offset in [-1, 0, 1] : # x offset : left, same col, right
            if row_offset == col_offset == 0 : # Skips itself (no vertical nor horizontal offset)
                continue
            
            neighbor_row, neighbor_col = row + row_offset, col + col_offset
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols : # Only return neighbors if they are inside the grid bounds
                neighbors.append((neighbor_row, neighbor_col))
    
    return neighbors
            
def step(grid:list[list[int]]) -> int :
    rows, cols = len(grid), len(grid[0]) # Grid size

    # Step 1 : All octopuses gain energy + 1
    for row in range(rows) :
        for col in range(cols) :
            grid[row][col] += 1

    # Step 2 : Chained reaction :
    flashed = set()
    new_flash_occured = True 
    while new_flash_occured :
        new_flash_occured = False
        for row in range(rows) :
            for col in range(cols) :
                if grid[row][col] > 9 and (row, col) not in flashed : # Detect all flashing octopuses that have not registered yet
                    flashed.add((row, col)) # Register octopus
                    new_flash_occured = True # Trigger reaction again
                    for neighbor_row, neighbor_col in get_neighbors(grid, row, col) :
                        grid[neighbor_row][neighbor_col] += 1 

    # Step 3 : Reset all of the flashing octopuses to 0 
    for row, col in flashed :
        grid[row][col] = 0

    return len(flashed) # Return amount of flashes for the step

def simulate(octopuses:str, steps:int=100) -> int :
    grid = text_to_grid(octopuses)
    return sum(step(grid) for _ in range(steps)) # Return total amount of flashes 

def find_sync(octopuses:str) :
    grid = text_to_grid(octopuses)

    step_count = 0
    while True : # Will break as soon as found
        step_count += 1
        flashes = step(grid)
        if flashes == len(''.join(octopuses.splitlines())) :
            return step_count
        
def run(octopuses) :
    grid = text_to_grid(octopuses)

print(simulate(energy_levels))
print(find_sync(energy_levels))