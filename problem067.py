# By starting at the top of the triangle below and moving to adjacent numbers on 
# the row below, the maximum total from top to bottom is 23.
#
#    3
#   7 4
#  2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 
# 'Save Link/Target As...'), a 15K text file containing a triangle with 
# one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not possible 
# to try every route to solve this problem, as there are 299 altogether! If you 
# could check one trillion (1012) routes every second it would take over twenty 
# billion years to check them all. There is an efficient algorithm to solve it.

small_triangle = """3
7 4
2 4 6
8 5 9 3"""

def make_triangle(triangle):
    return [map(int, line.split()) for line in triangle.rstrip().split('\n')]

# inspired by technique of maher in the forum:
# Suppose you have the triangle:  
#          3
#         7 4
#        2 4 6
#       8 5 9 3
# If you ended up at 2 in the second to last row, you 
# would choose 8 in the last row, so add 8 o that 2:
#           3
#          7 4
#        10 4 6
#       *  5 9 3
# Likewise for the rest of the numbers:
#            3
#          7  4
#        10 13 15
#       *  *  *  *
# The number you eventually end up with at the top is the answer. So, by working 
# 'backwards' we turn an exponentially growing problem into an implosion to the 
# solution. 

def maher(t):
    new_last_row = [max(t[-1][i:i+2])+t[-2][i] for i in range(len(t[-2]))]
    new_t = t[:-2] + [new_last_row]
    if len(new_t) == 1:
        global solution
        solution = new_t[0][0]
    else:
        maher(new_t)       

# check for example value
maher(make_triangle(small_triangle))
assert solution == 23

with open('data/triangle.txt', 'r') as f:
    big_triangle = f.read()

maher(make_triangle(big_triangle))
print solution

# 7273
#
# real	0m0.056s
# user	0m0.040s
# sys	0m0.000s

# Also, nice concise solution from tenigmanogo in the forum
#
# t = map(lambda x: map(int, x.split()), big_triangle.rstrip().split('\n')) 
#
# def maxsum(sum, line):
#     a = map(lambda x: x[0]+x[1], zip(sum, line)) 
#     b = map(lambda x: x[0]+x[1], zip(sum[1:], line)) 
#     return map(max, zip(a, b)) 
#
# print reduce(maxsum, t[::-1])[0]


