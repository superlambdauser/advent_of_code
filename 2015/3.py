# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:

#     > delivers presents to 2 houses: one at the starting location, and one to the east.
#     ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
#     ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
from inputs import input_3

def eggnog(directions:str) :
    x = 0
    y = 0

    visited_houses = {}

    for dir in directions :
        pos = (x, y)
        # Count position visits :
        visited_houses[pos] = visited_houses.get(pos, 0) + 1

        # Move
        if dir == '^' :
            x += 1
        elif dir == 'v' :
            x -= 1
        elif dir == '>' :
            y += 1
        else :
            y -= 1

    return len(visited_houses)

print(eggnog(input_3)) #FOUND
