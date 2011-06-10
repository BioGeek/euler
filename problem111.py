#def getprimes(max_n):
#    """http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/2073279#2073279"""
#    numbers = range(3, max_n+1, 2)
#    half = (max_n)//2
#    initial = 4

#    for step in xrange(3, max_n+1, 2):
#        for i in xrange(initial, half, step):
#            numbers[i-1] = 0
#        initial += 2*(step+1)

#        if initial > half:
#            return [2] + filter(None, numbers)
#        
#fourdigitprimes = [p for p in getprimes(10000) if len(str(p))==4]
#primes3ones = [p for p in fourdigitprimes if str(p).count('1')==3]

#def ndigitprimes(n):
#    return [p for p in getprimes(10**n) if len(str(p))==n]
"""
import gmpy

def ndigitprimes(n):
    primes = []
    m = gmpy.next_prime(gmpy.mpz(10**(n-1)))
    while m<10**n:
        primes.append(m)
        m = gmpy.next_prime(gmpy.mpz(m))
    return primes

"""


def M(n,d):
    """represents the maximum number of repeated digits for an n-digit prime where 
    d is the repeated digit"""
    return max([str(p).count(str(d)) for p in ndigitprimes(n)])

def N(n,d):
    """represents the number of such primes"""
    m = M(n,d)
    return len([p for p in ndigitprimes(n) if str(p).count(str(d))==m])

def S(n, d):
    """sum of these primes"""
    m = M(n,d)
    return sum([p for p in ndigitprimes(n) if str(p).count(str(d))==m])

for d in range(10):
    print "%d\t%d\t%d\t%d\t" % (d, M(4,d), N(4,d), S(4,d))
    
print
print sum(S(4,d) for d in range(10))
print
print sum(S(10,d) for d in range(10))


