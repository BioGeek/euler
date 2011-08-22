# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

# check for sample value
assert sum(map(int, str(2**15))) == 26

print sum(map(int, str(2**1000)))

# 1366
#
# real	0m0.043s
# user	0m0.030s
# sys	0m0.010s
