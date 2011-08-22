# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
# containing over five-thousand first names, begin by sorting it into alphabetical 
# order. Then working out the alphabetical value for each name, multiply this 
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is 
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
# obtain a score of 938 * 53 = 49714.
#
# What is the total of all the name scores in the file?

from string import uppercase

with open('data/names.txt') as f:
    data = f.read()

names = [i[1:-1] for i in data.split(',')]
names.sort()

letters = [i for i in uppercase]
digits = range(1,27)
letters_to_digits = dict(zip(letters, digits))

def alphabetical_value(name):
    return sum(letters_to_digits[letter] for letter in name)

# Check for example value
assert names[937] == 'COLIN' 
assert alphabetical_value('COLIN') == 53

print sum(alphabetical_value(name) * (names.index(name)+1) for name in names)

# 871198282
#
# real	0m0.368s
# user	0m0.350s
# sys	0m0.010s
