# If p is the perimeter of a right angle triangle with integral length sides, 
# {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p <= 1000, is the number of solutions maximised?

# Slow, ugly one-liner:
# sorted([(perimeter, len(set(([tuple(sorted([a,b,c])) for a in range(1,perimeter) for b in range(1,perimeter-a) for c in range(1,perimeter-a-b+1) if a+b+c==perimeter and a**2+b**2==c**2])))) for perimeter in range(1001)], key=lambda x: x[1])[-1][0]

def sides_of_right_angle_triangle(perimeter):
    sides = []
    for a in range(1,perimeter):
        for b in range(1,perimeter-a):
            for c in range(1,perimeter-a-b+1):
                if a+b+c==perimeter and a**2+b**2==c**2:
                    if sorted([a,b,c]) not in sides:
                        sides.append(sorted([a,b,c]))
    return (perimeter, len(sides))

# Checking for example value
assert sides_of_right_angle_triangle(120) == (120,3)

print sorted([sides_of_right_angle_triangle(i) for i in range(1001)], key=lambda x: x[1])[-1][0]

# 840
# 
# real	61m34.578s  # Still way too slow, took more than an hour!!
# user	61m9.350s
# sys	0m4.870s


