import sys 
input = sys.stdin.readline

M = int(input())
N = int(input())

def is_num_prime(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

prime = []

for i in range(M, N+1):
  if is_num_prime(i) == True:
      prime.append(i)

if 1 in prime:
  prime.remove(1)

if not prime:
  print(-1)
else:
  print(sum(prime))
  print(min(prime))