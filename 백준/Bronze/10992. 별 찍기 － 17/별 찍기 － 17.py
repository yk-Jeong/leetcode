n = int(input())
for i in range(1, n+1):
  if i != n: 
    if i == 1: 
      print(" "*(n-i)+"*"+" ")
    else:
      print(" "*(n-i)+"*"+" "*(2*i - 3) +"*")
  else:    
    print((2*i - 1)*"*")