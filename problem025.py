# The Fibonacci sequence is defined by the recurrence relation:
#
# F_n = F_n1 + F_n2, where F_1 = 1 and F_2 = 1.
# Hence the first 12 terms will be:
# 
# F_1 = 1
# F_2 = 1
# F_3 = 2
# F_4 = 3
# F_5 = 5
# F_6 = 8
# F_7 = 13
# F_8 = 21
# F_9 = 34
# F_10 = 55
# F_11 = 89
# F_12 = 144
#
# The 12th term, F_12, is the first term to contain three digits.
# 
# What is the first term in the Fibonacci sequence to contain 1000 digits?

def n_digit_fibonacci(n):
    term = 1
    a, b = 1, 1
    while 1:
        if len(str(a))==n:
            yield term
        a, b = b, a + b
        term += 1
        
# Check for example value
n = n_digit_fibonacci(3)
assert n.next() == 12

n = n_digit_fibonacci(1000)
print n.next()

# 4782
#
# real	0m0.120s
# user	0m0.090s
# sys	0m0.030s





