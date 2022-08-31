import sys 
input = sys.stdin.readline
N = int(input())

test = list(map(int, input().split()))
print(sorted(test)[0] * sorted(test)[-1])