# A perfect number is a number for which the sum of its proper divisors is exactly 
# equal to the number. For example, the sum of the proper divisors of 28 would be 
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than 
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By 
# mathematical analysis, it can be shown that all integers greater than 28123 
# can be written as the sum of two abundant numbers. However, this upper limit 
# cannot be reduced any further by analysis even though it is known that the 
# greatest number that cannot be expressed as the sum of two abundant numbers is 
# less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum 
# of two abundant numbers.

from math import ceil, sqrt
from itertools import product

def proper_divisors(n):
  """Find all divisors of n by trial division"""
  divisors = set([1])
  for i in range(2, int(ceil(sqrt(n)))+1):
      if n % i == 0:
        divisors.add(i)
        divisors.add(n/i)
  return divisors

def is_abundant(n):
    return sum(proper_divisors(n)) > n

# Check for example values
assert proper_divisors(28) == set([1, 2, 4, 7, 14])
assert is_perfect_number(28) == True

limit = 28123

abundants = [i for i in range(1,limit) if is_abundant(i)]
sums = set([i+j for (i,j) in product(abundants, abundants) if i+j<=limit])
integers = set(range(1,limit+1)) 

print sum(integers.difference(sums))

# 4179871
#
# real	1m28.749s    # Could benefit from a faster proper_divisors() function
# user	0m17.790s
# sys	0m0.960s



# solution from Peter Norvig in the forum
#
# abundants = set(i for i in range(1,28124) if is_abundant(i)) 
#
# def abundantsum(i):
#     return any(i-a in abundants for a in abundants) 
#
# print sum(i for i in range(1,28124) if not abundantsum(i))


        

    

