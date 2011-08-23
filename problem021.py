# Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
# which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and 
# each of a and b are called amicable_numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
# and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 
# 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable_numbers under 10000.

def d(n):
  """the sum of proper divisors of n (the numbers less than n
  which divide evenly into n"""
  proper_divisors = []
  for i in range(1, n-1):
    if n%i == 0:
      proper_divisors.append(i)
  return sum(proper_divisors)

# check for example values
assert d(220) == 284
assert d(284) == 220

amicable_numbers = []

for a in range(10001):
  b = d(a)
  x = d(b)
  if x == a and a != b:
    if a not in amicable_numbers:
        amicable_numbers.append(a)
    if b not in amicable_numbers:
        amicable_numbers.append(b)
        
print sum(amicable_numbers)        

# 31626
#
# real	0m8.842s
# user	0m8.820s
# sys	0m0.010s


