# Starting with the number 1 and moving to the right in a clockwise direction a 
# 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?


def sum_diagonals_spiral(size):
    z = 1
    diagonals = [1]
    for i in range(2,size,2):
        for j in range(4):
            z += i
            diagonals.append(z)
    return sum(diagonals)

# check for sample value
assert sum_diagonals_spiral(5) == 101

print sum_diagonals_spiral(1001)

# 669171001
#
# real	0m0.045s
# user	0m0.010s
# sys	0m0.020s

