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

    for direction in directions :
        pos = (x, y)
        # Count position visits :
        visited_houses[pos] = visited_houses.get(pos, 0) + 1

        # Move
        if direction == '^' :
            x += 1
        elif direction == 'v' :
            x -= 1
        elif direction == '>' :
            y += 1
        else :
            y -= 1

    return len(visited_houses)

print(eggnog(input_3)) #FOUND

# --- Part Two ---

# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

#     ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
#     ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
#     ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

def robo_eggnog(directions:str) :
    x = 0
    y = 0
    x_robo = 0
    y_robo = 0

    visited_houses = {}
    visited_houses.setdefault((x, y), 2)

    for i in range(len(directions)) :
        if i % 2 == 0 : # Santa
            if directions[i] == '^' :
                x += 1
            elif directions[i] == 'v' :
                x -= 1
            elif directions[i] == '>' :
                y += 1
            else :
                y -= 1
            visited_houses[(x, y)] = visited_houses.get((x, y), 0) + 1
        else : # Robo Santas
            if directions[i] == '^' :
                x_robo += 1
            elif directions[i] == 'v' :
                x_robo -= 1
            elif directions[i] == '>' :
                y_robo += 1
            else :
                y_robo -= 1
            visited_houses[(x_robo, y_robo)] = visited_houses.get((x_robo, y_robo), 0) + 1

    return len(visited_houses)

print(robo_eggnog(input_3))