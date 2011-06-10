# If p is the perimeter of a right angle triangle with integral length sides, 
# {a,b,c}, there are exactly three solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p <= 1000, is the number of solutions maximised?

def problem39(p):
    l = []
    for a in xrange(1, p):
        for b in xrange(1, p-a):
            for c in xrange(1, p-a-b+1):
                if a + b + c == p:
                    if a ** 2 + b ** 2 == c ** 2:
                        x = sorted([a, b, c])
                        if x not in l:
                            l.append(x)
    return l
max = 5
max_p = [[28, 195, 197], [60, 175, 185], [70, 168, 182], [105, 140, 175], [120, 126, 174]]
max_i = 420
for i in xrange(420,1000):
    p = problem39(i)
    if p != []:
       print i, p, len(p)
    if p != [] and len(p)>max:
        max = len(p)
        max_i = i
        max_p = p
        
print "max:", max_i, max_p, max
        

