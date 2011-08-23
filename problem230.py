# -*- coding: utf-8 -*-
# For any two strings of digits, A and B, we define F_A,B to be the sequence 
# (A,B,AB,BAB,ABBAB,...) in which each term is the concatenation of the previous 
# two.
#
# Further, we define D_A,B(n) to be the n^th digit in the first term of F_A,B 
# that contains at least n digits.
#
# Example:
#
# Let A=1415926535, B=8979323846. We wish to find D_A,B(35), say.
#
# The first few terms of F_A,B are:
# 1415926535
# 8979323846
# 14159265358979323846
# 897932384614159265358979323846
# 14159265358979323846897932384614159265358979323846
#
# Then D_A,B(35) is the 35th digit in the fifth term, which is 9.
#
# Now we use for A the first 100 digits of π behind the decimal point:
#
# 14159265358979323846264338327950288419716939937510 
# 58209749445923078164062862089986280348253421170679
#
# and for B the next hundred digits:
#
# 82148086513282306647093844609550582231725359408128 
# 48111745028410270193852110555964462294895493038196 .
#
# Find ∑_n=0,1,...,17   10^n * D_A,B((127+19n)7^n) 


def F(A,B):
    l = [A,B]
    while True:
        l.append(l[-2]+l[-1])
        yield l[-1]
        
def D(f,n):
    fn = f.next()
    while len(fn)<n: 
        fn = f.next()
    return fn[n-1]

# Checking for example values:
assert D(F('1415926535','8979323846'), 35) == '9'

# Now for the real question
A = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
B = '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'

f = F(A,B)

print sum(map(int, [D(f,((127+(19*n))*(7**n))) for n in range(18)]))

# TODO: runs in under two seconds for sum(... for n in range(8)])) 
# but any larger values of n take excessively long. 
