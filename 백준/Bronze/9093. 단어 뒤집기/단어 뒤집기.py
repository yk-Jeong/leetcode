T = int(input())

for _ in range(T):
  S = input()
  S = S.split(' ')
  for i in S:
    print(i[::-1], end=' ')  