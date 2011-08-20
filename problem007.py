# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
#
# What is the 10001st prime number?

from math import sqrt

# List of primes:
primes = [2, 3, 5, 7, 11, 13, 17, 19]

# The prime we're looking for:
limit = 10001

def isprime(n):
    for i in primes:
        if i > sqrt(n):
            break
        if n % i == 0:
            return False
    return True

candidate = primes[-1] + 2
  
while len(primes) < limit:
  if(isprime(candidate)):
    primes.append(candidate)
  candidate += 2
  
print primes[-1]

# 104743
#
# real	0m0.282s
# user	0m0.260s
# sys	0m0.010s

