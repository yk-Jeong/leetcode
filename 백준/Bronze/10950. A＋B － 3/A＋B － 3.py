n = int(input())
num_list = []
for i in range(n):
  num_list.append(list(map(int, input().split())))
for j in range(n):
  print(num_list[j][0] + num_list[j][1])