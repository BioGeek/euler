l = [1] * 5


[i for i in [[j[-2:]+[sum(j[:-2])]][0] for j in [l[:-i] + [sum(l[-i:])] for i in range(1,len(l))]] + [l[:-i] + [sum(l[-i:])] for i in range(1,len(l))] if 0 not in i]

