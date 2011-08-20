# -*- coding: utf-8 -*-
"""#l = [1] * 5


#[i for i in [[j[-2:]+[sum(j[:-2])]][0] for j in [l[:-i] + [sum(l[-i:])] for i in range(1,len(l))]] + [l[:-i] + [sum(l[-i:])] for i in range(1,len(l))] if 0 not in i]

# http://thestringy.wordpress.com/2011/05/27/project-euler-problem-76/
#Essentially you loop through all numbers, n, from 1 to 100, and nest another loop, i, within which counts from n to the target number. Now, using an array, the number of ways is expressed by adding the stored number in the array at i – n. This is essentially checking the number of ways for all numbers under the target as well as the target itself. The number stored in the array at the target, is the number of ways of getting there.

for n in range(1,101):
"""
from itertools import combinations_with_replacement

print len(list(t for t in combinations_with_replacement(range(101),100) if sum(t) == 100)) - 1


