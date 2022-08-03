N = int(input())
for i in range(N):
  A = list(input())
  point = 0
  sum = 0
  for j in range(len(A)):
    if (A[j] == "O"):
      point += 1
      sum += point
    else:
      point = 0
  print(sum)