n = int(input())
def fact(n):
  if n > 1: 
    return fact(n - 1)*n
  else: 
    return 1
print(fact(n))