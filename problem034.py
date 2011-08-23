# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of 
# their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


fac = lambda n: n<=0 or reduce(lambda a,b: a*b, xrange(1,n+1))

def sum_factorial_of_digits(number):
    return sum(map(fac, map(int, list(str(number)))))

# check for sample value
assert sum_factorial_of_digits(145) == 145

# substract 1! and 2!
print sum(i for i in range(fac(9)) if i == sum_factorial_of_digits(i)) - 3

# 40730
#
# real	0m10.011s
# user	0m7.340s
# sys	0m0.450s

