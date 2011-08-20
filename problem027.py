# Euler published the remarkable quadratic formula:
#
# n² + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
# However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when 
# n = 41, 41² + 41 + 41 is clearly divisible by 41.
#
# Using computers, the incredible formula  n²  79n + 1601 was discovered, which produces 80 primes 
# for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.
#
# Considering quadratics of the form:
# 
# n² + an + b, where |a| < 1000 and |b| < 1000
#
# (where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |4| = 4)
#
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum 
# number of primes for consecutive values of n, starting with n = 0.


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

maxlen = 0
A,B=0,0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        def f(n):
            return n**2 + (a*n) + b
        if all(isprime(f(i)) for i in range(b-1)): # and len(range(b-1)) > maxlen:
            # maxlen = len(range(b-1))
            # A,B=a,b
            print "n**2%sn%s" % ((str(a) if a<0 else '+%d'%a), (str(b) if b<0 else '+%d'%b)),  a*b, [f(i) for i in range(b-1)] # , maxlen
        if all(isprime(f(i)) for i in range(a)): # and len(range(a)) > maxlen:
            # maxlen = len(range(a))
            #A,B=a,b
            print "n**2%sn%s" % ((str(a) if a<0 else '+%d'%a), (str(b) if b<0 else '+%d'%b)),  a*b, [f(i) for i in range(a)] # , maxlen
            

            



        
