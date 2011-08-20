# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

print [(a*b*c) for a in range(1,1000) for b in range(1,1000-a) for c in range(1,1000-a-b+1) if a+b+c==1000 and a**2+b**2==c**2][0]

# 31875000
#
# real	0m25.645s
# user	0m25.510s
# sys	0m0.080s

# Faster solution from tskww on the forum:
# First, a little analysis reveals the following properties. For all triples,
# a^2+b^2 = c^2; a+b > c, c > a, c > b. We can also define b > a. Since a + b + 
# c = 1000, it follows that 500 > c > 334. (If c > 500, then a+b > c doesn't 
# hold. If c < 334 and b > a, then c > b doesn't hold.) So, in Python: 

# for c in xrange(334,500):
#    for a in xrange(1, (1000-c)/2):
#        b = (1000 - c) - a
#        if a**2 + b**2 == c**2:
#            print a*b*c 

# real	0m0.068s
# user	0m0.060s
# sys	0m0.000s
            
