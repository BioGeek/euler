def laggedFibonacciGenerator():
    s = []
    for k in range(1,56):
        s_k = ((100003 - (200003*k) + (300007*(k**3))) % 1000000) - 500000
        s.append(s_k)
    for k in range(56,4000000):
        s_k = ((s[k-24-1] + s[k-55-1] + 1000000) %  1000000) - 500000
        s.append(s_k)
    return s

S = laggedFibonacciGenerator()
for k in [10,100]:
    print k, S[k-1]
    
table = [S[i:i+2000] for i in range(2000)]

sample = [[-2, 5, 3, 2],
          [9, -6, 5, 1],
          [3, 2, 7, 3],
          [-1, 8, -4, 8]]

def maxsum(matrix):
    for row in matrix:
        
        
