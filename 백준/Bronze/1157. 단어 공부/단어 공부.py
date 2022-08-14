S = input().upper()

from collections import Counter

counter = Counter(S)
test = list(counter.values())
test = [item for item in test if item == max(test)]
if len(test) > 1:
  print('?')
else:
  print(max(counter, key=counter.get))
