n = int(input())
curr, next = 0, 1
for i in range(n):
  curr, next = next, curr + next
print(curr)