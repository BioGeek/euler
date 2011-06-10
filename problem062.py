from itertools import permutations

def iscube(n):
    cubed_root = n**(1/3.0)
    if round(cubed_root)**3 == n:
        return True
    else:
        return False


for x in range(1000,1000000):
    cube = x**3
    cube_permutations = set([int(''.join(i)) for i in permutations(str(cube)) if len(str(int(''.join(i))))==len(str(cube)) and iscube(int(''.join(i)))])
    if len(cube_permutations) == 5:
      print x, cube_permutations
      break
    
"""    
n = 0
i = 300
while n != 3:
    cube = i**3
    n = len(set(int(''.join(i)) for i in permutations(str(cube)) if iscube(int(''.join(i)))))
    i += 1
    
print i, cube

"""
