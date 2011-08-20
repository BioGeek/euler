# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12^th digit of the fractional part is 1.
#
# If d_n represents the n^th digit of the fractional part, find the value of the 
# following expression.
#
# d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

from operator import mul

fraction = ""
i = 1
while len(fraction) <= 1000000:
    fraction += str(i)
    i += 1

print reduce(mul, map(int, [fraction[(10**j)-1] for j in range(7)]))

# 210
#
# real	0m0.267s
# user	0m0.130s
# sys	0m0.010s

