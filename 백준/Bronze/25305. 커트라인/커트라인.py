import sys 
input = sys.stdin.readline
N, k = map(int, input().split())

x = list(map(int, input().split()))
x = sorted(x, reverse=True)
print(x[k-1])