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

    # PART 2 
# Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

# The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

# What is the new total output joltage?

from day_3_input import batteries

def text_to_batteries(text:str) -> list[list[int]] :
    return [[int(char) for char in line] for line in text.splitlines()]
            
def max_joltage(bank:list[int], combination_size:int=12) -> int :
    n = len(bank)

    if n <= combination_size :
        return int(''.join(str(num) for num in bank)) # Not enough digits, use them all
    
    best_combination = []
    
    start = 0 
    for i in range(combination_size) :
        digits_remaining = combination_size - 1 - i # Decrement window size each time a digit is added

        end = n - digits_remaining # Leave room for enough digits to bo add

        best_idx = start # Defaults at first item in the window

        # Find best index in bank[start:end]
        for j in range (start, end) :
            if bank[j] > bank[best_idx] :
                best_idx = j # Find max index
        
        best_combination.append(bank[best_idx])
        start = best_idx + 1 # Start at next number in the list

    return int(''.join(str(num) for num in best_combination))
    
def turn_batteries_on(batteries:str, digits_amount:int=2) -> int :
    banks = text_to_batteries(batteries)

    total = 0
    for bank in banks :
        total += max_joltage(bank, digits_amount)

    return total

print(turn_batteries_on(batteries, 12))