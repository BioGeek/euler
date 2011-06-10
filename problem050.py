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
  
primes = get_primes(100)
print 'len(primes):', len(primes)

l = []
for i in range(len(primes)):
    for j in range(2,len(primes)):
        if len(primes[i:i+j])==j and sum(primes[i:i+j]) in primes:
            print '.',
            l.append(primes[i:i+j])
print            
print 'len(l):', len(l)
print sorted(l, key=len)[-1]
print sum(sorted(l, key=len)[-1]) 
	
            
# long one-liner that takes WAAAY to much time!!
#print sum(sorted([primes[i:i+j] for i in range(len(primes)) for j in range(2,len(primes)) if len(primes[i:i+j])==j and sum(primes[i:i+j]) in primes], key=len)[-1])

    
