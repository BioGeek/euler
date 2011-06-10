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
            

            



        
