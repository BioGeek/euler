# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Very easy in Mathematica:
# Max[FactorInteger[600851475143]]

import sys, math

def factorize(n):
    """Prime factorization. This algorithm decomposes an integer into a product 
    of factors that are prime numbers. The fundamental theorem of arithmetic 
    guarantees that this decomposition is unique."""
    def isPrime(n):
        return not [x for x in xrange(2,int(math.sqrt(n))) if n%x == 0]
    primes = []
    candidates = xrange(2,n+1)
    candidate = 2
    while not primes and candidate in candidates:
        if n%candidate == 0 and isPrime(candidate):
            primes = primes + [candidate] + factorize(n/candidate)
        candidate += 1            
    return primes

print max(factorize(600851475143))

# 6857
#
# real	0m0.780s
# user	0m0.770s
# sys	0m0.000s

