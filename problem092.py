def number_chain(n):
  x = sum(int(i)**2 for i in str(n))
  if x == 89:
    return True
  elif x == 1:
    return False
  else: 
    return number_chain(x)
    
print sum(number_chain(i) for i in range(1,10000000))

