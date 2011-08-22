# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
# through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing 
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity 
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

from itertools import product

def is_pandigital(number):
    return map(int, sorted(str(number))) == range(1,len(str(number))+1)

# check for example value
assert is_pandigital(15234)

products = set()

# A 1-9 pandigital product is a 2-digit number times a 3-digit number,
# or a 1-digit number times a 4-digit number
pairs = [(a,b) for (a,b) in product(range(1,10),range(1000,10000))] + \
        [(a,b) for (a,b) in product(range(10,100),range(100,1000))]

for (multiplicand, multiplier) in pairs:
    product = multiplicand * multiplier
    identity = str(multiplicand) + str(multiplier) + str(product)
    if len(identity) == 9 and is_pandigital(identity):
        products.add(product)
            
print sum(products)          


# 45228
#
# real	0m1.242s
# user	0m0.820s
# sys	0m0.080s
 
            

