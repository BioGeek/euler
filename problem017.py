# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
# words, how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
# letters. The use of "and" when writing out numbers is in compliance with 
# British usage.

words = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
         'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
         'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 
         'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 
         'thousand']
digits = map(str, range(20) + range(20,101,10) + [1000])

get_num = dict(zip(digits,words))   

def normalize(num):
    """Normelize number (remove 0's prefix). Return number and string"""
    n = int(num)
    return n, str(n)  

def number_to_word(num):
    """English representation of a number <= 1000"""
    n, num = normalize(num)
    hundred = ''
    ten = ''
    if len(num) == 4:
        return 'one thousand'
    if len(num) == 3:
        hundred = get_num[num[0]] + ' hundred'
        num = num[1:]
        n, num = normalize(num)
    if (n > 20) and (n != (n / 100)):
        tens = get_num[num[0] + '0']
        ones = get_num[num[1]]
        ten = tens + ' ' + ones
    else:
        ten = get_num[num]
    if hundred and ten:
        return hundred + ' and ' + ten
    else: # One of the below is empty
        return hundred + ten
    
def count_letters(number):
    return sum(len(i) for i in number.replace('-',' ').split())

# Check for example values
assert sum(len(get_num[str(i)]) for i in range(1,6)) == 19
assert sum(count_letters(number_to_word(i)) for i in range(1,6)) == 19
assert count_letters('three hundred and forty-two') == 23
assert count_letters(number_to_word(342)) == 23
assert count_letters('one hundred and fifteen') == 20
assert count_letters(number_to_word(115)) == 20

print sum(count_letters(number_to_word(i)) for i in range(1,1001))

# 21124
#
# real	0m0.052s
# user	0m0.040s
# sys	0m0.000s


