
S = input()

char = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = len(S)

for i in range(len(char)):
  if char[i] in S:
    a = S.count(char[i])
    count = count - a

print(count)