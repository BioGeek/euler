# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2     (n is even)
# n -> 3n + 1  (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13  40  20  10  5  16  8  4  2  1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
# that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?

greatest = 0

def collatz(n):
    """generates iterative sequence (does not include the final 1)"""
    while n != 1:
        yield n
        if not n%2:
            n = n/2
        else:
            n = (3*n) + 1
            
print sorted([(i,len(list(collatz(i)))) for i in range(1,1000000)], key=lambda x: x[1])[-1][0]    

# 837799
#
# real	0m47.068s
# user	0m37.220s
# sys	0m1.980s


