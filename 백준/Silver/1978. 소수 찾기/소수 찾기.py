N = int(input())
list_n = list(map(int, input().split()))

prime = 0
for i in list_n:
  count = 0
  if i == 1:
    continue
  for j in range(2, i+1):
    if i % j == 0:
      count += 1
  if count == 1:
    prime += 1

print(prime)