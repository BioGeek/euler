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

