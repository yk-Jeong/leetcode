C = int(input())
for i in range(C):
  N = list(map(int, input().split()))
  M = (sum(N) - N[0]) / (len(N) - 1)
  avg = 0
  for j in range(1, len(N)):
    if N[j] > M:
      avg += 1
    else:
      pass
  print('%.3f'%((avg / (len(N) - 1))*100)+'%')