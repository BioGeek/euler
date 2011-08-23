# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in 
# base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include 
# leading zeros.)

hex2bin = {"0":"0000", "1":"0001", "2":"0010", "3":"0011",
          "4":"0100", "5":"0101", "6":"0110", "7":"0111",
          "8":"1000", "9":"1001", "A":"1010", "B":"1011",
          "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

def int_to_base2(number):
  return "".join([hex2bin[h] for h in '%X'%number]).lstrip('0')

def is_palindrome(string):
  return str(string) == str(string)[::-1] 

# check for sample values
assert is_palindrome(585)
assert is_palindrome(int_to_base2(585))

print sum(i for i in range(1000000) if is_palindrome(i) and is_palindrome(int_to_base2(i)))

# 872187
#
# real	0m0.901s
# user	0m0.850s
# sys	0m0.040s

