# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

def is_prime(n):
    """range starts with 2 and only needs to go up the squareroot of n"""
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def is_circular_prime(n):
    return all(is_prime(int(str(n)[i:i+len(str(n))]+str(n)[:i])) for i in range(len(str(n))))

# check for example values
assert [i for i in range(2,100) if is_circular_prime(i)] == [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]

print sum(1 for i in range(2,1000000) if is_circular_prime(i))

# 55
#
# real	0m23.823s
# user	0m23.680s
# sys	0m0.060s



    
