# Starting in the top left corner of a 2x2 grid, there are 6 routes (without 
# backtracking) to the bottom right corner.
# .__.__.
# .  .  |
# .  .  |
#
# .__.  .
# .  |__.
# .  .  |
# 
# .__.  .
# .  |  .
# .  |__.
#
# .  .  .
# |__.__.
# .  .  |
#
# .  .  .
# |__.  .
# .  |__.
#
# .  .  .
# |  .  .
# |__.__.
#
# How many routes are there through a 20x20 grid?

from itertools import permutations
from operator import mul

# in the 2x2 grid images above, the first image can be described as RRDD (where
# R is a step to the Right and D is a step Down). So all the different routes 
# through the grid are all the unique permutations of 'RRDD'

# Check for sample values
assert len(set(list(permutations('RRDD', 4)))) == 6

# However the equivalent for the 20x20 grid
# print len(set(list(permutations('R'*20 + 'D'*20, 20))))
# doesn't complete within a minute. So back to the drawing board.

# The number of permutations is the factorial of((number of R's) + (number of 
# D's)). To remove the duplicates divide by (factorial(number of R') * 
# factorial(number of D's))

def factorial(n):
    return reduce(mul, range(1,n+1))

# check for sample values
assert factorial(2+2)/(factorial(2)*factorial(2)) == 6

print factorial(20+20)/(factorial(20)*factorial(20))

# 137846528820
#
# real	0m0.036s
# user	0m0.020s
# sys	0m0.010s

 
