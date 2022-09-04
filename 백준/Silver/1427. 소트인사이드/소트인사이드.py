import sys 
input = sys.stdin.readline
N = input()

print(int(''.join(sorted(N, reverse=True))))