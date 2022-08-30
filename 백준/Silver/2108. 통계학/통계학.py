from collections import Counter
import sys 
input = sys.stdin.readline
N = int(input())

num = []
for _ in range(N):
  i = int(input())
  num.append(i)
num = sorted(num)
c = Counter(num).most_common(2)

if len(num) > 1:
  if c[0][1] == c[1][1]:
    mode = c[1][0]
  else:
    mode = c[0][0]
else:
  mode = c[0][0]

print(round(sum(num) / len(num))) # 산술평균
print(int(num[len(num) // 2])) # 중앙값
print(mode)
print(max(num) - min(num)) # 범위