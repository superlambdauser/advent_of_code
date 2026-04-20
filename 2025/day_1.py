    # PART 1
# The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. 
# A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). 
# Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

# So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.
# Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.
# So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.

# The dial starts by pointing at 50.

# You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. 
# The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

# For example, suppose the attached document contained the following rotations:
# Because the dial points at 0 a total of three times during this process, the password in this example is 3.

# Analyze the rotations in your attached document. What's the actual password to open the door?

    # PART 2
# "Due to newer security protocols, please use password method 0x434C49434B until further notice."
# You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.
# Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

# Using password method 0x434C49434B, what is the password to open the door?

from day_1_input import code

def code_to_list(code:str) -> list[str] :
    return [line for line in code.splitlines()]

def crack_code(code:str, method:str=None) -> int :
    instructions = code_to_list(code) 
    total = 50 # Dial starts at 50
    zero_pointed = 0 # Times we pointed at 0

    for chunk in instructions :
        match method :
            case None : # Part 1
                if chunk[0] == "L" :
                    total -= int(chunk[1:])
                else :
                    total += int(chunk[1:])

                total = total % 100 # Remaining of division by 100 -> Locks dial numbers to 0 -> 99

                if total == 0 :
                    zero_pointed += 1

            
            case '0x434C49434B' : # Part 2
                direction = -1 if chunk[0] == 'L' else 1
                steps = int(chunk[1:])
                    
                for _ in range(steps) :
                    total = (total + direction) % 100 # Increment total by direction step by step and check if == 0
                    if total == 0 :
                        zero_pointed += 1

            case _ : 
                print("Method invalid.")
                return
    return zero_pointed

method = '0x434C49434B'
print(crack_code(code=code, method=method))