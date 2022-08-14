A, B = map(str, input().split())

A = list(reversed(A))
A = int(''.join(A))
B = list(reversed(B))
B = int(''.join(B))

print(max(A, B))