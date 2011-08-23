# A unit fraction contains 1 in the numerator. The decimal representation of the 
# unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
# seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in 
# its decimal fraction part.

from decimal import Decimal

def length_recurring_cycle(denominator, n=1):
    """Uses the following property, described on
    http://en.wikipedia.org/wiki/Repeating_decimal#Converting_repeating_decimals_to_fractions
    that if a fraction multiplied by 10^n minus that fraction has a remainder of 
    zero,then the fraction has a recurring cycle of length n. Example:
        
            x = 1./7
            x =      0.142857142857142857...
    1000000*x = 142857.142857142857142857... (multiply each side by 1000000)
     999999*x = 142857.0                     (subtract the 1st line from the 2nd)
    """
    fraction = Decimal(1) / Decimal(denominator)
    multiple = (10**n) * fraction
    difference = multiple - fraction
    print denominator, fraction, multiple, difference
    if (difference % 1).is_zero():
        return n

def isPrime(n):
    """we only check for prime denominators"""
    return not [x for x in xrange(2,int(math.sqrt(n))) if n%x == 0]

# TODO: solution not yet complete


    


