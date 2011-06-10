from math import sqrt

def pentagonal():
  n = 1
  while 1:
    yield n*(3*n-1)/2
    n += 1

def firstn(g, n):
  for i in range(n):
    yield g.next()
    

def isPentagonal(x):
  # see: http://en.wikipedia.org/wiki/Pentagonal_number
  return ((sqrt(24*x +1) + 1)/6)%1==0

# with inspiration from http://duncan99.wordpress.com/2009/12/12/project-euler-problem-44/
pentagonals = []
penta = pentagonal()
flag = True
while flag:
  p = penta.next()
  for pentagonal in pentagonals:
    diff = abs(p - pentagonal)
    if isPentagonal(diff):
      sum = p + pentagonal
      if isPentagonal(sum):
        print diff, p, pentagonal
        flag = False
  pentagonals.append(p)

