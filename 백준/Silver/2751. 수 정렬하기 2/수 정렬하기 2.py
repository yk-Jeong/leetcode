import sys 
input = sys.stdin.readline
N = int(input())
    
num = []
for _ in range(N):
  i = int(input())
  num.append(i)
print(*sorted(num), sep='\n')