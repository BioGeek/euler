# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of 
# each of the digits 0 to 9 in some order, but it also has a rather interesting 
# sub-string divisibility property.
#
# Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we 
# note the following:
#
# d_2d_3d_4=406 is divisible by 2
# d_3d_4d_5=063 is divisible by 3
# d_4d_5d_6=635 is divisible by 5
# d_5d_6d_7=357 is divisible by 7
# d_6d_7d_8=572 is divisible by 11
# d_7d_8d_9=728 is divisible by 13
# d_8d_9d_10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations

def hasSubStringProperty(n):
    return int(str(n)[1:4])%2==0 and \
           int(str(n)[2:5])%3==0 and \
           int(str(n)[3:6])%5==0 and \
           int(str(n)[4:7])%7==0 and \
           int(str(n)[5:8])%11==0 and \
           int(str(n)[6:9])%13==0 and \
           int(str(n)[7:10])%17==0

#Check for example value 
assert hasSubStringProperty(1406357289) == True

l = []
for pandigital in (int(''.join(i)) for i in permutations('0123456789', 10)):
  if hasSubStringProperty(pandigital):
    l.append(pandigital)
    
print sum(l)

# 16695334890
#
# real	0m15.248s
# user	0m12.630s
# sys	0m0.590s
