N = int(input())
cyc = 0
new_num = N

while True:
  a = N // 10
  b = N % 10 
  c = (a + b) % 10 
  N = 10 * b + c 

  cyc += 1 

  if new_num == N:
    break
    
print(cyc)