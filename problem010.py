# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import itertools

def erat2( ):
    """Recipe 18.10: Computing Prime Numbers from the Python Cookbook
    see: http://oreilly.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=last
    and: http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python"""
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p
            
def primes_below(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))      

# Check on example values
assert sum(primes_below(10)) == 17

print sum(primes_below(2000000))

# 142913828922
#
# real	0m1.447s
# user	0m1.340s
# sys	0m0.060s

