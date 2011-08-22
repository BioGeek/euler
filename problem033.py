# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
# correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than 
# one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

for numerator in range(10,100):
    for denominator in range(10,100):
        if numerator%10==0 or denominator%10==0:
            pass # trivial
        else:
            d = set(str(denominator))
            n = set(str(numerator))
            x = d.intersection(n)
            if len(x) == 1:
                D = list(d.difference(x))
                N = list(n.difference(x))
                if len(D) != 0 and len(N) != 0 :
                    if float(D[0]) / int(N[0]) == float(denominator) / numerator:
                        print "%s / %s = %d / %d" % (D[0], N[0], denominator, numerator)
                        
# returns:
# 4 / 1 = 64 / 16
# 5 / 1 = 95 / 19
# 5 / 2 = 65 / 26
# 8 / 4 = 98 / 49
# 1 / 4 = 16 / 64
# 2 / 5 = 26 / 65
# 1 / 5 = 19 / 95
# 4 / 8 = 49 / 98

# The first 4 are mirrors of the last four
#                           2*4
# 1/4 * 2/5 * 1/5 * 4/8 = ---------
#                          4*5*5*8
# Hence, the solution is 100
                          
# real	0m0.096s
# user	0m0.060s
# sys	0m0.000s                          

                        
