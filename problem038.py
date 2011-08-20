# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 * 1 = 192
# 192 * 2 = 384
# 192 * 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 
# 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
# and 5, giving the pandigital, 918273645, which is the concatenated product 
# of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

def isPandigital(n):
    assert len(str(n)) == 9
    return ''.join(sorted(list(str(n)))) == '123456789'

def concatenated_product(x, l):
    return ''.join(map(lambda i: str(x * i), l))

# Cjecking for example values:
# concatenated_product(192, [1,2,3])
# concatenated_product(9, range(1,6))

largest = 0
for x in range(10000):
  for l in [range(1,n) for n in range(3,11)]:
    cp = concatenated_product(x, l)
    if len(cp) == 9:
      if isPandigital(cp):
        if cp > largest:
          largest = cp
        
print largest

# 932718654
#
# real	0m0.450s
# user	0m0.440s
# sys	0m0.000s
