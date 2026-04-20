    # PART 1
# As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! 
# Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

# They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

# 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124
# (The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

# The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

# Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

# None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

# Adding up all the invalid IDs in this example produces 1227775554.

# What do you get if you add up all of the invalid IDs?

    # PART 2
# Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. 
# So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

# Adding up all the invalid IDs in this example produces 4174379265.

# What do you get if you add up all of the invalid IDs using these new rules?

from day_2_input import ranges

def parse(products:str) -> list[str] :
    return [id_range for id_range in products.split(',')]

def solve(products:str, part:int=1) :
    id_ranges = parse(products)

    def is_invalid(n: int) -> bool :
        s = str(n) # Work with num as str in order to slice it
        match part :
            case 1 :
                if len(s) % 2 != 0 :
                    return False # Odd num of digits -> no split into equel parts -> always valid
                
                half = len(s) // 2
                return s[half:] == s[:half] # "1010" -> "10" == "10"
            case 2 :
                # Try every possible block size from 1 up to half the length
                for chunk_size in range(1, (len(s) // 2) + 1) : 
                    chunk = s[:chunk_size]
                    if chunk * (len(s) // chunk_size) == s : # Repeat block to fill whole string and compare results
                        return True 
                return False
            case _ :
                print("Invalid part")

    total = 0

    for r in id_ranges :
        start = int(r.split('-')[0]) 
        end = int(r.split('-')[1])

        for x in range(start, end + 1) :
            if is_invalid(x) :
                total += x
    
    return total

print(solve(ranges))
print(solve(ranges, part=2))