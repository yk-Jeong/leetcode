A, B = map(int, input().split())
C = int(input())
time = int((B + C ) / 60)
day = int((time + A) / 24)
if B + C < 60:
  print(f'{A} {B + C}')
else:
  if A + time < 24:
    print(f'{A + time} {B + C - 60*time}')
  else:
    print(f'{A + time - 24*day} {B + C - 60*time}')