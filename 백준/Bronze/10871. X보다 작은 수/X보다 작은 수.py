N, X = map(int, input().split())
A = list(map(int, input().split()))
A_sort = []
for i in range(len(A)):
  if A[i] < X:
    A_sort.append(A[i])
  else:
    pass
print(' '.join(map(str, A_sort)))