a = input()
count = 0
count_list = a.split(' ')
for i in range(len(count_list)):
  if len(count_list[i]) > 0:
    count += 1

print(count)