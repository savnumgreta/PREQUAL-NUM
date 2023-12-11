def premier(n):
  i = 2
  while i < n:
    if n%i !=0:
      return False
    else:
      result = True      
    i+= 1

  return result



m = 1137
#A compléter

print(premier(m))