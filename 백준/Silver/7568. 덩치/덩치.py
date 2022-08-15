N = int(input())

test_list = []
for _ in range(N):
  x, y = map(int, input().split())
  test_list.append((x, y))

count_list = []

for i in range(N):
  count = 0
  for j in range(N):
    if test_list[i][0] < test_list[j][0] and test_list[i][1] < test_list[j][1]:
      count += 1
  count_list.append(count + 1)

for s in count_list:
  print(s, end=' ')