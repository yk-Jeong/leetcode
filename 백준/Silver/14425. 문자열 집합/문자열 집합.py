N, M = map(int, input().split())

S = []
count = 0

for i in range(N):
  a = input()
  S.append(a)
for j in range(M):
  b = input()
  if b in S: 
    count += 1

print(count)