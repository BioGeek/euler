# 2520 is the smallest number that can be divided by each of the numbers from 1 
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

# First try, brute force but takes way too much time:
# while 1:
#     n = 2520
#    if all(not n%i for i in range(1,21)):
#        print n
#        break
#    n += 1


def gcd(m, n):
    """Greatest Common Divisor using Euclids algorithm"""
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

def lcd(m, n):
    """Lowest Common Denominator"""
    GCD = gcd(m, n)
    return m*n/GCD

result = 2
constant = 20
for i in range(3, constant):
  result = lcd(result, i)

# produces lcd(20, lcd(19, ... lcd(5, lcd(4, lcd(3, lcd(2,1))))...))
# the lowest common denominator for the values 1 through 20.

print result

# lcd(2 , 3) = 2  * 3 / 1 = 6   = 2   * 3
# lcd(6 , 4) = 6  * 4 / 2 = 12  = 2^2 * 3
# lcd(12, 5) = 12 * 5 / 1 = 60  = 2^2 * 3 * 5
# lcd(60, 6) = 60 * 6 / 6 = 60  = 2^2 * 3 * 5
# lcd(60, 7) = 60 * 7 / 1 = 420 = 2^2 * 3 * 5 * 7
# lcd(420,8) = 420* 8 / 4 = 840 = 2^3 * 3 * 5 * 7
# and so on till eventually... 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560


# with constant = 1000, the answer is:
# 712886527466509305316638415571427292066835886188589304045200199115432408758111
# 149947644415191387158691171781701957525651298026406762100925146587100430513107
# 268626814320019660997486274593718834370501543445252373974529896314567498212823
# 695623282379401106880926231770886197954079124775455804932647573782992335275179
# 673524804246363805113703433121478174685087845348567802188807537324992199567205
# 6932029099390891687487672697950931603520000

# 232792560
#
# real	0m0.043s
# user	0m0.040s
# sys	0m0.000s

