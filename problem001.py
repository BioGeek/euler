# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

print sum(i for i in range(1000) if not i%3 or not i%5)

# Answer: 233168
#
# real	0m0.041s
# user	0m0.040s
# sys	0m0.000s

