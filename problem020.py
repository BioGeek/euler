# n! means n * (n - 1) * ... * 3 * 2 * 1
#
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

from operator import mul

def factorial(n):
    return reduce(mul, range(1,n+1))

def sum_of_digits(number):
    return sum(map(int, list(str(number))))

# check for example values
assert factorial(10) == 3628800
assert sum_of_digits(factorial(10)) == 27

print sum_of_digits(factorial(100)) 

# 648
#
# real	0m0.044s
# user	0m0.040s
# sys	0m0.000s

