X = int(input())
N = int(input())
sum_list = []
for i in range(N):
  a, b = map(int, input().split())
  sum_list.append(a*b)
if sum(sum_list) == X:
  print("Yes")
else:
  print("No")