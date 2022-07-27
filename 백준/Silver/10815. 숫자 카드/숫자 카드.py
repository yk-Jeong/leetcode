n = int(input())
list_n = set(map(str, input().split()))
m = int(input())
list_m = list(map(str, input().split()))
bool_list = []

for i in range(m):
  if list_m[i] in list_n:
    bool_list.append(1)
  else:
    bool_list.append(0)

print(' '.join(map(str, bool_list)))