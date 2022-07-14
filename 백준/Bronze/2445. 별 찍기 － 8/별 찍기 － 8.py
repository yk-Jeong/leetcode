n = int(input())
for i in range(1, n+1):
  if i < n: 
    print("*"*i + 2*(" "*(n-i)) + "*"*i)
  elif i == n:
    print("*"*i*2)
for i in range(1, n):
    print("*"*(n-i) + 2*(" "*(i)) + "*"*(n-i))