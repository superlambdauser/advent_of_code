    # PART 1
# There are batteries nearby that can supply emergency power to the escalator for just such an occasion. 
# The batteries are each labeled with their joltage rating, a value from 1 to 9. 
# You make a note of their joltage ratings (your puzzle input). For example:

# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111

# The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. 
# Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. 
# For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

# The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.
# There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?

from day_3_input import batteries

def text_to_batteries(text:str) -> list[list[int]] :
    return [[int(char) for char in line] for line in text.splitlines()]

def max_joltage(bank:list[int]) :
    best_combination = 0 
    for i in range(len(bank)) :
        for j in range(i+1, len(bank)) :
            # Compose a 2 digits number
            number = bank[i] * 10 + bank[j]
            best_combination = max(best_combination, number)
    return best_combination
            

def turn_batteries_on(batteries:str) -> int :
    banks = text_to_batteries(batteries)

    total = 0
    for bank in banks :
        total += max_joltage(bank)

    return total

print(turn_batteries_on(batteries))