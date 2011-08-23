# Looking at the table below, it is easy to verify that the maximum possible sum 
# of adjacent numbers in any direction (horizontal, vertical, diagonal or 
# anti-diagonal) is 16 (= 8 + 7 + 1).
#
# -2   5   3   2
#  9  -6   5   1
#  3   2   7   3
# -1   8  -4   8
#
# Now, let us repeat the search, but on a much larger scale:
#
# First, generate four million pseudo-random numbers using a specific form of 
# what is known as a "Lagged Fibonacci Generator":
#
# For 1 <= k <= 55, s_k = [100003  200003k + 300007k^3] (modulo 1000000) - 500000.
# For 56 <= k <= 4000000, s_k = [s_k-24 + s_k-55 + 1000000] (modulo 1000000) - 500000.
#
# Thus, s_10 = 393027 and s_100 = 86613.
#
# The terms of s are then arranged in a 2000x2000 table, using the first 2000 
# numbers to fill the first row (sequentially), the next 2000 numbers to fill 
# the second row, and so on.
#
# Finally, find the greatest sum of (any number of) adjacent entries in any 
# direction (horizontal, vertical, diagonal or anti-diagonal).


import numpy as np

def laggedFibonacciGenerator():
    s = []
    for k in range(1,56):
        s_k = ((100003 - (200003*k) + (300007*(k**3))) % 1000000) - 500000
        s.append(s_k)
    for k in range(56,4000001):
        s_k = ((s[k-24-1] + s[k-55-1] + 1000000) %  1000000) - 500000
        s.append(s_k)
    return s

S = laggedFibonacciGenerator()
    
table = [S[i:i+2000] for i in range(0,4000000,2000)]
        

def diagonals(m):
    """http://stackoverflow.com/q/6313308/50065bv"""
    l = len(m)
    matrix = np.array(m)
    diags = [matrix[::-1,:].diagonal(i) for i in range(-l+1,l)]
    diags.extend(matrix.diagonal(i) for i in range(l-1,-l,-1))
    return [list(n) for n in diags]
    

def max_subarray(A):
    """http://en.wikipedia.org/wiki/Maximum_subarray_problem"""
    max_so_far = max_ending_here = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def problem149(m):
    maximum = 0
    for row in m:
        if max_subarray(row) > maximum:
            maximum = max_subarray(row)
    for column in zip(*m):
        if max_subarray(column) > maximum:
            maximum = max_subarray(column)
    for diagonal in diagonals(m):
        if max_subarray(diagonal) > maximum:
            maximum = max_subarray(diagonal)
    return maximum

# test on example value
sample = [[-2,  5,  3,  2],
          [ 9, -6,  5,  1],
          [ 3,  2,  7,  3],
          [-1,  8, -4,  8]]
assert problem149(sample) == 16

print problem149(table)

# 52852124
#
# real	0m22.148s
# user	0m21.370s
# sys	0m0.590s

