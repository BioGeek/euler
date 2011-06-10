from itertools import permutations
"""
def isPandigital(n):
    assert len(str(n)) == 10
    return ''.join(sorted(list(str(n)))) == '0123456789'
"""
def hasSubStringProperty(n):
    return int(str(n)[1:4])%2==0 and int(str(n)[2:5])%3==0 and int(str(n)[3:6])%5==0 and int(str(n)[4:7])%7==0 and int(str(n)[5:8])%11==0 and int(str(n)[6:9])%13==0 and int(str(n)[7:10])%17==0

# print hasSubStringProperty(1406357289)

l = []
for pandigital in (int(''.join(i)) for i in permutations('0123456789', 10)):
  if hasSubStringProperty(pandigital):
    print pandigital,
    l.append(pandigital)
    
print "\nsum", sum(l)

"""
# create pandigitals
pandigitals = []
n = 1000000000
while len(str(n)) == 10:
  if isPandigital(n):
    pandigitals.append(n)
    print n,
  n += 1
    
print len(pandigitals)
"""

"""
l = []
for i in range(1000000000,1406357290):
    assert len(i) == 10
    if hasSubStringProperty(i):
        l.append(i)

print sum(l)
"""
