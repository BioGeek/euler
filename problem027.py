# Euler published the remarkable quadratic formula:
#
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive values 
# n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible 
# by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#
# Using computers, the incredible formula n^2 - 79n + 1601 was discovered, which 
# produces 80 primes for the consecutive values n = 0 to 79. The product of the 
# coefficients, 79 and 1601, is 126479.
#
# Considering quadratics of the form:
# 
# n^2 + an + b, where |a| < 1000 and |b| < 1000
#
# (where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4)
#
# Find the product of the coefficients, a and b, for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, starting 
# with n = 0.

from itertools import product

def isprime(n):
    '''check if integer n is a prime'''
    # negative numbers, 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

# check for example values
quadratic_1 = lambda n: n**2 + n + 41
quadratic_2 = lambda n: n**2 - 79*n + 1601
assert all(isprime(quadratic_1(i)) for i in range(40))
assert all(isprime(quadratic_2(i)) for i in range(80))

def quadratic(a,b,n):
    assert abs(a) < 1000
    assert abs(b) < 1000
    return n**2 + a*n + b

max_length = 0
max_a, max_b = 0,0
for (a,b) in product(range(-999,1000),range(-999,1000)):
    for n in range(max(a,b)):
        if all(isprime(quadratic(a,b,n)) for i in range(n)):
            if n > max_length:
                max_length = n
                max_a, max_b = a, b
                print max_length, max_a, max_b
                
print max_a * max_b

# TODO: doesn't yet finish in under a minute


        
