# Surprisingly there are only three numbers that can be written as the sum of 
# fourth powers of their digits:
#
#    1634 = 1^4 + 6^4 + 3^4 + 4^4
#    8208 = 8^4 + 2^4 + 0^4 + 8^4
#    9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers 
# of their digits.


def equals_sum_of_power(number, power):
    return number == sum(map(lambda x: x**power, map(int, str(number))))

# check for example values
assert equals_sum_of_power(1634, 4)
assert equals_sum_of_power(8208, 4)
assert equals_sum_of_power(9474, 4)
assert sum(i for i in range(2,10000) if   equals_sum_of_power(i, 4)) == 19316

print sum(i for i in range(2,1000000) if   equals_sum_of_power(i, 5))

# 443839
#
# real	0m7.172s
# user	0m7.100s
# sys	0m0.040s

