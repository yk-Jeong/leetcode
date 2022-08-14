S = input().upper()

alphabet = list(set(S))
test = []

for i in alphabet:
  cnt = S.count(i)
  test.append(cnt)

if test.count(max(test)) >= 2:
  print("?")
else:
  print(alphabet[(test.index(max(test)))])