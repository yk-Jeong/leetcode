import sys 
input = sys.stdin.readline

a, b = 1, 1

while (a != 0) or (b != 0):
  a, b = map(int, input().split())
  if a != 0 and b != 0:
    if (b % a) == 0:
      print('factor')
    elif (a % b) == 0:
      print('multiple')
    else:
      print('neither')
  else:
    break