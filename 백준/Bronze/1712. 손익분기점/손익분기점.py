A, B, C = map(int, input().split())

if C == B:
  print(-1)
else:
  n = int(A / (C-B))
  if B < C: 
    print(n+1)
  else:
    print(-1)