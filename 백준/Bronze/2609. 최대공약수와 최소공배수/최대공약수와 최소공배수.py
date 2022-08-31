import sys 
input = sys.stdin.readline

a, b = map(int, input().split())
a1, b1 = a, b

r = 1
while r != 0:
  r = a % b 
  a = b
  b = r

GCD = a
LCM = (a1 * b1) / a
print(GCD)
print(int(LCM))