# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(number):
  return str(number) == str(number)[::-1]

print max(x*y for x in range(900,1000) for y in range(900,1000) if palindrome(x*y))

# Alternative:
# import itertools
# print max(a*b for (a,b) in (itertools.product(range(900,1000),range(900,1000))) if palindrome(a*b))

# 906609
#
# real	0m0.051s
# user	0m0.040s
# sys	0m0.010s

