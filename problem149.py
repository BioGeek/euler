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
#for k in [10,100]:
#    print k, S[k-1]
    
table = [S[i:i+2000] for i in range(0,4000000,2000)]

sample = [[-2,  5,  3,  2],
          [ 9, -6,  5,  1],
          [ 3,  2,  7,  3],
          [-1,  8, -4,  8]]
        

#def msum(a):
#    """Maximum Subarray Sum
#       http://20bits.com/articles/introduction-to-dynamic-programming/"""
#    return max([sum(a[j:i]) for i in range(1,len(a)+1) for j in range(i)])


def diagonals(m):
    """http://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python"""
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

# print problem149(sample)
print problem149(table)
