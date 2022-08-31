import sys 
input = sys.stdin.readline
N = int(input())

for _ in range(N):
  a, b = map(int, input().split())
  a1, b1, r = a, b, 1
  while r != 0:
    r = a % b 
    a = b
    b = r

  LCM = (a1 * b1) / a
  print(int(LCM))