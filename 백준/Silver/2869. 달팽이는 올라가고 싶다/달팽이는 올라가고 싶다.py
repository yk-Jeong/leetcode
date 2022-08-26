import sys 
import math
input = sys.stdin.readline

A, B, V = map(int, input().split())

count = (V - B) / (A - B)
print(math.ceil(count))