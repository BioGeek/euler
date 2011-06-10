import itertools

def erat2( ):
    """see: http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/2068412#2068412"""
    D = {  }
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
            
def get_primes(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))
  
primes = get_primes(10000)
primes = [prime for prime in primes if len(str(prime))==4]

