# For a number written in Roman numerals to be considered valid there are basic rules which must be 
# followed. Even though the rules allow some numbers to be expressed in more than one way there is 
# always a "best" way of writing a particular number.
# 
# For example, it would appear that there are at least six ways of writing the number sixteen:
# 
# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI
# 
# However, according to the rules only XIIIIII and XVI are valid, and the last example is considered
# to be the most efficient, as it uses the least number of numerals.
# 
# The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand 
# numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals
# for the definitive rules for this problem.
# 
# Find the number of characters saved by writing each of these in their minimal form.
# 
# Note: You can assume that all the Roman numerals in the file contain no more than four consecutive
# identical units.

def roman_to_int(roman, strict=False):
    """
    Convert a Roman numeral string to an integer.
    Validates according to the same rules as int_to_roman's docstring.
    """
    roman = roman.upper()
    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Allowed subtractive pairs
    subtractives = {
        "I": ("V", "X"),
        "X": ("L", "C"),
        "C": ("D", "M")
    }

    total = 0
    i = 0
    prev_value = float("inf")
    counts = {"D": 0, "L": 0, "V": 0}

    while i < len(roman):
        if roman[i] not in roman_map:
            raise ValueError(f"Invalid Roman numeral character: {roman[i]}")

        # Look ahead for subtractive pair
        if i + 1 < len(roman) and roman_map[roman[i]] < roman_map[roman[i + 1]]:
            # Check subtractive rules
            if roman[i] not in subtractives or roman[i + 1] not in subtractives[roman[i]]:
                raise ValueError(f"Invalid subtractive combination: {roman[i]}{roman[i + 1]}")

            value = roman_map[roman[i + 1]] - roman_map[roman[i]]
            if roman[i] in "IXC" and roman[i + 1] in subtractives[roman[i]]:
                pass  # valid
            else:
                raise ValueError(f"Illegal subtractive pair: {roman[i]}{roman[i+1]}")

            if roman[i + 1] == roman[i]:  # can't be equal in subtractive
                raise ValueError(f"Invalid subtractive repetition: {roman[i]}{roman[i+1]}")

            if value >= prev_value:
                raise ValueError("Numerals must be in descending order.")

            prev_value = value
            total += value
            i += 2
        else:
            value = roman_map[roman[i]]
            if value > prev_value:
                raise ValueError("Numerals must be in descending order.")

            # Count D, L, V occurrences
            if roman[i] in counts:
                counts[roman[i]] += 1
                if counts[roman[i]] > 1 and strict:
                    raise ValueError(f"{roman[i]} can only appear once.")

            total += value
            prev_value = value
            i += 1

    return total


def int_to_roman(num):
    """
    In order for a number written in Roman numerals to be considered valid there are three basic rules which must be followed.

    * Numerals must be arranged in descending order of size.
    * M, C, and X cannot be equalled or exceeded by smaller denominations.
    * D, L, and V can each only appear once.

    In addition to the three rules given above, if subtractive combinations are used then the following four rules must be followed.

    * Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
    * I can only be placed before V and X.
    * X can only be placed before L and C.
    * C can only be placed before D and M.

    """
    # Mapping of integer to Roman numeral respecting subtractive rules
    val_map = [
        (1000, "M"),
        (900, "CM"),  # C before M
        (500, "D"),
        (400, "CD"),  # C before D
        (100, "C"),
        (90, "XC"),   # X before C
        (50, "L"),
        (40, "XL"),   # X before L
        (10, "X"),
        (9, "IX"),    # I before X
        (5, "V"),
        (4, "IV"),    # I before V
        (1, "I"),
    ]

    result = []
    for val, numeral in val_map:
        while num >= val:
            result.append(numeral)
            num -= val

    return "".join(result)
    




if __name__ == '__main__':
    examples = [('IIIIIIIIIIIIIIII', 16),
                ('VIIIIIIIIIII', 16),
                ('VVIIIIII', 16),
                ('XIIIIII', 16),
                ('XIIIIII', 16),
                ('VVVI', 16),
                ('XVI', 16),
                ('XXXXIIIIIIIII', 49),
                ('XXXXVIIII', 49),
                ('XXXXIX', 49),
                ('XLIIIIIIIII', 49),
                ('XLVIIII', 49),
                ('XLIX', 49)]
    for roman, expected in examples:
        assert roman_to_int(roman) == expected, f"Failed for {roman}, got {roman_to_int(roman)} expected {expected}"

    with open('data/0089_roman.txt', 'r') as f:
        lines = f.readlines()
    
    total_saved = 0
    for line in lines:
        original = line.strip()
        minimal = int_to_roman(roman_to_int(original))
        total_saved += len(original) - len(minimal)
        print(f"Original: {original}, Minimal: {minimal}, value: {roman_to_int(original)}, saved: {len(original) - len(minimal)}")

    print(f"Total characters saved: {total_saved}")

    

